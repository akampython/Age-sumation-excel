import pandas as pd

try:
    # Load the Excel file
    input_file = 'data/input.xlsx'
    output_file = 'data/summed_ages.xlsx'

    # Read the Excel file
    df = pd.read_excel(input_file)

    # Check if 'Age' column exists
    if 'Age' not in df.columns:
        raise ValueError("The 'Age' column is missing from the input file.")

    # Sum the "Age" column
    total_age = df['Age'].sum()

    # Create a DataFrame to store the result
    result_df = pd.DataFrame({'Total Age': [total_age]})

    # Save the result to a new Excel file
    result_df.to_excel(output_file, index=False)
    
    print("Total Age:", total_age)
except Exception as e:
    print("Error:", e)
