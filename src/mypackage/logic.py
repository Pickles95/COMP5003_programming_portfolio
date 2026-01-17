# 1. Encryption (RSA algorithm) #

# 2. Dynamic Programming (Nth fibonacci numbers) #
class FibonacciNth:

    def __init__(self):
         self.array = [0, 1]

    def fibonacci(self, n):
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
     fibonacci_input = int(input("Please enter a number: "))
     print("The Fibonacci number is: ", fibonacci_class.fibonacci(fibonacci_input))

# Adapted from https://www.geeksforgeeks.org/python/python-program-for-n-th-fibonacci-number/

# 3. Sorting (bubble sort) #
class SortingBubble:

    def bubble_sort(self, array):

        n = len(array)

        for i in range(n):
            moved = False
            for j in range (0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    moved = True
            if (moved == False):
                break

        return array

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
            middle = len(array) // 2
            left = array[:middle]
            right = array[middle:]
            left_sorted = self.sort(left)
            right_sorted = self.sort(right)

            return self.merge(left_sorted, right_sorted)

    def merge(self, left, right):
        sorted_list = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        while i < len(left):
            sorted_list.append(left[i])
            i += 1

        while j < len(right):
            sorted_list.append(right[j])
            j += 1
        
        return sorted_list

if __name__ == "__main__":
    merge_class = SortingMerge()
    merge_input = input("Please enter a list of numbers separated by spaces: ")
    sorted_list = [int(x) for x in merge_input.split()]
    print("The sorted list is: ", merge_class.sort(sorted_list))

# Adapted from https://www.geeksforgeeks.org/dsa/divide-and-conquer-in-python/

# 5. Randomised (card shuffle) #
import random

class ShuffleDeck:

    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.nums = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.deck = []
        for suit in self.suits:
            for rank in self.nums:
                card = rank + " of " + suit
                self.deck.append(card)

    def shuffle(self):
            n = len(self.deck)

            for i in range(n - 1, 0, -1):
                j = random.randint(0, i + 1)
                self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
                
            return self.deck

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

if __name__ == "__main__":
    factorial_class = FactorialofN()
    factorial_input = int(input("Please enter a number: "))
    factorial = factorial_class.factorial_of(factorial_input)
    print("The factorial of", factorial_input, "is", factorial)

# 7. Search (array) #
class SearchAlgorithm:

    def search(self, array):
        sorted_array = sorted(array)
        n = len(sorted_array)

        # Largest
        largest = sorted_array[-1]
        
        # Smallest
        smallest = sorted_array[0]
        
        # Mode
        total = {}
        for x in sorted_array:
            total[x] = total.get(x, 0) + 1
        mode = max(total, key=total.get)

        # Adapted from https://stackoverflow.com/questions/10797819/finding-the-mode-of-a-list

        # Median
        if n % 2 == 1:
            median = sorted_array[n // 2]
        else:
            median = (sorted_array[n // 2 - 1] + sorted_array[n // 2]) / 2

        # Adapted from https://stackoverflow.com/questions/24101524/finding-median-of-list-in-python

        # 1st IQF
        lower = sorted_array[:n // 2]
        lower_n = len(lower)
        if lower_n % 2 == 1:
            iqf_q1 = lower[lower_n // 2]
        else:
            iqf_q1 = (lower[lower_n // 2 - 1] + lower[lower_n // 2]) / 2
            
        # 3rd IQF
        upper = sorted_array[(n + 1) // 2 if n % 2 != 0 else n // 2:]
        upper_n = len(upper)
        if upper_n % 2 == 1:
            iqf_q3 = upper[upper_n // 2]
        else:
            iqf_q3 = (upper[upper_n // 2 - 1] + upper[upper_n // 2]) / 2

        return [smallest, largest, mode, median, iqf_q1, iqf_q3]  

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
   
    def __init__(self):
        self.palindrome = None

    def palindrome_length(self, string):
        n = len(string)
        self.palindrome = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        reversed_string = string[::-1]
        return self.find_palindrome(string, reversed_string, n, n)

    def find_palindrome(self, s1, s2, n1, n2):
        if n1 == 0 or n2 == 0:
            return 0

        if self.palindrome[n1][n2] != -1:
            return self.palindrome[n1][n2]

        if s1[n1 - 1] == s2[n2 - 1]:
            self.palindrome[n1][n2] = 1 + self.find_palindrome(s1, s2, n1 - 1, n2 - 1)
        else:
            self.palindrome[n1][n2] = max(
                self.find_palindrome(s1, s2, n1 - 1, n2), 
                self.find_palindrome(s1, s2, n1, n2 - 1)
            )
            
        return self.palindrome[n1][n2]

if __name__ == "__main__":
    palindrome_class = PalindromeSubstring()
    palindrome_input = str(input("Please enter a word: "))
    print("The longest palindrome substring in this word is: ", palindrome_class.palindrome_length(palindrome_input), "letters long.")

# 9. Behavioural Design Pattern #

# 10. Creational Design Pattern #

# 11. Structural Design Pattern #

