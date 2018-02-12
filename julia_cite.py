"""Test Quotes for the julia child project."""

from random import randint as rint

citations = ['A party without cake is just a meeting.',
                'I was 32 when I started cooking; up until then, I just ate.',
                'The only real stumbling block is fear of failure. In cooking you\'ve got to have a what-the-hell attitude.']


def rand_cite(c):
    """Return random citation from list of citations."""
    number = (len(c) - 1)
    rand = rint(0, number)
    print(c[rand])

# if __name__ == '__main__':
#     rand_cite(citations)
