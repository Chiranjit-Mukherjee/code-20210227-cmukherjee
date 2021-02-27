from bmi_index import process_bmi
import json


def test_function():
	json_string = 	[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
					{ "Gender": "Male", "HeightCm": 161, "WeightKg":85 }, 
					{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, 
					{ "Gender": "Female", "HeightCm": 166,"WeightKg": 62}, 
					{"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, 
					{"Gender": "Female","HeightCm": 167, "WeightKg": 82},
					{"Gender": "Female","HeightCm": 130, "WeightKg": 95},
					{"Gender": "Female","HeightCm": 145, "WeightKg": 92},
					{"Gender": "Female","HeightCm": 140, "WeightKg": 40},
					{"Gender": "Female","HeightCm": 140, "WeightKg": 35},
					{"Gender": "Female","HeightCm": 167, "WeightKg": 45}]

	file_name = "sample.json"

	with open(file_name, "w") as out_file:
		json.dump(json_string, out_file)


	response = process_bmi(file_name, None)

	# print("response : ", response)

	if response == 3:
		print("The test result is : success")
	else:
		print("The test result is : failed")
		

if __name__ == "__main__":
	test_function()