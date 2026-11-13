"""Quote check for research and copy docs.

Usage: python3 -I verify_quotes.py DOC.md SOURCE [SOURCE ...]
SOURCE can be a file or a folder (searched recursively): raw call transcripts,
quote libraries (CSV), existing research docs.

Checks every bullet line that starts with - " ... For each quoted passage it
splits on ... and [brackets], and checks every fragment of 4+ words appears
verbatim (case and punctuation ignored) somewhere in the sources.
Exit code 1 if anything is not found.
"""
import re, sys, glob, os

def norm(s):
    s = s.lower().replace('’', "'").replace('‘', "'")
    return re.sub(r'[^a-z0-9 ]', '', re.sub(r'\s+', ' ', s))

src = []
for p in sys.argv[2:]:
    files = glob.glob(os.path.join(p, '**', '*'), recursive=True) if os.path.isdir(p) else [p]
    for f in files:
        if os.path.isfile(f):
            src.append(open(f, errors='ignore').read())
S = norm(' '.join(src))
bad = tot = 0
for line in open(sys.argv[1], errors='ignore'):
    if not line.lstrip().startswith('- "'):
        continue
    for q in re.findall(r'["“]([^"”]{15,})["”]', line):
        for part in re.split(r'\.\.\.|…|\[[^\]]*\]', q):
            if len(part.split()) < 4:
                continue
            tot += 1
            if norm(part).strip() not in S:
                bad += 1
                print('NOT FOUND:', part.strip()[:150])
print(f'{tot} quote fragments checked, {bad} not found')
sys.exit(1 if bad else 0)
