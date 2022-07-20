## Fibonacci Sequence generator
## 
## Select a number and it will generate the sequence up to that point
## Fibonacci Sequence: 0,1,1,2,3,5,8...
## 0+1 = 1, 1+1 = 2, 1+2 = 3, 2+3 = 5, 3+5 = 8, etc

print('Enter length of the sequence: ')

## Validate user input
while True:
    seq_num = input()
    try:
        usr_val = int(seq_num)
        break
    except ValueError:
        print('Input is not a number! Please enter a new value.')

## Generate sequence
counter = 0
val_1 = 0
val_2 = 1