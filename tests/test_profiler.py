'''
Test logfile reader
'''

import datetime
import time
import unittest

from log_analyzer import logfile_reader, profiler, queries


class TestProfiler(unittest.TestCase):

    def setUp(self):
        super(TestProfiler, self).setUp()
        self.reader_positive = (
            logfile_reader.LogfileReader('./test_log_file.txt')
        )
        self.profiler = profiler.Profiler()

    def test_profiling_with_simple(self):
        @self.profiler
        def my_sleep(secs):
            time.sleep(secs)

        for i in range(3):
            my_sleep(i)

    def test_profiling_with_query(self):
        get_all_lines_by_log_level = self.profiler(
            queries.get_all_lines_by_log_level)

        get_all_lines_by_business_id = self.profiler(
            queries.get_all_lines_by_business_id)

        get_all_lines_by_session_id = self.profiler(
            queries.get_all_lines_by_session_id)

        get_all_lines_by_date_range = self.profiler(
            queries.get_all_lines_by_date_range)

        for _ in range(20):
            get_all_lines_by_log_level(self.reader_positive, "DEBUG")
            get_all_lines_by_business_id(self.reader_positive, "1329")
            get_all_lines_by_session_id(self.reader_positive, "34523")
            from_date, end_date = (
                datetime.date(2012, 9, 13), datetime.date(2012, 9, 14))
            get_all_lines_by_date_range(self.reader_positive,
                                        from_date, end_date)

if __name__ == "__main__":
    unittest.main()
