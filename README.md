# Interactive Data Dashboard for COVID-19 Statistics

A web-based data dashboard that presents and visualizes COVID-19 statistics from
a publicly available data source. Allows users to interact with the data,
selecting from different countries, date ranges, and metrics for visualization.

Data is retrieved from the public API provided by [Our World in
Data](https://ourworldindata.org/).

![A screen recording showing the web app generating bar charts in response to
changes in the form controls for location, date, and metric](demo.gif)

## Features

1. Uses **Python** to **fetch data from the API** and **preprocess** it (JSON
data to Pandas DataFrame).
2. Uses the Python web framework **Flask** to serve a simple web application.
3. Has a dashboard designed with **Bootstrap**.
4. Implements **interactive** elements like dropdown menus, date selectors, and
radio buttons for users to choose the country, date range, and metrics they want
to see.
5. Uses the Python **data visualization** framework **Matplotlib** to create bar
charts
6. Is **responsive** and works well on different devices: desktops, tables, and
mobile.

## Methods Applied

1. **Data acquisition**: fetch and handle data from an external API.
2. **Data processing**: preprocess and clean the data for visualization.
3. **Data visualization**: present data in a visually appealing and interactive
way (crucial for **data-driven decision making**).
4. **Web development**: build web applications with the **Python** framework
**Flask**
5. **Problem-solving**: tackle challenges with **data manipulation**,
visualization, and user **interaction**.

## Prerequisites

You must have Python installed.

Make sure you have the following dependencies installed via `pip`:

- flask
- matplotlib
- requests
- pandas

## Installation

Clone this repository:

```sh
git clone https://github.com/travishorn/python-covid-dashboard
```

Change into the directory:

```sh
cd python-covid-dashboard
```

Run the application:

```sh
python app.py
```

Wait for the data to be downloaded and processed. Once the web app is ready, go
to http://127.0.0.1:5000

## License

Copyright 2023 Travis Horn

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
