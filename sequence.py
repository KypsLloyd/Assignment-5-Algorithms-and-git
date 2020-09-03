# Byrja nú þegar með fyrstu 3 tölurnar í röðinni í lista, nota svo tvær for loop-ur til að leggja saman seinustu þrjár tölur og append-a svo sú tölu í sama lista  

inital_sequence = [1, 2, 3]

n = int(input("Enter the length of the sequence: ")) # Do not change this line

for x in range(0, n-3):
    sum = 0
    for i in inital_sequence[-3:]:
        sum += i
    inital_sequence.append(sum)

for i in inital_sequence:
    print(i)
print(inital_sequence)