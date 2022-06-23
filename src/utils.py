import numpy as np

def normalize_name(X):
	X = np.char.join(' ', np.char.split(X))
	return np.char.title(np.char.strip(X))