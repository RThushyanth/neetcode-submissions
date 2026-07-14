class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        greater_dict = {}

        for i in range(0,len(words)-1):
            for j in range(0,len(words[i])):
                try:
                    words[i+1][j]
                except IndexError:
                    return ""
                else:
                    if words[i][j] == words[i+1][j]:
                        continue
                    else:
                        if words[i+1][j] not in greater_dict:
                            greater_dict[words[i+1][j]] = set()

                        greater_dict[words[i+1][j]].add(words[i][j])
                        break

        word_set = set()

        for word in words:
            for letter in word:
                word_set.add(letter)

        point_dict = {}

        for letter in word_set:
            if letter not in greater_dict:
                point_dict[letter] = 0

        parent_set = set()
        backedge = False

        def getpoint(character):
            nonlocal parent_set
            nonlocal backedge

            parent_set.add(character)

            if character in point_dict:
                parent_set.remove(character)
                return point_dict[character]+1

            temp = []
            
            for letter in greater_dict[character]:
                if letter in parent_set:
                    backedge = True
                    return 0
                else:
                    temp.append(getpoint(letter))

            point_dict[character] = max(temp)
            
            parent_set.remove(character)
            return point_dict[character]+1
                


        for letter in greater_dict:
            getpoint(letter)
            if backedge:
                return ""

        rev_point_dict = {}

        for letter in point_dict:
            if point_dict[letter] not in rev_point_dict:
                rev_point_dict[point_dict[letter]] = [letter]
            else:
                rev_point_dict[point_dict[letter]].append(letter)

        ans_l = []

        for i in range(0,len(word_set)):
            if i not in rev_point_dict:
                break
            ans_l.extend(rev_point_dict[i])

        ans = ""

        for letter in ans_l:
            ans = ans + letter

        return ans


        