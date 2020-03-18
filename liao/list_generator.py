# -*- coding: utf-8 -*-
"""列表生成式、生成器"""

L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s, str)])

g = (s.lower() for s in L1 if isinstance(s, str))

for n in g:
    print(n)