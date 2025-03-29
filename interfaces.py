from pydantic import BaseModel


class DataCultivo(BaseModel):
    N:int
    P:int
    K:int
    temperature: float
    humidity: float
    ph: float
    rainfall: int
    
