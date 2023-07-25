import matplotlib.pyplot as plt
def generate_chart(data, metric):
    # Group data by location and sum new cases for each
    grouped_data = data.groupby('date')[metric].sum()

    # Convert metric from snake_case to Title Case
    pretty_metric = ' '.join(word.capitalize() for word in metric.split('_'))

    # Create a bar chart
    plt.bar(grouped_data.index, grouped_data.values)
    plt.xlabel('Date')
    plt.ylabel(pretty_metric)
    plt.title(f'COVID-19: {pretty_metric} in {data["location"].iloc[0]}')
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Save the generated chart to a file so the template can render it
    plt.savefig('static/chart.png')
    plt.close()