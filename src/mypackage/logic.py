import random

# 1. Encryption (RSA algorithm) #

# 2. Dynamic Programming (Nth fibonacci numbers) #
class FibonacciNth:

    # Uses a list to store previous results
    def __init__(self):
         self.array = [0, 1]

    def fibonacci(self, n):
            if n < 0:
                return "error"
            elif n <= len(self.array):
                return self.array[n - 1]

            # Calculate new numbers based on sum of last two
            for i in range(len(self.array), n + 1):
               memory = self.array[i - 1] + self.array[i - 2]
               self.array.append(memory)

            return self.array[n]

# Fibonacci Algorithm Test
if __name__ == "__main__":
     fibonacci_class = FibonacciNth()
     fibonacci_input = int(input("Please enter a number: "))
     print("The Fibonacci number is: ", fibonacci_class.fibonacci(fibonacci_input))

# Adapted from https://www.geeksforgeeks.org/python/python-program-for-n-th-fibonacci-number/

# 3. Sorting (bubble sort) #
class SortingBubble:

    def bubble_sort(self, array):

        n = len(array)

        # Check list is already sorted
        for i in range(n):
            moved = False
            for j in range (0, n - i - 1):
                # Compare and swap adjacent numbers
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    moved = True
            # If nothing gets moved then break        
            if (moved == False):
                break

        return array

# Bubble Sort Algorithm Test
if __name__ == "__main__":
    sorting_class = SortingBubble()
    bubble_input = input("Please enter a list of numbers separated by spaces: ")
    sorted_list = [int(x) for x in bubble_input.split()]
    print("The sorted list is: ", sorting_class.bubble_sort(sorted_list))

# Adapted from https://www.geeksforgeeks.org/dsa/bubble-sort-algorithm/

# 4. Brute Force (divide and conquer merge) #
class SortingMerge:

    def sort(self, array):
        if len(array) <= 1:
            return array
        else:
            # Split the list into two halves
            middle = len(array) // 2
            left = array[:middle]
            right = array[middle:]
            # Sort the halves recursively
            left_sorted = self.sort(left)
            right_sorted = self.sort(right)

            return self.merge(left_sorted, right_sorted)

    # Merge the halves back together
    def merge(self, left, right):
        sorted_list = []
        i = 0
        j = 0

        # Compare and find smallest number
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        # Append remaining numbers
        while i < len(left):
            sorted_list.append(left[i])
            i += 1

        while j < len(right):
            sorted_list.append(right[j])
            j += 1
        
        return sorted_list

# Merge Sort Algorithm Test
if __name__ == "__main__":
    merge_class = SortingMerge()
    merge_input = input("Please enter a list of numbers separated by spaces: ")
    sorted_list = [int(x) for x in merge_input.split()]
    print("The sorted list is: ", merge_class.sort(sorted_list))

# Adapted from https://www.geeksforgeeks.org/dsa/divide-and-conquer-in-python/

# 5. Randomised (card shuffle) #
class ShuffleDeck:

    # Create a deck of cards using lists
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.nums = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.deck = []
        # Generate all combinations
        for suit in self.suits:
            for rank in self.nums:
                card = rank + " of " + suit
                self.deck.append(card)

    def shuffle(self):
            n = len(self.deck)

            # Swap each card randomly (Fisher-Yates)
            for i in range(n - 1, 0, -1):
                j = random.randint(0, i + 1)
                self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
                
            return self.deck

# Deck Shuffle Algorithm Test
if __name__ == "__main__":
    shuffle_class = ShuffleDeck()
    shuffled_deck = shuffle_class.shuffle()
    print("Shuffled Deck: ", shuffled_deck)

# Adapted from https://www.geeksforgeeks.org/dsa/shuffle-a-given-array-using-fisher-yates-shuffle-algorithm/

