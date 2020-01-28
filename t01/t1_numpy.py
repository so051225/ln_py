
#
# 1. use norm_dist to generate a dataset
# 2. apply OLS regression
# 3. draw
#

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

nsample = 100

# generate an array wiht length 100 evenly
# upper & lower bound is 0 & 10
x = np.linspace(0,10,nsample)

#
# [0, ..., 10] -> [[1, 0], ..., [1, 10]]
X = sm.add_constant(x)

#
# here assume the beta_constant is 1, beta_1 is 10
beta = np.array([1, 10])

# multiply 100 to enlarge error
e = np.random.normal(size = nsample) * 100

# real y
y_real = np.dot(X, beta) + e

model = sm.OLS(y_real, X)

results = model.fit()

print(results.summary())

y_fitted = results.fittedvalues
fig, ax = plt.subplots(figsize=(8,6))

ax.plot(x, y_real, 'o', label='data')
ax.plot(x, y_fitted, 'r--', label='OLS')
ax.legend(loc='best')

fig.show()






