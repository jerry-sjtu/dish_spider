# -*- coding: utf-8 -*-
import sys,json,codecs
o_fh = codecs.open(sys.argv[1], 'r', 'utf-8')
t_fh = codecs.open(sys.argv[2], 'w', 'utf-8')

for line in o_fh:
    print line
    tag, word = line.strip().split(',')
    arr = word.split()
    for x in arr:
        line = '%s\t%s\n' % (x, tag)
        t_fh.write(line)
t_fh.close()
o_fh.close()
