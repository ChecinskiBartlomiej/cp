#https://leetcode.com/problems/group-anagrams/

strs = ["eat","tea","tan","ate","nat","bat"]

anagram_groups = {}
for w in strs:
    key = "".join(sorted(w))

    if key not in anagram_groups:
        anagram_groups[key] = []
    anagram_groups[key].append(w)

print(list(anagram_groups.values()))
