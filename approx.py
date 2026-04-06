# Carr Madan approximation of VIX 
import math 
from datetime import timedelta, datetime





# Load initial values 
T = 30 / 365 
sm = 0 
r = 0.02

# When loading bid, ask and strike prices, ensure you flip between put and call such that the option used is always out of the money. 

ticker_symbol = ""

days_until_expiry = T * 365
option_expiry_date = datetime.now() + timedelta(days=days_until_expiry) # Assumption: we mean business days 
print(option_expiry_date)

S0 = 0 # placeholder 
F = S0 * math.e ** r * T 
bids = []
asks = []
strikes = []

K0 = 0 # placeholder - K0 is the first strike less than or equal to s0 

# ignore first and last term for delta_strike calculations 
for i in range(1, len(strikes) - 1):
    delta_strike = (strikes[i + 1] - strikes[i - 1]) / 2 # midpoint rule 
    discount = math.e ** r * T
    q_term = (bids[i] + asks[i]) / 2

error_correction = -(1 / T) * (F / K0 - 1) ** 2 
sigma_square = (2 / T) (sm) + error_correction

print("Numerical Approx value:", sigma_square)