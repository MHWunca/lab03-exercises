def find_duplicates_nested_loop(l: list) -> list:
    s = l.copy()
    d = []
    for i in range(len(s)-1):
        a = True
        j = i+1
        while j<len(s):
            if (s[i]==s[j]):
                if a:
                    d.append(s.pop(j))
                    a = False
                else:
                    s.pop(j)
            else:
                j += 1
    return d

def find_all_duplicates_nested_loop(l: list) -> list:
    s = l.copy()
    d = []
    for i in range(len(s)-1):
        j = i+1
        while j<len(s):
            if (s[i]==s[j]):
                d.append(s.pop(j))
            else:
                j += 1
    return d

if __name__ == "__main__":
    sample1 = [3, 7, 5, 6, 7, 4, 8, 5, 7, 66]
    sample2 = [3, 5, 6, 4, 4, 5, 66, 6, 7, 6]
    sample3 = [3, 0, 5, 1, 0]
    sample4 = [3]

    print("Sample 1:", find_duplicates_nested_loop(sample1))
    print("Sample 2:", find_duplicates_nested_loop(sample2))
    print("Sample 3:", find_duplicates_nested_loop(sample3))
    print("Sample 4:", find_duplicates_nested_loop(sample4))
    '''
    print("Sample 1:", find_all_duplicates_nested_loop(sample1))
    print("Sample 2:", find_all_duplicates_nested_loop(sample2))
    print("Sample 3:", find_all_duplicates_nested_loop(sample3))
    print("Sample 4:", find_all_duplicates_nested_loop(sample4))
    '''