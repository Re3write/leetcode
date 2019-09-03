s="ababababab"
p="aab"

length_p = len(p)
length_s = len(s)
# if length_s < length_p:
#     return []
result = []
for i in range(length_s):
    set_p = list(p)
    if i <= (length_s - length_p):
        set_s = [s[index] for index in range(i, i + length_p)]
        if sorted(set_p) == sorted(set_s):
            result.append(i)
print(result)