def groupAnagrams(strs):
    groups = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())

def main():
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(groupAnagrams(["won", "now", "aaa", "ooo", "ooo"]))

if __name__ == "__main__":
    main()
