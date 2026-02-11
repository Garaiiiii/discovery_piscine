#!/usr/bin/env python3
num_arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []
for i in num_arr:
	if (i > 5):
		new_arr.append(i + 2)
print(f"Original array: {num_arr}\nNew array: {new_arr}")
