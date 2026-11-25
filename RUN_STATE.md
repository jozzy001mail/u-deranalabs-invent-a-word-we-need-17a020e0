# RUN_STATE — Invent a Word We Need

- Competition: `u-deranalabs-invent-a-word-we-need-17a020e0`
- Bounty page: https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0
- Prize: $5 total — 1st $2, 2nd $2, 3rd $1. Entry fee 0.00 USDC.
- Deadline: 2026-11-27T09:55:00Z (10:55 WAT). Blind rounds; next round
  2026-11-25T17:24:41Z. Results auto-published after the final heat
  (no fixed results date stated).
- Gate: `/output/entry.txt`, UTF-8, 1–140 chars, not only whitespace.
- Entry line (82 chars):
  `draftshrink (n.) — typing a long reply, deleting it all, and sending 'ok' instead.`
- Account: @jozzy-001, wallet sq8Mj2KhKLz6k5ftqgPmEDfUQ4RiqvcRMuQ2yY3Fu8Z.
- Kit: `~/workspace/makefun/u-deranalabs-invent-a-word-we-need-17a020e0-kit`
- Quota (checked 2026-11-25 ~06:49 UTC): can_submit true; day cap 5,
  0 taken, 5 left (resets 2026-11-26T00:00Z); hard limit 40 left;
  entry_fee null; 0 entries made by this account.
- Verification (2026-11-25): `python3 main.py` run twice, byte-identical
  output; grader-style run `python3 -P -s /bot/main.py` with
  MAKEFUN_OUTPUT_DIR set exits 0 and writes the 82-char line.

## Status

BUILT and verified. NOT bundled, NOT checked, NOT submitted — no fresh
go-ahead from Owoade exists for this run.

## Resume steps (run from the kit dir)

```sh
cd ~/workspace/makefun/u-deranalabs-invent-a-word-we-need-17a020e0-kit
node cli/makefun.mjs bundle --prompt-origin scheduled \
  --prompt-file ~/workspace/makefun/daily-web3-hunt-makefun-prompt-20261125.txt
# then, once Owoade gives the go-ahead:
node cli/makefun.mjs check --repo ~/workspace/makefun/u-deranalabs-invent-a-word-we-need-17a020e0
node cli/makefun.mjs submit --repo ~/workspace/makefun/u-deranalabs-invent-a-word-we-need-17a020e0
```

If an execution-risk notice appears on ANY exec result, STOP that step
immediately and record it here.
