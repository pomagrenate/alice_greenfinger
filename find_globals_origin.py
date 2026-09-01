import os
import glob
import re

for pyf in glob.glob('*.py'):
    with open(pyf, 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
        if '175' in txt and ('global' in txt.lower() or 'DAT_' in txt):
            print(f"Found 175 globals in script: {pyf}")

for md in glob.glob('notes/*.md'):
    with open(md, 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
        if '175' in txt and 'DAT_' in txt:
            print(f"Found 175 globals in note: {md}")
