# StockPredictorApp - Advanced Stock Predictor with Prophet

## Overview

This repository contains a Python script named `AdvancedStockPredictor.py` that leverages the `Prophet` library from Facebook for advanced stock price forecasting. This tool is designed to predict future stock prices based on historical data, using time-series forecasting techniques.

## Changes Made in This Version

In this version, several improvements have been made to enhance the functionality and readability of the code:

1. **Indexing in Train-Test Split:**
   - Utilized the `iloc` method for indexing in the train-test split to ensure correct integer-location-based indexing.

2. **Visualization Adjustments:**
   - Adjusted the `xlabel` and `ylabel` parameters in the `plot` method to improve the visualization of the results.

3. **Enhanced Visualization:**
   - Added a scatter plot for the test data points to provide a visual representation of the actual stock prices in the visualization.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/KannurAnudeepRaj/AdvancedStockPredictor.git
   cd AdvancedStockPredictorProphet
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Replace Dataset:**
   - Replace `'your_data.csv'` with the actual filename of your stock price dataset in the script.

4. **Run the Script:**
   ```bash
   python AdvancedStockPredictor.py
   ```

5. **Adapt and Modify:**
   - Feel free to adapt and further modify the code based on your specific requirements. Explore different hyperparameters, feature engineering, or additional visualizations to improve the model's performance.

## Author

- Kannur Anudeep Raj ([GitHub](https://github.com/KannurAnudeepRaj))

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the [Prophet](https://facebook.github.io/prophet/) development team for providing a powerful tool for time-series forecasting.
