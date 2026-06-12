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
2. Cada respuesta asigna points a cada una de las casas (a tu elección).
3. Una vez finalizado, el sombrero indica el nombre del alumno
   y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria, 
   pero indicándole al alumno que la decisión ha sido complicada).


'''
import random

class start:
    def __init__(self):
        name = input("Introduce tu nombre")



class questions:
    questions_list = [
    {
        "question": "¿Cuál es tu framework favorito?",
        "answers": [
            {"text": "Angular", "house": "Front"},
            {"text": "Django", "house": "Back"},
            {"text": "Flutter", "house": "Mobile"},
            {"text": "Redis", "house": "Data"}
        ]
    }, 
    {
    "question": "¿En qué te centras más en tu trabajo?",
        "answers": [
            {"text": "Me gusta gestionar la experiencia del usuario en pantalla", "house": "Front"},
            {"text": "Me centro en la lógica del negocio", "house": "Back"},
            {"text": "Creo aplicaciones nativas o híbridas", "house": "Mobile"},
            {"text": "Me gusta la velocidada en la recuperación de datos", "house": "Data"}
        ]
    }, 
    {"question": "¿Qué no puede faltar ningún día en tu trabajo?",
        "answers": [
            {"text": "Documen Objetc Model", "house": "Front"},
            {"text": "Endpints", "house": "Back"},
            {"text": "Control de notificaciones push", "house": "Mobile"},
            {"text": "Normalización de datos", "house": "Data"}
        ]
    },
    {"question": "¿Cuál es tu entorno de ejecución principal?",
        "answers": [
            {"text": "El navegador web (Chrome, Firefox, Safari)", "house": "Front"},
            {"text": "Un servidor remoto o VPS en la nube", "house": "Back"},
            {"text": "El procesador y la memoria de un smartphone", "house": "Mobile"},
            {"text": "Un sistema de almacenamiento en disco optimizado", "house": "Data"}
        ]
    },
    {"question": "¿Qué herramienta o IDE abres casi por obligación al empezar el día?",
        "answers": [
            {"text": "Chrome DevTools para inspeccionar elementos", "house": "Front"},
            {"text": "Chrome DevTools para inspeccionar elementos", "house": "Back"},
            {"text": "Android Studio o Xcode para emular dispositivos", "house": "Mobile"},
            {"text": "DBeaver o pgAdmin para lanzar consultas", "house": "Data"}
        ]
    },
    {"question": "Si tuvieras que elegir una de estas tecnologías como tu fuerte, ¿cuál sería?",
        "answers": [
            {"text": "Tailwind CSS y empaquetadores como Vite", "house": "Front"},
            {"text": "FastAPI, Node.js o contenedores Docker", "house": "Back"},
            {"text": "Swift, Kotlin o entornos híbridos como React Native", "house": "Mobile"},
            {"text": "PostgreSQL, MySQL o bases NoSQL como MongoDB", "house": "Data"}
        ]
    },
    {"question": "¿Qué concepto dominas a la perfección en tu día a día?",
        "answers": [
            {"text": "Media Queries y diseño adaptable (Responsiveness)", "house": "Front"},
            {"text": "Autenticación por tokens (JWT) y seguridad de accesos", "house": "Back"},
            {"text": "El ciclo de vida de una App (Segundo plano y suspensión)", "house": "Mobile"},
            {"text": "Transacciones seguras y propiedades ACID", "house": "Data"}
        ]
    },
    {"question": "¿Cuál de estos problemas te daría más dolor de cabeza solucionar?",
        "answers": [
            {"text": "Que un botón no renderice bien en la pantalla de un iPhone", "house": "Front"},
            {"text": "Un error de CORS o variables de entorno del servidor corruptas", "house": "Back"},
            {"text": "Que denieguen la actualización de la app en la Google Play o App Store", "house": "Mobile"},
            {"text": "Una consulta lenta que bloquee las tablas por falta de indexación", "house": "Data"}
        ]
    }, 
    {"question": "¿Qué tarea te resulta más satisfactoria completar?",
        "answers": [
            {"text": "Almacenar datos en LocalStorage y ver la interfaz fluida", "house": "Front"},
            {"text": "Programar tareas en segundo plano (cron jobs) automatizadas", "house": "Back"},
            {"text": "Integrar el acceso nativo a la cámara o la huella dactilar", "house": "Mobile"},
            {"text": "Diseñar relaciones complejas mediante claves primarias y foráneas", "house": "Data"}
        ]
    },
    {"question": "Tu mayor orgullo como profesional sería lograr...",
        "answers": [
            {"text": "Una web interactiva idéntica al diseño que se adapta a cualquier pantalla", "house": "Front"},
            {"text": "Una arquitectura robusta capaz de procesar miles de compras encriptadas", "house": "Back"},
            {"text": "Una aplicación ligera instalada en millones de dispositivos móviles", "house": "Mobile"},
            {"text": "Una base de datos estructurada que escupe millones de registros en milisegundos", "house": "Data"}
        ]
    }
    ]

    def show_cuestion(self):
        pass

class start_playing:
    def __init__(self):
        print("Bienvenido a la escuela de programación.")

    def start_questions(self):
        answers_list = []
        front_count = 0
        back_count = 0
        mobile_count = 0
        data_count = 0

        for i, element in enumerate(questions.questions_list, start=1):
            my_list = [0, 1, 2, 3]
            random.shuffle(my_list)
            print(f"{i}. {element.get("question")}")
            print(f"A) {element.get("answers")[my_list[0]].get("text")}")
            print(f"B) {element.get("answers")[my_list[1]].get("text")}")
            print(f"C) {element.get("answers")[my_list[2]].get("text")}")
            print(f"D) {element.get("answers")[my_list[3]].get("text")}")
            print()
            answer = input("Introduce una opción: ")
            answer = answer.upper()
            match answer:
                case "A":
                    answers_list.append(element.get("answers")[my_list[0]].get("house"))
                case "B":
                    answers_list.append(element.get("answers")[my_list[1]].get("house"))
                case "C":
                    answers_list.append(element.get("answers")[my_list[2]].get("house"))
                case "D":
                    answers_list.append(element.get("answers")[my_list[3]].get("house"))
                case _:
                    print("No se ha respondido correctamente, no se valorará la pregunta. ")
        #print(answers_list)
        for element in answers_list:
            match element:
                case "Front":
                    front_count += 1
                case "Back":
                    back_count += 1
                case "Mobile":
                    mobile_count += 1
                case "Data":
                    data_count += 1
                case _:
                    pass
        # py Guardamos los resultados mapeados en un diccionario para no perder el rastro de quién es quién
        scores = {
            "Front": front_count,
            "Back": back_count,
            "Mobile": mobile_count,
            "Data": data_count
        }

        # 1. Obtenemos la puntuación más alta
        max_puntuation = max(scores.values())

        # 2. Buscamos qué casas tienen esa puntuación máxima (por si hay empates)
        winners = [house for house, points in scores.items() if points == max_puntuation]

        # 3. Evaluamos el resultado final
        if len(winners) > 1:
            # Si hay más de un ganador en la lista, es un empate
            # " , ".join(winners) junta los nombres bonitos, por ejemplo: "Front y Back"
            print(f"¡Tenemos un empate técnico entre: {' y '.join(winners)} con {max_puntuation} points!")
        else:
            # Si solo hay uno, mostramos el ganador absoluto
            ganador_unico = winners[0]
            
            match ganador_unico:
                case "Front":
                    print(f"¡Front gana con {max_puntuation} puntos!")
                case "Back":
                    print(f"¡Back gana con {max_puntuation} puntos!")
                case "Mobile":
                    print(f"¡Mobile gana con {max_puntuation} puntos!")
                case "Data":
                    print(f"¡Data gana con {max_puntuation} puntos!")
            
            



questions()
start_playing().start_questions()

'''
        "question": "¿Cuál es tu framework favorito?",
        "answers": [
            {"text": "Angular", "house": "Front"},
            {"text": "Django", "house": "Back"},
            {"text": "Flutter", "house": "Mobile"},
            {"text": "Redis", "house": "Data"}
        ],
'''