import datetime
import regex as re

names = ['20231211.json','20231212.json','20231213.json','20231214.json','20231314.json']

print(re.search('[0-9]{8}', max(names)).group(0))
