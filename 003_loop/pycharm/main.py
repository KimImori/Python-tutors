number = int(input('Enter the number'))

reversed_number = 0
tmp_original = number

while tmp_original > 0:
    reversed_number = (reversed_number * 10) +tmp_original % 10
    tmp_original = tmp_original //10
    print("----------")
    print(reversed_number, tmp_original)


if number == reversed_number:
    print('Palindrome')
else:
    print("No Palindrome")
