import flet as ft

def mostrar_nombre(text_field, page):
    nombre = text_field.value
    dialog = ft.AlertDialog(
        title=ft.Text("Mostrar Nombre"),
        content=ft.Text(f"Tu nombre es: {nombre}. "),
        actions=[
            ft.TextButton("Da click para salir", on_click=lambda e: close_dialog(page))
        ],
    )
    
    page.dialog = dialog
    page.dialog.open = True
    page.update()  # Asegúrate de actualizar la página para mostrar el diálogo

def close_dialog(page):
    page.dialog.open = False
    page.update()  # Actualiza para cerrar el diálogo

def main(page: ft.Page):
    page.title = "Mostrar Nombre"
    page.bgcolor = "LightBlue"  # Cambié a un azul más claro
    
    text_field = ft.TextField(label="Ingresa tu nombre")  # Agregué un label
    
    button = ft.ElevatedButton(
        text="Di mi nombre", 
        on_click=lambda e: mostrar_nombre(text_field, page)
    )
    
    page.add(
        ft.Row(controls=[
            text_field,
            button
        ])
    )

ft.app(target=main)
