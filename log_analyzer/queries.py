

# return a filter function to filter the list by
# the matching of a field on a entry
def _generate_filter_func_by_value(field, value):
    def filter_func(entry):
        return entry[field] == value
    return filter_func


# return a filter function to filter the list by
# the matching of a field in a range of (vqlue1, value2)
def _generate_filter_func_by_range(field, value1, value2):
    def filter_func(entry):
        return entry[field] >= value1 and entry[field] <= value2
    return filter_func


# return_original_line will return the original line
# if that sets to False, return the dictionary entry
def get_all_lines_by_log_level(reader, log_level,
                               return_original_line=True):
    """get_all_lines_by_log_level.

    :param reader: A logfile_reader.LogfileReader object
    :param log_level: The log_level value to be matched
    :param return_original_line: return orignal line or the entries
    :return a list matching entries/lines
    """
    if not reader.loaded:
        reader.load_entries()
    filter_func = _generate_filter_func_by_value('log_level',
                                                 log_level)
    filtered_entries = filter(filter_func, reader.entries)
    if return_original_line:
        return [entry['original_line'] for entry in filtered_entries]
    else:
        return [entry for entry in filtered_entries]


def get_all_lines_by_business_id(reader, business_id,
                                 return_original_line=True):
    """get_all_lines_by_business_id.

    :param reader: A logfile_reader.LogfileReader object
    :param log_level: The business_id value to be matched
    :param return_original_line: return orignal line or the entries
    :return a list matching entries/lines
    """
    if not reader.loaded:
        reader.load_entries()
    filter_func = _generate_filter_func_by_value('business_id',
                                                 business_id)
    filtered_entries = filter(filter_func, reader.entries)
    if return_original_line:
        return [entry['original_line'] for entry in filtered_entries]
    else:
        return [entry for entry in filtered_entries]


def get_all_lines_by_session_id(reader, session_id, return_original_line=True):
    """get_all_lines_by_session_id.

    :param reader: A logfile_reader.LogfileReader object
    :param log_level: The session_id value to be matched
    :param return_original_line: return orignal line or the entries
    :return a list matching entries/lines
    """
    if not reader.loaded:
        reader.load_entries()
    filter_func = _generate_filter_func_by_value('session_id',
                                                 session_id)
    filtered_entries = filter(filter_func, reader.entries)
    if return_original_line:
        return [entry['original_line'] for entry in filtered_entries]
    else:
        return [entry for entry in filtered_entries]

### Could use more generic functions to reduce code repetition...
### But I can refactor later if needed
##################################################################


def get_all_lines_by_date_range(reader, from_date, end_date,
                                return_original_line=True):
    """get_all_lines_by_date_range.

    :param reader: A logfile_reader.LogfileReader object
    :param from_date: The starting date object of the query
    :param end_date: The end date object of the query
    :param return_original_line: return orignal line or the entries
    :return a list matching entries/lines
    """
    if not reader.loaded:
            reader.load_entries()
    filter_func = _generate_filter_func_by_range('date',
                                                 from_date,
                                                 end_date)
    filtered_entries = filter(filter_func, reader.entries)
    if return_original_line:
        return [entry['original_line'] for entry in filtered_entries]
    else:
        return [entry for entry in filtered_entries]
