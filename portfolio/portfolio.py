import pandas as pd
import yfinance as yf
import numpy as np
import statsmodels.api as sm
from statsmodels import regression
from MCForecastTools import MCSimulation
from report.report import prepare_portfolio_report

# Function to perform portfolio analysis (historical, present plus future analysis)
# Portfolio_df contains:stock names, outstanding holding of each stock (e.g. 10 stocks of GOOG, 13 stocks of FB etc)
# User_df contains : user name, user password, available fund to trade
def perform_portfolio_analysis(user_df, portfolio_df):
    
    # Get the list of all tickers in user portfolio and add SPY
    tickers = portfolio_df['ticker'].tolist()
    # add S&P 500 ticker to the list for analysis purpose
    tickers.append('SPY')

    # call perform analysis function that provides all the results in a dictionary
    results_dict = perform_analysis('', 0, tickers, user_df, portfolio_df, 'portfolio')
    
    # Prepare the portfolio analysis report
    prepare_portfolio_report(results_dict)
    
    return True


# key function that performs all the risk/ratio metrics calculations and also performs the monte carlo simulation
def perform_analysis(user_stock, user_stock_weight, tickers, user_df, portfolio_df, indicator):
    
    portfolio_dic = dict()
    for ticker in portfolio_df['ticker'].tolist():
        portfolio_dic[ticker.upper()] = portfolio_df[portfolio_df['ticker']==ticker]['number_of_shares'].iloc[0]

    ## Use Yahoo finance to retrieve 5 yrs of price data
    portfolio = yf.Tickers(tickers)
    portfolio_history_df = portfolio.history(period = "5y")
    prices_df = portfolio_history_df["Close"]
    
    # calculate portfolio NAV
    portfolio_prices_df = prices_df[portfolio_df['ticker'].tolist()].mul(portfolio_dic)
    prices_df['PORTFOLIO'] = portfolio_prices_df.sum(axis=1)
    
    # Use pct_change to convert into returns
    returns_df = prices_df.pct_change().dropna()

    # Standard devs and annualized STDev
    std_devs = returns_df.std()
    number_of_trading_days = 252
    annualized_std_devs = std_devs*np.sqrt(number_of_trading_days)
    ## Rolling_std_60d = returns_df.rolling(window=60).std().dropna()

    ## Stock Covariance Calculation into a df
    covariance_df = returns_df.cov()
    covariance_df = covariance_df[["SPY"]]
    covariance_df.columns = ["Covariance"]

    ## Variance calculation
    spy_variance = returns_df['SPY'].var()

    ## Beta calculation into a df
    beta_df = returns_df.cov()/spy_variance
    beta_df = beta_df[["SPY"]]
    beta_df.columns = ["Beta"]
    
    ## Calculate the annual average return data for the for the portfolio and the S&P 500
    annualized_average_returns = returns_df.mean()*number_of_trading_days
    
    ## Calculate the annualized Sharpe Ratios for the portfolio and the S&P 500.
    sharpe_ratios = annualized_average_returns/annualized_std_devs

    ## Create df starting by correlation
    ratios_df = returns_df.corr()
    
    ## Drop columns for correlation against each other, leave only correlation against SPY i.e. S&P 500
    ratios_df = ratios_df[['SPY']]
    
    ## Rename column from SPY to Correlation
    ratios_df.rename(columns = {"SPY":"Correlation"},inplace = True) 

    ## Calculate additional ratios 
    ratios_df["Volatility"] = returns_df.std() * np.sqrt(252)
    ratios_df["Sharpe"] =  (returns_df.mean() * 252) / (returns_df.std() * np.sqrt(252))
    ratios_df["Sortino"] = (returns_df.mean() * 252) / (returns_df[returns_df<0].std() * np.sqrt(252))

    ## Add covariance and beta from calculation in cell above
    ratios_df["Covariance"] = covariance_df["Covariance"]
    ratios_df["Beta"] = beta_df["Beta"]

    ## Prepare for monte carlo simulation
    if indicator == 'portfolio':
        sim_input_prices_df = prices_df[portfolio_df['ticker'].tolist()]
        column_names = [(x,"close") for x in portfolio_df['ticker'].tolist()]
        ## Print(column_names)
        sim_input_prices_df.columns = pd.MultiIndex.from_tuples(column_names)

        ## Calculate portfolio weights
        weights = ((portfolio_prices_df.iloc[-1]) / (prices_df['PORTFOLIO'].iloc[-1])).values
    else:
        ## Print('user stock is -->', user_stock)
        sim_input_prices_df = prices_df[[user_stock, 'PORTFOLIO']]
        column_names = [(user_stock,'close'), ('PORTFOLIO','close')]
        sim_input_prices_df.columns = pd.MultiIndex.from_tuples(column_names)

        ## Calculate portfolio weights
        weights = [user_stock_weight,1-user_stock_weight]

    ## Configure the Monte Carlo simulation to forecast 2 years cumulative returns
    portfolio_2y_sim = MCSimulation(
        sim_input_prices_df,
        weights,
        num_simulation=100,
        num_trading_days=252*2
    )

    ## Run simulation
    portfolio_2y_sim.calc_cumulative_return()
    
    ## Calculate alphas
    for ticker in returns_df.columns:
        if ticker == 'SPY':
            ratios_df.at[ticker, 'alpha'] = 0
        else:
            input_returns_df = returns_df[[ticker, 'SPY']].dropna()
            alpha = linear_regression(input_returns_df['SPY'],input_returns_df[ticker])
            ratios_df.at[ticker, 'alpha'] = alpha
   
    ## Put all these results in a dictionary
    results_dict = dict()
    results_dict['tickers'] = tickers
    results_dict['tickers'] = tickers
    results_dict['Prices'] = prices_df
    results_dict['Returns'] = returns_df
    results_dict['Ratios'] = ratios_df
    results_dict['MonteCarlo'] = portfolio_2y_sim
    results_dict['user_stock'] = user_stock
    results_dict['user_stock_weight'] = user_stock_weight
    
    return results_dict

# function to perform linear regression and return alpha for the stock
def linear_regression(x,y):

    x = sm.add_constant(x)

    model = regression.linear_model.OLS(y,x).fit()
    
    ## Remove the constant
    x = x.iloc[:,1]
    
    return model.params[0]