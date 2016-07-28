#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess


AFPLAY = '/usr/bin/afplay'

def afplay(audio_file):
    return subprocess.check_call([AFPLAY, audio_file])


if __name__ == '__main__':
    try:
        audio_file = sys.argv[1]
        afplay(audio_file)
    except IndexError:
        print 'Usage: ...'