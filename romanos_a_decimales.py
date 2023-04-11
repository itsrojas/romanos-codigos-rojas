def roman_to_decimal(roman):
    total = 0
    for letter in roman:
        if letter == 'I':
            total += 1
        elif letter == 'V':
            if total > 0:
                total = -1
            total += 5
        elif letter == 'X':
            if total > 0:
                total = -1
            total += 10
        elif letter == 'L':
            if total > 0:
                total = -1
            total += 50
        elif letter == 'C':
            if total > 0:
                total = -1
            total += 100
        elif letter == 'D':
            if total > 0:
                total = -1
            total += 500
        elif letter == 'M':
            if total > 0:
                total = -1
            total += 1000
    return total

if __name__ == '__main__':
    print(roman_to_decimal(1))