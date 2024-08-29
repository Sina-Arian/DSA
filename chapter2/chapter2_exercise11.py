from chapter2_exercise10 import Rational

'''11. Use your Rational class to write a program that investigate Egyptian fractions ...'''

def egyption():
    rational_in = input("Enter the number: ")
    r_list = rational_in.split('/')
    n, d = int(r_list[0]), int(r_list[1])
    r = Rational(n, d)
    egyption_number = []
    if r.numinator() == 1 or r.numinator() == 0:
        print('Enter the correct number')
    else:
        while r.numinator() != 1:
            a = Rational(1, r.reverse_ceil())
            egyption_number.append(a)
            r = r - a
            if r.numinator() == 1:
                egyption_number.append(r)

    for i in egyption_number:
        print(i)

if __name__ == '__main__':
    egyption()