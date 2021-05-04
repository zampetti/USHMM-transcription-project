# 

from fuzzysearch import find_near_matches
my_string = 'aaaPATERNaaa'
matches = find_near_matches('PATTERN', my_string, max_l_dist=1)

# print([my_string[m.start:m.end] for m in matches])

for m in matches:
    print(m.matched)