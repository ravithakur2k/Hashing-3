# Time complexity: O(n), for building song map and then creating the result with the highest freq of the genre. If freq is same then add both to the result
# Space is also O(n)

from collections import defaultdict

class Solution:

    def favoritegenre(self, userMap, genreMap):
        songMap = {}

        result = defaultdict(list)
        for key, val in genreMap.items():
            for song in val:
                songMap[song] = key

        print(songMap)

        for key, val in userMap.items():
            freqMap = {}
            maxVal = 0
            for song in val:
                genre = songMap[song]
                if genre not in freqMap:
                    freqMap[genre] = 1
                else:
                    freqMap[genre] += 1
                maxVal = max(freqMap[genre], maxVal)
            for k, v in freqMap.items():
                if v == maxVal:
                    result[key].append(k)

        return result

userSongs = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma": ["song5", "song6", "song7"]
}

songGenres = {
    "Rock": ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno": ["song2", "song4"],
    "Pop": ["song5", "song6"],
    "Jazz": ["song8", "song9"]
}
solution = Solution()
res = solution.favoritegenre(userSongs, songGenres)
print(res)