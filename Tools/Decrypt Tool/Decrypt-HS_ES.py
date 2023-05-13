import tkinter as tk
from tkinter import ttk
## from PIL import Image, ImageTk - Importa módulos para agregar imágenes.


def set_language(selected_language):
    if selected_language == 'English':
        label.config(text="Enter the encrypted string:")
        button.config(text="Decrypt")
        language_var.set('English')
    elif selected_language == 'Español':
        label.config(text="Ingresa la cadena cifrada:")
        button.config(text="Descifrar")
        language_var.set('Español')
    else:
        result_label.config(text="Invalid language selection.")
        result_label.config(text="")
    
    language_menu['menu'].delete(0, 'end')
    language_menu['menu'].add_command(label='English', command=lambda: set_language('English'))
    language_menu['menu'].add_command(label='Español', command=lambda: set_language('Español'))

def decrypt():
    string = entry.get()  # Obtener el texto ingresado en la entrada de texto
    output = ''  # Variable para almacenar la salida cifrada
    arr = string.split(':')  # Divide la cadena en una lista de objetos separados por ':'
    for arr_obj in arr:  # Itera sobre cada objeto en la lista
        if all(c.isdigit() or c.upper() in 'ABCDEF' for c in arr_obj):  # Verifica si cada carácter del objeto es un dígito o una letra hexadecimal
            output += arr_obj + ':'  # Agrega el objeto a la salida con ':' al final

    if output:  # Si hay una salida generada
        output = output[:-1]  # Elimina el último ':' de la salida
        root.clipboard_clear()  # Limpia el portapapeles
        root.clipboard_append(output)  # Agrega la salida al portapapeles
        result_label.config(text=output + " ¡Copiado en el portapapeles!", fg="#029A02")  # Configura el color del texto en verde
    else:
        result_label.config(text="No se ha copiado NADA en el portapapeles. No hay coincidencias.", fg="#FF0000")  # Configura el color del texto en rojo
    entry.delete(0, 'end')  # Vaciar la entrada de texto después de mostrar el resultado


# Interfaz General
root = tk.Tk()
root.title("Decrypt Tool - Hacker Simulator")
root.geometry("400x200")
root.configure(bg="#01000a")  # Color de fondo hexadecimal

""" Logo 
logo_path = "C:\\Users\\benja\\Desktop\\Logo-decrypt.png"
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((30, 30))
logo_tk = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_tk, bg="#01000a")
logo_label.pack(anchor="nw", padx=10, pady=10) """

# Selección de idioma
language_var = tk.StringVar()
language_var.set('English')  # Establecer valor predeterminado como cadena vacía

# Estilos menú de idiomas
language_menu_style = ttk.Style()
language_menu_style.configure('TMenubutton', background='#161616', foreground='#FFFFFF')  # Color de fondo y texto en hexadecimal
language_menu_style.map('TMenubutton', background=[('active', '#01000a')])  # Color de fondo hexadecimal cuando se activa el menú

language_menu = ttk.OptionMenu(root, language_var, 'English', 'Español', command=set_language, style='TMenubutton')
language_menu.pack(pady=10)

# Titulo
label = tk.Label(root, text="Enter the encrypted string:", font=("Arial", 11), bg="#01000a", fg="#FFFFFF")  # Color de fondo y color del texto en hexadecimal
label.pack(pady=10)

# Entrada de texto
entry = tk.Entry(root, font=("Arial", 10), bg="#FFFFFF")
entry.pack(pady=10)

# Botón descifrar
button = tk.Button(root, text="Decrypt", command=decrypt, font=("Arial", 10), bg="#A2A2A2", fg="#000000")  # Color de fondo hexadecimal
button.pack(pady=10)

# Zona Resultado
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#01000a")  # Color de fondo hexadecimal
result_label.pack()

# Repite las solicitudes
root.mainloop()