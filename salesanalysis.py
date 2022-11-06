# Required imports

import pandas as pd
import plotly.express as px


# Reduce amount which has to be typed in subsequent functions

def read_data():
    df = pd.read_csv('sales.csv')

    return df

# Basic stat info


def sales_info():
    df = read_data()

    total_sales = df['sales'].sum()
    highest_sales = df['sales'].max()
    lowest_sales = df['sales'].min()
    average = round(df['sales'].mean(), 2)

    total_costs = df['expenditure'].sum()
    total_profit = total_sales - total_costs

    print('Total sales: £{}, Average sales: £{}, Highest sales: £{}, Lowest sales: £{}'
          .format(total_sales, average, highest_sales, lowest_sales))
    print('Total profit: £{}'.format(total_profit))


# Graph for sales vs month

def sales_month():
    df = read_data()

    fig = px.line(df, x='month', y='sales', title='Sales vs Month')
    fig.show()


# adding percentage change to csv and creating graph for % change vs Jan

def p_change():
    df = read_data()

    df['Percentage Change'] = (1 - df.iloc[0].sales / df.sales) * 100
    df.to_csv('sales.csv', index=False)
    print(df['Percentage Change'])

    fig = px.line(df, x='month', y='Percentage Change', title='Percentage Change Compared to Jan')
    fig.show()


sales_info()
sales_month()
p_change()
