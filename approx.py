# Carr Madan approximation of VIX 
import math 


# Load initial values 
T = 0 
sm = 0 
r = 0.02

# When loading bid, ask and strike prices, ensure you flip between put and call such that the option used is always out of the money. 
bids = []
asks = []
strikes = []
F = 0 
K0 = 0 

# ignore first term 
for i in range(1, len(strikes)):
    delta_strike = strikes[i] - strikes[i - 1] 
    discount = math.e ** r * T
    q_term = (bids[i] + asks[i]) / 2

error_correction = -(1 / T) * (F / K0 - 1) ** 2 
sigma_square = (2 / T) (sm) + error_correction

print("Numerical Approx value:", sigma_square)