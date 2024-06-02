import json
from llamaapi import LlamaAPI

llama = LlamaAPI("LL-mg9vpjm8fvbiJgzhVVq4MtDZjBtJyHLwTQaU5NcEwBJNnF98rhc9aXMDAo0V92KY")

def fetch_recommendation(prompt):
    api_request_json = {
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    response = llama.run(api_request_json)
    response_json = response.json()

    if "choices" in response_json:
        return response_json["choices"][0]["message"]["content"]
    return None


def get_plant_care_recommendation(temperature, humidity, sunlight):
    temp_prompt = f"The temperature is {temperature}°C. Should i move my plant in a different environment?  Answer briefly (maximum 15 words)."
    humidity_prompt = f"The humidity is {humidity}%. Should i water my plant?  Answer briefly (maximum 15 words)."
    sunlight_prompt = f"The sunlight is {sunlight} lux. Should i move the plant closer to sunlight. Answer briefly (maximum 15 words)."

    temp_recommendation = fetch_recommendation(temp_prompt)
    humidity_recommendation = fetch_recommendation(humidity_prompt)
    sunlight_recommendation = fetch_recommendation(sunlight_prompt)


    recommendations = [
        f"Temperature: {temp_recommendation}",
        f"Humidity: {humidity_recommendation}",
        f"Sunlight: {sunlight_recommendation}"
    ]

    return " ".join(recommendations) or "No recommendation available."
