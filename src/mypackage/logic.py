# 1. Encryption (RSA algorithm) #

# 2. Dynamic Programming (Nth fibonacci numbers) #
class FibonacciNth:

    def __init__(self):
         self.array = [0, 1]

    def fibonacci(self, n: int):
            if n < 0:
                return "error"
            elif n <= len(self.array):
                return self.array[n - 1]

            for i in range(len(self.array), n + 1):
               memory = self.array[i - 1] + self.array[i - 2]
               self.array.append(memory)

            return self.array[n]

if __name__ == "__main__":
     fibonacci_class = FibonacciNth()
     user_input = int(input("Please enter your number:"))
     print(fibonacci_class.fibonacci(user_input))



# 3. Sorting (bubble sort) #

# 4. Brute Force (divide and conquer merge) #

# 5. Randomised (card shuffle) #

# 6. Recursion (factorial calculation) #

# 7. Search (array ...) #

# 8. Dynamic Programming (memoization palindrome substrings) #

# 9. Behavioural Design Pattern #

