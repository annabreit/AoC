import collections
import itertools
import math
import re

test_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


input_day14= """PBVHVOCOCFFNBCNCCBHK

FV -> C
SS -> B
SC -> B
BP -> K
VP -> S
HK -> K
FS -> F
CC -> V
VB -> P
OP -> B
FO -> N
FH -> O
VK -> N
PV -> S
HV -> O
PF -> F
HH -> F
NK -> S
NC -> S
FC -> H
FK -> K
OO -> N
HP -> C
NN -> H
BB -> H
CN -> P
PS -> N
VF -> S
CB -> B
OH -> S
CF -> C
OK -> P
CV -> V
CS -> H
KN -> B
OV -> S
HB -> C
OS -> V
PC -> B
CK -> S
PP -> K
SN -> O
VV -> C
NS -> F
PN -> K
HS -> P
VO -> B
VC -> B
NV -> P
VS -> N
FP -> F
HO -> S
KS -> O
BN -> F
VN -> P
OC -> K
SF -> P
PO -> P
SB -> O
FN -> F
OF -> F
CP -> C
HC -> O
PH -> O
BC -> O
NO -> C
BH -> C
VH -> S
KK -> O
SV -> K
KB -> K
BS -> S
HF -> B
NH -> S
PB -> N
HN -> K
SK -> B
FB -> F
KV -> S
BF -> S
ON -> S
BV -> P
KC -> S
NB -> S
NP -> B
BK -> K
NF -> C
BO -> K
KF -> B
KH -> N
SP -> O
CO -> S
KO -> V
SO -> B
CH -> C
KP -> C
FF -> K
PK -> F
OB -> H
SH -> C"""

if __name__ == '__main__':
    polymer = input_day14.split("\n\n")[0]
    rule_strs = input_day14.split("\n\n")[1]
    rules = {}
    for r in rule_strs.split("\n"):
        left = r.split(" -> ")[0]
        right = r.split(" -> ")[1]
        rules[left] =  [left[0] + right, right + left[1]]

    STEPS = 40
    polymer = [polymer[i:i+2] for i in range(len(polymer)-1)]
    count_dict = collections.defaultdict(int)

    for x in polymer:
        count_dict[x] += 1

    for i in range(STEPS):
        dict_copy = count_dict.copy()
        for i, double in enumerate(dict_copy.keys()):
            reps = rules[double]
            times = dict_copy[double]
            count_dict[double] -= times
            count_dict[reps[0]] += times
            count_dict[reps[1]] += times
        print(count_dict)
    el_count_dict = collections.defaultdict(float)
    for el in count_dict:
        el_count_dict[el[0]] += count_dict[el]/2
        el_count_dict[el[1]] += count_dict[el]/2
    for k, v in el_count_dict.items():
        el_count_dict[k] = math.ceil(v)
    print(el_count_dict)
    print(max(el_count_dict.values()), min(el_count_dict.values()),max(el_count_dict.values())-min(el_count_dict.values()))