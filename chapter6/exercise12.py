'''12.Write a program that solves word jumble problems. You will need a large file of English words. If you have a Unix or Linux ...s'''

def anagrams(s):
    if s == "":
        return [s]

    else:
        ans = []
        for w in anagrams(s[1:]):
            for pos in range(len(w) + 1):
                ans.append(w[:pos] + s[0] + w[pos:])
        return ans

def main():
    inWord = input("Enter the jumble: ")
    inWord = inWord.lower()
    anagram_list = anagrams(inWord)

    inFile = open('linuxwords.txt', 'r')
    words = []
    w = inFile.read()
    words = w.split('\n')
    
    print(words)
    for i in anagram_list:
        if i in words:
            return i

print(main())