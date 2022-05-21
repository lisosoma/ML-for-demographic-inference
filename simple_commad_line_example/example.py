import sys
import pickle
import pandas as pd
import numpy as np
from demographic_model_dadi import model_func
import dadi
import pylab
import matplotlib.pyplot as plt


if len(sys.argv) < 4:
    print('Too few arguments')
    print('Usage: <Model file (MultiOutputRegressor1.sav or RegressorChain1.sav)>, <labels file (y_test1.txt)>)

filename = sys.argv[1]
testy = sys.argv[2]
testx = sys.argv[3]

pts_l = 20

names = np.linspace(1, (pts_l + 1) ** 2, (pts_l + 1) ** 2, endpoint = True, dtype = int)
a = " ".join(names.astype(str))
a += '\n'

MultiOutputRegressor = pickle.load(open(filename, 'rb'))
y_test = pd.read_table(testy, sep='\s+', engine='python', names = [0, 1, 2, 3, 4]).to_numpy()
X_test = pd.read_table(testx,sep='\s+', engine='python', names = names).to_numpy()
y_pred = MultiOutputRegressor.predict(X_test)

n_pop = 2
pop_labels = ["Pop 1", "Pop 2"]
par_labels = ['nu1', 'nu2', 'm12', 'm21', 'T']

mu = 2.5e-8  # mutation rate
L = 20000000  # effective length of sequence
Nanc = 10000
theta = 4 * mu * L * Nanc  # mutation flux

ns_per_pop = 20
ns = [ns_per_pop for _ in range(n_pop)]


print('True parameters:', y_test[0])
print('Predicted parameters:', y_test[0])
print('Images of true and predicted spectrums, saved in jpeg format')

popt = y_test[0]
func_ex = dadi.Numerics.make_extrap_log_func(model_func)
model = func_ex(popt, ns, pts_l)
data = model * theta
plt.figure()
dadi.Plotting.plot_single_2d_sfs(data, vmin = 1)
plt.savefig('true.jpeg', dpi=300)
plt.plot()

popt = y_pred[0]
func_ex = dadi.Numerics.make_extrap_log_func(model_func)
model = func_ex(popt, ns, pts_l)
data = model * theta
plt.figure()
dadi.Plotting.plot_single_2d_sfs(data, vmin = 1)
plt.savefig('pred.jpeg', dpi=300)
