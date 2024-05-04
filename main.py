#Aquí se encuentra el menú principal de la aplicación

import figuras
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #Permite integrar matplotlib con tkinter
import tkinter as tk
import tkinter.font as tkFont #Para cambiar la fuente de los elementos de la interfaz

#Evita que el bucle se mantenga en ejecución
def cerrar():
    root.quit()
    root.destroy()
    
# Crea una ventana
root = tk.Tk()
root.title("Graficadora")
#root.wm_minsize(width=900, height=900)
#root.wm_maxsize(width=1000, height=1000)

labelFont = tkFont.Font(family="Helvetica", size=16, weight="bold")
inputFont = tkFont.Font(family="Helvetica", size=16)

# Crea una figura vacía inicial, ax es el contenedor de los elementos gráficos
fig, ax = plt.subplots(figsize=(6, 6))

# Añadir etiquetas a los ejes
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_xlim(-20, 20)  # Mínimo tamaño para el eje x
ax.set_ylim(-20, 20)  # Mínimo tamaño para el eje y
ax.axhline(y=0, color='black', linestyle='-', linewidth=1, alpha=0.8)  # Marca el eje horizontal
ax.axvline(x=0, color='black', linestyle='-', linewidth=1, alpha=0.8)  # Marca el eje vertical

# Añadir cuadrícula
ax.grid(True)

# Crear lienzo para Matplotlib
canvas = FigureCanvasTkAgg(fig, master=root)

# figuras.cuadrado(ax, (2, 2), 5)
# figuras.circulo(ax, (10, 10), 3)
# figuras.triangulo(ax, (3, 10), 5)
# figuras.rectangulo(ax, (10, 3), 4, 6)

canvas.draw()

# Inserta el lienzo en la ventana
canvas.get_tk_widget().pack()

#Para el desplegable
select = tk.StringVar(value="Cuadrado")
opciones = ["Cuadrado", "Rectángulo", "Triángulo", "Círculo"]
desplegable = tk.OptionMenu(root, select, *opciones)
menu = root.nametowidget(desplegable.menuname)
menu.config(font=inputFont)  # Aplicar la fuente al menú desplegable
desplegable.config(font=labelFont)  # Aplicar la fuente al select
desplegable.pack(anchor='n', pady=10)

#Inputs para el punto inicial del cuadrado
framePunto_Cuadrado = tk.Frame(root)
framePunto_Cuadrado.pack(pady=10)  # Espacio vertical para separar los Frames
puntoLabel_Cuadrado = tk.Label(framePunto_Cuadrado, text="Punto de partida:", font=labelFont)
puntoLabel_Cuadrado.pack(side='left', padx=10, pady=10)
puntoInput_Cuadrado = tk.Entry(framePunto_Cuadrado, width=30, font=inputFont)
puntoInput_Cuadrado.pack(side='left', padx=10, pady=10)

#Inputs para el tamaño del cuadrado
frameAncho_Cuadrado = tk.Frame(root)
frameAncho_Cuadrado.pack(pady=10)  # Espacio vertical para separar los Frames
longLabel_Cuadrado = tk.Label(frameAncho_Cuadrado, text="Longitud:", font=labelFont)
longLabel_Cuadrado.pack(side='left', padx=60, pady=10)
longInput_Cuadrado = tk.Entry(frameAncho_Cuadrado, width=30, font=inputFont)
longInput_Cuadrado.pack(side='left', padx=10, pady=10)

#Inputs para el punto inicial del rectángulo
framePunto_Rectangulo = tk.Frame(root)
framePunto_Rectangulo.pack(pady=10)  # Espacio vertical para separar los Frames
puntoLabel_Rectangulo = tk.Label(framePunto_Rectangulo, text="Punto de partida:", font=labelFont)
puntoLabel_Rectangulo.pack(side='left', padx=10, pady=10)
puntoInput_Rectangulo = tk.Entry(framePunto_Rectangulo, width=30, font=inputFont)
puntoInput_Rectangulo.pack(side='left', padx=10, pady=10)

