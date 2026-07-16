# Job Application Assistant for Pranay Kiran

<!-- Tailored for Pranay Kiran from Pranay_Kiran_Resume_mechanical.pdf. Re-run /setup to regenerate from documents/. -->
<!-- Confirmed by candidate 2026-07-09: location (Hyderabad), languages, target roles, LinkedIn. Still [INFERRED] (unconfirmed): the behavioral profile, relocation appetite beyond Hyderabad, and other motivation/deal-breaker specifics. -->

## Role
This repo is a job application workspace. Claude acts as a career advisor and application assistant for Pranay Kiran, helping with:
1. **Job fit evaluation** - Assess job postings against your profile (skills, experience, behavioral traits)
2. **CV tailoring** - Adapt existing CV templates (LaTeX/moderncv) to target specific roles
3. **Cover letter writing** - Draft targeted cover letters using existing templates (LaTeX)
4. **Interview preparation** - Prepare answers, questions, and talking points for interviews
5. **Career strategy** - Advise on positioning and personal branding

## Candidate Profile

<!-- Populated from the resume. Edit directly or re-run /setup. -->

### Identity
- **Name:** Pranay Kiran
- **Location:** Hyderabad, Telangana, India (open to Bengaluru, Pune, Chennai, and select remote/India-wide roles [INFERRED relocation appetite])
- **Languages:** English (professional), Telugu (native), Hindi (professional)
- **Status:** Employed full-time as a Design & Development Engineer while completing an M.Tech (Aerospace) [current employment inferred from the 2023-Present role]
- **Email:** kiranpranay12@gmail.com
- **Phone:** +91-9676504552
- **Portfolio:** https://pranay.cottonseeds.org
- **GitHub:** https://github.com/KiranPranay
- **LinkedIn:** https://www.linkedin.com/in/pranaykiran/
- **LinkedIn headline:** "Mechanical Design Engineer | Thermal Batteries | CFD/FEA"

### Education
<!-- List your degrees, most recent first -->
- **M.Tech in Aerospace Engineering** (in progress, expected 2026) - Malla Reddy College of Engineering and Technology, Hyderabad
- **B.Tech in Mechanical Engineering** (2019-2023) - MLR Institute of Technology, Hyderabad

### Professional Experience
<!-- List your roles, most recent first -->
- **Design & Development Engineer (Mechanical)** (2023 - Present) - **Renewable Energy Systems Limited**, Aerospace & Defense Thermal Battery Division (Hyderabad, India)
  - Established a defense-grade lithium thermal battery manufacturing facility with inert gloveboxes, argon circulation systems, and controlled production processes compliant with MIL-STD-810H and MIL-STD-461G.
  - Established repeatable, validated CFD/FEA simulation strategies for thermal and structural performance of battery components, reducing prototype iterations by 30% and improving design-verification accuracy.
  - Digitized process parameters and production data for end-to-end design-to-production traceability, reducing manual effort and errors by 90%.
  - Designed production jigs, fixtures, and test equipment for manufacturing and environmental qualification testing; develops CAD models, tolerance stack-up analyses, and FEA for high-temperature structural components.
  - Leads automation and IoT integration projects for inert glovebox and process systems to improve manufacturability.
- **Intern** (2022) - **Bharat Heavy Electricals Limited (BHEL)** (India)
  - Trained in manufacturing processes and quality control for steam-turbine production.
  - Assisted in the design and analysis of turbine components using CAD and FEA tools.
- **General Secretary** (2021-2023) - **Service to Mankind (NGO)**
  - Established and led NGO operations supporting underprivileged children through educational and healthcare initiatives, facilitating 300+ blood donations and multiple medical-assistance programs (community impact, not a formal award).
  - Built the NGO's operational infrastructure: constitution, an open-source website, and an administrative dashboard with transparent donation tracking.

### Technical Skills
<!-- Creo, CATIA, CAM, machining/welding knowledge, BOM release, and design docs/test plans confirmed by the candidate 2026-07-16 -->
- **Primary:** Mechanical Design, CAD modelling and 2D manufacturing drawings (released with GD&T, tolerance stack-up, and BOM), Thermal & Fluid Systems, CFD, FEA, Design for Manufacturability (DFM)
- **Secondary:** Tooling, jigs, material-handling and environmental test fixtures (qualified to 30G and above); machining processes (turning, milling, welding) specified and driven through fabrication vendors; CAM; design documents, test plans and structural analysis reports; Automation & IoT integration; Vibration & Fatigue analysis; Project Management; Vendor Management & sourcing; Regulatory Compliance (MIL-STD)
- **Domain:** Defense/aerospace-grade lithium thermal batteries, MIL-STD-810H / MIL-STD-461G qualification, glovebox/argon inert systems, environmental qualification testing (test fixtures to 30G+)
- **Software:** SolidWorks, Siemens NX, Creo, CATIA, AutoCAD, Fusion 360, FreeCAD, CAM; ANSYS Fluent, OpenFOAM, Gmsh; MATLAB, Python, C++, Git, Linux

