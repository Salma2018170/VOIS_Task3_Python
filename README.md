# Employee Data Processing with Python

This Task processes employee data from a CSV file using Python and pandas. The goal is to clean the data, calculate some basic statistics, and write the results to a new CSV file.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running in PyCharm](#running-in-pycharm)
- [File Descriptions](#file-descriptions)

## Project Overview
This project loads employee data from a CSV file into a pandas DataFrame, performs data cleaning, calculates some statistical values, and writes the processed data to a new CSV file. The key tasks include:

- Removing any duplicate rows.
- Removing decimal places from the "Age" column.
- Converting salaries from USD to EGP using the current exchange rate.
- Calculating and displaying:
  - Average age of employees.
  - Median salary.
  - The ratio of male to female employees.
- Writing the calculated data into a new CSV file.


## Technologies Used
- **Python 3.x**
- **pandas**: For data manipulation and analysis.
- **CSV module**: For handling CSV file operations.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Install the required dependencies:
    ```bash
    pip install pandas
    ```

## Running in PyCharm
To run the project in PyCharm, follow these steps:

1. Open PyCharm and clone the repository or open the project folder:
    - Go to **File > Open...** and select the project directory.

2. Install required dependencies using the terminal inside PyCharm or by going to:
    - **File > Settings > Project: <project-name> > Python Interpreter** and installing pandas if not already installed.

3. Place your `Employees.csv` file inside the project directory.

4. Set up the Python script as the main script:
    - Right-click `employee_data_processing.py` in the Project pane and select **Run 'employee_data_processing'**.

5. Check the **Run** pane for the output statistics and verify that `EmployeesAfterUpdate.csv` is created.

## File Descriptions
- **Employees.csv**: The input CSV file containing raw employee data.
- **employee_data_processing.py**: The main Python script that processes the employee data and performs the required tasks.
- **EmployeesAfterUpdate.csv**: The output CSV file generated after data cleaning and processing.
