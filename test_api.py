import requests
import pdb

URL = "http://127.0.0.1:8000/predict"

states_in_india = ['ANDHRAPRADESH', 'ARUNACHALPRADESH', 'ASSAM', 'BIHAR', 'CHHATTISGARH', 'GOA', 'HARYANA', 'HIMACHALPRADESH', 'JHARKHAND', 'KARNATAKA', 'KERALA', 'MADHYAPRADESH', 'MAHARASHTRA', 'MANIPUR', 'MEGHALAYA', 'MIZORAM', 'NAGALAND', 'ODISHA', 'PUNJAB', 'RAJASTHAN', 'SIKKIM', 'TAMILNADU', 'TELANGANA', 'TRIPURA', 'UTTARPRADESH', 'UTTARAKHAND', 'WESTBENGAL']

for i in states_in_india:
    try:
        car = {
        'MAKE_YEAR':2010,
        'Make_Clean':'ASHOKLEYLAND',
        'Model_Clean':'STILE',
        'Variant_Clean':'LE7STR',
        'Fuel_Clean':'DIESEL',
        'CV_State_Clean':i,
        'SELLER_SEGMENT':'RETAIL',
        'METERREADING': 100.00
    }


        response = requests.post(URL, json=car)
        prediction = response.json()
        print(f"Car price prediction in {i}: ", prediction)

    except:
        print("Error Occured")