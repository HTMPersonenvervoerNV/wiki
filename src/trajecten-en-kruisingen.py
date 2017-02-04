#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

alles = []

def renderBuffer(buf):
    global alles

    p = re.compile('^Tram [0-9enK, ()]+(Avenio)?$|^Bus [N0-9en ]+$')

    if len(buf) == 0:
        return

    filenames = set(re.findall(r"[\w]+", buf[0])) - set(['Traject', 'Kruising', 'en'])

    alles.append((buf[0].replace('\n', '').replace('\r', ''), list(filenames)[0]),)

    buf[0] = '# ' + buf[0]
    buf.insert(1, '## Maatregel')

    for x in range(0, len(buf)):
        if buf[x].startswith('Beide richtingen') or buf[x].startswith('Eén richting') or buf[x].startswith('Alle gevallen'):
            buf[x] = '### ' + buf[x]
        elif buf[x].startswith('Reizigerseffecten') or buf[x].startswith('Vervangend vervoer') or buf[x].startswith('Aanvullende maatregelen'):
            buf[x] = '## ' + buf[x]
        elif buf[x].startswith('Vervallen halten:') or p.match(buf[x]):
            buf[x] = '#### ' + buf[x]

    output = ''.join(buf)

    for filename in filenames:
        open(filename + '.md', 'w').write(output)

with open(sys.argv[1], 'r') as f:
    buf = []

    content = f.readlines()

    for x in content:
        if x.startswith('Traject') or x.startswith('Kruising'):
            renderBuffer(buf)
            buf = []

        buf += [x]

    renderBuffer(buf)

with open('index.md', 'w') as f:
    f.write('\n'.join(['[%s](%s.md)' % (x, y) for x, y in alles]))

