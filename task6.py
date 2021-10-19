import math
def ari_sum():
    d = seq[1] - seq[0]
    an = seq[0] + d * len(seq)
    return an
def geo_mul():
    q = seq[1] / seq[0]
    bn = round(seq[len(seq) - 1] * q)
    return bn
def sqrt_ari():
    sqrt_list = []
    for item in seq:
        msq = math.sqrt(item)
        sqrt_list.append(msq)
    d = sqrt_list[1] - sqrt_list[0]
    an = sqrt_list[0] + d * len(seq)
    an = an ** 2
    return an
def sqrt_tri():
    sqrt_list = []
    for item in seq:
        msq = item ** (1/3)
        sqrt_list.append(msq)
    d = sqrt_list[1] - sqrt_list[0]
    an = sqrt_list[0] + d * len(seq)
    an = an ** 3
    return an
seqq = (input('insert your sequence:'))
mo_seq = list(seqq.split(' '))
seq = list(map(int, mo_seq))
if seq[1] - seq[0] == seq[2] - seq[1]:
    print(round(ari_sum()))
elif seq[1] / seq[0] == seq[2] / seq[1]:
    print(round(geo_mul()))
elif math.sqrt(seq[1]) - math.sqrt(seq[0]) == math.sqrt(seq[2]) - math.sqrt(seq[1]):
    print(round(sqrt_ari()))
elif (seq[1] ** (1/3)) - (seq[0] ** (1/3)) == (seq[2] ** (1/3)) - (seq[1] ** (1/3)):
    print(round(sqrt_tri()))