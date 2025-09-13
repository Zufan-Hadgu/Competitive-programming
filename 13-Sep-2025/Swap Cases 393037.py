# Problem: Swap Cases - https://www.hackerrank.com/challenges/swap-case?isFullScreen=true

def swap_case(s):
    new = ""
    for char in s:
        if char.islower():
            new += char.upper()
        elif char.isupper():
            new += char.lower()
        else:
            new += char
    return new

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)