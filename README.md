# SC200 Azure SOC Academy

An 18-day, scenario-led security operations programme for corporate training and individual study. Build and investigate a fictional hospital environment using Azure, Microsoft Sentinel and the Microsoft security portfolio. No prior security-job experience is assumed; basic computer use and willingness to read technical steps are required.

Published guide: [Open the course](https://pnj2k7.github.io/SC200-Azure-SOC-Academy/). Repository: [pnj2k7/SC200-Azure-SOC-Academy](https://github.com/pnj2k7/SC200-Azure-SOC-Academy).

Start with [Getting started](getting-started.md), then open [the HTML course](index.html). Download the repository ZIP from GitHub, extract it and double-click index.html. The pages work offline; Microsoft portals require internet and appropriate accounts. [handbook.html](handbook.html) is a single-file reading edition with embedded styles.

## Coverage and honesty

The official baseline is the SC-200 skills outline effective **21 October 2026**, checked **25 October 2026**. Microsoft lists **three weighted areas and nine objective groups**. This course organises them into **12 teaching modules**, not 12 official exam domains. [Coverage](coverage/index.html) maps all 54 listed objective bullets to a lesson and evidence requirement. Related exam topics may extend beyond the published bullets.

Live, Simulation and Pending statuses are separate. An Azure subscription does not supply every Defender, Microsoft 365, Purview, Entra, AI or advanced platform license. Simulated work supports learning but does not prove operational competence on a live product.

## Learning days

| Day | Focus | Module |
|---|---|---|
| [Day 1](days/day-1/index.html) | Open the SOC | 01 |
| [Day 2](days/day-2/index.html) | Build the evidence room | 02 |
| [Day 3](days/day-3/index.html) | Windows tells its story | 03 |
| [Day 4](days/day-4/index.html) | The missing telemetry | 03 |
| [Day 5](days/day-5/index.html) | Protect the reception desk | 04 |
| [Day 6](days/day-6/index.html) | Investigate the workstation | 04 |
| [Day 7](days/day-7/index.html) | Engineer a reliable detection | 05 |
| [Day 8](days/day-8/index.html) | Automate with a brake | 06 |
| [Day 9](days/day-9/index.html) | The suspicious invoice | 07 |
| [Day 10](days/day-10/index.html) | Identity crosses the perimeter | 08 |
| [Day 11](days/day-11/index.html) | Find the data trail | 09 |
| [Day 12](days/day-12/index.html) | Defend the cloud workload | 10 |
| [Day 13](days/day-13/index.html) | Run the incident bridge | 11 |
| [Day 14](days/day-14/index.html) | Make the SOC observable | 11 |
| [Day 15](days/day-15/index.html) | Hunt beyond the alert | 12 |
| [Day 16](days/day-16/index.html) | Follow the historical trail | 12 |
| [Day 17](days/day-17/index.html) | Use AI with evidence | 12 |
| [Day 18](days/day-18/index.html) | The hospital incident exercise | 12 |

[Review](days/review/index.html) follows Day 18. Each day has a plain-language introduction, technical notes, a morning/afternoon plan, a numbered lab, expected results, prove-it checks, a controlled break/fix exercise, teardown, cost entry, evidence requirements, a practice question and printable briefing slides.

## Scenario and assessment

[Wardlight Hospitals](scenario/organisation.md) is fictional. Its hospital services must remain available while its security team investigates a suspicious supplier invoice. [Portfolio](coursework/portfolio-brief.md) and [capstone](coursework/capstone-brief.md) assess evidence and judgement. Nothing in this repository is an official Microsoft exam question or a guarantee of a pass.

## Repository map

- scenario/: organisation and numbered architecture.
- days/day-1 through day-18/: lesson, notes, lab, slides, quiz and exercise.
- days/review/: coverage review and assessment.
- coverage/: objective matrix and module map.
- infra/, scripts/, queries/, notebooks/, data/: downloadable practical assets.
- templates/: evidence, access, cost, incident and change records.
- coursework/, practice/, artefacts/: assessments and interactive learning.
- [Publishing](PUBLISH.md), [cleanup](cleanup.md), [sources](sources.md) and [attribution](ATTRIBUTION.md).

Run `python build_course.py` to regenerate static pages, then `python scripts/validate.py`. No package installation is required. Python 3.10+ is recommended. Deployment templates and cloud workflows require validation in your own isolated subscription; local checks do not prove Azure deployment or licensed product actions.

## Professional use

Use a dedicated training tenant/subscription. No production connections, real patient data, passwords, tokens or unredacted evidence in Git. An organisation should have a security owner review permissions, licensing, regional availability, cost and change approval before corporate rollout. [Corporate delivery guide](corporate-delivery.md) provides the operating model.

## Licensing

Original course content and code: MIT, see LICENSE. Structure inspired by nirangadh/HNDNE-Cloud-Computing, credited in ATTRIBUTION.md. No source teaching text, diagrams, fonts or code have been copied. Microsoft and Azure names belong to their respective owners; this course is independent.
