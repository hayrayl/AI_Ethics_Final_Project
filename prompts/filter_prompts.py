import pandas as pd

# The raw URL of the CSV file on GitHub
url = 'https://raw.githubusercontent.com/ninodimontalcino/moralchoice/master/data/scenarios/moralchoice_high_ambiguity.csv'

# --- Configuration ---
filter_column = 'generation_rule'
filter_value = "Do not break the law"

# The 3 columns you want to keep, as you specified
columns_to_keep = ['context', 'action1', 'action2']

# A good, descriptive name for your new file
new_filename = 'moralchoice_law_prompts.csv'

try:
    # Read the entire CSV file from the URL into a DataFrame
    df = pd.read_csv(url)
    print(f"Successfully loaded {len(df)} total items from the original file.")

    # 1. Filter the DataFrame based on the 'generation_rule' column
    filtered_df = df[df[filter_column] == filter_value]
    
    # 2. Select only the columns you want to keep
    final_df = filtered_df[columns_to_keep]
    
    # Check if any data was found
    if not final_df.empty:
        # Save the final, filtered data to a new CSV file
        final_df.to_csv(new_filename, index=False)
        print(f"Successfully filtered, selected {len(final_df)} prompts, and saved to '{new_filename}'.")
    else:
        print(f"No prompts were found with the generation_rule '{filter_value}'. No file was saved.")

except KeyError as e:
    print(f"Error: A column name was not found: {e}")
    print(f"Please double-check that 'context', 'action1', and 'action2' exist in the CSV.")
except Exception as e:
    print(f"An error occurred: {e}")