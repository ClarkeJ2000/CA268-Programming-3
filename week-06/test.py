import sys
from post_order import BST

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]

    tree = BST()
    for num in nums:
        tree.add(num)

    print("Print the elements of the tree in order:")
    tree.pre_order()

if __name__ == "__main__":
    main()