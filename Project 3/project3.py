def special_encoding_scheme(N: int):
    powers = [81, 27, 9, 3, 1]
    nums = [0,0,0,0,0]
    for i in range(5):
        if abs(N) >= powers[i]:
            if N < 0:
                nums[i] = -1
                N = N + powers[i]
            else:
                nums[i] = 1
                N = N - powers[i]
        elif i != len(nums) - 1:
            if abs(N) > powers[i + 1]:
                if N < 0:
                    nums[i] = -1
                    N = N + powers[i]
                else:
                    nums[i] = 1
                    N = N - powers[i]
            else:
                nums[i] = 0
    return nums

print(special_encoding_scheme(-3))
print(special_encoding_scheme(7))
print(special_encoding_scheme(-5))
print(special_encoding_scheme(9))
print(special_encoding_scheme(-16))
print(special_encoding_scheme(25))
print(special_encoding_scheme(-89))
print(special_encoding_scheme(121))
print(special_encoding_scheme(-121))