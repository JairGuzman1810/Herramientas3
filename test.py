import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(r"C:\Users\fca\Downloads\Herramientas3_2023_banco.csv")


# Select the columns you're interested in
columns_of_jobs = ['job'], 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome'

# Get unique values for the selected columns and store them in a new DataFrame
job = pd.DataFrame(df['job'].drop_duplicates())
marital = pd.DataFrame(df['marital'].drop_duplicates())
education = pd.DataFrame(df['education'].drop_duplicates())
housing = pd.DataFrame(df['housing'].drop_duplicates())
loan = pd.DataFrame(df['loan'].drop_duplicates())
contact = pd.DataFrame(df['contact'].drop_duplicates())
month = pd.DataFrame(df['month'].drop_duplicates())
day_of_week = pd.DataFrame(df['day_of_week'].drop_duplicates())
listPaises = df["job"].unique().tolist()


# Print the resulting DataFrame
print(listPaises)
