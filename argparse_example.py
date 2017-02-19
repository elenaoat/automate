
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