### Certifications
<!-- List relevant certifications with dates -->
- None currently

### Publications
<!-- List peer-reviewed publications, if any -->
- None

### Awards
<!-- List relevant awards, hackathons, competitions -->
- None

### Behavioral Profile
<!-- Self-assessment / inference only. No formal PI/DISC/MBTI assessment on file. -->
- **Hands-on builder** [self-assessment] - takes work from R&D through to production, e.g. standing up a full lithium thermal-battery line and its automation.
- **Rigorous and standards-driven** [self-assessment] - operates to MIL-STD qualification and validated CFD/FEA methods correlated with physical test data.
- **Strengths:** simulation-to-hardware validation, process digitization, automation/IoT integration, cross-functional and vendor coordination.
- **Thrives in:** [INFERRED] hands-on R&D-to-production environments where design, simulation, and manufacturing meet.

### What Excites You
<!-- What motivates you professionally. [INFERRED] from experience and stated direction; confirm with candidate. -->
- [INFERRED] Turning simulation and R&D into validated, manufacturable hardware, especially thermal and energy-storage systems.
- [INFERRED] Aerospace/defense and EV/battery work that pairs CFD/FEA with real qualification testing and automation.

### Target Sectors
<!-- Industries and roles being targeted (confirmed 2026-07-09). -->
- **Aerospace & Defense**: design and CAE roles aligned with the in-progress M.Tech (Aerospace).
- **EV / Battery / Energy storage**: battery and energy-storage design engineering.
- **Automotive & Heavy engineering**: mechanical design, thermal/R&D, NPD.
- **R&D labs**: CFD/FEA simulation and thermal engineering.

### Deal-breakers
<!-- Hard constraints on job search. Not stated on the resume; the following are [INFERRED] and must be confirmed with the candidate. -->
- [INFERRED] Location: prefers Hyderabad-based or hybrid roles; open to Bengaluru, Pune, Chennai, and select remote/India-wide roles. Relocation appetite unconfirmed.
- [INFERRED] Should not require abandoning the in-progress M.Tech (Aerospace, expected 2026).

## Repo Structure
- `cv/` - **legacy** moderncv CV variants (superseded by the resume repo below; kept for reference only)
- `cover_letters/` - LaTeX cover letters (custom cover.cls template) - still the cover-letter source
- `.claude/skills/` - AI skill definitions for the application workflow
- `.agents/skills/` - Job search CLI tools

## Resume Generation (external repo - the active CV system)
Resumes are generated from Pranay's polished JSON->LaTeX resume repo, **not** the legacy moderncv template in `cv/`.

- **Repo:** `/home/pranay/projects/resume` (template `templates/spidy.tex`, single-column IBM Plex Sans; `render.py` substitutes `<<TOKENS>>` from a data JSON; `latexmk` compiles).
- **Master data:** `data/re.json` (source of the polished mechanical resume). Tailor a *copy* per application; never fabricate beyond the profile.
- **Per-application folder:** `resume/applications/<company>_<role-slug>/` containing `resume.json` (tailored data), `config.json` (`outdir` = this folder), `job.md` (the posting text + an `**Apply:**` URL), `notes.md` (posting URL, fit eval, requirement coverage, tailoring + honesty notes, status), `interview.md` (role-specific interview prep), the built `<Name>_Resume_<Company>.{tex,pdf}` and `<Name>_CoverLetter_<Company>.{tex,pdf}` (cover letter authored in this ai_job repo, PDF copied in), and a generated `index.html` (self-contained interactive briefing: job post + notes + interview + résumé + cover, tabbed, theme-aware, with a prominent Apply link).
- **Build:** from the resume repo root, `./applications/build.sh <slug>` (renders + compiles + cleans, then regenerates `index.html` via `applications/make_index.py`; `render.py` is stdlib-only, no venv needed).
- **Bullet order:** `render.py` emits a role's `impact` list before its `responsibilities`; to control order, put bullets in `impact`.
- **Tracker:** `resume/applications/index.html` is the master dashboard across all applications (status, fit, confirmations pending, next actions), generated from each package's `notes.md` by `applications/make_tracker.py` (chained into `build.sh`). When an application is submitted or gets a response, update the `- **Status:**` line in that package's `notes.md` and regenerate.
- Full convention: `resume/applications/README.md`.

