#!/usr/bin/env python3
"""De-AI / humaniser lint for resumes and cover letters.

Flags the mechanical "tells" that make honest writing read as AI-generated:
buzzword vocabulary, em-dashes / smart quotes, cover-letter cliches, and a
robotically uniform rhythm (every sentence/bullet the same length or opener).

It does NOT try to beat AI detectors (unreliable, and the content is real). It
nudges the text toward how a real practitioner writes: specific, plain, varied.

Usage:
    python3 tools/humanize_check.py <file.tex|.json|.md|.txt> [...]
    cat file | python3 tools/humanize_check.py -

Exit code: 1 if any HARD tell is found, else 0. Warnings never fail the run.
"""
from __future__ import annotations
import json, re, statistics, sys
from pathlib import Path

# --- hard tells: strong buzzword/AI vocabulary; almost never belongs in honest copy
HARD_WORDS = [
    r"leverag\w*", r"spearhead\w*", r"passionate(?:ly)?", r"passion for", r"delv\w+",
    r"robust", r"seamless(?:ly)?", r"cutting[- ]edge", r"state[- ]of[- ]the[- ]art",
    r"boast\w*", r"underscore\w*", r"pivotal", r"meticulous(?:ly)?", r"showcas\w+",
    r"tapestry", r"realm", r"landscape", r"testament", r"elevat\w+", r"streamlin\w+",
    r"synerg\w+", r"holistic", r"best[- ]in[- ]class", r"world[- ]class", r"game[- ]chang\w+",
    r"unlock\w*", r"empower\w*", r"harness\w*", r"results[- ]driven", r"detail[- ]oriented",
    r"team player", r"proven track record", r"hit the ground running",
    r"think outside the box", r"go[- ]getter", r"self[- ]starter", r"wheelhouse",
    r"in today'?s (?:fast[- ]paced|ever[- ]evolving)", r"ever[- ]evolving",
    r"at the forefront", r"wealth of experience", r"dynamic (?:environment|team)",
]
# cover-letter cliches (also hard)
HARD_PHRASES = [
    "i am writing to", "i am reaching out", "i would be thrilled", "i am thrilled",
    "i am excited to apply", "perfect candidate", "perfect fit", "look no further",
    "i believe i would be a great", "i believe i am the", "make a meaningful impact",
    "contribute to your esteemed", "esteemed organization", "dream job", "dream company",
]
# soft tells: fine in moderation, suspicious in bulk
SOFT_WORDS = [
    r"furthermore", r"moreover", r"additionally", r"notably", r"utili[sz]e\w*",
    r"facilitate\w*", r"comprehensive", r"innovative", r"dynamic", r"strategic",
    r"significant(?:ly)?", r"various", r"numerous", r"plethora", r"myriad",
    r"crucial", r"vital", r"key (?:role|player|driver)", r"drive\w* results",
]

def strip_tex(t: str) -> str:
    t = re.sub(r"(?m)%.*$", " ", t)                       # comments
    t = re.sub(r"\\(?:documentclass|usepackage|newcommand|renewcommand|fontspec|"
               r"namesection|signature|closing|currentdate|section|item|textbf|"
               r"href|url|vspace|hspace|rfoot|pagestyle|fancyhf|thispagestyle)\b",
               " ", t)
    t = re.sub(r"\\[a-zA-Z@]+\*?", " ", t)                # any remaining commands
    t = re.sub(r"[{}\\$&#_^~]|\[[^\]]*\]", " ", t)        # tex syntax
    return t

def extract(path: str) -> str:
    raw = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    ext = "" if path == "-" else Path(path).suffix.lower()
    if ext == ".json":
        vals = []
        def walk(x):
            if isinstance(x, str): vals.append(x)
            elif isinstance(x, dict): [walk(v) for v in x.values()]
            elif isinstance(x, list): [walk(v) for v in x]
        try: walk(json.loads(raw))
        except json.JSONDecodeError: return raw
        return "\n".join(vals)
    if ext == ".tex":
        return strip_tex(raw)
    if ext in (".md", ".markdown"):
        raw = re.sub(r"`[^`]*`", " ", raw)               # inline code
        raw = re.sub(r"(?m)^\s*[-*#>|].*$", " ", raw)    # lists/headings/tables/quotes
    return raw

