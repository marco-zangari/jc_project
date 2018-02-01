"""Command line operation for the julia project."""

from julia_cite import rand_cite


def command_line(c):
    """Connection to the julia_cite module."""
    print(rand_cite(c))

if __name__ == '__main__':
    quotes = ['A party without cake is just a meeting.',
                'I was 32 when I started cooking; up until then, I just ate.',
                'The only real stumbling block is fear of failure. In cooking you\'ve got to have a what-the-hell attitude.']
    command_line(quotes)
