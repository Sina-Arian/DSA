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
    nine, eight, seven, six, below = numbers(lst)
    print('numbers of 90s are {nine}\nnumbers of 80s are {eight}\nnumbers of 70s are {seven}\nnumbers of 60s are {six}\nnumbers of below 50s are {below}'.format(**locals()))


def numbers(nums):
    """ finds the numbers in 90s, 80s, 70s, 60s and below 50
    
    pre: nums is a list of numbers between 1 to 100
    post: returns five numbers in order of 
          numbers in 90s, numbers in 80s, numbers in 70s, numbers in 60s and numbers below 50 """

    nine = eight = seven = six = below = 0
    for i in nums:
        if (i//9) == 10:
            nine += 1
        elif (i//8) == 10:
            eight += 1
        elif (i//7) == 10:
            seven += 1
        elif (i//6) == 10:
            six += 1
        else:
            below += 1
    return nine, eight, seven, six, below


if __name__ == '__main__':
    main()
