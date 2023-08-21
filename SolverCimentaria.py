from tkinter.ttk import Scrollbar

from pulp import *
import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedStyle
import customtkinter as ctk

# Função para resolver o problema
def resolver_problema():
    try:
        # Obter os valores das restrições e das variáveis do usuário
        valor_restricao_1 = float(restricao_1_entry.get())
        valor_restricao_2 = float(restricao_2_entry.get())
        valor_restricao_3 = float(restricao_3_entry.get())
        valor_restricao_4 = float(restricao_4_entry.get())
        valor_restricao_5 = float(restricao_5_entry.get())
        valor_restricao_6 = float(restricao_6_entry.get())
        valor_restricao_7 = float(restricao_7_entry.get())

        # Obter os valores de custo das variáveis do usuário
        valor_custo_x1 = float(custo_x1_entry.get())
        valor_custo_x2 = float(custo_x2_entry.get())
        valor_custo_x3 = float(custo_x3_entry.get())
        valor_custo_x4 = float(custo_x4_entry.get())

        # Obter os valores de gasto com os insumos
        valor_insumo_1 = float(valor_insumo_1_entry.get())
        valor_insumo_2 = float(valor_insumo_2_entry.get())
        valor_insumo_3 = float(valor_insumo_3_entry.get())
        valor_insumo_4 = float(valor_insumo_4_entry.get())

        # Obter % dos insumos usados em cada Cimento
        porc_clinquer_x1 = float(porc_clinquer_x1_entry.get())
        porc_clinquer_x2 = float(porc_clinquer_x2_entry.get())
        porc_clinquer_x3 = float(porc_clinquer_x3_entry.get())
        porc_esc_x1 = float(porc_esc_x1_entry.get())
        porc_esc_x2 = float(porc_esc_x2_entry.get())
        porc_esc_x3 = float(porc_esc_x3_entry.get())
        porc_gesso_x1 = float(porc_gesso_x1_entry.get())
        porc_gesso_x2 = float(porc_gesso_x2_entry.get())
        porc_gesso_x3 = float(porc_gesso_x3_entry.get())
        porc_mat_carb_x1 = float(porc_mat_carb_x1_entry.get())
        porc_mat_carb_x2 = float(porc_mat_carb_x2_entry.get())
        porc_mat_carb_x3 = float(porc_mat_carb_x3_entry.get())
        porc_aditivo_x1 = float(porc_aditivo_x1_entry.get())
        porc_aditivo_x2 = float(porc_aditivo_x2_entry.get())
        porc_aditivo_x3 = float(porc_aditivo_x3_entry.get())

        # Cria o problema de maximização
        prob = LpProblem("Problema de Otimização", LpMaximize)

        # Variáveis de decisão
        X1 = LpVariable("X1", lowBound=0, cat='Continuous')
        X2 = LpVariable("X2", lowBound=0, cat='Continuous')
        X3 = LpVariable("X3", lowBound=0, cat='Continuous')
        X4 = LpVariable("X4", lowBound=0, cat='Continuous')

        # Função objetivo
        prob += valor_custo_x1 * X1 + valor_custo_x2 * X2 + valor_custo_x3 * X3 + valor_custo_x4 * X4 - valor_insumo_1 * (
                (porc_esc_x1 / 100) * X1 + (porc_esc_x2 / 100) * X2 + (porc_esc_x3 / 100) * X3) - valor_insumo_2 * \
                ((porc_gesso_x1 / 100) * X1 + (porc_gesso_x2 / 100) * X2 + (porc_gesso_x3 / 100) * X3) - valor_insumo_3 * (
                        (porc_mat_carb_x1 / 100) * X1 + (porc_mat_carb_x2 / 100) * X2 + (porc_mat_carb_x3 / 100) * X3) -\
                valor_insumo_4 * ((porc_aditivo_x1 / 100) * X1 + (porc_aditivo_x2 / 100) * X2 + (porc_aditivo_x3 / 100) * X3)

        # Restrições
        prob += (porc_esc_x1 / 100) * X1 + (porc_esc_x2 / 100) * X2 + (porc_esc_x3 / 100) * X3 <= valor_restricao_1
        prob += (porc_gesso_x1 / 100) * X1 + (porc_gesso_x2 / 100) * X2 + (porc_gesso_x3 / 100) * X3 <= valor_restricao_2
        prob += (porc_mat_carb_x1 / 100) * X1 + (porc_mat_carb_x2 / 100) * X2 + (porc_mat_carb_x3 / 100) * X3 <= valor_restricao_3
        prob += (porc_aditivo_x1 / 100) * X1 + (porc_aditivo_x2 / 100) * X2 + (porc_aditivo_x3 / 100) * X3 <= valor_restricao_4
        prob += X4 <= valor_restricao_5
        prob += X1 + X2 + X3 <= valor_restricao_6
        prob += (porc_clinquer_x1 / 100) * X1 + (porc_clinquer_x2 / 100) * X2 + (porc_clinquer_x3 / 100) * X3 + X4 <= valor_restricao_7

        # Resolve o problema
        prob.solve()

        # Atualiza os rótulos com os resultados
        x1_label.configure(text="Valor de X1 = " + str(value(X1)))
        x2_label.configure(text="Valor de X2 = " + str(value(X2)))
        x3_label.configure(text="Valor de X3 = " + str(value(X3)))
        x4_label.configure(text="Valor de X4 = " + str(value(X4)))
        objetivo_label.configure(text="Valor ótimo da função objetivo = " + str(value(prob.objective)))

    except Exception:
        # Exibe mensagem de erro caso haja falha de digitação
        messagebox.showerror("Erro", "Dados não compativeis", )
    finally:
        # Limpa os campos wdiget
        limpaValores()

