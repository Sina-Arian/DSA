import math

def get_scores():
    scoList = []
    while True:
        score = input("Enter the score ( enter f to calculate): ")
        if score == 'f': break
        scoList.append(int(score))
    return scoList

def min_value(nums):
    min = nums[0]
    for i in nums:
        if i < min:
            min = i
    return i

def max_value(nums):
    min = nums[0]
    for i in nums:
        if i > min:
            min = i
    return i

def average(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum/len(nums)

def std_deviation(nums):
    xbar = average(nums)
    sum = 0.0
    for num in nums:
        sum += (xbar - num) ** 2
    return math.sqrt(sum / (len(nums) - 1))

def main():
    scores = get_scores()
    print('''min score is {0}
max score is {1} 
average of scores is {2}
standard deviation is {3}'''.format(min_value(scores), max_value(scores), average(scores), std_deviation(scores)))

if __name__ == "__main__":
    main()