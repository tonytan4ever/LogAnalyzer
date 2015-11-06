'''
Test logfile reader
'''
import datetime
import unittest

from log_analyzer import logfile_reader


class TestLogfieReader(unittest.TestCase):

    def test_log_entries_happy_path(self):
        lgf_reader = logfile_reader.LogfileReader('./test_log_file.txt')
        lgf_reader.load_entries()
        self.assertTrue(lgf_reader.entries is not None)
        self.assertTrue(len(lgf_reader.entries) > 0)
        fields = ['date', 'log_level', 'session_id', 'business_id',
                  'request_id', 'message']
        for field in fields:
            for entry in lgf_reader.entries:
                self.assertTrue(field in entry)
                self.assertTrue(isinstance(entry['date'],
                                           datetime.date))

    def test_log_entries_file_does_not_exist(self):
        lgf_reader = logfile_reader.LogfileReader('./not_exist.txt')
        with self.assertRaises(IOError):
            lgf_reader.load_entries()

    def test_log_entries_corrupted_data(self):
        lgf_reader = logfile_reader.LogfileReader(
            './test_log_file_corrupted.txt')
        # Raise index error when one field is missing
        # Could be other error cases but I here just list one
        with self.assertRaises(IndexError):
            lgf_reader.load_entries()


if __name__ == "__main__":
    unittest.main()
