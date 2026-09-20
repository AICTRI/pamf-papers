# China-Track Expert Blind Study

Two sequential rounds. Each round is self-contained.

| Round | Directory | Task | Published result |
|---|---|---|---|
| Round 1 | [`round1/`](round1/README.md) | Unbounded Mandatory/Recommended/Optional rating of all 61 viewpoints on Case X | `round1/round1_agreement.json` |
| Round 2 | [`round2/`](round2/README.md) | Forced top-20 ranking on Case X and Case M | `round2/round2_results.json` |

Round 1 and Round 2 use different outcome spaces (three-category rating vs.
binary forced selection). Their agreement statistics are not directly
comparable and are never merged into a single kappa.

Only aggregate statistics are released. Participant metadata and per-item
individual ratings are withheld; see [`../../PRIVACY.md`](../../PRIVACY.md).

This track is the fallback to the international `../expert-study/` track and is
not pooled with it without an explicit cross-channel analysis.
