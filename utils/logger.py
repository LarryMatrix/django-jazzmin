import time
from time import perf_counter
from pathlib import Path
from functools import wraps


def custom_logger(fn):
    """
        Custom logger function output result to a file.
    """
    logs_file_path = Path('../logs')

    @wraps(fn)
    def logger_writer(*args, **kwargs):
        start = perf_counter()
        fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        r = 'Function {0} called and it takes {1:.6f} seconds to Execute '.format(fn.__name__, elapsed)

        filename = time.strftime("%Y%m%d-%H%M%S")

        with open(f'{logs_file_path}/{filename}.txt', 'w', encoding='utf-8') as f:

            try:
                f.write(r)
            finally:
                f.close()

    return logger_writer
