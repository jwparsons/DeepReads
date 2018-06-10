import random
from random import shuffle


def main():
    nums = []
    for x in range(5):
        for y in range(5):
            nums.append((x, random.randint(1, 101)))
    shuffle(nums)
    for num in nums:
        print(num)


if __name__ == "__main__":
    main()
