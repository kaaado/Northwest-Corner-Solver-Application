import tkinter as tk
from tkinter import ttk

def northwest_corner(costs, supply, demand):
    rows = len(supply)
    cols = len(demand)
    solution = [[0] * cols for _ in range(rows)]
    i, j = 0, 0
    while i < rows and j < cols:
        quantity_allocated = min(supply[i], demand[j])
        solution[i][j] = quantity_allocated
        supply[i] -= quantity_allocated
        demand[j] -= quantity_allocated
        if supply[i] == 0:
            i += 1
        if demand[j] == 0:
            j += 1
    total_cost = sum(costs[i][j] * solution[i][j] for i in range(rows) for j in range(cols))
    return solution, total_cost

class NorthwestCornerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Northwest Corner Solver")
        self.label_rows = ttk.Label(root, text="Enter the number of rows:")
        self.label_rows.grid(row=0, column=0, pady=5)
        self.entry_rows = ttk.Entry(root)
        self.entry_rows.grid(row=0, column=1, pady=5)
        self.label_cols = ttk.Label(root, text="Enter the number of columns:")
        self.label_cols.grid(row=1, column=0, pady=5)
        self.entry_cols = ttk.Entry(root)
        self.entry_cols.grid(row=1, column=1, pady=5)
        self.text_costs_label = ttk.Label(root, text="Enter costs:")
        self.text_costs_label.grid(row=2, column=0)
        self.text_costs = tk.Text(root, height=6, width=30)
        self.text_costs.grid(row=3, column=0)
        self.text_supply_label = ttk.Label(root, text="Enter supply:")
        self.text_supply_label.grid(row=0, column=1, rowspan=4, pady=5)
        self.text_supply = tk.Text(root, height=1, width=15)
        self.text_supply.grid(row=0, column=2, rowspan=4, pady=5)
        self.text_demand_label = ttk.Label(root, text="Enter demand:")
        self.text_demand_label.grid(row=2, column=1, rowspan=4, pady=5)
        self.text_demand = tk.Text(root, height=1, width=15)
        self.text_demand.grid(row=2, column=2, rowspan=4, pady=5)
        self.solve_button = ttk.Button(root, text="Solve", command=self.solve)
        self.solve_button.grid(row=5, column=0, columnspan=4, pady=10)
        self.example_button = ttk.Button(root, text="Example", command=self.load_example)
        self.example_button.grid(row=6, column=0, columnspan=4, pady=10)
        self.result_label = ttk.Label(root, text="Result:")
        self.result_label.grid(row=7, column=0, columnspan=4, pady=5)
        self.text_result = tk.Text(root, height=15, width=40)
        self.text_result.grid(row=8, column=0, columnspan=4, pady=5)
        self.desired_height = 550
        self.desired_width = 550
        self.center_window()
#yacine kermame  & farouk khaldii
    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - self.desired_width) // 2
        y = (screen_height - self.desired_height) // 2
        self.root.geometry(f"{self.desired_width}x{self.desired_height}+{x}+{y}")

    def solve(self):
        try:
            rows = int(self.entry_rows.get())
            cols = int(self.entry_cols.get())
            costs = [[int(cell) for cell in row.split()] for row in self.text_costs.get("1.0", tk.END).splitlines()]
            supply = [int(val) for val in self.text_supply.get("1.0", tk.END).split()]
            demand = [int(val) for val in self.text_demand.get("1.0", tk.END).split()]
            if len(costs) != rows or len(costs[0]) != cols or len(supply) != rows or len(demand) != cols:
                raise ValueError("Dimensions of costs, supply, and demand do not match the specified rows and columns.")
            solution, total_cost = northwest_corner(costs, supply, demand)
            self.text_result.delete(1.0, tk.END)
            self.text_result.insert(tk.END, "Costs:\n")
            for row in costs:
                self.text_result.insert(tk.END, f"{row}\n")
            self.text_result.insert(tk.END, "\nSupply:\n")
            for val in supply:
                self.text_result.insert(tk.END, f"{val} ")
            self.text_result.insert(tk.END, "\nDemand:\n")
            for val in demand:
                self.text_result.insert(tk.END, f"{val} ")
            self.text_result.insert(tk.END, "\nSolution:\n")
            for row in solution:
                self.text_result.insert(tk.END, f"{row}\n")
            self.text_result.insert(tk.END, f"Total cost: {total_cost}")
        except ValueError as e:
            self.text_result.delete(1.0, tk.END)
            self.text_result.insert(tk.END, f"Error: {str(e)}")

    def load_example(self):
        example_costs = "2 3 1 7\n5 4 8 2\n7 6 9 4"
        example_demand= "10 20 20 10"
        example_supply = "15 15 30"
        self.entry_rows.delete(0, tk.END)
        self.entry_rows.insert(0, "3")
        self.entry_cols.delete(0, tk.END)
        self.entry_cols.insert(0, "4")
        self.text_costs.delete(1.0, tk.END)
        self.text_costs.insert(tk.END, example_costs)
        self.text_supply.delete(1.0, tk.END)
        self.text_supply.insert(tk.END, example_supply)
        self.text_demand.delete(1.0, tk.END)
        self.text_demand.insert(tk.END, example_demand)

if __name__ == "__main__":
    root = tk.Tk()
    app = NorthwestCornerApp(root)
    root.mainloop()
