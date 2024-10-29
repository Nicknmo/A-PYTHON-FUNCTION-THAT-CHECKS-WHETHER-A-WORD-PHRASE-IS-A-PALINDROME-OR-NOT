def chk_palindrome(string):
    left_side_pos = 0
    right_side_pos = len(string) - 1
    
    while right_side_pos >= left_side_pos:
        if string[left_side_pos] != string[right_side_pos]:
            return False
        left_side_pos += 1
        right_side_pos -= 1
    
    return True

str1 = input("Enter the string: ")
print(chk_palindrome(str1))




