import pygsheets
import pandas as pd
import os
# Este ID es de "Interesados en Comprar un libro"
SHEET_ID = "1AQn-m8rBOXREcZdGizuytF-QEYVQMy5Cw-q7s72u4D0" #**************************************************************************************************
SHEET_NAME = "solicitudes_libreria" #*********************************************************************************************************************************
# --- CAMBIO CLAVE AQUÍ ---
# Le decimos a Python que busque el archivo un nivel ARRIBA (en la carpeta del proyecto)

#SERVICE_ACCOUNT_PATH = '../project-mlops-10-streamlit-42bec9881718.json'
SERVICE_ACCOUNT_PATH = os.path.join(os.path.dirname(__file__), '..', 'ethereal-aria-479215-s0-d75abfe5b174.json') #***************************************

def registrar_interes_en_sheet(nombre: str, apellido: str, email: str, telefono: int, libro: str, notifications: bool, events: bool) -> str:
    """
    Registra los datos de un nuevo usuario interesado en un libro en una hoja de cálculo de Google Sheets.
    Usa la lógica de `df.loc` para añadir la nueva fila.
    """
    try:
        url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
        
        # Intentamos leer el CSV. Si la hoja está vacía, puede dar un error, así que lo manejamos.
        try:
            df = pd.read_csv(url)
        except Exception:
            # Si falla (ej. hoja vacía), creamos un DataFrame con las columnas correctas
            df = pd.DataFrame(columns=['ID', 'Nombre Completo', 'Correo', 'Teléfono', 'Libro', 'Notificaciones', 'Eventos'])
        
        # --- USANDO TU LÓGICA SIMPLIFICADA ---
        # Combinamos nombre y apellido
        nombre_completo = f"{nombre} {apellido}"
        # Creamos el ID para la nueva fila
        nuevo_id = len(df) + 1
        
        # Añadimos la nueva fila usando df.loc, como en tu ejemplo
        df.loc[len(df.index)] = [nuevo_id, nombre_completo, email, telefono, libro, notifications, events]

        # Autorizamos y escribimos en la hoja
        gc = pygsheets.authorize(service_file=SERVICE_ACCOUNT_PATH)
        sh = gc.open_by_key(SHEET_ID)
        wks = sh.worksheet_by_title(SHEET_NAME)
        # Escribimos el DataFrame completo desde la celda A1
        wks.set_dataframe(df, start='A1', copy_index=False, fit=True)
        
        print(f"✅ Registro exitoso para {email} en el libro {libro}")
        return f"Registro exitoso para {email} en el libro {libro}"

    except FileNotFoundError:
        error_msg = f"Error: No se pudo encontrar el archivo de credenciales en la ruta '{SERVICE_ACCOUNT_PATH}'."
        print(f"❌ {error_msg}")
        return error_msg
    except Exception as e:
        error_msg = f"Error inesperado al registrar en Google Sheets: {e}"
        print(f"❌ {error_msg}")
        return error_msg



#--- Bloque de Prueba para Ejecución Directa --- ctrol K ctrol U#
# if __name__ == '__main__':
#   print("--- Iniciando prueba de registro directo en Google Sheet (versión simplificada) ---")
  
#   # Datos de prueba que quieres insertar
#   nombre_prueba = "Domenica"
#   apellido_prueba = "Diaz"
#   email_prueba = "domenica.diaz@gmail.com"
#   telefono_prueba = "987654321"
#   libro_prueba = "Libros de ciencia ficción"
#   notifications_prueba = True
#   events_prueba = False
  
#   # Llamamos a la función directamente
#   resultado = registrar_interes_en_sheet(
#       nombre=nombre_prueba,
#       apellido=apellido_prueba,
#       email=email_prueba,
#       telefono=telefono_prueba,
#       libro=libro_prueba,
#       notifications=notifications_prueba,
#       events=events_prueba
#   )
  
#   print("\n--- Resultado de la prueba ---")
#   print(resultado)
#   print("---------------------------------")
#   print("Por favor, verifica la hoja de cálculo en tu navegador para confirmar el registro.")