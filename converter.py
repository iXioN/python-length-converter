# !/usr/bin/env python
#  converter.py
#  python-length-converter
#  
#  Created by Antonin Lacombe on 2013-04-16.
#  Copyright 2013 Antonin Lacombe. All rights reserved.
# 

"""
The idea of the converter is:
    we register unit converter instance on converter init
    we convert the input value in meter
    then we can convert this value in each other unit
    
we will use the meter as 'reference' because it's the SI length unit.

Unit converter objects have simple interface to convert their unit in meter and convert meter in their unit

the converter class just know all unit converter, detect the input value, 
search the converter for the unit and convert convert in meter.
After that we just have to convert meter in desired unit

"""
import sys
import re
import decimal
from optparse import OptionParser

PARSE_INPUT_PATTERN = re.compile('([-+]?[0-9]*\.?[0-9]*)([a-z]*)')

from unit_converters import MeterConverter, YardConverter, InchConverter

class ConverterException(Exception):
    pass
class UnitConvertNotFound(ConverterException):
    pass

class Converter(object):
    """
    a class that convert length units
    for the how to use read the README
    """
    def __init__(self):
        super(Converter, self).__init__()
        #the registered unit converters 
        unit_converters_class = (
            MeterConverter,
            YardConverter,
            InchConverter,
        )
        #load the unit_converters objects into the unit_converters property
        self.unit_converters = [unit_cnvrtr_cls() for unit_cnvrtr_cls in unit_converters_class]
        
        #the the intial length to convert, always stored in meter
        self.intial_length = None
        self.intial_unit = None
        
    def _get_unit_converter(self, short_unit_name):
        """
        return a unit_convert from their short_unit_name
        else raise a UnitConvertNotFound
        """
        if not hasattr(self, 'unit_converter_cache'):
            self.unit_converter_cache = {}
            for uc in self.unit_converters:
                self.unit_converter_cache[uc.short_unit] = uc
        if not short_unit_name in self.unit_converter_cache:
            raise UnitConvertNotFound()
        return self.unit_converter_cache[short_unit_name]
            
    def set_value(self, length, unit):
        """
        length is a number (float or decimal) representing the initial length 
        unit is the of initial value ex : 'm', 'meter', 'yd'... depend on registered unit_converters
        """
        initial_unit_converter = self._get_unit_converter(unit)
        #check if the unit is know
        if initial_unit_converter:
            self.intial_unit = unit
            #store the initial length in meter
            self.intial_length = initial_unit_converter.to_meter(length)
        return None
        
    def convert_to_unit(self, short_unit_name, as_string=False):
        """
        convert the intial_length value into the given short unit
        if as_string is True, a string is return containing the converted value + the unit name
        """
        #get the unit converter registered for the short_unit_name
        unit_converter = self._get_unit_converter(short_unit_name)
        if unit_converter:
            result = unit_converter.from_meter(self.intial_length)
            if as_string:
                #use the decimal and the %g to print the result user friendly
                decimal_result = decimal.Decimal(result).quantize(decimal.Decimal('0.1'), rounding=decimal.ROUND_UP)
                return "%g %s" % (decimal_result, short_unit_name)
            return result
        return None
    
    def convert(self, string_to_convert, target_unit, as_string=False):
        """
        hight level methode:
        string_to_convert : a string with number and short unit name like '2.4yd'
        target_unit : a short unit name like 'in'
        as_string : if True the method return an human readable string else return a float 
        """
        m = re.match(PARSE_INPUT_PATTERN, string_to_convert)
        #parse the original value to get the number and the original unit
        original_length = float(m.group(1)) 
        original_unit = m.group(2)
        #set the value in the convert 
        self.set_value(original_length, original_unit)
        return self.convert_to_unit(target_unit, as_string=as_string)

if __name__ == "__main__":
    try:
        #parse the options
        parser = OptionParser(usage="usage: %prog filename",
            version="%prog 0.1")
        parser.add_option("-v", "--value", dest="value",
            help="the value to convert woth unit ex: '2.5yd'", default="")
        parser.add_option("-u", "--unit", dest="trg_unit",
            help="the target unit ex: 'm'", default="m")
        parser.add_option("-t", "--tidy", dest="tidy", action="store_true",
            help="print the result user friendly (rounded and with unit)", default=False)
        (options, args) = parser.parse_args()
        original_value_to_convert = options.value
        target_unit = options.trg_unit
        tidy = options.tidy
        #create a converter instance
        converter = Converter()
        #then convert
        print converter.convert(original_value_to_convert, target_unit, tidy)
    except (KeyboardInterrupt, SystemExit):
        sys.exit()