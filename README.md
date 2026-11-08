# Distillation for Agents

[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code_Plugin-555?logo=claude)](https://code.claude.com/docs/en/plugins)
[![Codex Plugin][codex_plugin_badge]](https://developers.openai.com/plugins/build/plugins)
[![CI](https://github.com/kylehughes/distillation-for-agents/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/kylehughes/distillation-for-agents/actions/workflows/ci.yml)\
[![Latest Release](https://img.shields.io/github/v/release/kylehughes/distillation-for-agents)](https://github.com/kylehughes/distillation-for-agents/releases)

A shared simplification skill for Claude Code and Codex. It finds the essential structure of an explanation, model, decision, process, design, or piece of writing, then simplifies it without losing the distinctions, evidence, and uncertainty the task depends on.

The procedure has six steps: frame what the work must accomplish, establish what has to survive, examine the structure before cutting anything, build a candidate and count its full cost, test it against the cases most likely to break it, then deliver the result and stop. Removal, recombination, a new representation, a corrected premise, and no change at all are all valid outcomes. Simple tasks get three quick questions instead of the full procedure.

## Installation

### Claude Code

Run these commands inside Claude Code:

```text
/plugin marketplace add kylehughes/distillation-for-agents
/plugin install distillation-for-agents@distillation-for-agents
```

Start a new session after installation.

For a team repository, merge the following into `.claude/settings.json`:

```json
{
  "enabledPlugins": {
    "distillation-for-agents@distillation-for-agents": true
  },
  "extraKnownMarketplaces": {
    "distillation-for-agents": {
      "source": {
        "source": "github",
        "repo": "kylehughes/distillation-for-agents"
      }
    }
  }
}
```

Claude Code prompts team members to install the plugin when they trust the repository's marketplace configuration. See [Claude Code's marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces).

### Codex

With a Codex CLI version that supports plugin marketplaces, run:

```sh
codex plugin marketplace add kylehughes/distillation-for-agents
codex plugin add distillation-for-agents@distillation-for-agents
```

Start a new session after installation. Codex gets the same skill as Claude Code.

These commands use Codex's [plugin marketplace support](https://learn.chatgpt.com/docs/cli/reference#codex-plugin-marketplace). The repository includes a portable `plugin.json`, a compatible `.codex-plugin/plugin.json`, and a Codex marketplace catalog.

### Standalone skill

Download `distill-skill.zip` from the [releases page](https://github.com/kylehughes/distillation-for-agents/releases). Extract it into a directory named `distill` in your host's skills directory. The archive has `SKILL.md` at its root and includes its references, UI metadata, icon, and license.

For the Claude apps, download `distill.skill` instead and upload it under **Settings → Capabilities → Skills**. It holds the same files inside a `distill/` folder.

For Codex, a user-level skill can live at `~/.agents/skills/distill/`. Install either the standalone skill or the plugin, not both, so the skill isn't discovered twice. Other [Agent Skills](https://agentskills.io) hosts can use the same directory.

## Usage

Ask in plain language:

> Distill this design doc down to the decisions that actually matter.

> We keep adding exceptions to this onboarding process. Find the rule underneath them.

> Explain how TCP congestion control works from first principles, without leaning on the jargon.

The skill can be selected automatically when its description matches your task. It stays out of the way for simple lookups, mechanical edits, and instructions that are already clear. To select it explicitly in Codex, type `$` and choose `distillation-for-agents:distill` from the skill picker. A standalone installation uses `$distill`. In Claude Code, use `/distillation-for-agents:distill`.

Distill delivers the requested result, not a worksheet. It reports consequential tradeoffs and the checks it actually ran. When a simplification would drop a necessary distinction or overstate a claim, it keeps the complexity or narrows the claim.

The [skill](skills/distill/SKILL.md) contains the procedure. Its references are loaded on demand: [operators](skills/distill/references/operators.md) for choosing a technique, [validation](skills/distill/references/validation.md) for testing losses, [examples](skills/distill/references/examples.md), and the [foundations](skills/distill/references/foundations.md) and [sources](skills/distill/references/sources.md) behind the method. No extra tools, credentials, or runtime dependencies are needed to use the skill.

## Development

Use Python 3.10 or later for the repository checks and packaging:

```sh
python3 scripts/check.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/package.py
```

The checks verify manifest consistency, skill metadata against the `.skill` upload rules, local references, and the license. Packaging creates three archives in `dist/`: `distill-skill.zip` for manual installation, `distill.skill` for upload to the Claude apps, and `distill-plugin.zip`, which contains the shared skill, runtime manifests, and license.

Validate a local checkout with Claude Code:

```sh
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
claude --plugin-dir .
```

Claude's validator warns that the checkout's `CLAUDE.md` is not installed plugin context. It imports maintainer instructions from `AGENTS.md`; both files are excluded from the plugin archive. Validate the extracted plugin archive with `--strict` to check the shipping contents without that repository-only warning.

To test the local marketplace in Codex, run `codex plugin marketplace add "$PWD"`, install the plugin with the command above, and start a new session. When switching between a local checkout and the GitHub marketplace, remove the existing source with `codex plugin marketplace remove distillation-for-agents` before adding the replacement.

### Source updates

Record any new or changed research claim in [sources.md](skills/distill/references/sources.md) with its passage, edition, and caveat, and keep existing source IDs stable. Check every worked example against its stated premises. Keep the entrypoint short and put detailed guidance in the references.

### Releases

From a clean `main` branch, check a proposed release without changing the repository:

```sh
./release.sh --dry-run 1.0.1
```

Run `./release.sh 1.0.1` to update all manifest versions, validate and package the content, commit, tag, and push the branch and new tag together. The release workflow checks that the tag matches the manifests and publishes all three archives.

## Contributions

Not accepting source contributions. Bug reports are welcome.

## Author

[Kyle Hughes](https://kylehugh.es)

[![Bluesky][bluesky_image]][bluesky_url]  
[![LinkedIn][linkedin_image]][linkedin_url]  
[![Mastodon][mastodon_image]][mastodon_url]

[bluesky_image]: https://img.shields.io/badge/Bluesky-0285FF?logo=bluesky&logoColor=fff
[bluesky_url]: https://bsky.app/profile/kylehugh.es
[linkedin_image]: https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=fff
[linkedin_url]: https://www.linkedin.com/in/kyle-hughes
[mastodon_image]: https://img.shields.io/mastodon/follow/109356914477272810?domain=https%3A%2F%2Fmister.computer&style=social
[mastodon_url]: https://mister.computer/@kyle

## License

Distributed under the [MIT License](LICENSE).

<!-- Official OpenAI artwork: https://cdn.openai.com/brand/OpenAI-Logos-2025.zip -->
[codex_plugin_badge]: https://img.shields.io/badge/Codex_Plugin-555?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjExOC41NTcgMTIwLjc1OCA0ODQuMTM5IDQ3OS44MTgiPjxwYXRoIGZpbGw9IndoaXRlIiBkPSJNMzA0LjI0NiAyOTUuNDExVjI0OS44MjhDMzA0LjI0NiAyNDUuOTg5IDMwNS42ODcgMjQzLjEwOSAzMDkuMDQ0IDI0MS4xOTFMNDAwLjY5MiAxODguNDEyQzQxMy4xNjcgMTgxLjIxNSA0MjguMDQyIDE3Ny44NTggNDQzLjM5NCAxNzcuODU4QzUwMC45NzEgMTc3Ljg1OCA1MzcuNDQgMjIyLjQ4MiA1MzcuNDQgMjY5Ljk4MkM1MzcuNDQgMjczLjM0IDUzNy40NCAyNzcuMTc5IDUzNi45NTkgMjgxLjAxOEw0NDEuOTU0IDIyNS4zNThDNDM2LjE5NyAyMjIgNDMwLjQzNyAyMjIgNDI0LjY4IDIyNS4zNThMMzA0LjI0NiAyOTUuNDExWk01MTguMjQ1IDQ3Mi45NDVWMzY0LjAyNEM1MTguMjQ1IDM1Ny4zMDQgNTE1LjM2NCAzNTIuNTA3IDUwOS42MDggMzQ5LjE0OUwzODkuMTc0IDI3OS4wOTZMNDI4LjUxOSAyNTYuNTQzQzQzMS44NzcgMjU0LjYyNiA0MzQuNzU3IDI1NC42MjYgNDM4LjExNSAyNTYuNTQzTDUyOS43NjIgMzA5LjMyM0M1NTYuMTU0IDMyNC42NzkgNTczLjkwNSAzNTcuMzA0IDU3My45MDUgMzg4Ljk3MUM1NzMuOTA1IDQyNS40MzYgNTUyLjMxNSA0NTkuMDI0IDUxOC4yNDUgNDcyLjk0MVY0NzIuOTQ1Wk0yNzUuOTM3IDM3Ni45ODJMMjM2LjU5MiAzNTMuOTUyQzIzMy4yMzUgMzUyLjAzNCAyMzEuNzk0IDM0OS4xNTQgMjMxLjc5NCAzNDUuMzE1VjIzOS43NTZDMjMxLjc5NCAxODguNDE2IDI3MS4xMzkgMTQ5LjU0OCAzMjQuNCAxNDkuNTQ4QzM0NC41NTUgMTQ5LjU0OCAzNjMuMjY0IDE1Ni4yNjggMzc5LjEwMiAxNjguMjYyTDI4NC41NzggMjIyLjk2NEMyNzguODIyIDIyNi4zMjEgMjc1Ljk0MiAyMzEuMTE5IDI3NS45NDIgMjM3LjgzOFYzNzYuOTg2TDI3NS45MzcgMzc2Ljk4MlpNMzYwLjYyNiA0MjUuOTIyTDMwNC4yNDYgMzk0LjI1NVYzMjcuMDgzTDM2MC42MjYgMjk1LjQxNkw0MTcuMDAyIDMyNy4wODNWMzk0LjI1NUwzNjAuNjI2IDQyNS45MjJaTTM5Ni44NTIgNTcxLjc4OUMzNzYuNjk4IDU3MS43ODkgMzU3Ljk4OSA1NjUuMDcgMzQyLjE1MSA1NTMuMDc1TDQzNi42NzQgNDk4LjM3NEM0NDIuNDMxIDQ5NS4wMTcgNDQ1LjMxMSA0OTAuMjE5IDQ0NS4zMTEgNDgzLjQ5OVYzNDQuMzUyTDQ4NS4xMzggMzY3LjM4MkM0ODguNDk1IDM2OS4yOTkgNDg5LjkzNiAzNzIuMTc5IDQ4OS45MzYgMzc2LjAxOFY0ODEuNTc3QzQ4OS45MzYgNTMyLjkxNyA0NTAuMTA5IDU3MS43ODUgMzk2Ljg1MiA1NzEuNzg1VjU3MS43ODlaTTI4My4xMzQgNDY0Ljc5TDE5MS40ODYgNDEyLjAxQzE2NS4wOTQgMzk2LjY1NCAxNDcuMzQzIDM2NC4wMjkgMTQ3LjM0MyAzMzIuMzYyQzE0Ny4zNDMgMjk1LjQxNiAxNjkuNDE1IDI2Mi4zMDkgMjAzLjQ4IDI0OC4zOTNWMzU3Ljc5MUMyMDMuNDggMzY0LjUxIDIwNi4zNjEgMzY5LjMwOCAyMTIuMTE3IDM3Mi42NjVMMzMyLjA3NCA0NDIuMjM3TDI5Mi43MjkgNDY0Ljc5QzI4OS4zNzIgNDY2LjcwNyAyODYuNDkxIDQ2Ni43MDcgMjgzLjEzNCA0NjQuNzlaTTI3Ny44NTkgNTQzLjQ4QzIyMy42MzkgNTQzLjQ4IDE4My44MTMgNTAyLjY5NSAxODMuODEzIDQ1Mi4zMTRDMTgzLjgxMyA0NDguNDc1IDE4NC4yOTQgNDQ0LjYzNiAxODQuNzcxIDQ0MC43OTdMMjc5LjI5NSA0OTUuNDk4QzI4NS4wNTEgNDk4Ljg1NiAyOTAuODEyIDQ5OC44NTYgMjk2LjU2OCA0OTUuNDk4TDQxNy4wMDIgNDI1LjkyN1Y0NzEuNTA5QzQxNy4wMDIgNDc1LjM0OSA0MTUuNTYyIDQ3OC4yMjkgNDEyLjIwNCA0ODAuMTQ2TDMyMC41NTcgNTMyLjkyNkMzMDguMDgxIDU0MC4xMjIgMjkzLjIwNiA1NDMuNDggMjc3Ljg1NCA1NDMuNDhIMjc3Ljg1OVpNMzk2Ljg1MiA2MDAuNTc2QzQ1NC45MTEgNjAwLjU3NiA1MDMuMzcgNTU5LjMxMyA1MTQuNDEgNTA0LjYxMkM1NjguMTQ5IDQ5MC42OTYgNjAyLjY5NiA0NDAuMzE1IDYwMi42OTYgMzg4Ljk3NkM2MDIuNjk2IDM1NS4zODcgNTg4LjMwMyAzMjIuNzYyIDU2Mi4zOTIgMjk5LjI1QzU2NC43OTEgMjg5LjE3MyA1NjYuMjMxIDI3OS4wOTYgNTY2LjIzMSAyNjkuMDI0QzU2Ni4yMzEgMjAwLjQxMSA1MTAuNTcxIDE0OS4wNjcgNDQ2LjI3NCAxNDkuMDY3QzQzMy4zMjIgMTQ5LjA2NyA0MjAuODQ2IDE1MC45ODQgNDA4LjM3IDE1NS4zMDVDMzg2Ljc3NSAxMzQuMTkyIDM1Ny4wMjYgMTIwLjc1OCAzMjQuNCAxMjAuNzU4QzI2Ni4zNDIgMTIwLjc1OCAyMTcuODgzIDE2Mi4wMiAyMDYuODQzIDIxNi43MjFDMTUzLjEwNCAyMzAuNjM3IDExOC41NTcgMjgxLjAxOCAxMTguNTU3IDMzMi4zNTdDMTE4LjU1NyAzNjUuOTQ2IDEzMi45NSAzOTguNTcxIDE1OC44NjEgNDIyLjA4M0MxNTYuNDYyIDQzMi4xNiAxNTUuMDIyIDQ0Mi4yMzcgMTU1LjAyMiA0NTIuMzA5QzE1NS4wMjIgNTIwLjkyMiAyMTAuNjgyIDU3Mi4yNjYgMjc0Ljk3OCA1NzIuMjY2QzI4Ny45MzEgNTcyLjI2NiAzMDAuNDA3IDU3MC4zNDkgMzEyLjg4MyA1NjYuMDI4QzMzNC40NzMgNTg3LjE0MSAzNjQuMjIyIDYwMC41NzYgMzk2Ljg1MiA2MDAuNTc2WiIvPjwvc3ZnPg%3D%3D
