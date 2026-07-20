class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = []
        hashlists = []

        for word in strs:
            charFreq = {}

            for letter in word:
                if letter in charFreq:
                    charFreq[letter]+= 1
                else:
                    charFreq[letter] = 1
            
            foundGroup = False

            for i in range(len(hashlists)):
                if charFreq==hashlists[i]:
                    sublists[i].append(word)
                    foundGroup = True
                    break;
            
            if not foundGroup:
                sublists.append([word])
                hashlists.append(charFreq)
        return sublists

        

        