# Função para limpar os widget
def limpaValores():
    custo_x1_entry.delete(0, 'end')
    custo_x2_entry.delete(0, 'end')
    custo_x3_entry.delete(0, 'end')
    custo_x4_entry.delete(0, 'end')
    restricao_1_entry.delete(0, 'end')
    restricao_2_entry.delete(0, 'end')
    restricao_3_entry.delete(0, 'end')
    restricao_4_entry.delete(0, 'end')
    restricao_5_entry.delete(0, 'end')
    restricao_6_entry.delete(0, 'end')
    restricao_7_entry.delete(0, 'end')
    valor_insumo_1_entry.delete(0, 'end')
    valor_insumo_2_entry.delete(0, 'end')
    valor_insumo_3_entry.delete(0, 'end')
    valor_insumo_4_entry.delete(0, 'end')
    porc_clinquer_x1_entry.delete(0, 'end')
    porc_clinquer_x2_entry.delete(0, 'end')
    porc_clinquer_x3_entry.delete(0, 'end')
    porc_esc_x1_entry.delete(0, 'end')
    porc_esc_x2_entry.delete(0, 'end')
    porc_esc_x3_entry.delete(0, 'end')
    porc_gesso_x1_entry.delete(0, 'end')
    porc_gesso_x2_entry.delete(0, 'end')
    porc_gesso_x3_entry.delete(0, 'end')
    porc_mat_carb_x1_entry.delete(0, 'end')
    porc_mat_carb_x2_entry.delete(0, 'end')
    porc_mat_carb_x3_entry.delete(0, 'end')
    porc_aditivo_x1_entry.delete(0, 'end')
    porc_aditivo_x2_entry.delete(0, 'end')
    porc_aditivo_x3_entry.delete(0, 'end')

# Cria a janela principal
janela = tk.Tk()
janela.title("Solver de Programação Linear")
janela.minsize(width=1280, height=720)
janela.maxsize(width=1920, height=1080)
style = ThemedStyle(janela)
style.set_theme("breeze")

# Frame
frame = tk.Frame(janela)
frame.pack()

# LabelFrame para entrada dos valores
infoEntrada = tk.LabelFrame(frame, text="Valor do Produto")
infoEntrada.grid(row=0, column=0, sticky="news", padx=10, pady=10)

