import json


sample_json = """
{
    "company": {
        "employee": {
            "name": "Emma",
            "payable": {
                "salary": 7000,
                "bonus": 800
            }
        }
    }
}
"""


data = json.loads(sample_json)

salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

data["company"]["employee"]["birth_date"] = "2003-12-25"

with open("modif_sample.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file saved successfully.")