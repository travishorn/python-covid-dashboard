from datetime import datetime, timedelta
from flask import Flask, render_template, request
from data_fetcher import fetch_data
from data_preprocessor import preprocess_data
from chart_generator import generate_chart

# Create the Flask application
app = Flask(__name__)

# Create an empty list to scope the data
df_covid = {}

# Define a route and a view function
@app.route('/')
def hello():
    # Generate a list of unique locations
    locations = df_covid['location'].unique().tolist()

    # Get the selected location from the URL search parameter
    selected_location = request.args.get('location')

    # If there is no location in the URL, use the first location in the DataFrame
    if not selected_location:
        selected_location = df_covid['location'].iloc[0]

    # Get the selected "from" date from the URL search parameter
    from_date = request.args.get('from')

    # If there is no "from" date in the URL, use 1 year ago
    if not from_date:
        from_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

    # Get the selected "to" date from the URL search parameter
    to_date = request.args.get('to')

    # If there is no "to" date in the URL, use today
    if not to_date:
        to_date = (datetime.now()).strftime('%Y-%m-%d')

    # Convert 'from_date' and 'to_date' to datetime objects
    from_date_datetime = datetime.strptime(from_date, '%Y-%m-%d')
    to_date_datetime = datetime.strptime(to_date, '%Y-%m-%d')

    # Get the selected metric from the URL search parameter
    metric = request.args.get('metric')

    # If there is no metric in the URL, use 'new cases'
    if not metric:
        metric = 'new_cases'

    # Filter the DataFrame so that only items with the correct location and dates are included
    filtered_covid_data = df_covid.loc[(df_covid['location'] == selected_location) & (df_covid['date'] >= from_date_datetime) & (df_covid['date'] <= to_date_datetime)]

    # Generate the bar chart
    generate_chart(filtered_covid_data, metric)

    # Render a template with the COVID data
    return render_template('dashboard.html', locations=locations, selected_location=selected_location, from_date=from_date, to_date=to_date, selected_metric=metric)

# Run the application if this script is executed directly
if __name__ == '__main__':
    # Fetch the COVID data
    covid_data = fetch_data()

    # Preprocess the data and load into a DataFrame
    df_covid = preprocess_data(covid_data)

    # Run the Flask app
    app.run()
