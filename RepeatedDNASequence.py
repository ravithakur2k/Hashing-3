# Time is O(10*n), space is O(n) as well for using the hashset.

#The intuition here is to use the loop through 10 elements at a time and check if it existed more than one times, if it did then add to the result.
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashSet = set()
        resultSet = set()
        for i in range(0, len(s) - 10 + 1):
            currStr = s[i: i + 10]
            if currStr not in hashSet:
                hashSet.add(currStr)
            else:
                resultSet.add(currStr)

        return list(resultSet)


# The time is almost the same: (n). This is just using the rolling hash, hence the set will have the rolling hash value and it will compared to other 10 characters rolling hashvalue.
# If another one is found then add to the result. So instead of comparing string values, here we compare hash values. Now why rolling hash because when we reach the character which
# is greater than 10 then we have delete the left most char which is done with pos factorial and we are anyways adding the curr hash value.
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        allSeq = set()
        result = set()

        hash_val = 0
        map_char = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
        posFac = 4 ** 10

        for i in range(len(s)):
            hash_val = hash_val * 4 + map_char[s[i]]

            if i >= 10:
                hash_val -= posFac * map_char[s[i - 10]]

            if i >= 9:
                if hash_val in allSeq:
                    result.add(s[i - 9:i + 1])
                else:
                    allSeq.add(hash_val)

        return list(result)