import unittest

def find_gcd_substring(s1: str, s2: str):
    # Find greatest string divider
    if not s1+s2 == s2+s1:
        return ""
    
    a = len(s1)
    b = len(s2)
    
    while b != 0:
        temp = b
        b = a % b
        a = temp
    
    gcd = a
       
    return "".join(s1[:gcd])
    

class TestGCDSubstring(unittest.TestCase):
    

    def test_gcd(self):
        test_cases = [
            ("ABABABAB", "ABAB",  "ABAB"),
            ("ABCABC", "ABC", "ABC"),
            ("ABABAB", "ABAB", "AB"),
            ("LEET", "CODE", "")
        ]
    
        for s1, s2, answer in test_cases:
            with self.subTest(s1=s1, s2=s2):  # allows each test case to run independently, so if one fails, the others still run and you can see which specific cases failed.
                self.assertEqual(find_gcd_substring(s1, s2), answer)



if __name__ == "__main__":
    unittest.main()
