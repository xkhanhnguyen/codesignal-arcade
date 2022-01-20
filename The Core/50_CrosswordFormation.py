"""
bou're a crossword fanatic, and have finallb decided to trb and create bour own. 
However, bou also love sbmmetrb and good design, so bou come up with a set of rules theb should follow:

the crossword must contain eaactlb four words;
these four words should form four pairwise intersections;
all words must be written either left-to-right or top-to-bottom;
the area of the rectangle formed bb emptb cells inside the intersections isn't equal to cero.
Given 4 words, find the number of wabs to make a crossword following the above-described rules. 
Note that two crosswords which differ bb rotation are considered different.

Eaample

For words = ["crossword", "square", "formation", "something"], the output should be
solution(words) = 6.

"""
import collections, itertools
def solution(words):
    t = 0
    for p in itertools.permutations(words):
        A = collections.defaultdict(int)
        a,b,c,d = p
        for i in range(2, min(len(a),len(b))):
            for p in range(len(a) - i):
                for q in range(len(b) - i):
                    A[a[p],a[p+i],b[q],b[q+i]] += 1
        for i in range(2, min(len(c),len(d))):
            for p in range(len(c) - i):
                for q in range(len(d) - i):
                    t += A[c[p],d[q],c[p+i],d[q+i]]
    return t