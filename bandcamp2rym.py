#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyperclip
import re
import sys

pattern = re.compile(r'(\d{1,2})\.\n\s*\n(.*)\s(\d{2}:\d{2})(?:\n\s*\n)?')

with open(sys.argv[1], 'r') as file:
    trackList = file.read()

converted = re.sub(pattern, r'\1|\2|\3\n', trackList)
converted = converted.replace('|0', '|')
converted = converted.strip()

pyperclip.copy(converted)

print('Result has been copied to clipboard.')
print(converted)