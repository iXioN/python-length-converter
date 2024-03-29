# !/usr/bin/env python
# 
#  converter_tests.py
#  python-length-converter
#  
#  Created by Antonin Lacombe on 2013-04-16.
#  Copyright 2013 Antonin Lacombe. All rights reserved.
# 
import unittest
import converter
 
class ConverterTestCase(unittest.TestCase):   

    def test_check_registered_short_unit(self):
        """
        given a converter with the 3 unit converters registered
        when I search the unit converter for each short unit name
        then I get unit_convert for each name
        """
        converter_instance = converter.Converter()
        for short_unit_name in ('m', 'yd', 'in'):
            unit_converter = converter_instance._get_unit_converter(short_unit_name)
            self.assertEquals(short_unit_name, unit_converter.short_unit)
    def test_check_registered_short_unit_unknow_raise(self):
        """
        given a converter with the 3 unit converters registered
        when I search the unit converter for short name ft
        then I get an UnitConvertNotFound exception
        """
        converter_instance = converter.Converter()
        with self.assertRaises(converter.UnitConvertNotFound):
         converter_instance._get_unit_converter('ft')
    
    def test_set_value_register_meter_value(self):
        """
        given a converter with the 3 unit converters registered
        when I set a value with set_value 
        then the intial_length is register as meter
        """
        yard_value = 2
        meter_value = 1.8288
        converter_instance = converter.Converter()
        converter_instance.set_value(2, 'yd')
        self.assertAlmostEqual(converter_instance.intial_length, meter_value, places=4)
        self.assertEquals(converter_instance.intial_unit, 'yd')

    def test_value_convertion_yard_to_inche(self):
        """
        given a converter with the 4 unit converters registered and 3 yards set as value
        when I get converted value in inches
        then I get 144 inches
        """
        converter_instance = converter.Converter()
        converter_instance.set_value(4, 'yd')
        result = converter_instance.convert_to_unit('in')
        self.assertAlmostEqual(result, 144, places=4)
        
    def test_value_convertion_yard_to_inches_as_string(self):
        """
        given a converter with the 3 unit converters registered and 3 yards set as value
        when I get converted value in meters with the as_string flag
        then I get litteraly "112.98 m" 
        """
        converter_instance = converter.Converter()
        converter_instance.set_value(123.56, 'yd')
        result = converter_instance.convert_to_unit('m', as_string=True)
        self.assertEquals(result, "113 m")
    
    def test_value_convertion_yard_to_feet(self):
        """
        given a converter with the 3 unit converters registered and 3 yards set as value
        when I get converted value in feets
        then I get an UnitConvertNotFound exception
        """
        converter_instance = converter.Converter()
        converter_instance.set_value(23, 'yd')
        with self.assertRaises(converter.UnitConvertNotFound):
         converter_instance.convert_to_unit('ft')
    
    def test_convert_method_yard_to_inch(self):
        """
        given a converter with the 3 unit converters registered and 3 yards set as value
        when I convert the string '79.4yd' into 'in'
        then I get 2858.4007
        """
        converter_instance = converter.Converter()
        result = converter_instance.convert('79.4yd', 'in')
        self.assertAlmostEqual(result, 2858.4007, places=4)
    
    def test_convert_method_yard_to_inch_human_readable(self):
        """
        given a converter with the 3 unit converters registered and 3 yards set as value
        when I convert the string '79.4yd' into 'in' with a result as string
        then I get 2858.4007
        """
        converter_instance = converter.Converter()
        result = converter_instance.convert('79.4yd', 'in', as_string=True)
        self.assertEquals(result, '2858.5 in')
