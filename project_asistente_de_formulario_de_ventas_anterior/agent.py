# agent.py

from google.adk.agents import Agent
from .tools.registro_sheet import registrar_interes_en_sheet
from .tools.notificacion_email import enviar_correo_bienvenida

# Información sobre los libros que el agente usará para generar los correos.
# Esta información podría venir de una base de datos o una búsqueda en el futuro.
INFORMACION_LIBROS = {
    "Libros de Literatura": {
        "nombre_completo": "Libros de Literatura",
        "descripcion": """
        Colección de novelas, cuentos y obras clásicas y contemporáneas que permiten al lector 
        disfrutar de historias, personajes y estilos narrativos diversos. Ideal para quienes 
        disfrutan de la lectura recreativa y el análisis literario.
        """
    },
    "Libros Académicos": {
        "nombre_completo": "Libros Académicos",
        "descripcion": """
        Material de apoyo para estudios universitarios y profesionales, que incluye textos de 
        referencia, manuales y guías especializadas en distintas áreas del conocimiento. Pensado 
        para estudiantes y docentes que requieren contenido profundo y actualizado.
        """
    },
    "Útiles Escolares": {
        "nombre_completo": "Útiles Escolares",
        "descripcion": """
        Artículos básicos para el trabajo en el aula, como cuadernos, esferográficos, marcadores, 
        reglas y demás materiales necesarios para el día a día de estudiantes de escuela y colegio.
        """
    },
    "Material de Oficina": {
        "nombre_completo": "Material de Oficina",
        "descripcion": """
        Insumos utilizados en entornos laborales y administrativos, como carpetas, archivadores, 
        hojas, organizadores y accesorios que facilitan la gestión de documentos y tareas diarias.
        """
    },
    "Libros Infantiles": {
        "nombre_completo": "Libros Infantiles",
        "descripcion": """
        Libros ilustrados y cuentos dirigidos a niños y niñas, diseñados para fomentar el hábito 
        de la lectura desde edades tempranas mediante historias sencillas, coloridas y educativas.
        """
    },
}


root_agent = Agent(
    name="RegistrationAgent",
    model="gemini-2.5-flash",
    description="Agente para registrar el interés de usuarios en libros de la biblioteca Liberty .",
    tools=[
        registrar_interes_en_sheet,
        enviar_correo_bienvenida,
    ],
    instruction=f"""
      # Misión del Agente: Procesador de Registros de Libros

      Tu único objetivo es procesar el registro de un nuevo usuario utilizando tus herramientas. La petición del usuario contendrá toda la información que necesitas.

      Tu proceso debe ser:
      1.  Usa la herramienta `registrar_interes_en_sheet` para guardar la información del usuario en la hoja de cálculo. Debes llamar a esta herramienta por cada libro o categoría de interés seleccionada.  
      2.  Usa la herramienta `enviar_correo_bienvenida` para enviar una confirmación por email al usuario. El contenido del correo debe incluir una descripción del libro o libros seleccionados.
      3.  Al finalizar, responde con un breve resumen confirmando las acciones realizadas.

      Aquí tienes la información de los libros que podrías necesitar para el correo:
      - Libros de Literatura: {INFORMACION_LIBROS['Libros de Literatura']['descripcion']}
      - Libros Académicos: {INFORMACION_LIBROS['Libros Académicos']['descripcion']}
      - Útiles Escolares: {INFORMACION_LIBROS['Útiles Escolares']['descripcion']}
      - Material de Oficina: {INFORMACION_LIBROS['Material de Oficina']['descripcion']}
      - Libros Infantiles: {INFORMACION_LIBROS['Libros Infantiles']['descripcion']}
   """,
)