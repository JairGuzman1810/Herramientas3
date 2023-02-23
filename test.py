import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(r"C:\Users\fca\Downloads\Herramientas3_2023_banco.csv")


# Select the columns you're interested in
columns_of_interest = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome']

# Get unique values for the selected columns and store them in a new DataFrame
unique_data = pd.DataFrame(df[columns_of_interest].drop_duplicates())

# Print the resulting DataFrame
print(unique_data)
