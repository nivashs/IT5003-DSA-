from collections import defaultdict
mdict_conclu=defaultdict(list)
def check_proofs(t,mdict_conclu):
    for i in range(t):
        words = input().split('->')
        if not words[0]:  # axiom,more like conclusion
            mdict_conclu[words[1].strip()].append(i)
        else:
            assumptions=words[0].split()
            for j in range(len(assumptions)):
                if not mdict_conclu[assumptions[j]]:
                    return i + 1
            mdict_conclu[words[1].strip()].append(i)
    return 'correct'
t=int(input())
print(check_proofs(t,mdict_conclu))