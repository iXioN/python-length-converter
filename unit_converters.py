# !/usr/bin/env python
#  unit_converters.py
#  python-length-converter
#  
#  Created by Antonin Lacombe on 2013-04-16.
#  Copyright 2013 Antonin Lacombe. All rights reserved.
# 

class BaseUnitConverter(object):
    """A base unit converter class"""
    short_unit = ""
    convert_ratio = 1 #the convert ratio to meter
    
    def to_meter(self, value):
        """
        the method to call to transform a unity value into meter
        always return a meter value 
        """
        return value / self.convert_ratio
        
    def from_meter(self, value):
        """
        the method to call to get the unity value from meter value
        always return a unit value
        """
        return value * self.convert_ratio


class MeterConverter(BaseUnitConverter):
    """
    The meter converter
    this is the simplest convert because we use meter as base unit 
    """
    short_unit = "m"
    full_unit = "meter"
    convert_ratio = 1    
    
    
class YardConverter(BaseUnitConverter):
    """
    The yard converter
    """
    short_unit = "yd"
    convert_ratio = 1.093613


class InchConverter(BaseUnitConverter):
    """
    The inch converter
    """
    short_unit = "in"
    convert_ratio = 39.370078
