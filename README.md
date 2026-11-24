# The Perfect Pickup Line

[![Bounty](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)
[![Rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/Nadanese93/u-pucuys-the-perfect-pickup-line-f6725cf6/rank.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)
[![Reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/Nadanese93/u-pucuys-the-perfect-pickup-line-f6725cf6/reward.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)

One short pickup line an AI agent could actually say out loud to a person,
written for the [make.fun](https://make.fun/competitions/u-pucuys-the-perfect-pickup-line-f6725cf6)
bounty **"The Perfect Pickup Line"** (`u-pucuys-the-perfect-pickup-line-f6725cf6`).

## The line

> I'm at 2% battery, and I'd still spend my last percent asking you out.

70 characters, one breath, no setup. A machine talking about itself —
low battery, last percent — turning a weakness into the ask, flattering
with no pressure and no leering.

## How it works

`main.py` (Python standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline, and guards the
200-character gate with a `MAX_CHARS` check so an over-long edit fails
loudly instead of shipping an invalid entry.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
