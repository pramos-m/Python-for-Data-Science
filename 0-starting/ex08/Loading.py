import time
import sys

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_length = 40

    for i, elem in enumerate(lst):
        progress = (i + 1) / total #calculating the current progress
        bar = '=' * int(progress * bar_length) + '>' * (1 if progress < 1 else 0)
        bar = bar.ljust(bar_length, ' ') # ljust fills out the bar with spaces to mantain the 40 lenght characters fixed
        # Formatear la línea de progreso
        sys.stdout.write(f'\r{int(progress * 100)}%|[{bar}] {i + 1}/{total}')
        sys.stdout.flush()

        yield elem

    print()  # Salto de línea al finalizar

