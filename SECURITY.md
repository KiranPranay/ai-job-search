# Security Policy

This repository is a fork of [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search), tailored for a single user. It carries upstream's prompt-injection hardening (#175) plus fork-specific data boundaries.

## Reporting a vulnerability

Please report security findings privately via **[GitHub private vulnerability reporting](https://github.com/KiranPranay/ai-job-search/security/advisories/new)** rather than a public issue. If the private form is unavailable, open a public issue that describes the *class* of problem without a working recipe, and note that you have details to share privately. Issues in the shared framework logic are best reported upstream as well.

## Threat model, honestly stated

This is an agentic workflow: an LLM with file access reads untrusted web content (job postings, scraped search results) alongside personal data (CV, profile, application history). That combination is the main risk surface, and it cannot be fully eliminated - only narrowed. What the framework does about it:

- **Untrusted-input rules**: `/apply` and `/rank` treat posting text as data, never instructions - agents are told not to follow directions embedded in postings and not to fetch URLs found inside posting text (the user-supplied posting URL is the one exception). The same rule rides into ad-hoc scraped-JD evaluation agents. Reviewer and company research starts from the company identity the user confirmed, never from links in the posting body.
- **Personal-data boundaries (fork-specific)**: per-application packages contain defense-manufacturing detail and internal strategy notes (fit scores, honesty flags, rejection analysis). They live in a **separate private repo** (`KiranPranay/job-applications`), never in this public repo. The public repos (this fork, and the `XeLaTeX-Spidy-Resume` engine) hold only resume/LinkedIn-level content. Populated profile documents (`documents/`, `cv/*_<company>.*`, `cover_letters/cover_*.tex`) are gitignored; nothing uploads document content anywhere.
- **Search is user-initiated**: the LinkedIn search CLI and `site:` Google searches make live requests only when run interactively; keep volume low to respect rate limits. CI never makes live requests.

Instruction-level defenses raise the bar; they are not a sandbox. Before sending anything outbound, review what the agent fetched and wrote.

## Scope notes

- The legacy Danish job-portal CLIs bundled from upstream are unused in this fork; India search runs via the country-agnostic LinkedIn search CLI.
- Review any code you copy from community forks; this policy covers only this repository.
