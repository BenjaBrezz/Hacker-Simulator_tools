import tkinter as tk

def set_language(selected_language):
    if selected_language == 'English':
        label.config(text="Enter the encrypted string:")
        button.config(text="Decrypt")
        result_label.config(text="")
    elif selected_language == 'Español':
        label.config(text="Ingresa la cadena cifrada:")
        button.config(text="Descifrar")
        result_label.config(text="")
    else:
        result_label.config(text="Invalid language selection.")

def decrypt():
    string = entry.get()  # Obtiene el texto ingresado en la entrada de texto
    output = ''  # Variable para almacenar la salida cifrada
    arr = string.split(':')  # Divide la cadena en una lista de objetos separados por ':'
    for arr_obj in arr:  # Itera sobre cada objeto en la lista
        if all(c.isdigit() or c.upper() in 'ABCDEF' for c in arr_obj):  # Verifica si cada carácter del objeto es un dígito o una letra hexadecimal
            output += arr_obj + ':'  # Agrega el objeto a la salida con ':' al final
    
    if output:  # Si hay una salida generada
        output = output[:-1]  # Elimina el último ':' de la salida
        root.clipboard_clear()  # Limpia el portapapeles
        root.clipboard_append(output)  # Agrega la salida al portapapeles
        result_label.config(text=output + " ¡Copiado en el portapapeles!")
        result_label.config(fg="#029A02")  # Configura el color del texto en verde 
    else:  
        result_label.config(text="No se ha copiado NADA en el portapapeles. No hay coincidencias.")  
        result_label.config(fg="#FF0000")  # Configura el color del texto en rojo 


#Interfaz General
root = tk.Tk()
root.title("Decrypt Tool - Hacker Simulator")
root.geometry("400x200")
root.configure(bg="#161616")  # Color de fondo hexadecimal

# Selección de idioma
language_var = tk.StringVar()
language_var.set('English')  # Idioma predeterminado
language_menu = tk.OptionMenu(root, language_var, 'English', 'Español', command=set_language)
language_menu.pack(pady=10)

# Titulo
label = tk.Label(root, text="Enter the encrypted string:", font=("Arial", 10), bg="#161616", fg="#FFFFFF")  # Color de fondo y color del texto en hexadecimal
label.pack(pady=10)

# Entrada de texto
entry = tk.Entry(root, font=("Arial", 10), bg="#A2A2A2")
entry.pack(pady=10)

# Botón descifrar
button = tk.Button(root, text="Decrypt", command=decrypt, font=("Arial", 10), bg="#808080", fg="#FFFFFF")  # Color de fondo hexadecimal
button.pack(pady=10)

# Zona Resultado
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#161616")  # Color de fondo hexadecimal
result_label.pack()

# Repite las solicitudes
root.mainloop()

