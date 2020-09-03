all_numbers = []
while True:
    num_int = int(input("Input a number: "))

    if num_int >= 0:
        all_numbers.append(num_int)
    else: 
        break

max_int = max(all_numbers)

print("The maximum is", max_int)