# 6. Recursion (factorial calculation) #
class FactorialofN:

    def factorial_of(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial_of(n - 1)

# Factorial Algorithm Test
if __name__ == "__main__":
    factorial_class = FactorialofN()
    factorial_input = int(input("Please enter a number: "))
    factorial = factorial_class.factorial_of(factorial_input)
    print("The factorial of", factorial_input, "is", factorial)

# Adapted from https://www.geeksforgeeks.org/python/recursion-in-python/

# 7. Search (array) #
class SearchAlgorithm:

    # Sort the array in ascending order
    def search(self, array):
        sorted_array = sorted(array)
        n = len(sorted_array)

        # Smallest is the first index and largest is the last
        largest = sorted_array[-1]
        smallest = sorted_array[0]
        
        # Find the mode by counting frequency of numbers
        total = {}
        for x in sorted_array:
            total[x] = total.get(x, 0) + 1
        mode = max(total, key=total.get)

        # Adapted from https://stackoverflow.com/questions/10797819/finding-the-mode-of-a-list

        # Find the median by calculating the average
        if n % 2 == 1:
            median = sorted_array[n // 2]
        else:
            median = (sorted_array[n // 2 - 1] + sorted_array[n // 2]) / 2

        # Adapted from https://stackoverflow.com/questions/24101524/finding-median-of-list-in-python

        # Find the 1st IQF by finding the median of the lower half of the array
        lower = sorted_array[:n // 2]
        lower_n = len(lower)
        if lower_n % 2 == 1:
            iqf_q1 = lower[lower_n // 2]
        else:
            iqf_q1 = (lower[lower_n // 2 - 1] + lower[lower_n // 2]) / 2
            
        # Find the 3rd IQF by finding the median of the upper half of the array
        upper = sorted_array[(n + 1) // 2 if n % 2 != 0 else n // 2:]
        upper_n = len(upper)
        if upper_n % 2 == 1:
            iqf_q3 = upper[upper_n // 2]
        else:
            iqf_q3 = (upper[upper_n // 2 - 1] + upper[upper_n // 2]) / 2

        return [smallest, largest, mode, median, iqf_q1, iqf_q3]  

# Search Algorithm Test
if __name__ == "__main__":
    search_class = SearchAlgorithm()
    user_input = input("Enter an array of numbers (space separated): ")
    sorted_list = [float(x) for x in user_input.split()]
    results = search_class.search(sorted_list)
    print("Smallest:", results[0])
    print("Largest:", results[1])
    print("Mode:", results[2])
    print("Median:", results[3])
    print("1st IQF:", results[4])
    print("3rd IQF:", results[5])
    
# 8. Dynamic Programming (memoization palindrome substrings) #
class PalindromeSubstring:

    # Matrix to store results
    def __init__(self):
        self.palindrome = None

    def palindrome_length(self, string):
        n = len(string)
        self.palindrome = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        # Find the palindrome (same as finding LCS of a string)
        reversed_string = string[::-1]
        return self.find_palindrome(string, reversed_string, n, n)

    def find_palindrome(self, s1, s2, n1, n2):
        if n1 == 0 or n2 == 0:
            return 0

        # Return saved result if already calculated
        if self.palindrome[n1][n2] != -1:
            return self.palindrome[n1][n2]

        # +1 to result if letters match
        if s1[n1 - 1] == s2[n2 - 1]:
            self.palindrome[n1][n2] = 1 + self.find_palindrome(s1, s2, n1 - 1, n2 - 1)
        # If no match, find best result 
        else:
            self.palindrome[n1][n2] = max(
                self.find_palindrome(s1, s2, n1 - 1, n2), 
                self.find_palindrome(s1, s2, n1, n2 - 1)
            )
            
        return self.palindrome[n1][n2]

# Palindrome Algorithm Test
if __name__ == "__main__":
    palindrome_class = PalindromeSubstring()
    palindrome_input = str(input("Please enter a word: "))
    print("The longest palindrome substring in this word is: ", palindrome_class.palindrome_length(palindrome_input), "letters long.")

# Adapted from https://www.geeksforgeeks.org/dsa/longest-palindromic-subsequence-in-python/

# 9. Behavioural Design Pattern #

# 10. Creational Design Pattern (Factory) #
class FactoryAlgorithm:
    
    # Acts like a warehouse to handle the creation of objects
    def get_algorithm(self, algorithm_type):
        if algorithm_type == "Fibonacci":
            return FibonacciNth()
        elif algorithm_type == "Bubble":
            return SortingBubble()
        elif algorithm_type == "Merge":
            return SortingMerge()
        elif algorithm_type == "Random":
            return ShuffleDeck()
        elif algorithm_type == "Factorial":
            return FactorialofN()
        elif algorithm_type == "Search":
            return SearchAlgorithm()
        elif algorithm_type == "Palindrome":
            return PalindromeSubstring()
        else:
            return None

# 11. Structural Design Pattern (Facade) #
class FacadeAlgorithm:
    
    # Uses the Factory to creat objects
    def __init__(self):
        self.factory = FactoryAlgorithm()

    # Allows GUI to run the algorithms
    def run_algorithm(self, name, user_input):
        obj = self.factory.get_algorithm(name)
        
        # Links GUI call to algorithm
        if name == "Fibonacci":
            return obj.fibonacci(user_input)
        elif name == "Bubble":
            return obj.bubble_sort(user_input)
        elif name == "Merge":
            return obj.sort(user_input)
        elif name == "Random":
            return obj.shuffle()
        elif name == "Factorial":
            return obj.factorial_of(user_input)
        elif name == "Search":
            return obj.search(user_input)
        elif name == "Palindrome":
            return obj.palindrome_length(user_input)