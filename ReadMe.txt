# Credit Card Monthly Transaction Predictor

**Built by:** Soumik Das (BT24CSE019) | VNIT Nagpur

## The Goal
The primary aim of this project is to answer a specific financial question: *Can we accurately predict the overall volume of credit card transactions in India for a specific future month?* Instead of looking at individual user purchases, this project takes a macro approach. By analyzing historical spending data, it attempts to capture the momentum, seasonal spikes, and overall trends in how people spend their money over time.

## How it was built (The Pipeline)

This project follows a complete end-to-end machine learning workflow, moving from raw data to a trained forecasting model.

**1. Finding the Data**
The project is built on a dataset sourced from Kaggle containing over 26,000 individual credit card transactions. It includes details like the city of the transaction, the card type (Gold, Platinum), the expense category (Bills, Food), and the exact dates and amounts.

**2. Cleaning the Mess**
Real-world data is rarely ready for machine learning. The first step was getting the data into shape:
* **Dates:** Converted string dates into native Pandas datetime objects.
* **Corrupted values:** Used error coercion to safely handle any weird characters in the amount column without crashing the script.
* **Trimming:** Dropped redundant system indexes to save memory and cleaned up string artifacts (like stripping ", India" from the city names).

**3. Exploratory Data Analysis (EDA)**
Before training a model, I needed to see what the data actually looked like. Plotting the transaction amounts over time revealed extreme volatility—spending doesn't follow a straight line. There are massive, predictable spikes during specific months (likely driven by festival seasons like Diwali), which completely changes how the model needs to be built.

**4. Feature Engineering**
Because my goal was to predict *monthly totals* rather than *individual swipes*, I had to transform the dataset. I extracted the exact month and year from the timestamps and grouped the thousands of individual rows into aggregate monthly totals. This created the core time-series timeline.

**5. Splitting the Data**
In standard machine learning, you usually shuffle your data randomly before splitting it into training and testing sets. Because this is a time-series problem, doing that would "leak" future data into the past. Instead, I split the data strictly chronologically—training the model on the older months so it could attempt to predict the newer, unseen months.

**6. Model Selection & Training**
Initially, I explored baseline models like Linear Regression. However, a straight line cannot capture the jagged, seasonal peaks of human spending. The project pivoted toward time-series forecasting strategies (or more complex tree-based ensembles) to better map the historical momentum to future targets. 

**7. Evaluation & Tuning**
To see if the model was actually working, I evaluated its predictions against the test data using Mean Absolute Error (MAE) and Mean Absolute Percentage Error (MAPE). This tells me exactly how far off my predictions are in actual currency, allowing me to iterate and tune the model's parameters to handle the seasonal spikes better.

---

## Tech Stack
* **Language:** Python 3.12
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib
* **Machine Learning:** Scikit-Learn
* **Environment:** Built and tested on Linux (using a `.venv` virtual environment)

## Running the Project Locally

If you want to run this code on your own machine:

1. Clone this repository:
   `git clone https://github.com/das-soumik-20/Credit-card-monthly-transaction-predictor.git`
2. Navigate into the folder and activate your virtual environment (recommended).
3. Install the required libraries:
   `pip install pandas numpy matplotlib scikit-learn`
4. Run the main execution script:
   `python main.py`
