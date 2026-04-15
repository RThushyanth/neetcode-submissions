class Solution:
    def isPalindrome(self, s: str) -> bool:


        count = 0
        i = 0
        j = len(s)-1
        is_a_alphanum = "False"
        is_b_alphanum = "False"
        total_rem = 0
        while i <= j:
            
            a = ord(s[i])
            b = ord(s[j])
            if 48 <= a <=57 or 65 <= a <=90 or 97 <= a <= 122:
                is_a_alphanum = "True"
            else:
                i = i + 1
                total_rem = total_rem + 1
            if 48 <= b <=57 or 65 <= b <=90 or 97 <= b <= 122:
                is_b_alphanum = "True"
            else:
                j = j - 1
                total_rem = total_rem + 1
            if is_a_alphanum == "True" and is_b_alphanum == "True":
                if a == b:
                    count = count + 1
                    is_a_alphanum = "False"
                    is_b_alphanum = "False"
                    i = i+1
                    j = j-1
                elif (65 <= a <=90 and 97 <= b <= 122) or (65 <= b <=90 and 97 <= a <= 122):
                    if abs(a-b) == 32:
                        count = count + 1
                        is_a_alphanum = "False"
                        is_b_alphanum = "False"
                        i = i+1
                        j = j-1
                    else:
                        return False
                else:
                    return False
        


        if count == ((len(s) - total_rem)+1)//2:
            return True
                


                    
            