# Cria os campos de entrada para os custos das variáveis
custo_x1_label = tk.Label(infoEntrada, text="Custo do cimento A = ")
custo_x1_label.grid(column=0, row=1)
custo_x1_entry = tk.Entry(infoEntrada)
custo_x1_entry.grid(column=1, row=1)

custo_x2_label = tk.Label(infoEntrada, text="Custo do cimento B = ")
custo_x2_label.grid(column=0, row=2)
custo_x2_entry = tk.Entry(infoEntrada)
custo_x2_entry.grid(column=1, row=2)

custo_x3_label = tk.Label(infoEntrada, text="Custo do cimento C = ")
custo_x3_label.grid(column=0, row=3)
custo_x3_entry = tk.Entry(infoEntrada)
custo_x3_entry.grid(column=1, row=3)

custo_x4_label = tk.Label(infoEntrada, text="Custo do Clinquer = ")
custo_x4_label.grid(column=0, row=4)
custo_x4_entry = tk.Entry(infoEntrada)
custo_x4_entry.grid(column=1, row=4)

for widget in infoEntrada.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# LabelFrame para a restrições
infoRestricoes = tk.LabelFrame(frame, text="Restrições dos Componentes")
infoRestricoes.grid(column=0, row=1, sticky="news", padx=10,pady=10)

# Cria os campos de entrada para as restrições
restricao_1_label = tk.Label(infoRestricoes, text="Escória de Alto Forno <= ")
restricao_1_label.grid(column=0, row=0)
restricao_1_entry = tk.Entry(infoRestricoes)
restricao_1_entry.grid(column=1, row=0)

restricao_2_label = tk.Label(infoRestricoes, text="Gesso <= ")
restricao_2_label.grid(column=0, row=1)
restricao_2_entry = tk.Entry(infoRestricoes)
restricao_2_entry.grid(column=1, row=1)

restricao_3_label = tk.Label(infoRestricoes, text="Material Carbonático <= ")
restricao_3_label.grid(column=0, row=2)
restricao_3_entry = tk.Entry(infoRestricoes)
restricao_3_entry.grid(column=1, row=2)

restricao_4_label = tk.Label(infoRestricoes, text="Aditivo <= ")
restricao_4_label.grid(column=0, row=3)
restricao_4_entry = tk.Entry(infoRestricoes)
restricao_4_entry.grid(column=1, row=3)

restricao_5_label = tk.Label(infoRestricoes, text="Venda de Clínquer <= ")
restricao_5_label.grid(column=0, row=4)
restricao_5_entry = tk.Entry(infoRestricoes)
restricao_5_entry.grid(column=1, row=4)

restricao_6_label = tk.Label(infoRestricoes, text="Cimento <= ")
restricao_6_label.grid(column=0, row=5)
restricao_6_entry = tk.Entry(infoRestricoes)
restricao_6_entry.grid(column=1, row=5)

restricao_7_label = tk.Label(infoRestricoes, text="Clínquer <= ")
restricao_7_label.grid(column=0, row=6)
restricao_7_entry = tk.Entry(infoRestricoes)
restricao_7_entry.grid(column=1, row=6)

for widget in infoRestricoes.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Entrada do custo dos insumos
infoInsumos = tk.LabelFrame(frame, text="Valor do Custo dos Insumos")
infoInsumos.grid(row=1, column=1, sticky="news", padx=10, pady=10)

valor_insumo_1_label = tk.Label(infoInsumos, text='Preço da Escória de Alto Forno = ')
valor_insumo_1_label.grid(column=0, row=9)
valor_insumo_1_entry = tk.Entry(infoInsumos)
valor_insumo_1_entry.grid(column=1, row=9)

valor_insumo_2_label = tk.Label(infoInsumos, text='Preço do Gesso = ')
valor_insumo_2_label.grid(column=0, row=10)
valor_insumo_2_entry = tk.Entry(infoInsumos)
valor_insumo_2_entry.grid(column=1, row=10)

