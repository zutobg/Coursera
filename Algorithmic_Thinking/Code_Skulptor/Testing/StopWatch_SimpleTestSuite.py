"""
Test suite for format function in "Stopwatch - The game"
"""

import poc_simpletest

def run_test(stopwatch_format):
    """
    Some informal testing code
    """
    
    # create a testSuite object
    suite = poc_simpletest.TestSuite()
    
    # test format_function on various inputs
    suite.run_test(stopwatch_format(0), "0:00.0", "Test #1:")
    suite.run_test(stopwatch_format(7), "0:00.7", "Test #2:")
    suite.run_test(stopwatch_format(17), "0:01.7", "Test #3:")
    suite.run_test(stopwatch_format(60), "0:06.0", "Test #4:")
    suite.run_test(stopwatch_format(63), "0:06.3", "Test #5:")
    suite.run_test(stopwatch_format(214), "0:21.4", "Test #6:")
    suite.run_test(stopwatch_format(599), "0:59.9", "Test #7:")
    suite.run_test(stopwatch_format(600), "1:00.0", "Test #8:")
    suite.run_test(stopwatch_format(602), "1:00.2", "Test #9:")
    suite.run_test(stopwatch_format(667), "1:06.7", "Test #10:")
    suite.run_test(stopwatch_format(1325), "2:12.5", "Test #11:")
    suite.run_test(stopwatch_format(4567), "7:36.7", "Test #12:")
    suite.run_test(stopwatch_format(5999), "9:59.9", "Test #13:")
    
    suite.report_results()
    
"""
Format function for a stopwatch
"""

import poc_format_testsuite

def stopwatch_format(ticks):
    """
    Convert tenths of seconds to formatted time
    """
    
    minutes = ticks // 600
    # minutes = ticks // 60
    tens_seconds = (ticks // 100) % 6
    seconds = (ticks // 10) % 10
    tenths = ticks % 10
    return str(minutes) + ':' + str(tens_seconds) + \
           str(seconds) + '.' + str(tenths)
    
# run the testing suite for our format function
run_test(stopwatch_format)