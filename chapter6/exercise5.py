def palindrome(string):
    print(string)
    if string == '' or len(string) == 1:
        return True
    else:
        if string[0] == string[-1]:
            string = string[1:-1]
            return palindrome(string)
        else:
            return False


def main():
    s = input("Enter the string: ")
    s_final = []
    for w in s:
        if w in ",! ":
            continue
        else:
            w = w.lower()
            s_final.append(w)
    s_final = ''.join(s_final)
    if palindrome(s_final):
        print("Its a palindrom")
    else:
        print("Its not a palindrom")

main()