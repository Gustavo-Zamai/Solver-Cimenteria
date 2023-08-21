from pulp import *
from tkinter import *

# Cria o problema de maximização
prob = LpProblem("Problema de Otimização", LpMaximize)

# Variáveis de decisão
X1 = LpVariable("X1", lowBound=0, cat='Continuous')
X2 = LpVariable("X2", lowBound=0, cat='Continuous')
X3 = LpVariable("X3", lowBound=0, cat='Continuous')
X4 = LpVariable("X4", lowBound=0, cat='Continuous')


# Função objetivo
prob += 42.0*X1 + 60.0*X2 + 12.0*X3 + 32.0*X4 - 60.0*(0.34*X1 + 0.65*X2) - 120.0*(0.05*X1 + 0.03*X2 + 0.05*X3) - 30.0*(0.1*X1 + 0.05*X2 + 0.05*X3) - 15.0*(0.0*X1 + 0.0*X2 + 0.0*X3)

# Restrições
prob += 0.34*X1 + 0.65*X2 + 0.0*X3 <= 900000
prob += 0.05*X1 + 0.03*X2 + 0.05*X3 <= 100000
prob += 0.1*X1 + 0.05*X2 + 0.05*X3 <= 300000
prob += 0.0*X1 + 0.0*X2 + 0.0*X3 <= 50000
prob += X4 <= 400000
prob += X1 + X2 + X3 <= 1680000
prob += 0.51*X1 + 0.27*X2 + 0.9*X3 + X4 <= 1280000

# Resolve o problema
prob.solve()

# Imprime o status da solução
print("Status:", LpStatus[prob.status])

# Imprime os valores das variáveis de decisão
print("Valor de X1 =", value(X1))
print("Valor de X2 =", value(X2))
print("Valor de X3 =", value(X3))
print("Valor de X4 =", value(X4))

# Imprime o valor ótimo da função objetivo
print("Valor ótimo da função objetivo =", value(prob.objective))


janela = Tk()

janela.title("Maximizar Lucro")

cimento = Label(janela, text="Valor do cimento: ")
cimento.grid(column=1,row=1)
valCimento = Entry(janela)
valCimento.grid(column=1,row=2)
janela.mainloop();