import unittest

def addition(num_1, num_2):
    return abs(num_1) + num_2

class BlackBoxTest(unittest.TestCase):
    """ 
    It is the class in charge of storing the test cases that can be carried out within the code.
    """
    def test_add_two_positives(self):
        num_1 = 10
        num_2 = 5

        result = addition(num_1, num_2)

        self.assertEqual(result, 15)

    
    def test_add_two_negatives(self):
        num_1 = -10
        num_2 = -7

        result = addition(num_1, num_2)

        self.assertEqual(result, -17)


if __name__ == "__main__":
    unittest.main()