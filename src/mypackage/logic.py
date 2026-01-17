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

# 6. Recursion (factorial calculation) #

# 7. Search (array ...) #

# 8. Dynamic Programming (memoization palindrome substrings) #

# 9. Behavioural Design Pattern #

