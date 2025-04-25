import tkinter as tk
import random
import string

def generar_contraseña():
    longitud = longitud_var.get()
    incluir_letras = letras_var.get()
    incluir_numeros = numeros_var.get()
    incluir_simbolos = simbolos_var.get()
    
    caracteres = ""
    if incluir_letras:
        caracteres += string.ascii_letters
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        resultado_var.set("Selecciona al menos una opción.")
        return

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    resultado_var.set(contraseña)

# Ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("400x300")
ventana.resizable(False, False)

# Variables
resultado_var = tk.StringVar()
longitud_var = tk.IntVar(value=12)
letras_var = tk.IntVar(value=1)
numeros_var = tk.IntVar(value=1)
simbolos_var = tk.IntVar(value=0)

# Título
tk.Label(ventana, text="Generador de Contraseñas", font=("Arial", 16)).pack(pady=10)

# Resultado
tk.Entry(ventana, textvariable=resultado_var, font=("Arial", 12), width=35, justify="center").pack(pady=5)

# Longitud
tk.Label(ventana, text="Longitud:", font=("Arial", 12)).pack()
tk.Scale(ventana, from_=4, to=32, orient="horizontal", variable=longitud_var).pack()

# Opciones
tk.Checkbutton(ventana, text="Incluir letras", variable=letras_var).pack()
tk.Checkbutton(ventana, text="Incluir números", variable=numeros_var).pack()
tk.Checkbutton(ventana, text="Incluir símbolos", variable=simbolos_var).pack()

# Botón de generar
tk.Button(ventana, text="Generar Contraseña", command=generar_contraseña).pack(pady=15)

ventana.mainloop()
