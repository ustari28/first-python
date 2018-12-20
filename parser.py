import argparse

parser = argparse.ArgumentParser(description="New Parser")
parser.add_argument('bar', help="New Bar", type=int, default=66)
parser.add_argument('--foo', '-foo', help="New food", type=int, default=99)
input = parser.parse_args()

print(input)
print(input.__getattribute__('foo'))