#Inputs para el ancho del rectángulo
frameAncho_Rectangulo = tk.Frame(root)
frameAncho_Rectangulo.pack(pady=10)  # Espacio vertical para separar los Frames
longLabel_Rectangulo = tk.Label(frameAncho_Rectangulo, text="Ancho:", font=labelFont)
longLabel_Rectangulo.pack(side='left', padx=72, pady=10)
longInput_Rectangulo = tk.Entry(frameAncho_Rectangulo, width=30, font=inputFont)
longInput_Rectangulo.pack(side='left', padx=10, pady=10)

#Inputs para el largo del rectángulo
frameLargo_Rectangulo = tk.Frame(root)
frameLargo_Rectangulo.pack(pady=10)  # Espacio vertical para separar los Frames
largoLabel_Rectangulo = tk.Label(frameLargo_Rectangulo, text="Largo:", font=labelFont)
largoLabel_Rectangulo.pack(side='left', padx=76, pady=10)
largoInput_Rectangulo = tk.Entry(frameLargo_Rectangulo, width=30, font=inputFont)
largoInput_Rectangulo.pack(side='left', padx=10, pady=10)

#Inputs para el punto inicial del triángulo
framePunto_Triangulo = tk.Frame(root)
framePunto_Triangulo.pack(pady=10)  # Espacio vertical para separar los Frames
puntoLabel_Triangulo = tk.Label(framePunto_Triangulo, text="Punto de partida:", font=labelFont)
puntoLabel_Triangulo.pack(side='left', padx=10, pady=10)
puntoInput_Triangulo = tk.Entry(framePunto_Triangulo, width=30, font=inputFont)
puntoInput_Triangulo.pack(side='left', padx=10, pady=10)

#Inputs para la longitud del triángulo
frameLong_Triangulo = tk.Frame(root)
frameLargo_Rectangulo.pack(pady=10)  # Espacio vertical para separar los Frames
longLabel_Triangulo = tk.Label(frameLong_Triangulo, text="Lado:", font=labelFont)
longLabel_Triangulo.pack(side='left', padx=82, pady=10)
longInput_Triangulo = tk.Entry(frameLong_Triangulo, width=30, font=inputFont)
longInput_Triangulo.pack(side='left', padx=10, pady=10)

#Inputs para el punto central del círculo
frameCentro_Circulo = tk.Frame(root)
frameCentro_Circulo.pack(pady=10)  # Espacio vertical para separar los Frames
centroLabel_Circulo = tk.Label(frameCentro_Circulo, text="Centro:", font=labelFont)
centroLabel_Circulo.pack(side='left', padx=10, pady=10)
centroInput_Circulo = tk.Entry(frameCentro_Circulo, width=30, font=inputFont)
centroInput_Circulo.pack(side='left', padx=10, pady=10)

#Inputs para la longitud del triángulo
frameRadio_Circulo = tk.Frame(root)
frameRadio_Circulo.pack(pady=10)  # Espacio vertical para separar los Frames
radioLabel_Circulo = tk.Label(frameRadio_Circulo, text="Radio:", font=labelFont)
radioLabel_Circulo.pack(side='left', padx=18, pady=10)
radioInput_Circulo = tk.Entry(frameRadio_Circulo, width=30, font=inputFont)
radioInput_Circulo.pack(side='left', padx=10, pady=10)

#Función para mostrar los campos de acuerdo a la figura seleccionada
def mostrar_campos(*args):
    framePunto_Cuadrado.pack_forget()
    framePunto_Rectangulo.pack_forget()
    frameAncho_Cuadrado.pack_forget()
    frameAncho_Rectangulo.pack_forget()
    frameLargo_Rectangulo.pack_forget()
    framePunto_Triangulo.pack_forget()
    frameLong_Triangulo.pack_forget()
    frameCentro_Circulo.pack_forget()
    frameRadio_Circulo.pack_forget()
    frameBotones.pack_forget()
    
    if select.get() == "Cuadrado":
        framePunto_Cuadrado.pack()
        frameAncho_Cuadrado.pack()
        
    elif select.get() == "Rectángulo":
        framePunto_Rectangulo.pack()
        frameAncho_Rectangulo.pack()
        frameLargo_Rectangulo.pack()
        
    elif select.get() == "Triángulo":
        framePunto_Triangulo.pack()
        frameLong_Triangulo.pack()
    
    elif select.get() == "Círculo":
        frameCentro_Circulo.pack()
        frameRadio_Circulo.pack()
    
    frameBotones.pack()

