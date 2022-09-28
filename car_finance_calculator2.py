from turtle import fillcolor
import pandas as pd
from sqlalchemy import create_engine
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.io import show
# Make sure to update the path below as needed
engine_new = create_engine('sqlite:///D:\\coding\\project 2\\data_new.sqlite3')
engine_used = create_engine('sqlite:///D:\\coding\\project 2\\data_used.sqlite3')
# Make sure to update the path above as needed
df_new = pd.read_sql_table('credit', engine_new)
df_used = pd.read_sql_table('credit', engine_used)
# merging DF
new_df = df_new.merge(df_used, how='right')
# getting rid of "NaN"
new_df = new_df.dropna()
# Getting database to lists

superprime = new_df.loc[1, :].values.tolist()

prime = new_df.loc[3, :].values.tolist()

nonprime = new_df.loc[5, :].values.tolist()

subprime = new_df.loc[7, :].values.tolist()

deep_subprime = new_df.loc[9, :].values.tolist()

# function to get rates from credit score and condition

def get_rate(credit_score, condition):
    if condition == 1:
        if credit_score >= 781:
            rate = superprime[2]
        elif credit_score >= 661:
            rate = prime[2]
        elif credit_score >= 601:
            rate = nonprime[2]
        elif credit_score >= 501:
            rate = subprime[2]
        elif credit_score <= 500:
            rate = deep_subprime[2]
    if condition == 2:
        if credit_score >= 781:
            rate = superprime[3]
        elif credit_score >= 661:
            rate = prime[3]
        elif credit_score >= 601:
            rate = nonprime[3]
        elif credit_score >= 501:
            rate = subprime[3]
        elif credit_score <= 500:
            rate = deep_subprime[3]
    return rate

def get_int(principal, rate):
    int3 = int(principal * rate * 3)
    int4 = int(principal * rate * 4)
    int5 = int(principal * rate * 5)
    int6 = int(principal * rate * 6)
    int7 = int(principal * rate * 7)
    int_rates = (int3, int4, int5, int6, int7)
    return int_rates

def get_years(principal, int_rates):
    three_year = int((principal + int_rates[0]) / 36)
    four_year = int((principal + int_rates[1]) / 48)
    five_year = int((principal + int_rates[2]) / 60)
    six_year = int((principal + int_rates[3]) / 72)
    seven_year = int((principal + int_rates[4]) / 84)
    loan_years = (three_year, four_year, five_year, six_year, seven_year)
    return loan_years

def main():
    print("This is a Auto loan finance calculator. Please enter whole numbers only, no commas needed!")
    # new or used, trade in, down payment, credit score and overall car values:
    while True:
        try:
            condition = float(input("If vehicle is New, enter 1. If used enter 2: "))
            if (condition < 1) or (condition > 2):
                print("Invalid number: try again")
                continue
        except ValueError:
            print('1 or 2 only:')
            continue
        else:
            break
    while True:
        try:
            trade_in = float(input("If you have a trade in enter value, if not put 0: "))
        except ValueError:
            print('Numerics only')
            continue
        else:
            break
    while True:
        try:
            down_payment = float(input("If you have a down payment enter value, if not put 0: "))
        except ValueError:
            print('Numerics only')
            continue
        else:
            break
    while True:
        try:
            credit_score = float(input("Enter credit score number between 300-850: "))
            if (credit_score < 300) or (credit_score > 850):
                print("Invalid number: try again")
                continue
        except ValueError:
            print('Numerics only')
            continue
        else:
            break
    while True:
        try:
            auto_price = float(input("Enter the total price of the vehicle: "))
        except ValueError:
            print('Numerics only')
            continue
        else:
            break

# matching credit score to rate
    get_rate(credit_score, condition)
    rate = get_rate(credit_score, condition)

# figuring our principal and interest rate by year
    principal = (auto_price - (down_payment + trade_in))
    get_int(principal, rate)
    int_rates = get_int(principal, rate)

# getting monthly payments calculations
    get_years(principal, int_rates)
    loan_years = get_years(principal, int_rates)

# converting int_rates to string for annotation   
    rates_string = [str(x) for x in int_rates]

# using bokeh for visualizations
# graph for interest paid
    source1 = ColumnDataSource(data=dict(
        rates=[int_rates[0], int_rates[1], int_rates[2], int_rates[3], int_rates[4]],
        months=[36, 48, 60, 72, 84],
        amounts=[rates_string[0], rates_string[1], rates_string[2], rates_string[3], rates_string[4]],
        colors = ["blue", "green", "yellow", "orange", "red"]))
    graph1 = figure()
    graph1.vbar(x='months', top='rates', width=8, color='colors', source=source1)
    graph1.xaxis.axis_label = 'Total months'
    graph1.yaxis.axis_label = 'Total interest paid'
    labels1 = LabelSet(x='months', y='rates', text='amounts', source=source1)
    graph1.add_layout(labels1)
    show(graph1)
# bokeh graph for monthly payment
    source2 = ColumnDataSource(data=dict(
        rates=[int_rates[0], int_rates[1], int_rates[2], int_rates[3], int_rates[4]],
        months=[36, 48, 60, 72, 84],
        amounts=[rates_string[0], rates_string[1], rates_string[2], rates_string[3], rates_string[4]],
        colors = ["blue", "green", "yellow", "orange", "red"]))
    graph2 = figure()
    graph2.vbar(x='months', top='rates', width=8, color='colors', source=source2)
    graph2.xaxis.axis_label = 'Total months'
    graph2.yaxis.axis_label = 'Monthly payment'
    labels2 = LabelSet(x='months', y='rates', text='amounts', source=source2)
    graph2.add_layout(labels2)
    show(graph2)
    
main()