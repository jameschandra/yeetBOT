kmp_table = []

def kmp_border_function(pattern,j):
    k = j-1
    if k < 0:
        return -1
    elif k == 0:
        return 0
    else:

        prefix_array = []
        suffix_array = []
        prefix = ""
        suffix = ""
        for i in range(k):
            prefix += pattern[i]
            prefix_array.append(prefix)
        for j in range(k,0,-1):
            suffix = pattern[j] + suffix
            suffix_array.append(suffix)
            print(suffix)



def is_same(string1,string2):
    # exactmatch
    if string1 == string2:
        return True
    else:
        return False

# for i in range(len(pattern)):
#     kmp_table.append(kmp_border_function(pattern,i))
kmp_border_function("Vaza",4)