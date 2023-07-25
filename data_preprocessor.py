import pandas as pd

def preprocess_data(data):
    print("Preprocessing data.")
    
    # Extract data for specific metrics, e.g., 'total_cases', 'total_deaths', 'new_cases', 'new_deaths'
    selected_metrics = ['location', 'date', 'new_cases', 'new_deaths']
    
    # Create an empty list to store the preprocessed data
    preprocessed_data = []

    # Loop through all countries
    for country_code, country_data in data.items():
      # Extract the location
      location = country_data["location"]

      # Loop through each data entry (roughly daily)
      for entry in country_data["data"]:
        # Extract the selected metrics for each entry and create a new dictionary
        preprocessed_entry = {
            'location': location,
            **{metric: entry[metric] for metric in selected_metrics if metric in entry}
        }

        # Append the preprocessed entry to the list
        preprocessed_data.append(preprocessed_entry)

      # Convert the list of dictionaries to a Pandas DataFrame
      df = pd.DataFrame(preprocessed_data)

      # Convert the 'date' column from string to datetime
      df['date'] = pd.to_datetime(df['date'])

    return df
