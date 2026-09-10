# Dennis Moe

- 🌐 [moefrilans.no](https://moefrilans.no)
- 💼 [linkedin.com/in/dennismoe](https://www.linkedin.com/in/dennismoe)
- 📄 [English CV](https://moefrilans.no/cv-en.pdf) · [Norsk CV](https://moefrilans.no/cv-no.pdf) <sub>— last updated August 2026</sub>
- ✉️ post@moefrilans.no

Third-year Computer Engineering student at NTNU in Trondheim, specializing in software engineering
(systemutvikling). I came to code after a bachelor's in ancient history, so I care about clear
writing and reasoning as much as shipping.

Open to summer 2027 internships and graduate/junior roles.

*Most of the client work is private. What's public here is coursework and things I'm tinkering with.*

## Now

- **Konsulent, Tech department, [Junior Consulting](https://www.jrc.no)** — the student-run consultancy at NTNU, part-time alongside my studies.
- **Developer, Perception team, [Ascend NTNU](https://www.ascendntnu.no)** — a volunteer student organisation at NTNU that builds autonomous drones for the International Aerial Robotics Competition. Perception turns sensor input into meaningful information about the drone and its environment.

## Selected work

Client projects I built and still run through my one-person company, Moe Frilans.

| Project | What it is | Role / status | Links |
|---------|-----------|---------------|-------|
| **Eksamensportalen** | Exam-prep platform for Norwegian students. Rebuilt from scratch as V2 — 117 subjects, payments taken in-house with Stripe and Vipps, self-service admin — live in production since 29 August 2026<br><sub>React Router v7 · Node · Postgres · Stripe/Vipps · Railway</sub> | Lead dev on V1 · sole developer on V2 | [live](https://eksamensportalen.no) |
| **Insotech** | Bilingual B2B product catalogue with request-for-quote, 10 000+ product variants<br><sub>Nuxt · Supabase · Tailwind</sub> | Solo design + build · I run its domain, DNS, email and hosting | [live](https://insotech.no) · [case study](https://moefrilans.no/en/work/insotech) |
| **Xu Consulting** | Fast static site, migrated off Squarespace without losing search rankings<br><sub>Astro · Cloudflare</sub> | Solo build and migration · I run its domain, DNS and hosting | [live](https://xu.no) · [case study](https://moefrilans.no/en/work/xu-consulting) |

## Stack

**Languages**
<p>
  <img src="icons/typescript.svg" width="38" alt="TypeScript" title="TypeScript" />
  <img src="icons/java.svg" width="38" alt="Java" title="Java" />
  <img src="icons/python.svg" width="38" alt="Python" title="Python" />
</p>

**Frameworks**
<p>
  <img src="icons/astro.svg" width="38" alt="Astro" title="Astro" />
  <img src="icons/vuejs.svg" width="38" alt="Vue" title="Vue" />
  <img src="icons/nuxtjs.svg" width="38" alt="Nuxt" title="Nuxt" />
  <img src="icons/react.svg" width="38" alt="React / React Router" title="React / React Router" />
  <img src="icons/tailwindcss.svg" width="38" alt="Tailwind CSS" title="Tailwind CSS" />
</p>

**Infrastructure**
<p>
  <img src="icons/nodejs.svg" width="38" alt="Node.js" title="Node.js" />
  <img src="icons/postgresql.svg" width="38" alt="PostgreSQL" title="PostgreSQL" />
  <img src="icons/supabase.svg" width="38" alt="Supabase" title="Supabase" />
  <img src="icons/cloudflare.svg" width="38" alt="Cloudflare" title="Cloudflare" />
</p>

**Learning:** Go (backend side projects) · C++ ([INFT2503](https://www.ntnu.no/studier/emner/INFT2503), NTNU)

## Coursework (NTNU)

| Project | What it is | Role | Links |
|---------|-----------|------|-------|
| **IK-Kontrollsystem** | Internal-control system for a real restaurant client — food safety (IK-Mat) and alcohol compliance logging, replacing paper logbooks<br><sub>Vue 3 · Spring Boot · MySQL · Docker</sub> | Team of 4, grade A · my part: multi-tenant scoping, role-based security, dashboard + checklist modules | [course repo](https://github.com/dennismoe0/IDATT2105-Fullstack) · [team repo](https://github.com/Stcwal/fullstack) |
| **Network programming in Rust** | Course assignments (threads → thread pool → raw HTTP → TLS/UDP → sandboxed code-runner) and an RGA CRDT collaborative editor, Rust compiled to WASM with a React frontend<br><sub>Rust · WebAssembly · axum · React</sub> | Team of 3 on the editor, grade A · assignments solo | [code](https://github.com/dennismoe0/IDATT2104-Nettverksprogrammering) |

## How I work

I use AI heavily and openly. What makes that work is everything I've built around it: custom CLI
tooling and skills, and a review pipeline that checks every diff before it ships. At its core is [an
audit suite I built](https://moefrilans.no/en/quality) — 22 quality dimensions, from security and WCAG accessibility to performance,
i18n and supply-chain checks, each finding adversarially verified before it's reported. AI does the
typing; the design decisions, the debugging, and the quality bar are mine.

Lighthouse performance, desktop, measured August 2026: 100 for Eksamensportalen V2, 98 for Xu
Consulting, 97 for Insotech.
