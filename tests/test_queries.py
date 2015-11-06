'''
Test logfile reader
'''
import datetime
import unittest

from log_analyzer import logfile_reader, queries


class TestQuries(unittest.TestCase):

    def setUp(self):
        self.reader_positive = (
            logfile_reader.LogfileReader('./test_log_file.txt')
        )

    def test_query_by_log_level(self):
        # Here the test is a little data-driver, could use ddt to do that
        res = queries.get_all_lines_by_log_level(self.reader_positive, "DEBUG")
        self.assertTrue(len(res) > 0)
        for r in res:
            self.assertTrue("DEBUG" in r)

        # No matching test
        res = queries.get_all_lines_by_log_level(self.reader_positive, "INFO")
        self.assertTrue(len(res) == 0)

    def test_query_by_business_id(self):
        res = queries.get_all_lines_by_business_id(self.reader_positive,
                                                   "1329")
        self.assertTrue(len(res) > 0)
        for r in res:
            self.assertTrue("BID:1329" in r)

        # No matching test
        res = queries.get_all_lines_by_business_id(self.reader_positive,
                                                   "0000")
        self.assertTrue(len(res) == 0)

    def test_query_by_session_id(self):
        res = queries.get_all_lines_by_session_id(self.reader_positive,
                                                  "34523")
        self.assertTrue(len(res) > 0)
        for r in res:
            self.assertTrue("SID:34523" in r)

        # No matching test
        res = queries.get_all_lines_by_session_id(self.reader_positive,
                                                  "0000")
        self.assertTrue(len(res) == 0)

    def test_query_by_date_range(self):
        from_date, end_date = (
            datetime.date(2012, 9, 13), datetime.date(2012, 9, 14))
        res = queries.get_all_lines_by_date_range(self.reader_positive,
                                                  from_date,
                                                  end_date,
                                                  False)
        self.assertTrue(len(res) > 0)
        for r in res:
            self.assertTrue(r['date'] >= from_date and r['date'] <= end_date)

        # No matching test
        from_date, end_date = (
            datetime.date(2015, 9, 13), datetime.date(2015, 9, 14))
        res = queries.get_all_lines_by_date_range(self.reader_positive,
                                                  from_date,
                                                  end_date)
        self.assertTrue(len(res) == 0)


if __name__ == "__main__":
    unittest.main()
