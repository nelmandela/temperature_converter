import unittest
from temp_converter import convert_celsius_to_farenheight

class TempConveterTest(unittest.TestCase):
    #given temp in celcius = correct value in F
    #data type for input
    #check for null values -> throw an error
    #if it throws an exception when data type is incorrect

    def test_celsius_is-converted to farenheight(self):
        """
            F = C * 9/5 + 32
        """
        actual = convert_celsius_to_farenheight(10)
        expected = 50
        self.assertEqual(actual, expected, 'celsius should convert to correct Farenheight')