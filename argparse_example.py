
# You want an argument to be optional, it could be given, or it could be not
import os

cwd = os.getcwd()

parser = argparse.ArgumentParser(description='Parsing cli arguments')
# nargs specifies the number of arguments, ? means 0 or 1
parser.add_argument('--dir', default=cwd, type=str, nargs='?')


# to view help
parser.print_help()

# If you want an argument which can be of 3 different values
parser.add_argument('red_color', choices=('red', 'pink', 'ruby'))


# What if you want an argument which doesn't take any value, but instead is used as a flag
# ex. --cold, --hot. It's kind of a boolean value.


# What if you want two arguments to be mutually exclusive, i.e. either one or another 
# is used at the same time

parser = argparse.ArgumentParser(description='Doing some tasks')
group = parser.add_mutually_exclusive_group()
group.add_argument('-b', action='store_true', help="Proceed to task B")
group.add_argument('-c', action='store_true', help="Proceed to task C")

# error raised, because b and c are mutually exclusive
args=parser.parse_args('-b -c'.split())
# OK
args=parser.parse_args('-b'.split())
# OK
args=parser.parse_args('-c'.split())


# What if you want an argument to take an argument?
# Let's say you want some arg "book" to take the name of the book
# but if you say "newspaper", it should take the name of the newspaper

parser = argparse.ArgumentParser(description='parser with subcommands')
subparser = parser.add_subparsers(help='choose book/newspaper')
parser_book = subparser.add_parser('book', help='the book')
parser_newspaper = subparser.add_parser('newspaper', help='the newspaper')
parser_book.add_argument('title', help='title of the book', type=str)
# _StoreAction(option_strings=[], dest='title', nargs=None, const=None, default=None, type=<type 'str'>, choices=None, help='title of the book', metavar=None)

parser_newspaper.add_argument('title', help='title of the newspaper', type=str)
# _StoreAction(option_strings=[], dest='title', nargs=None, const=None, default=None, type=<type 'str'>, choices=None, help='title of the newspaper', metavar=None)
parser.print_help()
# usage: ipython [-h] {book,newspaper} ...

# parser with subcommands

# positional arguments:
#   {book,newspaper}  choose book/newspaper
#     book            the book
#     newspaper       the newspaper

# optional arguments:
#   -h, --help        show this help message and exit

# To ry it:
parser.parse_args(['book', 'Alice In Wonderland'])
