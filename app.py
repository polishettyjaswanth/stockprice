from flask import Flask, request, jsonify, render_template
import yfinance as yf
import pandas as pd

app = Flask(__name__)

# Function to calculate projected returns based on simple moving averages
def predict_stock_performance(stock_symbol, start_date, end_date, investment):
    try:
        # Fetch stock data
        data = yf.download(stock_symbol, start=start_date, end=end_date)
        if data.empty:
            return f"No data available for {stock_symbol} in the given date range."

        # Calculate moving averages
        data['SMA_20'] = data['Close'].rolling(window=20).mean()
        data['SMA_50'] = data['Close'].rolling(window=50).mean()

        # Strategy: If 20-day SMA > 50-day SMA, consider it a buy signal
        data['Signal'] = (data['SMA_20'] > data['SMA_50']).astype(int)

        # Calculate returns
        data['Daily_Return'] = data['Close'].pct_change()
        data['Strategy_Return'] = data['Signal'].shift(1) * data['Daily_Return']
        total_return = (1 + data['Strategy_Return']).prod() - 1

        # Project investment growth
        projected_value = investment * (1 + total_return)

        return {"stock": stock_symbol, "projected_value": round(projected_value, 2)}
    except Exception as e:
        return {"stock": stock_symbol, "error": str(e)}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    investment_amount = float(data.get('investment_amount'))
    stocks = data.get('stocks')

    results = []
    for stock in stocks:
        result = predict_stock_performance(stock, start_date, end_date, investment_amount)
        results.append(result)

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
