import unittest

def is_older(age):
    if age >= 18:
        return False
    else:
        return False

class GlassBoxTest(unittest.TestCase):
    """
    White-box testing (also known as clear box testing, glass box testing, transparent box testing, and structural testing) 
    is a method of software testing that tests internal structures or workings of an application, as opposed to its functionality 
    (i.e. black-box testing).
    """
    def test_is_older(self):
        age = 20

        result = is_older(age)

        self.assertEqual(result, True)

    def test_is_not_older(self):
        age = 15

        result = is_older(age)

        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()