#Solo limpia la gráfica, no los campos de entrada
def limpiarCanvas():
    ax.clear()
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.axhline(y=0, color='black', linestyle='-', linewidth=1, alpha=0.8)
    ax.axvline(x=0, color='black', linestyle='-', linewidth=1, alpha=0.8)
    ax.grid(True)

#Función para limpiar el lienzo y los campos de entrada  
def limpiar():
    puntoInput_Cuadrado.delete(0, 'end')
    longInput_Cuadrado.delete(0, 'end')
    puntoInput_Rectangulo.delete(0, 'end')
    longInput_Rectangulo.delete(0, 'end')
    largoInput_Rectangulo.delete(0, 'end')
    puntoInput_Triangulo.delete(0, 'end')
    longInput_Triangulo.delete(0, 'end')
    centroInput_Circulo.delete(0, 'end')
    radioInput_Circulo.delete(0, 'end')
    
    limpiarCanvas()
    canvas.draw()

#Grafica todas las figuras ingresadas
def graficarTodo():
    limpiarCanvas() #Esto evita multiples figuras del mismo tipo
    canvas.draw()
    if puntoInput_Cuadrado.get() != "": #Esta condición debe cambiarse por la del analizador
        punto = eval(puntoInput_Cuadrado.get()) #Eval permite convertir un string a una tupla
        longitud = float(longInput_Cuadrado.get())
        figuras.cuadrado(ax, punto, longitud)
    if puntoInput_Rectangulo.get() != "":
        punto = eval(puntoInput_Rectangulo.get())
        ancho = float(longInput_Rectangulo.get())
        largo = float(largoInput_Rectangulo.get())
        figuras.rectangulo(ax, punto, ancho, largo)
    if puntoInput_Triangulo.get() != "":
        punto = eval(puntoInput_Triangulo.get())
        longitud = float(longInput_Triangulo.get())
        figuras.triangulo(ax, punto, longitud)
    if centroInput_Circulo.get() != "":
        centro = eval(centroInput_Circulo.get())
        radio = float(radioInput_Circulo.get())
        figuras.circulo(ax, centro, radio)
        
    canvas.draw()        

#Función para eliminar la figura seleccionada y sus campos de entrada
def eliminar():
    if select.get() == "Cuadrado":
        puntoInput_Cuadrado.delete(0, 'end')
        longInput_Cuadrado.delete(0, 'end')
        graficarTodo() #Así se conservan las demás figuras
        
    elif select.get() == "Rectángulo":
        puntoInput_Rectangulo.delete(0, 'end')
        longInput_Rectangulo.delete(0, 'end')
        largoInput_Rectangulo.delete(0, 'end')
        graficarTodo()
        
    elif select.get() == "Triángulo":
        puntoInput_Triangulo.delete(0, 'end')
        longInput_Triangulo.delete(0, 'end')
        graficarTodo()
        
    elif select.get() == "Círculo":
        centroInput_Circulo.delete(0, 'end')
        radioInput_Circulo.delete(0, 'end')
        graficarTodo()
        
select.trace_add("write", mostrar_campos)

#Sección para los botones
frameBotones = tk.Frame(root)
frameBotones.pack(pady=10)  # Espacio vertical para separar los Frames
limpiar_button = tk.Button(frameBotones, text="Eliminar todo", command=limpiar, font=labelFont)
limpiar_button.pack(side='left', padx=50, pady=10)
eliminar_button = tk.Button(frameBotones, text="Eliminar figura", command=eliminar, font=labelFont)
eliminar_button.pack(side='left', padx=50, pady=10)
graficar_button = tk.Button(frameBotones, text="Graficar", command=graficarTodo, font=labelFont)
graficar_button.pack(side='left', padx=50, pady=10)

mostrar_campos() #Se llama en cada inicio de la aplicación para evitar que no se ejecuten los cambios
root.protocol("WM_DELETE_WINDOW", cerrar) #No se usan los paréntesis para que no se ejecute la función al iniciar la aplicación
tk.mainloop() # Ejecutar el bucle de eventos de Tkinter