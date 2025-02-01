def find_duplicates_nested_loop(l: list, all = False) -> list:
    s = l.copy()
    d = []
    for i in range(len(s)-1):
        a = True
        j = i+1
        while j<len(s):
            if (s[i]==s[j]):
                if a:
                    d.append(s.pop(j))
                    if not all:
                        a = False
                else:
                    s.pop(j)
            else:
                j += 1
    return d

def find_duplicates_dictionary(l: list, all = False) -> list:
    ld = {}
    d = [] if all else set()
    for i in l:
        if i in ld:
            d.append(i) if all else d.add(i)
        else:
            ld[i] = True
    return list(d)

if __name__ == "__main__":
    sample1 = [3, 7, 5, 6, 7, 4, 8, 5, 7, 66]
    sample2 = [3, 5, 6, 4, 4, 5, 66, 6, 7, 6]
    sample3 = [3, 0, 5, 1, 0]
    sample4 = [3]

    print("Sample 1 (nested):", find_duplicates_nested_loop(sample1))
    print("Sample 2 (nested):", find_duplicates_nested_loop(sample2))
    print("Sample 3 (nested):", find_duplicates_nested_loop(sample3))
    print("Sample 4 (nested):", find_duplicates_nested_loop(sample4))
    '''
    print("Sample 1 (nested):", find_duplicates_nested_loop(sample1, all=True))
    print("Sample 2 (nested):", find_duplicates_nested_loop(sample2, all=True))
    print("Sample 3 (nested):", find_duplicates_nested_loop(sample3, all=True))
    print("Sample 4 (nested):", find_duplicates_nested_loop(sample4, all=True))
    '''
    print("Sample 1 (dict):", find_duplicates_dictionary(sample1))
    print("Sample 2 (dict):", find_duplicates_dictionary(sample2))
    print("Sample 3 (dict):", find_duplicates_dictionary(sample3))
    print("Sample 4 (dict):", find_duplicates_dictionary(sample4))
    '''
    print("Sample 1 (dict):", find_duplicates_dictionary(sample1, all=True))
    print("Sample 2 (dict):", find_duplicates_dictionary(sample2, all=True))
    print("Sample 3 (dict):", find_duplicates_dictionary(sample3, all=True))
    print("Sample 4 (dict):", find_duplicates_dictionary(sample4, all=True))
    '''