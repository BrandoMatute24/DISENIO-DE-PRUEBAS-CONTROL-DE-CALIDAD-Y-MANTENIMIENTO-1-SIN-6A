import asyncio
import pytest

class TradingSystem:
    def __init__(self):
        self.state = "sin_orden"
        self.log = []

    async def buy(self):
        # La orden sale primero (menos latencia)
        await asyncio.sleep(0.2)
        self.state = "orden_pendiente"
        self.log.append("Orden enviada")

    async def cancel(self):
        # La cancelación llega después (más latencia)
        await asyncio.sleep(0.5)
        if self.state == "orden_pendiente":
            self.state = "cancelada"
        else:
            self.state = "sin_orden"
        self.log.append("Cancelación procesada")

@pytest.mark.asyncio
async def test_eventos_asincronos():
    sistema = TradingSystem()
    t1 = asyncio.create_task(sistema.buy())
    t2 = asyncio.create_task(sistema.cancel())
    await asyncio.gather(t1, t2)

    # A pesar del orden/latencia, el estado final NO debe quedar inconsistente
    assert sistema.state in ["sin_orden", "cancelada"]
    assert "Cancelación procesada" in sistema.log
