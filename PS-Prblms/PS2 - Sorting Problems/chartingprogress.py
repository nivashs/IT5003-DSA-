import sys
def mat_transpose(l):
    return [[l[i][j] for i in range(len(l))] for j in range(len(l[0]))]
def convert(lst):
    ans=mat_transpose(sorted(mat_transpose([list(x) for x in lst]),reverse=True))
    return ans
m,ans = [],[]
for line in sys.stdin:
    if line.strip()!= '':
        m.append(line.strip())
    else:
        ans.append(convert(m))
        m.clear()
if m:
    ans.append(convert(m))
for i in range(len(ans)):
    for k in ans[i]:
        print(''.join(k))
    if i!=len(ans)-1:print()

