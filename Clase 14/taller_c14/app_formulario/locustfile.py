from locust import HttpUser, task, between
import random

class FormularioUsuario(HttpUser):
    # Simula un tiempo de espera aleatorio entre 1 y 3 segundos entre cada acción del usuario
    wait_time = between(1, 3)

    @task(1)
    def cargar_pagina_principal(self):
        # Prueba de carga GET: Visitar/Renderizar la página principal
        self.client.get("/")

    @task(2)
    def enviar_formulario(self):
        # Prueba de carga POST: Enviar datos aleatorios simulando el registro a un evento
        eventos = ["Taller MapReduce", "Conferencia Docker", "Seminario QA"]
        num_aleatorio = random.randint(1000, 9999)
        
        datos = {
            "nombre": f"Usuario Prueba {num_aleatorio}",
            "email": f"usuario{num_aleatorio}@prueba.com",
            "evento": random.choice(eventos)
        }
        
        # Enviar los datos simulando la acción del formulario
        self.client.post("/", data=datos)
