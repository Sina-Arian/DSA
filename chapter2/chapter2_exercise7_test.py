from chapter2_exercise7 import Dataset1, Dataset2

def main():
    print('This is a program to compute the min, max, mean and')
    print('standard deviation doe a set of numbers. \n')
    data1 = Dataset1()
    data2 = Dataset2()
    while True:
        xStr = input("Enter a number (<Enter> to quit): ")
        if xStr == '':
            break
        try:
            x = float(xStr)
        except ValueError:
            print("Invalid Entry Ignored: Input was not a number")
            continue
        data1.add(x)
        data2.add(x)
    print('Summary of', data1.size(), data2.size(), 'scores.')
    print('Min:', data1.min(), data2.min())
    print('Max:', data1.max(), data2.max())
    print('Mean:', data1.average(), data2.average())
    print('Standard Deviation:', data1.std_deviation(), data2.std_deviation())

main()