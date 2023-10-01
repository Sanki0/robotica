import sympy as sp
x = sp.symbols("x")
expr=(x**2 + 2*x + 1) / (x + 1)
simp = sp.simplify(expr)
res=expr.subs(x,5) # Reemplaza la variable x por 5
print("Expresión original: ", expr)
print("Expresión simplificada: ", simp)
print("Resultado: ",res)