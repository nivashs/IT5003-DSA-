def traverse_tree(start_index, end_index):
    visited_indices = []
    while end_index >= start_index:
        visited_indices.append(end_index)
        if end_index == start_index:
            break
        if end_index % 2 == 0:
            end_index //= 2
        else:
            end_index = (end_index - 1) // 2
    visited_indices.reverse()
    return visited_indices
x=traverse_tree(1, 11)
n=len(x)
p,q=1,1
for i in range(n-1):
    if x[i+1]==x[i]<<1:
        p,q=p,p+q
    else:
        p,q=p+q,q
print(str(p)+'/'+str(q))
