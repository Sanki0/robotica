import sympy as sp
x, y = sp.symbols("x y")
expr = (x**2 + 2*x*y + y**2)/(x**2 - y**2)
simp= sp.simplify(expr)
res=simp.subs([(x,2),(y,5)])
resf=res.evalf() # Evalua numéricamente
print("Expresión original: ", expr)
print("Expresión simplificada: ", simp)
print("Resultado: ",res)
print("Resultado: ",resf)