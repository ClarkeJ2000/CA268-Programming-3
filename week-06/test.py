import sys
from rotation_type import avl_rotation_type
from student import rotation_type

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]

    tree = BST(nums)

    print(rotation_type(tree))

if __name__ == "__main__":
    main()