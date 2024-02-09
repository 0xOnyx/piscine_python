import sys
import time

def ft_tqdm(lst: range) -> iter:
    start_time = time.time()
    total = len(lst)

    for i, item in enumerate(lst):
        yield item
        percentage = (i + 1) / total
        bar_length = 50
        arrow = '=' * int(round(percentage * bar_length) - 1) + '>'
        spaces = ' ' * (bar_length - len(arrow))

        elapsed_time = time.time() - start_time
        try:
            speed = (i + 1) / elapsed_time
        except ZeroDivisionError:
            speed = 0

        sys.stdout.write("\r{0:3}%|[{1}{2}]| {3}/{4} [{5:.2f}s, {6:.2f}it/s]".format(
            int(round(percentage * 100)),
            arrow,
            spaces,
            i + 1,
            total,
            elapsed_time,
            speed
        ))
        sys.stdout.flush()
    print()