def find(patterns, text, flags=re.I):
    hits = {}
    for p in patterns:
        for m in re.finditer(rf"\b{p}\b" if p[0].isalpha() else p, text, flags):
            key = m.group(0).lower()
            hits[key] = hits.get(key, 0) + 1
    return hits

def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [s.strip() for s in parts if len(s.split()) >= 3]

def check(path: str):
    text = extract(path)
    findings = {"hard": [], "soft": [], "warn": []}

    hw = find(HARD_WORDS, text)
    for w, c in sorted(hw.items(), key=lambda x: -x[1]):
        findings["hard"].append(f'buzzword "{w}"' + (f" (x{c})" if c > 1 else ""))
    low = text.lower()
    for ph in HARD_PHRASES:
        n = low.count(ph)
        if n: findings["hard"].append(f'cliche "{ph}"' + (f" (x{n})" if n > 1 else ""))

    # punctuation tells (em-dash is the real AI signal; en-dash in date ranges is fine)
    for ch, name in [("—", "em-dash (—)"), ("‘", "curly quote"), ("“", "curly quote"),
                     ("”", "curly quote")]:
        n = text.count(ch)
        if n: findings["hard"].append(f"{name} (x{n})")
    # en-dash only when used as a prose dash (letter–letter), not a year/number range
    prose_endash = len(re.findall(r"[A-Za-z]\s*–\s*[A-Za-z]", text))
    if prose_endash:
        findings["soft"].append(f"en-dash (–) used mid-prose (x{prose_endash}) — a comma or period usually reads more human")

    sw = find(SOFT_WORDS, text)
    total_soft = sum(sw.values())
    if total_soft:
        top = ", ".join(f'{w}({c})' for w, c in sorted(sw.items(), key=lambda x: -x[1])[:6])
        (findings["hard"] if total_soft >= 6 else findings["soft"]).append(
            f"{total_soft} soft/transition words: {top}")

    # rhythm: burstiness + repeated openers
    sents = sentences(text)
    if len(sents) >= 6:
        lens = [len(s.split()) for s in sents]
        mean = statistics.mean(lens)
        cv = statistics.pstdev(lens) / mean if mean else 0
        if cv < 0.45:
            findings["warn"].append(
                f"uniform sentence length (burstiness {cv:.2f}; aim > 0.5 — mix short punchy "
                f"lines with longer ones)")
        openers = {}
        for s in sents:
            w0 = re.sub(r"[^a-z]", "", s.split()[0].lower())
            if w0 not in ("i", "the", "a", "an", "my", "we"):
                openers[w0] = openers.get(w0, 0) + 1
        for w0, c in openers.items():
            if c >= 3 and c / len(sents) >= 0.30:
                findings["warn"].append(f'{c} sentences/bullets open with "{w0}" — vary the openers')

    return findings

def main():
    args = [a for a in sys.argv[1:] if a != "-"] or (["-"] if not sys.stdin.isatty() else [])
    if not args:
        print(__doc__); return 2
    worst = 0
    for path in args:
        f = check(path)
        label = "stdin" if path == "-" else path
        if not (f["hard"] or f["soft"] or f["warn"]):
            print(f"✓ {label}: reads human — no tells found"); continue
        print(f"─ {label}")
        for x in f["hard"]: print(f"  [tell]  {x}")
        for x in f["soft"]: print(f"  [soft]  {x}")
        for x in f["warn"]: print(f"  [rhythm]{x}")
        if f["hard"]: worst = 1
    return worst

if __name__ == "__main__":
    sys.exit(main())
