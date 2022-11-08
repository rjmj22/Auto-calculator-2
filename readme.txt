This project will take input from a user, which is a trade in value if applicable, a down payment from the user if applicable, if the vehicle is new or used and the total amount of the vehicle cost, and give the monthly payment and total interest paid over the loan term.

Got the rates by credit score from:
https://www.nerdwallet.com/article/loans/auto-loans/average-car-loan-interest-rates-by-credit-score

*rates accurate as of 9/25/22

This is the information I used to setup a virtual environment:
https://code.visualstudio.com/docs/python/environments
To create a virtual environment, use the following command, where ".venv" is the name of the environment folder:
# macOS/Linux
# You may need to run sudo apt-get install python3-venv first
python3 -m venv .venv

# Windows
# You can also use py -3 -m venv .venv
python -m venv .venv

The install requirements are in the requirements.txt
Need to also download data_new.sqlite3 & data_used.sqlite3

Will need to change: line 8 "df_new = pd.read_sql_table(''sqlite:///D:\\coding\\project 2\\data_new.sqlite3'') 
And line 9 "df_used = pd.read_sql_table(''sqlite:///D:\\coding\\project 2\\data_used.sqlite3'') to the directory that data.sqlite3 is put into

The selections from the list are:

1st: Read in data from two databases. 
2nd: Use pandas to merge and clean data
3rd: Bar charts with Bokeh
4th: Virtual environment 
5th: Annontate with comments

run file: "car_finance_calculator.py"