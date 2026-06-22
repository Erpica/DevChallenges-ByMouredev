import logging
import time

logging.basicConfig(level=logging.DEBUG, # Esto es el nivel de error que quiero imprimir: mucho al principio y menos en producción
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[logging.StreamHandler()])

logging.debug("Esto es un mensaje de DEBUG")
logging.info("Esto es un mensaje de INFO")
logging.warning("Esto es un mensaje de WARNING")
logging.error("Esto es un mensaje de ERROR")
logging.critical("Esto es un mensaje de CRITICAL")
print("\n\n")

# EXTRA
class TaskManager:

    def __init__(self) -> None:
        self.tasks = {}

    def add_task(self, name: str, description: str):
        start_time = time.time()
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info(f"Tarea añadida: {name}")
        else:
            logging.warning(f"Se ha intentado añadir una tarea que ya existe: {name}")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def delete_task(self, name: str):
        start_time = time.time()
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"Tarea eliminada: {name}")
        else:
            logging.warning(f"Se ha intentado eliminar una tarea que no existe: {name}")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def list_tasks(self):
        start_time = time.time()
        if self.tasks:
            logging.info(f"Se va a imprimir la línea de tareas")
            for name, description in self.tasks.items():
                print(f"{name} - {description}")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def _print_time(self, start_time, end_time):
        logging.debug(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos.")


task_manager = TaskManager()
task_manager.add_task("Pan", "Comprar 2 barras de pan")
task_manager.add_task("Python", "Estudiar Python")

task_manager.list_tasks()
task_manager.delete_task("Python")
task_manager.list_tasks()
task_manager.delete_task("Pica")