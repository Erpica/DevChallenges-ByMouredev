'''
Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
de programación de Hogwarts para magos y brujas del código.
En ella, su famoso sombrero seleccionador ayuda a los programadores
a encontrar su camino...
Desarrolla un programa que simule el comportamiento del sombrero.
Requisitos:
1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
2. Deben existir cuatro casas. Por ejemplo: Frontend, Backend, Mobile y Data.
   (Puedes elegir las que quieras)
Acciones:
1. Crea un programa que solicite el nomre del alumno y realice diez
preguntas, con cuatro posibles respuestas cada una.
2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
3. Una vez finalizado, el sombrero indica el nombre del alumno
   y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria, 
   pero indicándole al alumno que la decisión ha sido complicada).


'''

class start:
    name = input("Introduce tu nombre")



class questions:
    questions_dict = {
        "question": "¿Cuál es tu framework favorito?",
        "answers": [
            {"text": "Angular", "house": "Front"},
            {"text": "Django", "house": "Back"},
            {"text": "Flutter", "house": "Mobile"},
            {"text": "Redis", "house": "Data"}
        ],
        "question": "¿En qué te centras más en tu trabajo?",
        "answers": [
            {"text": "Me gusta gestionar la experiencia del usuario en pantalla", "house": "Front"},
            {"text": "Me centro en la lógica del negocio", "house": "Back"},
            {"text": "Creo aplicaciones nativas o híbridas", "house": "Mobile"},
            {"text": "Me gusta la velocidada en la recuperación de datos", "house": "Data"}
        ],
        "question": "¿Qué no puede faltar ningún día en tu trabajo?",
        "answers": [
            {"text": "Documen Objetc Model", "house": "Front"},
            {"text": "Endpints", "house": "Back"},
            {"text": "Control de notificaciones push", "house": "Mobile"},
            {"text": "Normalización de datos", "house": "Data"}
        ],
        "question": "¿Cuál es tu entorno de ejecución principal?",
        "answers": [
            {"text": "El navegador web (Chrome, Firefox, Safari)", "house": "Front"},
            {"text": "Un servidor remoto o VPS en la nube", "house": "Back"},
            {"text": "El procesador y la memoria de un smartphone", "house": "Mobile"},
            {"text": "Un sistema de almacenamiento en disco optimizado", "house": "Data"}
        ],
        "question": "¿Qué herramienta o IDE abres casi por obligación al empezar el día?",
        "answers": [
            {"text": "Chrome DevTools para inspeccionar elementos", "house": "Front"},
            {"text": "Chrome DevTools para inspeccionar elementos", "house": "Back"},
            {"text": "Android Studio o Xcode para emular dispositivos", "house": "Mobile"},
            {"text": "DBeaver o pgAdmin para lanzar consultas", "house": "Data"}
        ],
        "question": "Si tuvieras que elegir una de estas tecnologías como tu fuerte, ¿cuál sería?",
        "answers": [
            {"text": "Tailwind CSS y empaquetadores como Vite", "house": "Front"},
            {"text": "FastAPI, Node.js o contenedores Docker", "house": "Back"},
            {"text": "Swift, Kotlin o entornos híbridos como React Native", "house": "Mobile"},
            {"text": "PostgreSQL, MySQL o bases NoSQL como MongoDB", "house": "Data"}
        ],
        "question": "¿Qué concepto dominas a la perfección en tu día a día?",
        "answers": [
            {"text": "Media Queries y diseño adaptable (Responsiveness)", "house": "Front"},
            {"text": "Autenticación por tokens (JWT) y seguridad de accesos", "house": "Back"},
            {"text": "El ciclo de vida de una App (Segundo plano y suspensión)", "house": "Mobile"},
            {"text": "Transacciones seguras y propiedades ACID", "house": "Data"}
        ],
        "question": "¿Cuál de estos problemas te daría más dolor de cabeza solucionar?",
        "answers": [
            {"text": "Que un botón no renderice bien en la pantalla de un iPhone", "house": "Front"},
            {"text": "Un error de CORS o variables de entorno del servidor corruptas", "house": "Back"},
            {"text": "Que denieguen la actualización de la app en la Google Play o App Store", "house": "Mobile"},
            {"text": "Una consulta lenta que bloquee las tablas por falta de indexación", "house": "Data"}
        ],
        "question": "¿Qué tarea te resulta más satisfactoria completar?",
        "answers": [
            {"text": "Almacenar datos en LocalStorage y ver la interfaz fluida", "house": "Front"},
            {"text": "Programar tareas en segundo plano (cron jobs) automatizadas", "house": "Back"},
            {"text": "Integrar el acceso nativo a la cámara o la huella dactilar", "house": "Mobile"},
            {"text": "Diseñar relaciones complejas mediante claves primarias y foráneas", "house": "Data"}
        ],
        "question": "Tu mayor orgullo como profesional sería lograr...",
        "answers": [
            {"text": "Una web interactiva idéntica al diseño que se adapta a cualquier pantalla", "house": "Front"},
            {"text": "Una arquitectura robusta capaz de procesar miles de compras encriptadas", "house": "Back"},
            {"text": "Una aplicación ligera instalada en millones de dispositivos móviles", "house": "Mobile"},
            {"text": "Una base de datos estructurada que escupe millones de registros en milisegundos", "house": "Data"}
        ]
    }

