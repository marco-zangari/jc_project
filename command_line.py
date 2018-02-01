"""Command line operation for the julia project."""

from julia_cite import rand_cite


def command_line():
    """Connection to the julia_cite module."""
    print(julia_cite.rand_cite())

if __name__ == '__main__':
    command_line()
