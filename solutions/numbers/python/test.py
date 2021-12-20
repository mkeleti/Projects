import unittest


class test(unittest.TestCase):
    
    def piTest1(self):
        """
        Test if the Numbers run properly
        """

        input = 1
        result = PI(input)

        self.assertEqual(result, 3)
        
        input = 3
        result = PI(input)

        self.assertEqual(result, 3.14)

    
if __name__ == '__main__':
    unittest.main()
