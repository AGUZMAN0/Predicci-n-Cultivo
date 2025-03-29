from pydantic import BaseModel

class dataTest(BaseModel):
    nombre: str
    estudiantes:float

class DataDiabetes(BaseModel):
    Pregnancies: int
    Glucose:int
    BloodPressure:int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: int
    Age:int
