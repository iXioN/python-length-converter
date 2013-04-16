# 
#  test_cases.py
#  python-lenght-converter
#  
#  Created by Antonin Lacombe on 2013-04-16.
#  Copyright 2013 Antonin Lacombe. All rights reserved.
# 

import unittest

def load_tests(loader, tests, pattern):
    """
    Discover and load all unit tests in all files named ``*_test.py`` in ``./tests/
    """ 
    
    suite = unittest.TestSuite()
    for all_test_suite in unittest.defaultTestLoader.discover('tests', pattern='*_tests.py'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite

if __name__ == '__main__':
    unittest.main()