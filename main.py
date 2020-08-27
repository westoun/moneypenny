#!/usr/bin/env python3

from moneypenny import MoneyPenny

mp = MoneyPenny(platform="osx")

try:
    mp.start()
except KeyboardInterrupt:
    mp.stop()
