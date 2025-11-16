# Sample Crypto Price Prediction

import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = pd.DataFrame({
    "Date": ["2025-11-10", "2025-11-11", "2025-11-12"],
    "Close": [50000, 51000, 49500]
})

print(data)

plt.plot(data['Date'], data['Close'])
plt.title('Bitcoin Closing Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = pd.DataFrame({
    "Date": ["2025-11-10", "2025-11-11", "2025-11-12"],
    "Close": [50000, 51000, 49500]
})

# Plot closing price
plt.plot(data['Date'], data['Close'])
plt.title('Bitcoin Closing Price')
plt.xlabel('Date')
plt.ylabel('Price')

# Save the plot into images folder
plt.savefig('crypto_price_prediction/images/price_plot.png')
plt.show()

