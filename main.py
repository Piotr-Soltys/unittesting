import unittest
# Funkcja sprawdzająca, czy podane trzy długości boków tworzą trójkąt
def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

class TestIsTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        # Testy z poprawnymi trójkątami
        self.assertTrue(is_triangle(3, 4, 5))
        self.assertTrue(is_triangle(5, 12, 13))
        self.assertTrue(is_triangle(8, 15, 17))
        
    def test_invalid_triangle(self):
        # Testy z błędnymi trójkątami
        self.assertFalse(is_triangle(1, 1, 3))
        self.assertFalse(is_triangle(2, 8, 6))
        self.assertFalse(is_triangle(5, 5, 10))
        
    def test_zero_or_negative_lengths(self):
        # Testy z długościami boków równymi zero lub ujemnymi
        self.assertFalse(is_triangle(0, 4, 5))
        self.assertFalse(is_triangle(3, -4, 5))
        self.assertFalse(is_triangle(-3, -4, -5))
if __name__ == '__main__':
    unittest.main()
