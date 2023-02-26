#Fibonnaci sequence
num_term = int(input("How many terms would you like to show? "))

#defining terms
count = 0
first_term = 0
sec_term = 1

if num_term <= 0:
    print("Please enter a positive integer")

elif num_term == 1:
    print("1")
else:
    print("Fibonnaci sequence: ")
    while count < num_term:
        print(first_term)
        #add
        num_fib = first_term + sec_term
        #update
        first_term = sec_term
        sec_term = num_fib
        count += 1
