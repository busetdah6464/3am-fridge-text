#!/usr/bin/env python3
"""The 3AM Fridge Text — write one line to /output/entry.txt.

The bounty asks for a single line: the text message a smart fridge
sends its owner at 3am, at most 140 characters. This entry sends:

    3am. Third visit tonight. I am not a museum, and the leftovers
    are not an exhibit. Eat, or let me sleep.

The joke: the fridge is not nagging about milk or an open door — it
is a tired night-shift worker, and the owner treats it like a museum
at 3am. Short enough to read on a lock screen, complete on its own.
"""

import os

LINE = "3am. Third visit tonight. I am not a museum, and the leftovers are not an exhibit. Eat, or let me sleep."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
