#HELLO WORLD! I AM PRIME 10000
#This program is meant to take a number from the user
#then collect prime numbers from 1 to the input number
#and prints the prime numbers
# Author: Yousef Kilany || Nov.18th 2021

#Necessary Libraries
import time
import math

#We start by declaring and assigning the storing list, an indicator for prime or not
#number of primes inside the list(items),
#and an index to use when dividing by elements in the list.
primes = [1, 2]
is_prime = True
measure_index = 0
largest_gap = 0

big = 0
small = 0

#We take a number from user, turn it to int, store it.
input_num = int(input("Please enter a number: "))

#This is the timer
start = time.time()

#Here we check because we already have all prime numbers < 3 inside our list
if (input_num < 3):
    print ("This is not a valid input!")
else:

    #This is the major loop that loops from 3 to the input number by user
    for number in range (3, input_num + 1):
        
        #everytime this loop changes the number that we need to check if prime
        #we assume at the start it is a prime
        #we reset measure index also to start from the begining of our primes list.
        is_prime = True
        measure_index = 0

        #This loop checks if the number(from major loop) we are at if prime
        #it goes from item 0 to number of items(items)
        while (measure_index < len(primes)):
            
            #we divide the number(from major loop) we are at by the first element
            #and check if (there is remainder, the number is not being divided by itself and by 1)
            #if true then it is not a prime and the indicator becomes (false)
            if (number % primes[measure_index] == 0 & number != primes[measure_index] & primes[measure_index] != 1):
                is_prime = False

            #this loop breaks immediatly when number is found to be non prime
            if (is_prime == False):
                break

            #Here we check if the index has reached the end of the primes list
            if (measure_index < len(primes) - 1):
                measure_index = measure_index + 1
            
            #this loop breaks right after the last element in the list which is >= squrt of the number
            if (primes[measure_index] > math.sqrt(number)):
                break

        #This is the storage unit, checks if the minor loop has returned a prime or not
        # if prime we add it our list of prime numbers, and we increase index of items inside    
        if (is_prime):
            primes.append(number)
        big = primes[len(primes) - 1]
        small = primes[len(primes) - 2]
        if (big - small > largest_gap):
            largest_gap = big - small


print("It Took me ", (time.time() - start), "seconds to Finish")
print("There are", len(primes), "prime numbers")
    #print(primes)
print("Largest gap between two primes is: ", largest_gap)
