# Air_Quality_Mining

In addressing the air quality challenge, the proposed solution incorporates several key techniques:
- ### BigQuery and Pandas Integration: 
  Utilizing Google's cloud-based data warehouse, BigQuery, along with the Pandas library in Python, the BigQueryHelper class from the PyBQ library facilitated interaction with the EPA air quality data stored in a Google Cloud project. This data was seamlessly loaded into a Pandas DataFrame for subsequent processing and analysis.
- ### SQL Queries for Data Extraction:
  Employing SQL queries, we selectively retrieved pertinent information from the EPA air quality dataset. Specifically, these queries focused on obtaining average Air Quality Index (AQI) values for a given pollutant and year within each county. Python functions were employed to generate these queries, executed through the BigQueryHelper class.
- ### Data Cleaning and Preprocessing:
  Prior to analysis, thorough data preprocessing and cleaning were imperative. This involved actions such as merging columns, discarding unnecessary ones, converting categorical columns to numerical format using one-hot encoding, and transforming object data types to float data types. The year column was designated as the DataFrame index and converted to a DatetimeIndex. Imputation of missing values was carried out using the mean of the respective columns.
- ### Time Series Analysis:
  Employing time series analysis, a statistical technique for studying and predicting time-dependent data, we modeled air quality data over time and made forecasts for future AQI values. The dataset was partitioned into training and testing sets, with predictions generated using an Autoregressive Integrated Moving Average (ARIMA) model.
- ### Performance Evaluation Metrics:
  The performance of our time series model was assessed using metrics such as mean absolute error (MAE) and root mean squared error (RMSE), offering quantitative insights into the disparities between actual and predicted values.
- ### Visualization Using Plotly:
  For effective communication of air quality data and analysis outcomes, we leveraged Plotly, a Python graphing library known for interactive and dynamic visualizations. Choropleth maps depicting AQI values for each pollutant and year at the county level in the USA were created. Additionally, time series data, as well as actual and predicted AQI values, were visualized.
