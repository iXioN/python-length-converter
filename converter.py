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

class BaseUnitConverter(object):
    """A base unit converter class"""
    short_unit = ""
    full_unit = short_unit #default full_unit = short_unit, implementation can override 
    convert_ratio = 1 #the convert ratio to meter
    
    def to_meter(self, value):
        """
        the method to call to transform a unity value into meter
        always return a meter value 
        """
        raise NotImplementedError
        
    def from_meter(self, value):
        """
        the method to call to get the unity value from meter value
        always return a unit value
        """
        raise NotImplementedError
        
class Converter(object):
    """
    a class that convert lenght units
    """
    def __init__(self, arg):
        """value is a value to convert like 3m or 6.5yd"""
        super(Converter, self).__init__(value)
        self.value_to_convert = value
        



if __name__ == "__main__":
    try:
        sys.argv[1:]
        import pdb
        pdb.set_trace()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
