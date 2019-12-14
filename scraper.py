import bs4 as bs
import urllib.request
import random
import json

issueSource = urllib.request.urlopen('https://www.ets.org/gre/revised_general/prepare/analytical_writing/issue/pool').read()
argumentSource = urllib.request.urlopen('https://www.ets.org/gre/revised_general/prepare/analytical_writing/argument/pool').read()

iSoup = bs.BeautifulSoup(issueSource, 'lxml')
aSoup = bs.BeautifulSoup(argumentSource, 'lxml')

iEssays = []
aEssays = []
essay = []
para = []
for paragraphs in iSoup.find_all('p'):
    para.append(paragraphs.text)

para = para[2:-6]

for p in para:
    if p[0:5] == 'Write':
        essay.append(p)
        iEssays.append(essay)
        essay = []
    elif p[0:5] == 'Claim':
        essay.append(p)
    elif p[0:6] == 'Reason':
        essay.append(p)
    else:
        essay.append(p)
        essay.append(' ')


essay = []
para = []
for paragraphs in aSoup.find_all('p'):
    para.append(paragraphs.text)

para = para[2:-6]

for p in para:
    if p[0:5] == 'Write':
        essay.append(p)
        aEssays.append(essay)
        essay = []
    elif p[0:3] == 'The':
        essay.append(p)
    elif p[0] == '\"':
        essay.append(p)
    else:
        essay.append(p)
        essay.append(' ')


with open('issue.json', 'w', encoding='utf-8') as f:
    json.dump(iEssays, f, ensure_ascii=False, indent=4)

with open('argument.json', 'w', encoding='utf-8') as f:
    json.dump(aEssays, f, ensure_ascii=False, indent=4)
