"""
Unit tests for the Roman Numeral library
"""
import roman_convert

class TestRoman:

    def test_ones(self):
        assert (5,False,False) == roman_convert.fromRoman('V')

    def test_tens(self):
        assert (20,False,False) == roman_convert.fromRoman('XX')
    
    def test_hundreds(self):
        assert (150, False, False) == roman_convert.fromRoman('CL')

    def test_thousands(self):
        assert (2028,False,False) == roman_convert.fromRoman('MMXXVIII')

    def test_blank(self):
        assert (0,True,False) == roman_convert.fromRoman('')

    def test_invalid(self):
        assert (0,False,True) == roman_convert.fromRoman('AABBCCDD')

