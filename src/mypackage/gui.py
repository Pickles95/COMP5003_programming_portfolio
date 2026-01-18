import tkinter as tk
from logic import FacadeAlgorithm

class PortfolioGUI:

    # Open main window
    def __init__(self, main_window):
        self.root = main_window
        self.root.title("COMP5003: Programming Portfolio")
        self.root.geometry("400x800")
        self.root.configure(bg="#7C2181")
        
        # Link the GUI to the Facade
        self.logic = FacadeAlgorithm()

        # UoW Logo
        self.UoWLogo = tk.PhotoImage(file="Summative/COMP5003_programming_portfolio/src/mypackage/UoWLogo.png")
        self.UoWLogo = self.UoWLogo.subsample(1, 1)
        self.logo_display = tk.Label(root, image=self.UoWLogo, bg="#702A6A")
        self.logo_display.pack(pady=10)

        # Add an entry field for user
        tk.Label(root, text="Enter Input:", bg="#7C2181", fg="white").pack()
        self.input_entry = tk.Entry(root, width = 40)
        self.input_entry.pack(pady = 10)

        # Add buttons to run specific algorithms
        tk.Button(root, text = "Fibonacci Number", width = 25, command=lambda: self.run("Fibonacci")).pack(pady = 2)
        tk.Button(root, text = "Factorial Number", width = 25, command=lambda: self.run("Factorial")).pack(pady = 2)
        tk.Button(root, text = "Bubble Sort", width = 25, command=lambda: self.run("Bubble")).pack(pady = 2)
        tk.Button(root, text = "Merge Sort", width = 25, command=lambda: self.run("Merge")).pack(pady = 2)
        tk.Button(root, text = "Search Array", width = 25, command=lambda: self.run("Search")).pack(pady = 2)
        tk.Button(root, text = "Shuffle Deck", width = 25, command=lambda: self.run("Random")).pack(pady = 2)
        tk.Button(root, text = "Palindrome Length", width = 25, command=lambda: self.run("Palindrome")).pack(pady = 2)

        # Add a label to show results
        tk.Label(root, text = "Results:", bg = "#702A6A", fg = "white").pack(pady = 10)
        self.result_text = tk.Text(root, height = 10, width = 40)
        self.result_text.pack(pady = 5)

    def run(self, algorithm):
        user_input = self.input_entry.get().strip()
        
        # String conversions for each algorithm
        if algorithm in ["Fibonacci", "Factorial"]:
            value = int(user_input)
        elif algorithm in ["Bubble", "Merge"]:
            value = [int(x) for x in user_input.split()]
        elif algorithm == "Search":
            value = [float(x) for x in user_input.split()]
        else:
            value = user_input

        # Run the logic through Facade
        answer = self.logic.run_algorithm(algorithm, value)

        # Clear previous results
        self.result_text.delete("1.0", tk.END)
        
    
        if algorithm == "Search":
            labels = ["Min", "Max", "Mode", "Median", "Q1", "Q3"]
            result = ""
            for i in range(len(labels)):
                label = labels[i]
                index = str(answer[i])
                result = result + label + ": " + index + "\n"
            self.result_text.insert(tk.END, result)
        elif algorithm == "Random":
            self.result_text.insert(tk.END, "\n".join(answer))
        else:
            self.result_text.insert(tk.END, str(answer))

# Run Tkinter loop
if __name__ == "__main__":
    root = tk.Tk()
    PortfolioGUI(root)
    root.mainloop()

# Adapted from https://www.geeksforgeeks.org/python/python-gui-tkinter/