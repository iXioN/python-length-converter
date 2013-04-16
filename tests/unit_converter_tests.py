# !/usr/bin/env python
#  unit_converter_tests.py
#  python-lenght-converter
#  
#  Created by Antonin Lacombe on 2013-04-16.
#  Copyright 2013 Antonin Lacombe. All rights reserved.
# 

import unittest
from unit_converters import MeterConverter, YardConverter, InchConverter
class UnitConverterTestCase(unittest.TestCase):    
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
    
    #inche converter tests
    def test_inch_convert_to_meter(self):
        """
        given a inch converter
        when convert 3 inches into meters
        then I get 0.9144 (inches)
        """
        unit_converter = InchConverter()
        value_to_convert = 3
        expected_converted_value = 0.0762 
        converted_value = unit_converter.to_meter(value_to_convert)
        self.assertAlmostEqual(converted_value, expected_converted_value, places=4)

    def test_inch_convert_from_meter(self):
        """
        given a inch converter
        when get inches from 3 meters
        then I get 118.110236 (inches)
        """
        unit_converter = InchConverter()
        value_to_convert = 3
        expected_converted_value = 118.110236
        converted_value = unit_converter.from_meter(value_to_convert)
        self.assertAlmostEqual(converted_value, expected_converted_value, places=4)
