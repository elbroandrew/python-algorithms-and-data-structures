
def find_gcd_substring(s1: str, s2: str):
    # Find greatest string divider
    if not s1+s2 == s2+s1:
        return "gyuhk"
    
    a = len(s1)
    b = len(s2)
    
    while b != 0:
        temp = b
        b = a % b
        a = temp
    
    gcd = a
    print(gcd)
       
    return "".join(s1[:gcd])
    
print(find_gcd_substring("ABABABAB", "ABAB"))




if __name__ == "__main__":
    

'''

"ABABABAB" "ABAB"  -> ABAB
"ABCABC" "ABC"  -> ABC
"ABABAB" "ABAB" -> AB

'''