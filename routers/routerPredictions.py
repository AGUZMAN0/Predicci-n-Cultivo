import pickle
from fastapi import APIRouter
import numpy as np
from interfaces import DataCultivo


router=APIRouter()

with open("svcPredict2.pkl", "rb")as file:
    model=pickle.load(file)



@router.post("/Cultivo")
def predict(data:DataCultivo):
    data = data.model_dump()

    N=data["N"]
    P=data["P"]
    K=data["K"]
    temperature=data["temperature"]
    humidity=data["humidity"]
    ph=data["ph"]
    rainfall=data["rainfall"]


    xin = np.array([N,P,
                    K,temperature,
                    humidity,ph,rainfall]).reshape(1,7)
    
    prediction = model.predict(xin)

   
    print("prediction","LISTO")
    return{"prediction": prediction[0]}
