import statsmodels.api as sm



# Split the data into training and testing sets
train_data = df['Ridership'].iloc[:-12]
test_data = df['Ridership'].iloc[-12:]

# Fit the ARIMA model
model = sm.tsa.ARIMA(train_data, order=(1,1,1))
model_fit = model.fit()

# Evaluate the model
predictions = model_fit.forecast(steps=12)
mae = abs(predictions - test_data).mean()

# Make predictions
future_predictions = model_fit.forecast(steps=24)

# Print the results
print(f"MAE: {mae}")
print(f"Future predictions:\n{future_predictions}")






train_size = 0.8  # proportion of data used for training
n_train = int(len(df) * train_size)
train_data = df['Ridership'].iloc[:n_train]
test_data = df['Ridership'].iloc[n_train:]

# Fit the ARIMA model
model = sm.tsa.ARIMA(train_data, order=(1,1,1))
model_fit = model.fit()

# Evaluate the model
predictions = model_fit.forecast(steps=len(test_data))
mae = abs(predictions - test_data).mean()

# Make predictions
future_predictions = model_fit.forecast(steps=24)

# Generate date range for the future predictions
last_date = df['Date'].iloc[-1]
date_range = pd.date_range(start=last_date, periods=24, freq='M')

# Combine the date range and future predictions into a DataFrame
future_df = pd.DataFrame({'Date': date_range, 'Predicted Ridership': future_predictions})

# Print the results
print(f"MAE: {mae}")
print(f"Future predictions:\n{future_df}")






# Prepare the data (e.g. remove trend/seasonality)

# Split the data into training and testing sets
train_data = df['Ridership'].iloc[:-12]
test_data = df['Ridership'].iloc[-12:]

# Fit the ARIMA model
model = sm.tsa.ARIMA(train_data, order=(1,1,1))
model_fit = model.fit()

# Evaluate the model
predictions = model_fit.forecast(steps=12)
mae = abs(predictions - test_data).mean()

# Make predictions
future_predictions = model_fit.forecast(steps=24)

# Generate date range for the future predictions
last_date = df['Date'].iloc[-1]
date_range = pd.date_range(start=last_date, periods=24, freq='M')

# Combine the date range and future predictions into a DataFrame
future_df = pd.DataFrame({'Date': date_range, 'Predicted Ridership': future_predictions})

# Print the results
print(f"MAE: {mae}")
print(f"Future predictions:\n{future_df}")


import matplotlib.pyplot as plt

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the actual values
ax.plot(df['Date'], df['Ridership'], label='Actual', color='blue')

# Plot the predicted values
ax.plot(future_df['Date'], future_df['Predicted Ridership'], label='Predicted', color='red')

# Set axis labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Ridership')
ax.set_title('Actual vs. Predicted Ridership')

# Add legend to the plot
ax.legend()

# Show the plot
plt.show()

fig, ax = plt.subplots(1,1, figsize=(12,4))
ax.plot(future_df['Date'], future_df['Predicted Ridership'], color='blue', alpha=1, label='Actual')
ax.legend(loc='best')
plt.show()