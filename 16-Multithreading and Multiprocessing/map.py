# def make_even(num):
#     if num%2==1:
#         num +=1
#         return num
#     else:
#         return num
    
# x = [102, 201, 304, 607, 509, 901, 603]
# # y= [make_even(i) for i in x ]
# y = list(map(make_even, x))

# print(y)
import sys
sys.set_int_max_str_digits(100000)

# x = int("9" * 99999)  # Gigantic number - can freeze/crash a system

x = int('9' * 10)
print(x)
