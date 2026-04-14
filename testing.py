# user_input = input("Enter your word: ")

# def palindrome_checker(user_input):
#     i = 0
#     while i <= len(user_input)/2:
#         if user_input[i] == user_input[-(i+1)]:
#             i += 1
#         else:
#             return False
#     return True

# answer = palindrome_checker(user_input)

# if answer == True:
#     print("This is a palindrome")
# elif answer == False:
#     print("This is not a palindrome")

user_input = input()

if user_input == user_input[::-1]:
    print("palindrome!")
else:
    print("not palindrome")