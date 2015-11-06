import timeit


class Profiler(object):
    """A Class profiling function exeuction times.

    In constructor, self.ns will act as a cache to store all
    the run information for each function run, and self.time_format_string
    will be used as a result execution time format

    It will keep track of the min, max and the average function
    execution time, and print a result as:
        Function: <function_names>
        NumSamples: 12
        Min: 0.02 secs
        Max: 0.34 secs
        Average: 0.09 secs

    """

    def __init__(self, num_samples=10):
        self.ns = {}
        self.time_format_string = "%.2f"

    def __call__(self, f):
        self.ns[f.__name__] = {
            'execution_time_samples': [],
        }

        def inner(*args, **kwargs):
            start = timeit.default_timer()
            f(*args, **kwargs)
            end = timeit.default_timer()
            elapsed = end-start
            self.ns[f.__name__]['execution_time_samples'].append(elapsed)

        return inner

    def _print_report(self):
        # print out statistics
        for func_name in self.ns:
            function_staticstic_entry = self.ns[func_name]
            print("Function: %s" % func_name)
            print("NumSamples: %s" %
                  len(function_staticstic_entry['execution_time_samples']))
            print(("Min: %s secs" % self.time_format_string) %
                  min(function_staticstic_entry['execution_time_samples']))
            print(("Max: %s secs" % self.time_format_string) %
                  max(function_staticstic_entry['execution_time_samples']))
            print(("Average: %s secs" % self.time_format_string) %
                  # this is the average
                  (float(
                      sum(
                          function_staticstic_entry['execution_time_samples']))
                   / len(function_staticstic_entry['execution_time_samples']))
                  )
            print "==========================================================="
            print "==========================================================="

    def __del__(self):
        self._print_report()
