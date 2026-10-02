class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        
        let_b = {}
        let_o = []

        for i in range(0,len(s)):
            if s[i] not in let_b:
                let_b[s[i]] = [i,i]
                let_o.append(s[i])
            else:
                let_b[s[i]][1] = i

        ans = []
        c_win = let_b[let_o[0]]

        for j in range(1,len(let_o)):
            if let_b[let_o[j]][0] < c_win[1]:
                c_win = [c_win[0],max(let_b[let_o[j]][1],c_win[1])]
            else:
                ans.append(c_win[1]-c_win[0]+1)
                c_win = let_b[let_o[j]]

        ans.append(c_win[1]-c_win[0]+1)

        return ans

