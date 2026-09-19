import csv
import os

TODOS_FILE = "todos.csv"

todo = []


def load_todos():
    todo.clear()
    if not os.path.exists(TODOS_FILE):
        return
    with open(TODOS_FILE, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                todo.append(row[0])


def save_todos():
    with open(TODOS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for title in todo:
            writer.writerow([title])


def add_one_task(title):
    title = title.strip()
    if not title:
        print("La tarea no puede estar vacía.")
        return
    todo.append(title)
    save_todos()
    print(f"Tarea agregada: {len(todo)} - {title}")


def print_list():
    if not todo:
        print("No hay tareas.")
        return
    for index, title in enumerate(todo, start=1):
        print(f"{index}. {title}")


def delete_task(number_to_delete):
    try:
        index = int(number_to_delete) - 1
        if index < 0 or index >= len(todo):
            raise IndexError
        removed = todo.pop(index)
        save_todos()
        print(f"Tarea eliminada: {removed}")
    except ValueError:
        print("Debes ingresar un número válido.")
    except IndexError:
        print("No existe una tarea con ese número.")


def menu():
    load_todos()
    while True:
        print("\n--- Menú de tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            title = input("Escribe la tarea: ")
            add_one_task(title)
        elif opcion == "2":
            print_list()
        elif opcion == "3":
            number_to_delete = input("Número de la tarea a eliminar: ")
            delete_task(number_to_delete)
        elif opcion == "4":
            save_todos()
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()