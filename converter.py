# !/usr/bin/env python
#  converter.py
#  python-lenght-converter
#  
#  Created by Antonin Lacombe on 2013-04-16.
#  Copyright 2013 Antonin Lacombe. All rights reserved.
# 

"""
The idea of the converter is:
    we register unit converter instance 
    we convert the input value in meter
    then we can convert this value in each other unit
    
we will use the meter as 'reference' because it's the SI lenght unit.

Unit converter objects have simple interface to convert their unit in meter and convert meter in their unit

the converter class just know all unit converter, detect the input value, 
search the converter for the unit and convert convert in meter.
After that we just have to convert meter in desired unit

"""
import sys
from unit_converters import MeterConverter, YardConverter, InchConverter

class ConverterException(Exception):
    pass
class UnitConvertNotFound(ConverterException):
    pass
   
class Converter(object):
    """
    a class that convert lenght units
    
    usage:
        >>>converter = converter()
        >>>converter.set_value('3.45', 'yd')
        >>>converter.convert_to_unit('m')
        3.15468
        >>>converter.convert_to_unit('feet')
        None #unsupported unit
        
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
        
        #the the intial lenght to convert, always stored in meter
        self.intial_lenght = None
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
            
    def set_value(self, lenght, unit):
        """
        lenght is a number (float or decimal) representing the initial lenght 
        unit is the of initial value ex : 'm', 'meter', 'yd'... depend on registered unit_converters
        """
        initial_unit_converter = self._get_unit_converter(unit)
        #check if the unit is know
        if initial_unit_converter:
            self.intial_unit = unit
            #store the initial lenght in meter
            self.intial_lenght = initial_unit_converter.to_meter(lenght)
        return None
        
    def convert_to_unit(self, short_unit_name, as_string=False):
        """
        convert the intial_lenght value into the given short unit
        if as_string is True, a string is return containing the converted value + the unit name
        """
        #get the unit converter registered for the short_unit_name
        unit_converter = self._get_unit_converter(short_unit_name)
        if unit_converter:
            result = unit_converter.from_meter(self.intial_lenght)
            if as_string:
                return "%.2f %s" % (result, short_unit_name)
            return result
        return None

if __name__ == "__main__":
    try:
        sys.argv[1:]
        import ipdb
        ipdb.set_trace()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
