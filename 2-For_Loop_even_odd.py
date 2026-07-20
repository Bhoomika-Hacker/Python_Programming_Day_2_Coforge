even_list = []
odd_list = []

# Separate even and odd numbers
for i in range(1, 11):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

# Display even numbers
print("Even Numbers:")
for i in even_list:
    print(i)

# Display odd numbers
print("\nOdd Numbers:")
for i in odd_list:
    print(i)

# Calculate sum
even_sum = sum(even_list)
odd_sum = sum(odd_list)

print("\nSum of Even Numbers:", even_sum)
print("Sum of Odd Numbers:", odd_sum)

# Calculate average
even_avg = even_sum / len(even_list)
odd_avg = odd_sum / len(odd_list)

print("Average of Even Numbers:", even_avg)
print("Average of Odd Numbers:", odd_avg)

# Count numbers
print("Count of Even Numbers:", len(even_list))
print("Count of Odd Numbers:", len(odd_list))