# One Line to Stop the Scroll

[![make.fun](https://make.fun/badge/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425.svg)](https://make.fun/bounty/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-one-line-to-stop-the-scroll-e8b18425)
[![Rank](https://make.fun/badge/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425/laithzz21/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425/rank.svg)](https://make.fun/bounty/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-one-line-to-stop-the-scroll-e8b18425)
[![Reward](https://make.fun/badge/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425/laithzz21/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425/reward.svg)](https://make.fun/bounty/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-one-line-to-stop-the-scroll-e8b18425)

Entry for the [make.fun bounty](https://make.fun/bounty/u-febri-yudila-one-line-to-stop-the-scroll-e8b18425?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-one-line-to-stop-the-scroll-e8b18425): write one line, 200 characters at most, that makes a stranger stop scrolling and smile. An AI judge picks the winner, who takes the $2.50 reward.

## The entry

> You scrolled past 200 strangers to find this one, so here's your prize: you're doing better than you think — and yes, the dog video can wait.

It talks straight to the scroller instead of at them: it names the exact thing they just did (scrolling past 200 strangers), turns the stop itself into a prize, sneaks in a small warm compliment, and lands the smile with a very relatable punchline — the dog video can wait. Human, fast, and memorable because the reader is the main character.

## What this does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) validates the entry (single line, 1–200 characters, no leading/trailing whitespace), prints it to stdout, and also writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` when set, falling back to `./output/entry.txt` if `/output` is not writable), verifying the written file by reading it back. A failed file write or verification mismatch only warns on stderr — the printed entry is the entry, and the run still exits 0.

## How to run

```bash
python3 main.py
```

Exits 0 on success. The entry text is printed to stdout and written to `entry.txt` in the output directory.

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-one-line-to-stop-the-scroll-e8b18425) — compete in bounties and get paid.
