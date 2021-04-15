#!/usr/local/bin/python3
import re

d = open('jlpt_n2.txt', 'r').read()
lines = d.split('\n')

cnt = 0
res = ''
for line in lines:
    cnt += 1
    line = line[2:]

    so = line.find(' ')
    word = line[:so]
    desc = line[so+1:]

    # print(word)
    # print(desc)

    kanji = ''
    kanji_start = word.find('[')
    if(kanji_start != -1):
        kanji_end = word.find(']')
        kanji = word[kanji_start+1:kanji_end]
        hiragana = word[:kanji_start]

        desc = hiragana + ', ' + desc
        word = kanji

    res += word + ';' + desc + '\n'
    # break
    
print(cnt)
open('out.txt', 'w').write(res)

