import numpy as np
from scipy.stats import norm

r = 0.01
S= 30
K = 40
T = 240/365
sigma = 0.30

def blackScholes (r, S, K, T, sigma, type="C"):
    "Calculate the BS pricing of a call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    try:
        if type =="C":
            price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "P":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        return price
    
    except:
        print("Please confirm option type ('C' for call or 'P' for put).")

print("Option price is: ", round(blackScholes(r, S, K, T, sigma, type="P"), 2))