valor_insumo_3_label = tk.Label(infoInsumos, text='Preço do Material Carbonático = ')
valor_insumo_3_label.grid(column=0, row=11)
valor_insumo_3_entry = tk.Entry(infoInsumos)
valor_insumo_3_entry.grid(column=1, row=11)

valor_insumo_4_label = tk.Label(infoInsumos, text='Preço do Aditivo = ')
valor_insumo_4_label.grid(column=0, row=12)
valor_insumo_4_entry = tk.Entry(infoInsumos)
valor_insumo_4_entry.grid(column=1, row=12)

for widget in infoInsumos.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Entrada da % dos componentes por Cimento
infoClinquer = tk.LabelFrame(frame, text="Porcentagem do Uso de Clinquer nos Cimentos")
infoClinquer.grid(row=2, column=1, sticky="news", padx=10, pady=10)

porc_clinquer_x1_label = tk.Label(infoClinquer, text='% do uso do Clinquer no Cimento Tipo A:')
porc_clinquer_x1_label.grid(column=1, row=2)
porc_clinquer_x1_entry = tk.Entry(infoClinquer)
porc_clinquer_x1_entry.grid(column=2, row=2)

porc_clinquer_x2_label = tk.Label(infoClinquer, text='% do uso do Clinquer no Cimento Tipo B:')
porc_clinquer_x2_label.grid(column=1, row=3)
porc_clinquer_x2_entry = tk.Entry(infoClinquer)
porc_clinquer_x2_entry.grid(column=2, row=3)

porc_clinquer_x3_label = tk.Label(infoClinquer, text='% do uso do Clinquer no Cimento Tipo C:')
porc_clinquer_x3_label.grid(column=1, row=4)
porc_clinquer_x3_entry = tk.Entry(infoClinquer)
porc_clinquer_x3_entry.grid(column=2, row=4)

for widget in infoClinquer.winfo_children():
    widget.grid_configure(padx=2, pady=2)

infoEsc = tk.LabelFrame(frame, text="Porcentagem do Uso de Escória de Alto Forno nos Cimentos")
infoEsc.grid(row=0, column=2, sticky="news", padx=10, pady=10)

porc_esc_x1_label = tk.Label(infoEsc, text='% do uso da Escória de Alto Forno no Cimento Tipo A:')
porc_esc_x1_label.grid(column=1, row=5)
porc_esc_x1_entry = tk.Entry(infoEsc)
porc_esc_x1_entry.grid(column=2, row=5)

porc_esc_x2_label = tk.Label(infoEsc, text='% do uso da Escória de Alto Forno no Cimento Tipo B:')
porc_esc_x2_label.grid(column=1, row=6)
porc_esc_x2_entry = tk.Entry(infoEsc)
porc_esc_x2_entry.grid(column=2, row=6)

porc_esc_x3_label = tk.Label(infoEsc, text='% do uso da Escória de Alto Forno no Cimento Tipo C:')
porc_esc_x3_label.grid(column=1, row=7)
porc_esc_x3_entry = tk.Entry(infoEsc)
porc_esc_x3_entry.grid(column=2, row=7)

for widget in infoEsc.winfo_children():
    widget.grid_configure(padx=2, pady=2)

infoGesso = tk.LabelFrame(frame, text="Porcentagem do Uso de Gesso nos Cimentos")
infoGesso.grid(row=1, column=2, sticky="news", padx=10, pady=10)

porc_gesso_x1_label = tk.Label(infoGesso, text='% do uso de Gesso no Cimento Tipo A:')
porc_gesso_x1_label.grid(column=1, row=8)
porc_gesso_x1_entry = tk.Entry(infoGesso)
porc_gesso_x1_entry.grid(column=2, row=8)

porc_gesso_x2_label = tk.Label(infoGesso, text='% do uso de Gesso no Cimento Tipo B:')
porc_gesso_x2_label.grid(column=1, row=9)
porc_gesso_x2_entry = tk.Entry(infoGesso)
porc_gesso_x2_entry.grid(column=2, row=9)

