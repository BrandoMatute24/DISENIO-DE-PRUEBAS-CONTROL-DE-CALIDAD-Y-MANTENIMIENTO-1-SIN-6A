# Por Brando Matute

from locust import HttpUser, task, between

class MiUsuario(HttpUser):
    wait_time = between(1, 3)

    @task
    def cargar_pagina_principal(self):
        self.client.get("/")
