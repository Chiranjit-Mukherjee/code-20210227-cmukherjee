import argparse
import pandas as pd
from pandas import ExcelWriter



def process_bmi(input, output): 
	try:
		df = pd.read_json(input)
	except Exception as e:
		print("Error: Specified file could not be found. Please check the file name and path")

	# calculating and storing BMI
	df['BMI'] = (df['WeightKg'] / (df['HeightCm']/100))

	# calculating and storing BMI Category
	df['BMI Category'] = df['BMI'].apply(lambda x: 'Underweight' if x <= 18.4 else \
													 "Normal weight" if x >= 18.5 and x <= 24.9 else \
													 "Overweight" if x >= 25 and x <= 29.9 else \
													 "Moderately obese" if x >= 30 and x <= 34.9 else \
													 "Severely obese" if x >= 35 and x <= 39.9 else "Very severely obese")

	# calculating and storing Health risk
	df['Health Risk'] = df['BMI'].apply(lambda x: 'Malnutrition risk' if x <= 18.4 else \
													 "Low risk" if x >= 18.5 and x <= 24.9 else \
													 "Enhanced risk" if x >= 25 and x <= 29.9 else \
													 "Medium risk" if x >= 30 and x <= 34.9 else \
													 "High risk" if x >= 35 and x <= 39.9 else "Very high risk")


	# row in which value of 'BMI' column is more than 25 and less than or equal to 29.9 (Overweight)
	seriesObj = df.apply(lambda x: True if x['BMI'] >= 25 and x['BMI'] <= 29.9 else False , axis=1)

	# Count number of True in series
	numOfRows = len(seriesObj[seriesObj == True].index)

	print("Total no of Overweight patient is : ", numOfRows)

	if output:
		if output == 'CSV':
			filename = "output.csv"
			df.to_csv(filename, index=False)
		else:
			writer = ExcelWriter('output.xlsx')
			df.to_excel(writer,'Sheet1',index=False)
			writer.save()

	return 0
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', help='input json file', required=True)
	parser.add_argument('-o', '--output',  help='output file type', choices=['CSV', 'XLS'], type=str.upper)
	args = parser.parse_args()

	response = process_bmi(args.input, args.output)