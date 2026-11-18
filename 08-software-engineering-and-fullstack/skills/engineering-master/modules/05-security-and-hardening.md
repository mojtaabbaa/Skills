# Module 05: Security, STRIDE Threat Modeling & Hardening

**Resolves Conflict C6 (Universal Layer):** Consolidated from `security-and-hardening` (pairs with `wordpress-master/modules/08-wp-security-performance-and-ops.md` for WordPress/WooCommerce-specific hooks & APIs).

---

## 1. Threat Model First (STRIDE Over Every Trust Boundary)

Before writing auth, input handlers, uploads, webhooks, or AI features, map:
1. **Trust Boundaries:** HTTP inputs, forms, file uploads, webhooks, third-party APIs, OS env/filenames, and **LLM outputs** (trust follows *who wrote a value*, never which channel delivered it).
2. **Assets:** Credentials, PII, payment/order integrity, admin actions, filesystem/DB integrity.
3. **STRIDE Check:** **S**poofing (auth/signatures) | **T**ampering (integrity/parameterized SQL/HTTPS) | **R**epudiation (audit logs) | **I**nformation Disclosure (encryption/allowlists/generic errors) | **D**enial of Service (rate limits/size caps/timeouts) | **E**levation of Privilege (least-privilege RBAC + object-level ownership).

---

## 2. The Three-Tier Security Boundary System

- **ALWAYS DO (Zero Exceptions):** Validate all external input at system boundaries; parameterize every SQL/DB query; context-encode output (prevent XSS); enforce HTTPS; hash passwords with `argon2`/`scrypt`/`bcrypt (>=12)`; set security headers (`CSP`, `HSTS`, `X-Frame-Options`, `X-Content-Type-Options`); use `httpOnly, Secure, SameSite` session cookies; run package-manager lockfile vulnerability audits before every release.
- **ASK FIRST (Explicit Human Approval):** Changing auth/session flows, storing new PII/payment categories, adding external integrations, modifying CORS/rate-limiting, adding file upload handlers, elevating user roles.
- **NEVER DO:** Never commit secrets/API keys/tokens; never log passwords/tokens/card numbers; never rely on client-side validation as security; never use `eval()` or unsanitized `innerHTML`; never store auth sessions in `localStorage`; never leak raw stack traces to public callers; never allow wildcard CORS `*` with credentials.

---

## 3. Specialized Threat Controls

- **SSRF Protection:** Allowlist external URL schemes/hosts, block private/link-local IP ranges (`127.0.0.0/8`, `169.254.169.254`, `10.0.0.0/8`), disable open redirects on server-side fetches.
- **Destructive Path Safety:** Canonicalize and verify resolved paths stay strictly inside the intended base directory before delete/move/overwrite.
- **Supply Chain Hygiene:** Commit lockfiles, disable untrusted postinstall scripts where possible, triage critical/high advisories by reachability, inspect typosquatting risk on new packages.
- **AI / LLM Security (OWASP LLM05):** Treat **model output as untrusted input** — never pass raw LLM text directly into `eval`, SQL, shell commands, `innerHTML`, or file paths without strict parsing/allowlisting.
- **Deep Code Patterns:** [`references/hardening-patterns.md`](../references/hardening-patterns.md).
