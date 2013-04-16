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
