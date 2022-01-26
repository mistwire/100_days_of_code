#!/usr/bin/env python3

import sys, time
import sevseg

try:
    while True:
        print("\n" * 60)

        # Get the current time from the computer clock
        currentTime = time.localtime()
        # % 12 so we can use a 12 hour format instead of 24
        hours = str(currentTime.tm_hour % 12)
        if hours == "0":
            hours = "12"
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        # Get the digit strings from the sevseg module
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        print(hTopRow + "    " + mTopRow + "    " + sTopRow)
        print(hMiddleRow + "    " + mMiddleRow + "    " + sMiddleRow)
        print(hBottomRow + "    " + mBottomRow + "    " + sBottomRow)
        print()
        print("Press Ctrl-C to quit.")

        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break

except KeyboardInterrupt:
    print("Digital Clock by Al Sweigart, copied for 100 days of code by Sean Doyle")
    sys.exit()
