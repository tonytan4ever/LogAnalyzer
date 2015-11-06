import timeit


class Profiler(object):
    """A Class profiling function exeuction times.

    The construction of take a num_samples parameter to let
    the decorated function run num_samples times

    It will keep track of the min, max and the average function
    execution time, and print a result as:
        Function: <function_names>
        NumSamples: 12
        Min: 0.02 secs
        Max: 0.34 secs
        Average: 0.09 secs

    """

    def __init__(self, num_samples=10):
        self.num_samples = num_samples
        self.ns = {}

    def __call__(self, f):
        self.ns[f.__name__] = {
            'NumSamples': self.num_samples,
            'execution_time_samples': [],
        }

        def inner(*args, **kwargs):
            for _ in range(self.num_samples):
                start = timeit.default_timer()
                f(*args, **kwargs)
                end = timeit.default_timer()
                elapsed = end-start
                self.ns[f.__name__]['execution_time_samples'].append(elapsed)
            # print out statistics
            function_staticstic_entry = self.ns[f.__name__]
            print("Function: %s" % f.__name__)
            print("NumSamples: %s" % function_staticstic_entry['NumSamples'])
            print("Min: %.2f secs" %
                  min(function_staticstic_entry['execution_time_samples']))
            print("Max: %.2f secs" %
                  max(function_staticstic_entry['execution_time_samples']))
            print("Average: %.2f secs" %
                  # this is the average
                  (float(sum(
                        function_staticstic_entry['execution_time_samples'])) /
                        len(function_staticstic_entry['execution_time_samples']
                            ))
                  )

        return inner
