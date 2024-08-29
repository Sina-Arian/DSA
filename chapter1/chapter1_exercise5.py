from math import sqrt

def get_scores() -> list:
    scores = []
    n = input("Enter the number: <Enter to finish>")
    while n != '':
        scores.append(int(n))
        n = input("Enter the number: <Enter to finish>")
    return scores

def min_value(nums) -> int:
    min = nums[0]
    for i in nums:
        if i < min:
            min = i
    return min

def max_value(nums) -> int:
    max = nums[0]
    for i in nums:
        if i > max:
            max = i
    return max

def average(nums) -> float:
    n = 0
    sum =0
    for i in nums:
        sum += i
        n += 1
    return sum/n

def std_deviation(nums) -> float:
    assert len(nums) > 1
    n = 0
    mean = average(nums)
    soorat = 0
    for i in nums:
        soorat += (mean - i)**2
        n += 1
    return sqrt(soorat/(n-1))

def main():
    lst = get_scores()
    print('min is {0}'.format(min_value(lst)))
    print('min is {0}'.format(max_value(lst)))
    print('average is {0}'.format(average(lst)))
    print('standard deviation is {0}'.format(std_deviation(lst)))


if __name__ == '__main__':
    main()