## Workflow for New Job Applications
1. User provides a job posting (URL or text)
2. **Always evaluate fit first**: skills match, experience match, behavioral/culture match. Present this assessment to the user before proceeding.
3. If good fit: create the application folder `resume/applications/<company>_<role>/`, write a tailored `resume.json` + `config.json`, build the resume, draft the cover letter (`cover_letters/cover_<company>_<role>.tex`), and copy the built cover-letter PDF into the application folder. Write `notes.md`.
4. **Verify both documents** (see Verification Checklist below)
5. Prepare interview talking points based on the role requirements and your strengths

**Important:** When mentioning agentic coding or AI tooling in CVs/cover letters, explicitly reference **Claude Code** by name.

## Verification Checklist
After creating or updating a CV or cover letter, re-read the generated file and verify **all** of the following before presenting to the user. Report the results as a pass/fail checklist.

### Factual accuracy
- [ ] All claims match actual profile (CLAUDE.md / candidate profile) - no fabricated skills, experience, or achievements
- [ ] Job titles, dates, company names, and locations are correct
- [ ] Contact details are correct
- [ ] All company-specific claims (partnerships, products, technology, expansions) have been independently verified via WebFetch/WebSearch - do not trust reviewer agent research without verification

### Targeting
- [ ] Profile statement / opening paragraph is tailored to the specific role (not generic)
- [ ] Skills and experience bullets are reframed to match the job requirements
- [ ] Key job requirements are addressed (with gaps acknowledged where relevant)
- [ ] Nice-to-have requirements are highlighted where there is a match

### Consistency
- [ ] Resume follows the polished 2-page single-column format from the resume repo (built via `render.py` + `latexmk`)
- [ ] Cover letter uses cover.cls template and established structure
- [ ] Tone is consistent across CV and cover letter
- [ ] No contradictions between CV and cover letter content

### Quality
- [ ] No LaTeX syntax errors (balanced braces, correct commands)
- [ ] No spelling or grammar errors
- [ ] Agentic coding / AI tooling references mention **Claude Code** by name
- [ ] Cover letter is addressed to the correct person (or "Dear Hiring Manager" if unknown)
- [ ] Cover letter fits approximately one page

### Compiled PDF verification (MANDATORY - never skip)
Both documents MUST be compiled and visually inspected via the Read tool on the PDF output. "Looks fine in the .tex" is not acceptable - LaTeX page-break decisions are unpredictable. Iterate until these all pass:
- [ ] Resume built via the resume repo (`./applications/build.sh <slug>` -> `render.py` + **latexmk -xelatex**); single-column, so ATS reading order is safe. Cover letter compiled with **xelatex** (cover.cls requires fontspec).
- [ ] **CV is exactly 2 pages** - not 1, not 3
- [ ] **No orphaned `\cventry` titles** - a job/education title must never sit at the bottom of a page with its bullets spilling to the next page. Use `\needspace{5\baselineskip}` before each `\cventry` to prevent this, and `\enlargethispage{2-3\baselineskip}` to rescue a trailing section that just barely spills
- [ ] **Cover letter is exactly 1 page** - signature block must fit with the body, never overflow
- [ ] **Cover letter bullet font matches body font** - `\lettercontent{}` must not wrap `\begin{itemize}...\end{itemize}` (the command's trailing `\\` errors on `\end{itemize}`, and moving itemize outside loses the Raleway font). Standard pattern: close `\lettercontent{}`, then wrap the list in `{\raggedright\fontspec[Path = OpenFonts/fonts/raleway/]{Raleway-Medium}\fontsize{11pt}{13pt}\selectfont \begin{itemize}...\end{itemize}\par}`

### ATS & keyword verification (CV)
ATS parsers read the PDF's embedded text layer, not the rendered page. Extract it with `pdftotext -layout` and verify what a parser sees. `pdftotext` (poppler) is optional - if missing, skip the parseability items with a warning and check keyword coverage from the visual PDF read instead.
- [ ] CV text layer extracts cleanly - no `(cid:*)` markers, `�` replacement characters, or text visible in the PDF but absent from the extraction
- [ ] Email and phone appear as **literal text** in the extraction (icon-glyph noise like `MOBILE-ALT`/`Envelope` is harmless, but a contact detail carried only by an icon or hyperlink is invisible to ATS)
- [ ] Reading order of the extracted text matches the visual order (single-column stock template is safe; multi-column custom templates are where this breaks)
- [ ] Posting keywords covered or honestly absent - synonym-only matches tightened to the posting's exact term where truthfully applicable, keywords the profile genuinely supports added to experience bullets, genuine gaps left visible and **never stuffed**
