import re

d = open('word.txt', 'r').read()
lines = d.split('\n')

res1 = ''
for line in lines:
    if line == '':
        continue
    
    s1 = line.split(',')
    if line.find('[') != -1:
        t = s1[0].split('[')
        hira = t[0][:-1]
        kanji = t[1][:-1]
        kor = s1[1][1:]
        res1 += '{}, {} {}\n'.format(kanji, hira, kor)
    else:
        hira = s1[0]
        kor = s1[1][1:]
        res1 += '{}, {}\n'.format(hira, kor)

open('out.txt', 'w').write(res1)
        
