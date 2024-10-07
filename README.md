# Twitter-Geo-Analysis-with-Python-and-SQL
This project analyzes a dataset of tweets by calculating the average longitude and latitude for each user. It involves querying a SQLite database, processing data from JSON files, and comparing different methods of execution (SQL and Python with regex). Additionally, runtime performances of various execution approaches are compared and visualized.

## Features
- Query execution using SQLite
- JSON data parsing in Python
- Regular expression-based data extraction
- Runtime comparisons for 5 and 20 executions
- Visualization of runtime distributions using Matplotlib

## Technologies
- **Python**: Used for data processing, JSON handling, and visualization.
- **SQLite**: Utilized for executing SQL queries on tweet data.
- **Matplotlib**: For visualizing runtime distributions.
- **Regex**: Applied for extracting specific data points from tweets without using JSON.

## Files in the Repository
1. `main.py`: The main Python script containing the entire workflow, including SQL execution, data processing, and runtime analysis.
2. `final_tweets.db`: The SQLite database storing tweet and geo data.
3. `README.md`: Project description and instructions.

## How to Run
1. Clone the repository.
2. Ensure Python and SQLite are installed.
3. Execute the `main.py` script to process tweets and generate visualizations.

## Visualizations
This project includes a visualization of runtimes for 5 and 20 executions of different methods:
- JSON parsing
- Regex-based data extraction

The visualization demonstrates how runtime scales with the number of executions.
