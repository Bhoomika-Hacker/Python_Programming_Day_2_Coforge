sum_odd = 0
sum_even = 0
count_odd = 0
count_even = 0

for num in range(1, 51):
    if num % 2 == 0:
        sum_even = sum_even + num
        count_even = count_even + 1
    else:
        sum_odd = sum_odd + num
        count_odd = count_odd + 1

avg_odd = sum_odd / count_odd if count_odd > 0 else 0
avg_even = sum_even / count_even if count_even > 0 else 0

total_sum = sum_odd + sum_even
total_count = count_odd + count_even
total_avg = total_sum / total_count if total_count > 0 else 0

print(f"Sum of odd numbers: {sum_odd}")
print(f"Sum of even numbers: {sum_even}")
print(f"Average of odd numbers: {avg_odd}")
print(f"Average of even numbers: {avg_even}")
print(f"Count of odd numbers: {count_odd}")
print(f"Count of even numbers: {count_even}")
print(f"Total sum of even and odd numbers: {total_sum}")
print(f"Total average of even and odd numbers: {total_avg}")
print(f"Total count of even and odd numbers: {total_count}")