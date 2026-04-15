class Solution:

    def encode(self, strs: List[str]) -> str:
        
        hnstr = "".join(strs)

        L = []
        for i in range(0,len(strs)):
            x = len(strs[i])
            if x//10 == 0:
                L.append("00"+str(x))
            elif x//100 == 0:
                L.append("0" + str(x))
            else:
                L.append(str(x))
        
        cap = "".join(L)


        y = len(strs)*3
        if y//10 == 0:
            tail = "00" + str(y)
        elif y//100 == 0:
            tail = "0" +str(y)
        else:
            tail = str(y)

        mstr = cap+hnstr+tail

        return mstr



    def decode(self, s: str) -> List[str]:

        tail_d = s[-3:]
        cap_d = s[0:int(tail_d)]

        strs_und = s[int(tail_d):-3]

        strs_dec = []

        lenght_i = 0
        for i in range(0,int(tail_d),3):
            lenght_f = int(cap_d[i:i+3]) + lenght_i
            strs_dec.append(strs_und[lenght_i:lenght_f])
            lenght_i = lenght_f

        return strs_dec



