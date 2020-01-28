
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

nsample = 100

x = np.linspace(0,10,nsample)
X = sm.add_constant(x)

beta = np.array([1, 10])

e = np.random.normal(size=nsample)*100

y = np.dot(X, beta) + e

model = sm.OLS(y, X)

results = model.fit()

print(results.summary())

y_fitted = results.fittedvalues
fig, ax = plt.subplots(figsize=(8,6))

ax.plot(x, y, 'o', label='data')
ax.plot(x, y_fitted, 'r--', label='OLS')
ax.legend(loc='best')

fig.show()






