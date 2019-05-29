import re

d = open('word.txt', 'r').read()
lines = d.split('\n')

cnt = 0 
res1 = ''
for line in lines:
    # if cnt == 20:
    #     break
    cnt +=1
    
    print cnt, line
    if line == '':
        continue
    if line[0] == '[':
        continue
    
    s1 = line.split('\t')
    print s1

    n = []
    for s in s1:
        if s=='' or s==' ':
            continue
        n.append( s )

    if len(n) == 3:
        hira = n[0]
        kanji = n[1].replace('[','').replace(']','')
        kor = n[2]
    
        res1 += '{}: {} {}\n'.format(kanji, hira, kor)
    else:
        hira = n[0]
        kor = n[1]
        res1 += '{}: {}\n'.format(hira, kor)

print res1        
open('out.txt', 'w').write(res1)
        
