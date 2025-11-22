import requests

url = 'http://127.0.0.1:8000/predict'

data = {
    "experience_level_encoded": 3.0,
    "company_size_encoded": 3.0,
    "employment_type_PT": 0,
    "job_title_Data_Engineer": 0,
    "job_title_Data_Manager": 1,
    "job_title_Data_Scientist": 0,
    "job_title_Machine_Learning_Engineer": 0
}

# Hacer la petición POST
response = requests.post(url, json=data)

# Mostrar la respuesta
print(response.json())