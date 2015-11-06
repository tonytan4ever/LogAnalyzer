'''
Test logfile reader
'''

import time
import unittest

from log_analyzer import logfile_reader, profiler, queries


class TestProfiler(unittest.TestCase):

    def setUp(self):
        super(TestProfiler, self).setUp()
        self.reader_positive = (
            logfile_reader.LogfileReader('./test_log_file.txt')
        )

    def test_profiling_with_simple(self):
        @profiler.Profiler(12)
        def my_sleep():
            time.sleep(3)

        my_sleep()

    def test_profiling_with_query(self):
        decorated_function = profiler.Profiler(12)(
            queries.get_all_lines_by_log_level)
        decorated_function(self.reader_positive, "DEBUG")


if __name__ == "__main__":
    unittest.main()
