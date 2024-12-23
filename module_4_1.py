from fake_math import divide as divide_fake
from true_math import divide as divide_true

result1 = divide_fake(69, 3)
result2 = divide_fake(3, 0)
result3 = divide_true(49, 7)
result4 = divide_true(15, 0)
result5 = divide_true(627054621.66666, 0)
result6 = divide_true(90192029021, 2109379172.222222)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)