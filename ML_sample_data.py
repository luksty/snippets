import pandas as pd, numpy as np

df = pd.DataFrame({'a':np.random.randn(10),'b':np.random.randn(10)+10})
X = df['a'].values[:, np.newaxis]
y = df['b'].values[:, np.newaxis]
