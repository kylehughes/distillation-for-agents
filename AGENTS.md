# Repository guidance

This repository distributes the Distill skill for Claude Code, Codex, and other Agent Skills hosts. Keep one shared skill under `skills/distill/`.

## Content

- `SKILL.md` contains the six-step procedure. The files in `references/` (operators, validation, examples, foundations, sources) are loaded only when a task needs them. Keep detailed guidance there rather than duplicating it in the entrypoint.
- `agents/openai.yaml` supplies the skill's Codex UI metadata and `assets/icon.svg` its icon. Keep `display_name`, `short_description`, and `default_prompt` as single-line quoted strings so the checks can read them.
- Keep the procedure domain-general and proportionate. Simplification must preserve the distinctions, evidence, uncertainty, and claim strength the task requires. Do not turn the skill into a mandatory checklist or promise a uniquely simplest answer.
- When adding or changing a research claim, update `references/sources.md` with the work, passage, edition, and caveat, and keep source IDs stable.

## Packaging and checks

`plugin.json` is the portable manifest. `.codex-plugin/plugin.json` supplies the compatible Codex manifest and interface metadata; `.claude-plugin/plugin.json` declares the Claude plugin. Both marketplace files point to this repository root. Keep identities and release versions synchronized; do not rename the published plugin or skill without an explicit migration.

Run `python3 scripts/check.py`, `python3 -m unittest discover -s scripts -p 'test_*.py'`, and `python3 scripts/package.py` after changes. Validate the Claude manifests with `claude plugin validate .claude-plugin/plugin.json` and `claude plugin validate .claude-plugin/marketplace.json`. For runtime checks, use the local marketplace in Codex and confirm skill discovery in both hosts.

Each release ships three archives. `distill-skill.zip` keeps `SKILL.md` at its root for compatibility. `distill.skill` is the Claude app upload format, with the `distill/` folder at its root; `scripts/check.py` enforces that format's frontmatter rules (allowed keys, a kebab-case name, a description of at most 1024 characters without angle brackets). `distill-plugin.zip` holds the plugin. All three archives must include the license. Package only runtime content; exclude repository instructions, build tooling, local settings, and caches.

## Releases

`./release.sh --dry-run <version>` checks release preconditions without changing files. `./release.sh <version>` updates the manifests, validates, commits `Release <version>`, creates the matching tag, and pushes the main branch and that tag. Run the publishing command only when a release is requested. GitHub Actions validates the tag and builds all three archives before publishing the release.

## License

Distributed under the MIT License. Preserve `LICENSE` in every distribution.
