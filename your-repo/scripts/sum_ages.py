import pandas as pd

# Load the Excel file
input_file = 'data/input.xlsx'
output_file = 'data/summed_ages.xlsx'

# Read the Excel file
df = pd.read_excel(input_file)

# Sum the "Age" column
total_age = df['Age'].sum()

# Create a DataFrame to store the result
result_df = pd.DataFrame({'Total Age': [total_age]})

# Save the result to a new Excel file
result_df.to_excel(output_file, index=False)
