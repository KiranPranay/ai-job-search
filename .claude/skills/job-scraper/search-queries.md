# Search Queries for Job Scraper

<!-- SETUP: Customize these queries based on your skills, target roles, and location -->

## Search Sites

Primary (Indian job market):
- **linkedin.com/jobs** - LinkedIn job listings (the repo's linkedin-search CLI is country-agnostic and works for India; filter: India / your city)
- **naukri.com** - largest Indian job board
- **in.indeed.com** - Indeed India
- **foundit.in** - Foundit (formerly Monster India)
- Company career pages (aerospace/defense, EV/battery, automotive, heavy engineering, R&D labs)

Secondary (company career pages via Google):
- Direct Google searches with `site:` filters for known target companies

> NOTE: The four Danish CLI tools bundled with this framework (Jobindex, Jobnet, Jobbank, Jobdanmark) are Denmark-only and are NOT used for this profile. India searches run through the country-agnostic LinkedIn CLI plus `site:` Google searches against Naukri, Indeed India, and Foundit.

## Query Categories

Queries are grouped by priority. Each query should be combined with your location terms (e.g. "Hyderabad", "Bengaluru", "Pune", "Chennai") where the site supports it.

### Priority 1: Mechanical Design Engineer

These match your strongest and most desired career direction.

```
site:naukri.com "Mechanical Design Engineer" Hyderabad
site:naukri.com "Design Engineer" (SolidWorks OR "Siemens NX") Hyderabad
site:in.indeed.com "Mechanical Design Engineer" CAD Hyderabad
site:linkedin.com/jobs "Mechanical Design Engineer" India
site:linkedin.com/jobs "Design Engineer" (NX OR SolidWorks OR AutoCAD) Hyderabad
```

### Priority 2: CFD / FEA / CAE Simulation

These match your domain expertise.

```
site:naukri.com ("CFD Engineer" OR "FEA Engineer" OR "CAE Engineer") Hyderabad OR Bengaluru
site:naukri.com (ANSYS OR OpenFOAM OR "ANSYS Fluent") simulation India
site:in.indeed.com ("CAE Engineer" OR "Simulation Engineer") (FEA OR CFD) Hyderabad
site:linkedin.com/jobs "Simulation Engineer" (CFD OR FEA) India
site:linkedin.com/jobs (ANSYS OR OpenFOAM) "thermal analysis" Hyderabad India
```

### Priority 3: Adjacent (Battery / EV / Thermal / R&D / NPD)

Adjacent roles you could pivot into.

```
site:naukri.com ("Battery Engineer" OR "EV Engineer" OR "Thermal Engineer") SolidWorks Hyderabad
site:naukri.com ("R&D Engineer" OR "NPD Engineer" OR "New Product Development") CAD Bengaluru OR Pune
site:in.indeed.com ("Thermal Engineer" OR "Battery Design Engineer") (ANSYS OR CFD) India
site:linkedin.com/jobs ("R&D Engineer" OR "Product Development Engineer") mechanical India
```

### Priority 4: Broader (Aerospace/Defense Design, Manufacturing/Production)

Wider net for general technical roles.

```
site:naukri.com ("Aerospace Design Engineer" OR "Defense Design Engineer") (NX OR CATIA OR FEA) Hyderabad
site:naukri.com ("Manufacturing Engineer" OR "Production Engineer") (DFM OR "jigs and fixtures") Hyderabad
site:in.indeed.com ("Aerospace Engineer" OR "Manufacturing Engineer") CAD India
site:linkedin.com/jobs "Manufacturing Engineer" (DFM OR tooling OR fixtures) Hyderabad India
site:linkedin.com/jobs "Aerospace Engineer" (design OR FEA OR CFD) India
```

## Location Filter

When evaluating results, verify the job location is realistic given the candidate's base and relocation willingness. Define acceptable areas:
- Hyderabad, Telangana and surrounding areas (ideal — home base)
- Bengaluru (acceptable — relocation/remote-willing [INFERRED])
- Pune (acceptable — relocation/remote-willing [INFERRED])
- Chennai (acceptable — relocation/remote-willing [INFERRED])
- Remote / hybrid, India-wide (borderline)
- International (too far, unless relocation is intended)

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline that has not yet passed. If a posting date cannot be determined, include it but flag as "date unknown".

## Adapting Queries

If the user specifies a focus area, select queries from the matching category and also generate 2-3 custom queries for that focus. For example:
- "/scrape [focus_area]" -> relevant category queries + custom focus-specific queries
