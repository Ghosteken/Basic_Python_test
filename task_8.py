import random

binary_number = ''.join([random.choice(['0', '1']) for _ in range(4)])

decimal_number = int(binary_number, 2)

print("binary number:", binary_number)
print("Converted to base 10:", decimal_number)
