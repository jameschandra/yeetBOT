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
        to_return = 0
        for i in range(k):
            prefix += pattern[i]
            prefix_array.append(prefix)
        for j in range(k,0,-1):
            suffix = pattern[j] + suffix
            suffix_array.append(suffix)
            print(suffix)
        for l in range(len(prefix_array)):
            if prefix_array[l] == suffix_array[l]:
                to_return = len(prefix_array[l])
        return to_return



def is_same(string1,string2):
    # exactmatch
    if string1 == string2:
        return True
    else:
        return False

# for i in range(len(pattern)):
#     kmp_table.append(kmp_border_function(pattern,i))
