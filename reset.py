#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os

FIRST_BOOT_FILE = "data/extra/first_boot.txt"

os.system('clear')

try:
	os.remove(FIRST_BOOT_FILE)
	print("oasis has been reset with success!")
except OSError:
	print("Error resetting oasis: oasis has already been reset or hasn't yet been ran.")
