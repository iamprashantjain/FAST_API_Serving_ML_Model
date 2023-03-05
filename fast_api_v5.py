import uvicorn
import joblib
import pandas as pd

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class FourW(BaseModel):
    MAKE_YEAR: int
    Make_Clean: str
    Model_Clean: str
    Variant_Clean: str
    Fuel_Clean: str
    CV_State_Clean: str
    SELLER_SEGMENT: str
    METERREADING: float


app = FastAPI()


@app.get("/")
def read_root():
    return {"Predict": "Price Prediction Tool"}


@app.post("/predict")
def predict(fourw: FourW):

    model_pkl_file = "Final_4W_CS.pkl"
    model_rf = joblib.load(model_pkl_file)

    # Create a pandas dataframe and select the features the current model expects
    input_data = pd.DataFrame([[fourw.MAKE_YEAR, 
                                fourw.Make_Clean, 
                                fourw.Model_Clean,
                                fourw.Variant_Clean,
                                fourw.Fuel_Clean,
                                fourw.CV_State_Clean,
                                fourw.SELLER_SEGMENT,
                                fourw.METERREADING]], 
                              columns=['MAKE_YEAR','Make_Clean','Model_Clean','Variant_Clean','Fuel_Clean','CV_State_Clean','SELLER_SEGMENT','METERREADING'])
    
    prediction = model_rf.predict(input_data)

    # Cast the prediction to int
    prediction = int(prediction[0])
    return {"predicted price": prediction}


if __name__ == "__main__":
    uvicorn.run(app, reload = True)




#add vehicle category to validate before proceeding
#add multi model
#research how     