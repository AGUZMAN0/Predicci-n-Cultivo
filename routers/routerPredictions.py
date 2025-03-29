import pickle
from fastapi import APIRouter
import numpy as np
from interfaces import DataDiabetes


router=APIRouter()

with open("RFDiabetesv132.pkl", "rb")as file:
    model=pickle.load(file)


label = ['Pesona Enferma', 'Persona Sana']



@router.post("/predict")
def predict(data:DataDiabetes):
    data = data.model_dump()
    
    Pregnancies=data["Pregnancies"]
    Glucose=data["Glucose"]
    BloodPressure=data["BloodPressure"]
    SkinThickness=data["SkinThickness"]
    Insulin=data["Insulin"]
    BMI=data["BMI"]
    DiabetesPedigreeFunction=data["DiabetesPedigreeFunction"]
    Age=data["Age"]

    xin = np.array([Pregnancies,Glucose,
                    BloodPressure,SkinThickness,
                    Insulin,BMI,DiabetesPedigreeFunction,Age]).reshape(1,8)
    
    prediction = model.predict(xin)

   
    print("prediction",label[prediction[0]])
    return{"prediction": label[prediction[0]]}
