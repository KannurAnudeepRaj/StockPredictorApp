# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Load your stock price data (replace 'your_data.csv' with your dataset)
data = pd.read_csv('your_data.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)

# Train-test split
train_size = int(len(data) * 0.8)
train, test = data.iloc[:train_size], data.iloc[train_size:]

# Prophet model initialization and fitting
model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
model.fit(train)

# Create a dataframe with future dates for forecasting
future = model.make_future_dataframe(periods=len(test), freq='D')

# Forecasting
forecast = model.predict(future)

# Evaluate the model
predictions = forecast['yhat'][train_size:]
mse = mean_squared_error(test['y'], predictions)
rmse = np.sqrt(mse)
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rmse}')

# Visualize the results
fig, ax = plt.subplots(figsize=(10, 6))
model.plot(forecast, ax=ax, xlabel='Date', ylabel='Stock Price', plot_cap=True)
ax.scatter(test['ds'], test['y'], label='Test', color='blue', s=10)
ax.plot(test['ds'], predictions, label='Predictions', color='red')
ax.legend()
plt.show()
