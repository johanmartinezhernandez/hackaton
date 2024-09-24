import flet as ft

def sumar_numeros(num_fields, result_text):
    try:
        suma = sum([int(field.value) for field in num_fields])
        result_text.value = f"La suma es: {suma}"
    except ValueError:
        result_text.value = "Error al sumar los números."
    
    result_text.update()

def main(page: ft.Page):
    page.title = "Suma de 5 números"  # Cambié a 5 para que coincida
    
    # Creación de los 5 campos de texto
    num_fields = [ft.TextField() for i in range(5)]
    
    # Texto para mostrar el resultado
    result_text = ft.Text()
    
    # Botón para realizar la suma
    sumar_button = ft.ElevatedButton(
        text="Sumar",
        on_click=lambda e: sumar_numeros(num_fields, result_text)  # Usando lambda
    )
    
    # Añadir los campos de texto y el botón a la página
    page.add(
        *num_fields, 
        sumar_button, 
        result_text
    )

ft.app(target=main)
