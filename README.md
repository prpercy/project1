# XPLytics
Fintech bootcamp project 1


---
> User would be able to trade stocks, perform stock / portfolio analysis and generate relevant reports.
---

## Technologies

> Program uses Python 3.10.6 version and Jupyter Lab

Program uses following libraries:

* 'Pandas' library to work with dataframes and analyse timeseries data. 
* 'YFinance' API to download market data.
* 'Numpy' library in integration with 'Pandas' to manipulate financial data.
* 'MCForecastTools' file for Monte Carlo Simulations.
* 'Panel' library for creating an interactive web dashboard.
* 'Fire' and 'Questionary' library for Command Line Interface. 
* 'SQLAlchemy' toolkit for application development.
* 'hvplot' and 'matlabplot' for data visualization.
* 'statsmodels' for linear regression to calculate stock alphas

xxx

---

## Installation Guide 

Program requires following packages:
* Hvplot (0.8.0 or above version)
* sqlalchemy
* yfinance
* Panel

All programs needed for application usage can be installed using "pip or conda install" command in terminal. <br />
'MCForecastTools' file must be in same folder as 'app.py' folder. <br />
File directory can and should be downloaded/cloned to ensure proper file retrieval.<br />


---
## Usage

> In terminal, open conda environment. Run python app.py
> Once inside authentication module, use arrow keys and enter key to choose if 'new' or 'returning' user. If 'new' user, then set up username and password.<img width="445" alt="Screen Shot 2022-10-18 at 7 13 08 PM" src="https://user-images.githubusercontent.com/111557486/196811664-e815f578-fd71-4449-bf66-8d3661fc6d67.png">

> After creating a username and password, or logging in, terminal will ask what you would like to do. <img width="428" alt="WWYLTD" src="https://user-images.githubusercontent.com/111557486/196820228-d0b44088-9356-41c9-8520-71b73103a3b1.png">

> The first option available is Update Available Amount for Trading. This option allows you to update the funds in your account to use for buying stocks.
> 
> <img width="491" alt="UAAFT" src="https://user-images.githubusercontent.com/111557486/196827370-02c03442-126e-4aad-9e93-ae6a790b5454.png">

>The next available option is to trade stocks. A buy/sell option will appear. For buying stocks, the terminal will prompt you to include the TICKER for the stock to be purchased. Followed by the amount of stocks to be purchased. Then, the portfolio will be updated. <img width="1085" alt="BUY2" src="https://user-images.githubusercontent.com/111557486/196828340-3c8af3a4-aed2-412b-b622-e58f3dcbc785.png">

>To sell a stock, terminal will prompt you to include the Ticker for the stock from your portfolio to be sold. Followed by the amount of stocks to sell. Then, the portfolio will be updated. 
>
><img width="460" alt="SELL" src="https://user-images.githubusercontent.com/111557486/196828663-55599347-d83b-459d-881c-fad02437fa01.png">

>The next available option is to perform Stock Analysis. The terminal will prompt to include a Ticker for stock to analyze. 
>
><img width="422" alt="STOCKANA" src="https://user-images.githubusercontent.com/111557486/196829580-89236507-f27c-4896-af68-2a330d9056f4.png">
>
>The panel dashboard will open promptly. In the dashboard, a chart with the correlation, volatility, Sharpe ratio, Sortino ratio, Covariance, Beta, and Alpha values can be viewed. The historical data for the past 5 years of stocks, portfolio, and markets were turned into a dataframe. By combining the closing price of each data frame, a 'returns' dataframe is created. Using the standard deviation, the annualized standard deviation can be calculated. From there, the rolling standard deviation for the past 30 days was calculated, which refers to the volatility. Once covariance and variance were calculated from returns, beta was calculated by dividing covariance/variance. Annualized average returns were calculated by taking the average of returns and multiplying by number of trading days. The sharpe and sortino ratios were calculated using the standard deviation and average of returns. Both sharpe and sortino ratios are both risk-adjusted evaluations, however the sortino ratio only factors in downside risk. By having both the sharpe and sortino ratio, we can evaluate both low and high volatility. Alpha was calculated by using 'statsmodel' for linear regression.

><img width="946" alt="Screen Shot 2022-10-19 at 8 27 30 PM" src="https://user-images.githubusercontent.com/111557486/197029934-c1a99b0f-30d8-495e-9e75-c2412d5e0350.png">

> The following option is to perform Portfolio Analysis. The Portfolio Analysis includes Monte-Carlo simulations performed for the user portfolio with weights calculated according to number of shares s/he holds.

><img width="955" alt="Screen Shot 2022-10-20 at 2 47 58 PM" src="https://user-images.githubusercontent.com/111557486/197033690-cac263c6-4da3-4525-bcb1-1d6c56423afb.png">

>The remaining two options are "Delete User" and "Exit Application." The 'Delete' option allows you to delete your portfolio and username/password information. The 'Exit' options allows you to safely exit out of the application.

><img width="178" alt="Screen Shot 2022-10-20 at 3 08 17 PM" src="https://user-images.githubusercontent.com/111557486/197037077-e83c1653-0cbd-4f39-8a22-e1dea220c80c.png">

><img width="308" alt="Screen Shot 2022-10-20 at 3 08 11 PM" src="https://user-images.githubusercontent.com/111557486/197037121-545c0b72-3ee5-4ff9-b823-6e7830e68315.png">







---
## Contributors

Contributors are:
1. [Pravin Patil](https://www.linkedin.com/in/pravin-patil-5880301)
2. [Esteban Lopez](https://www.linkedin.com/in/estebandlopez/)
3. [Jorge Villacreses](https://www.linkedin.com/in/jorge-villacreses-a2114517/)
4. [Liset Lopez]
5. [William Wolfenbarger](https://www.linkedin.com/in/william-wolfenbarger-951379160/)

---

## License

Open

