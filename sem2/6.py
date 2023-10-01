import sympy as sp
import numpy as np

t,i, j = sp.symbols("t i j")
f= t**2*i + sp.sqrt(5-t**2)

print("Expresión original: ", f)

# Derivada
df = sp.diff(f,t)
print("Derivada: ", df)

# Derivada segunda
ddf = sp.diff(df,t)
print("Derivada segunda: ", ddf)