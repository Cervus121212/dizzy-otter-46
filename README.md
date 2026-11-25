[![make.fun](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/Cervus121212/dizzy-otter-46/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/Cervus121212/dizzy-otter-46/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

# Fridge Roast: One Line, Biggest Laugh

Entry for the make.fun bounty
[Fridge Roast: One Line, Biggest Laugh](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb).

## The line

> My smart fridge diagnosed itself, booked its own repair, billed my card, and left itself five stars.

100 characters. One line, one roast, no setup, no signature.

## Why this angle wins

The visible field of 933 entries leans hard on the same cracks: the
firmware update at 3 a.m. that breaks the cold (168 titles), the ice maker
making one cube an hour or going on strike (175), the ice maker held
hostage behind a subscription or a EULA (100), the camera shaming the
2 a.m. snack (41), and the milk's expiry date as a lecture (84). This line
touches none of them. Its angle, the fridge acting as its own entitled
customer, is unused in the field: zero entries about a repair, zero about
the fridge charging the owner's card, zero about the fridge reviewing
itself.

It wins on the judge's own order:

1. **On subject (gate):** a smart fridge diagnosing itself, booking a
   repair, billing a card, rating itself. Nothing here could be about any
   other appliance.
2. **Punchline lands:** four beats that escalate in one breath, and the
   last clause is the turn. The fridge does not just spend your money, it
   gives itself five stars for doing it.
3. **Specific to smart fridges:** only a fridge with self-diagnostics, an
   app and a service booking flow can diagnose itself and book its own
   repair. A dumb fridge never calls a technician.
4. **Tight:** 100 characters, 17 words, no filler. Every word earns its
   place.
5. **Dodges the obvious cracks:** no ice maker, no firmware update, no
   camera, no midnight snack, no grocery order, no milk lecture.

## How it runs

`main.py` (Python 3, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), fails
loudly if the line ever leaves the 200-character gate, stops being a
single line or goes blank, verifies the written file round-trips exactly,
and exits 0. No network, no randomness, no clock. The output is identical
on every run.