porc_gesso_x3_label = tk.Label(infoGesso, text='% do uso de Gesso no Cimento Tipo C:')
porc_gesso_x3_label.grid(column=1, row=10)
porc_gesso_x3_entry = tk.Entry(infoGesso)
porc_gesso_x3_entry.grid(column=2, row=10)

for widget in infoGesso.winfo_children():
    widget.grid_configure(padx=2, pady=2)

infoMat = tk.LabelFrame(frame, text="Porcentagem do Uso de Material Carbonático nos Cimentos")
infoMat.grid(row=2, column=2, sticky="news", padx=10, pady=10)

porc_mat_carb_x1_label = tk.Label(infoMat, text='% do uso de Material Carbonático no Cimento Tipo A:')
porc_mat_carb_x1_label.grid(column=1, row=11)
porc_mat_carb_x1_entry = tk.Entry(infoMat)
porc_mat_carb_x1_entry.grid(column=2, row=11)

porc_mat_carb_x2_label = tk.Label(infoMat, text='% do uso de Material Carbonático no Cimento Tipo B:')
porc_mat_carb_x2_label.grid(column=1, row=12)
porc_mat_carb_x2_entry = tk.Entry(infoMat)
porc_mat_carb_x2_entry.grid(column=2, row=12)

porc_mat_carb_x3_label = tk.Label(infoMat, text='% do uso de Material Carbonático no Cimento Tipo C:')
porc_mat_carb_x3_label.grid(column=1, row=13)
porc_mat_carb_x3_entry = tk.Entry(infoMat)
porc_mat_carb_x3_entry.grid(column=2, row=13)

for widget in infoMat.winfo_children():
    widget.grid_configure(padx=2, pady=2)

infoAdi = tk.LabelFrame(frame, text="Porcentagem do Uso de Aditivo nos Cimentos")
infoAdi.grid(row=3, column=2, sticky="news", padx=10, pady=10)

porc_aditivo_x1_label = tk.Label(infoAdi, text='% do uso de Aditivo no Cimento Tipo A:')
porc_aditivo_x1_label.grid(column=1, row=14)
porc_aditivo_x1_entry = tk.Entry(infoAdi)
porc_aditivo_x1_entry.grid(column=2, row=14)

porc_aditivo_x2_label = tk.Label(infoAdi, text='% do uso de Aditivo no Cimento Tipo B:')
porc_aditivo_x2_label.grid(column=1, row=15)
porc_aditivo_x2_entry = tk.Entry(infoAdi)
porc_aditivo_x2_entry.grid(column=2, row=15)

porc_aditivo_x3_label = tk.Label(infoAdi, text='% do uso de Aditivo no Cimento Tipo C:')
porc_aditivo_x3_label.grid(column=1, row=16)
porc_aditivo_x3_entry = tk.Entry(infoAdi)
porc_aditivo_x3_entry.grid(column=2, row=16)

for widget in infoAdi.winfo_children():
    widget.grid_configure(padx=2, pady=2)

# LabelFrame de Resultados
infoResultados = tk.LabelFrame(frame, text="RESULTADOS")
infoResultados.grid(column=1, row=0, sticky="news", padx=10, pady=10)

# Cria os rótulos
x1_label = tk.Label(infoResultados, text="Valor de X1 = ")
x1_label.grid(column=0, row=0)
x2_label = tk.Label(infoResultados, text="Valor de X2 = ")
x2_label.grid(column=0, row=1)
x3_label = tk.Label(infoResultados, text="Valor de X3 = ")
x3_label.grid(column=0, row=2)
x4_label = tk.Label(infoResultados, text="Valor de X4 = ")
x4_label.grid(column=0, row=3)
objetivo_label = tk.Label(infoResultados, text="Valor ótimo da função objetivo = ")
objetivo_label.grid(column=0, row=4)

for widget in infoResultados.winfo_children():
    widget.grid_configure(padx=10, pady=5, columnspan=100)

# Cria o botão para resolver o problema
botao_resolver = ctk.CTkButton(frame, text="Resolver", command=resolver_problema)
botao_resolver.grid(column=0, row=2, sticky="news", padx=50, pady=20)


# Inicia a janela
janela.mainloop()
