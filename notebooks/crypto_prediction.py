# Sample Crypto Price Prediction

import pandas as pd
import matplotlib.pyplot as plt
import os

# make imgs fldr
if not os.path.exists('crypto_price_prediction/images'):
    os.makedirs('crypto_price_prediction/images')

# Sample data
data = pd.DataFrame({
    "Date": ["2025-11-10", "2025-11-11", "2025-11-12"],
    "Close": [50000, 51000, 49500]
})

print(data)

# graph
plt.plot(data['Date'], data['Close'])
plt.title('Bitcoin Closing Price')
plt.xlabel('Date')
plt.ylabel('Price')

# img
plt.savefig('crypto_price_prediction/images/price_plot.png')
plt.show()

