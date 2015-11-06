'''
Read log files into an generator
'''

import csv
import datetime


class LogfileReader(object):
    """Class for reading log file into a in memory list

    The constructor takes a log_file's pathm, and a default
    delimiter of ' '.

    The load_entries method will set the loaed flag
    """

    # These are index number of the field in each log entry
    DATE = 0
    LOGLEVEL = 2
    SESSION_ID = 3
    BUSINESS_ID = 4
    REQUEST_ID = 5
    MSG = 6

    def __init__(self, log_file_path, field_delimiter=' ', ):
        self.log_file_path = log_file_path
        self.field_delimiter = field_delimiter
        self.entries = []
        # if loaded flag
        self.loaded = False

    def load_entries(self):
        '''Load all entries into a in memory list. '''
        with open(self.log_file_path, 'rb') as log_file:
            # Using quote as a quotechar as MSG field is quoted
            reader = csv.reader(log_file, delimiter=self.field_delimiter,
                                quotechar='\'')
            # could/need use a generator in case the file is so large.
            for row in reader:
                fmt = '%Y-%m-%d %H:%M:%S'
                self.entries.append({
                    'date': datetime.datetime.strptime(
                        ' '.join([row[self.DATE], row[self.DATE+1]]),
                        fmt,
                    ).date(),
                    'log_level': row[self.LOGLEVEL],
                    'session_id': row[self.SESSION_ID].split(':')[1],
                    'business_id': row[self.BUSINESS_ID].split(':')[1],
                    'request_id': row[self.REQUEST_ID].split(':')[1],
                    'message': row[self.MSG],
                    'original_line': ' '.join(row)
                })
        self.loaded = True
