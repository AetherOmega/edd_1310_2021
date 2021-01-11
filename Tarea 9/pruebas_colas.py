from colas import Queue,BoundedPriorityQueue,PriorityQueue

q1 = Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)

print (q1.to_string())

print("Prueba 2 de Queue")
c1 = {"id":1, "nombre": "Mario", "balance": 20.5}
c2 = {"id":2, "nombre": "Diana", "balance": 3456.5}
c3 = {"id":3, "nombre": "Fernando", "balance": 100000.0}

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
siguiente = atencion.dequeue()
print(f"Bienvenido sr.{siguiente['nombre']},¿en que podemos servirle el dia de hoy?")


print("Prueba de colas con prioridad acotada")
maestres = {"prioridad":4, "descripcion":"Maestre", "personas": ["Juan P", "Diego H"]}
niños = {"prioridad":2, "descripcion":"Niños", "personas": ["Santi H", "Angel H"]}
mecanicos = {"prioridad":4, "descripcion":"Mecanicos", "personas": ["Diana P", "Maria Z"]}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'], maestres)
cpa.enqueue(niños['prioridad'], niños)
cpa.enqueue(mecanicos['prioridad'], mecanicos)
cpa.to_string()


print("TAREA: Prueba de colas con prioridad ")
m = PriorityQueue()

m.enqueue(100)
m.enqueue(150)
m.enqueue(20)
m.enqueue(33)
m.enqueue(80)
m.enqueue(2)
print(m.to_string())
while not m.is_empty():
        print(m.dequeue())
