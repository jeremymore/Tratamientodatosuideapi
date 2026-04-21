from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

devices = []

class Device(BaseModel):
    id: int
    name: str
    type: str
    brand: str
    status: str

@app.get("/")
def home():
    return {"message": "API Inventario activa"}

# 📋 Ver dispositivos
@app.get("/devices", response_model=List[Device])
def get_devices():
    return devices

# ➕ Agregar dispositivo
@app.post("/devices")
def add_device(device: Device):
    # evitar IDs duplicados
    for d in devices:
        if d.id == device.id:
            raise HTTPException(status_code=400, detail="ID ya existe")

    devices.append(device)
    return device

# 🔄 Actualizar estado
@app.put("/devices/{device_id}")
def update_device(device_id: int, status: str):
    for d in devices:
        if d.id == device_id:
            d.status = status
            return d

    raise HTTPException(status_code=404, detail="Dispositivo no encontrado")

# ❌ Eliminar dispositivo
@app.delete("/devices/{device_id}")
def delete_device(device_id: int):
    for d in devices:
        if d.id == device_id:
            devices.remove(d)
            return {"message": "Dispositivo eliminado"}

    raise HTTPException(status_code=404, detail="No encontrado")

# 📊 Conteo por tipo
@app.get("/devices/count")
def count_devices():
    result = {}
    for d in devices:
        result[d.type] = result.get(d.type, 0) + 1
    return result