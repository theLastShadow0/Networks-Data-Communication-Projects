def special_encoding_scheme(N: int):
    value = N
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
    
    for i in range(5):
        if nums[i] < 0:
            powers[i] = -powers[i]
    return nums, powers, value

nums, powers, value = special_encoding_scheme(-121)
print(f"The decomposition of the number is {powers} = {value} and the sequence is {nums}")
