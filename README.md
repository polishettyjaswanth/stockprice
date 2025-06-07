# Stock Price Prediction Using Machine Learning

## Overview
This project is a web-based stock price prediction tool that uses machine learning models to forecast stock performance. It consists of a Flask-based backend and an interactive frontend for user-friendly predictions.

## Features
- Web-based UI for stock prediction
- Data fetching from Yahoo Finance
- Implementation of machine learning models:
  - Simple Moving Average (SMA)-based strategy
  - Linear Regression
  - Decision Trees
  - Random Forest
  - LSTM (Long Short-Term Memory)
- Model evaluation using key metrics
- Investment growth projection

## Tech Stack
- **Backend:** Flask, Python, yfinance, pandas, scikit-learn, TensorFlow/Keras
- **Frontend:** HTML, CSS, JavaScript (Vanilla JS), FontAwesome

## Installation
To set up the project, follow these steps:
```bash
git clone https://github.com/Upender11/stock-prediction.git
cd stock-prediction
pip install -r requirements.txt
```

## Running the Application
1. **Start the Flask Server:**
```bash
python app.py
```
2. **Access the Web App:** Open `http://127.0.0.1:5000/` in a browser.

## Dataset
The dataset consists of historical stock prices retrieved from Yahoo Finance using the `yfinance` library. Stocks can be manually selected from the UI.

## Usage
1. Select a stock from the list.
2. Choose a start and end date for analysis.
3. Enter an investment amount.
4. Click the "Predict Stocks" button to view the projected returns.

## Results
- The strategy-based model evaluates whether buying or holding stock is beneficial based on moving averages.
- Final projected value of the investment is displayed along with error handling for invalid inputs.

## Future Improvements
- Implement deep learning models like Transformers
- Integrate real-time stock price updates
- Include sentiment analysis from news sources

## License
This project is licensed under the MIT License.

