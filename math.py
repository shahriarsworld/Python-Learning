# import math
#
# # Angle in radians
# angle = math.radians(90)
#
# # Trigonometric functions
# sin_result = math.sin(angle)
# cos_result = math.cos(angle)
# tan_result = math.tan(angle)
#
# print("Sine of 45 degrees:", sin_result)
# print("Cosine of 45 degrees:", cos_result)
# print("Tangent of 45 degrees:", tan_result)
#
# import math
#
# # Exponential function
# exp_result = math.exp(2)
# print("e raised to the power of 2:", exp_result)
#
# # Logarithm with base 10
# log_result = math.log(100, 10)
# print("Logarithm of 100 with base 10:", log_result)
#
# import math
#
# # Rounding examples
# ceil_result = math.ceil(3.14)
# floor_result = math.floor(3.14)
# trunc_result = math.trunc(3.14)
#
# print("Ceiling of 3.14:", ceil_result)
# print("Floor of 3.14:", floor_result)
# print("Truncated value of 3.14:", trunc_result)


import math

def compound_interest(principal, rate, time, n):
    return principal * (1 + rate/n)**(n*time)

print("Compound interest:", compound_interest(10000, 0.05, 10, 12))

