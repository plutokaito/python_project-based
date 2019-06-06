from collections import defaultdict
import re

d = defaultdict(int)
with open('in.txt', "r")  as f:
    for line in f:
        for words in filter(lambda x:x,re.split(r"\s", line)):
            d[words] += 1

print(d)
