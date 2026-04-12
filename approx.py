# Carr Madan approximation of VIX 
import math 
from datetime import timedelta, datetime
import yfinance as yf 
import numpy as np 

# Load initial values 
T = 30 / 365 
sm = 0 
r = 0.02

# When loading bid, ask and strike prices, ensure you flip between put and call such that the option used is always out of the money. 

days_until_expiry = T * 365
option_expiry_date = datetime.now() + timedelta(days=days_until_expiry) # Assumption: we mean business days 

option_expiry_date = "2026-05-13" # overwrite 
print("Option Expiry Date:", option_expiry_date)


tkr = "^SPX"
stock_data = yf.Ticker(tkr)
exp_dat_map = {}
for idx, exp in enumerate(stock_data.options): # this consists of a tuple of dates that is only iterable
    exp_dat_map[exp] = idx
# necessary unfortunately 

calls = stock_data.option_chain(stock_data.options[exp_dat_map[option_expiry_date]]).calls
puts = stock_data.option_chain(stock_data.options[exp_dat_map[option_expiry_date]]).puts

calls = calls[['bid', 'ask', 'strike']]
puts = puts[['bid', 'ask', 'strike']]
# current_price = tkr.info.get('currentPrice')
# print(current_price)
S0 = 6816.89 

F = S0 * math.e ** (r * T)

# load the 30 days out bid, ask and strike prices - only out of the money 
calls = calls[calls['strike'] > S0]
puts = puts[puts['strike'] <= S0]

bids = puts['bid'].to_list() + calls['bid'].to_list()
asks = puts['ask'].to_list() + calls['ask'].to_list()
strikes = puts['strike'].to_list() +  calls['strike'].to_list()
# print(strikes)
# print(1/0)


K0 = puts['strike'].to_list()[-1] # K0 is the first strike less than or equal to s0 
# print(puts['strike'].to_list())
print("K0:", K0)


# ignore first and last term for delta_strike calculations 
for i in range(1, len(strikes) - 1):
    delta_strike = (strikes[i + 1] - strikes[i - 1]) / 2 # midpoint rule 
    discount = math.e ** (r * T)
    q_term = (bids[i] + asks[i]) / 2
    sm += (delta_strike / strikes[i]**2) * discount * q_term

error_correction = -(1 / T) * (F / K0 - 1) ** 2 
sigma_square = (2 / T) * (sm) + error_correction

print("Error correction term:", error_correction)
print("Numerical Approx Sigma Squared:", sigma_square)
print("VIX:", 100 * math.sqrt(sigma_square))