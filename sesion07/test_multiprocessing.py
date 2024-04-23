import multiprocessing
import time

def task(i):
    print(f"Iniciando la tarea {i}")

    import pymssql

    conn = pymssql.connect("3.93.192.216", "test_curso", "TestCurso$123", "test_curso")

    cursor = conn.cursor()

    cursor.execute("select top(1) id, nombre, precio from frutas order by newid()")

    fruta = cursor.fetchone()

    cursor.close()

    conn.close()

    fruta = { "id": fruta[0], "nombre": fruta[1], "precio": fruta[2] }

    with open(f"task_{i}_result.txt", "w") as file:
        import json
        file.write(json.dumps(fruta))
        print(f"Task {i} ready")
    
    print("Esperando finalizar la tarea...")
    time.sleep(2)

# IMPORTANTE!!!!
if __name__ == "__main__":
    process = []

    for i in range(120):
        p = multiprocessing.Process(target=task, args=(i,))
        p.start()

    for p in process:
        p.join()

    print("Todas las tareas han finalizado")

