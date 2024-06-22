# Northwest Corner Solver Application

This application solves the transportation problem using the Northwest Corner method. It is built using Python's Tkinter library for the GUI and provides an easy-to-use interface for entering the cost matrix, supply, and demand values.

## Features

- **Input Fields**: Enter the number of rows and columns, cost matrix, supply, and demand values.
- **Solve Button**: Calculates the solution using the Northwest Corner method and displays the result.
- **Example Button**: Loads an example problem into the input fields.
- **Result Display**: Shows the cost matrix, supply, demand, solution matrix, and total cost.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter library (usually included with Python)

### Installation

1. Clone the repository to your local machine.
2. Ensure you have Python 3.x installed.
3. No additional installations are needed for Tkinter as it comes with Python by default.

### Running the Application

1. Navigate to the directory containing the script.
2. Run the script using Python:

   ```bash
   python northwest_corner_solver.py

## Usage

  1.Enter Rows and Columns: Specify the number of rows and columns for the cost matrix.
  2.Enter Costs: Input the cost matrix where each row is separated by a newline.
  3.Enter Supply and Demand: Input the supply and demand values separated by spaces.
  4.Solve: Click the "Solve" button to compute the solution using the Northwest Corner method.
  5.Example: Click the "Example" button to load a sample problem.

 **Buttons**

  - Solve: Computes the result based on the entered values.
  - Example: Loads a predefined example for demonstration purposes.

**Code Structure**

  - northwest_corner: Function implementing the Northwest Corner method.
  - NorthwestCornerApp: Class that creates and manages the GUI.

**Methods in NorthwestCornerApp:**

    _init__: Initializes the GUI components.
    center_window: Centers the application window on the screen.
    solve: Reads inputs, computes the solution, and displays the result.
    load_example: Loads an example problem into the input fields.
