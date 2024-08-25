from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

class DataModel(BaseModel):
    data: List[str]

@app.get("/bfhl")
async def get_operation_code():
    return {"operation_code": 1}

@app.post("/bfhl")
async def post_data(request: DataModel):
    user_id = "Tanvi_Chawla_29092003"  # Replace with your actual user_id format
    email = "tanvi.chawla2021@vitstudent.ac.in"  # Replace with your actual email
    roll_number = "21BCI0025"  # Replace with your actual roll number

    numbers = []
    alphabets = []
    highest_lowercase_alphabet = None

    for item in request.data:
        if isinstance(item, int) or item.isdigit():
            numbers.append(item)
        elif isinstance(item, str) and item.isalpha():
            alphabets.append(item)
            if item.islower() and (highest_lowercase_alphabet is None or item > highest_lowercase_alphabet):
                highest_lowercase_alphabet = item
    print(alphabets)
    return {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }
