#  converter.py
#  converter_tests.py
#  python-lenght-converter
#  
#  Created by Antonin Lacombe on 2013-04-16.
#  Copyright 2013 Antonin Lacombe. All rights reserved.
# 

import unittest
import converter
from converter_meter import MeterConverter
from converter_yard import YardConverter

class ConverterTestCase(unittest.TestCase):    
    #Meter converter tests
    def test_meter_convert_to_meter(self):
        """
        given a meter converter
        when convert 6 meters into meters
        then I get 6 (meters)
        """
        unit_converter = MeterConverter()
        value_to_convert = 6
        expected_converted_value = 6
        converted_value = unit_converter.to_meter(value_to_convert)
        self.assertAlmostEqual(converted_value, expected_converted_value, places=4)
        
    def test_meter_convert_from_meter(self):
        """
        given a meter converter
        when get meters from 6 meters
        then I get 6 (meters)
        """
        unit_converter = MeterConverter()
        value_to_convert = 6
        expected_converted_value = 6
        converted_value = unit_converter.from_meter(value_to_convert)
        self.assertAlmostEqual(converted_value, expected_converted_value, places=4)
        
    #yard converter tests
    def test_yard_convert_to_meter(self):
        """
        given a yard converter
        when convert 1 yard into meters
        then I get 0.9144 (meters)
        """
        unit_converter = YardConverter()
        value_to_convert = 2
        expected_converted_value = 1.8288
        converted_value = unit_converter.to_meter(value_to_convert)
        self.assertAlmostEqual(converted_value, expected_converted_value, places=4)
    
    def test_yard_convert_from_meter(self):
        """
        given a yard converter
        when get yards from 2 meters
        then I get 2.1872266 (yards)
        """
        unit_converter = YardConverter()
        value_to_convert = 2
        expected_converted_value = 2.1872266
        converted_value = unit_converter.from_meter(value_to_convert)
        self.assertAlmostEqual(converted_value, expected_converted_value, places=4)
        
if __name__ == '__main__':
    unittest.main()