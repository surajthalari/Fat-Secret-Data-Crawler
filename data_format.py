import json
import pandas as pd

df = pd.read_csv('trail.csv')

foodDetails = pd.DataFrame(columns=['foodId', 'label', 'category', 'categoryLabel'])

nutrientDetails =pd.DataFrame(columns=['foodId','servingId','metricServingAmount', 'numberOfUnits', 'measurementDescription', 'servingDescription', 'Energy (value)', 'Energy (unit)', 'Fat (value)', 'Fat (unit)', 'Saturated Fat (value)', 'Saturated Fat (unit)', 'Monounsaturated Fat (value)', 'Monounsaturated Fat (unit)', 
'Polyunsaturated Fat (value)', 'Polyunsaturated Fat (unit)', 'Carbs (value)', 'Carbs (unit)', 'Fiber (value)', 'Fiber (unit)', 'Sugars (value)', 'Sugars (unit)', 'Protein (value)', 'Protein (unit)',
'Cholesterol (value)', 'Cholesterol (unit)', 'Sodium (value)', 'Sodium (unit)', 'Calcium (value)', 'Calcium (unit)', 'Magnesium (value)', 'Magnesium (unit)', 'Potassium (value)', 'Potassium (unit)',
'Iron (value)', 'Iron (unit)', 'Zinc (value)', 'Zinc (unit)', 'Phosphorus (value)', 'Phosphorus (unit)', 'Vitamin A (value)', 'Vitamin A (unit)', 'Vitamin C (value)', 'Vitamin C (unit)',
'Thiamin B1 (value)', 'Thiamin B1 (unit)', 'Riboflavin B2 (value)', 'Riboflavin B2 (unit)', 'Niacin B3 (value)', 'Niacin B3 (unit)', 'Vitamin B6 (value)', 'Vitamin B6 (unit)', 'Folate equivalent (total)(value)', 'Folate equivalent (total)(unit)',
'Folate (value)', 'Folate (unit)', 'Folic acid (value)', 'Folic acid (unit)', 'Vitamin B12 (value)', 'Vitamin B12 (unit)', 'Vitamin D (value)', 'Vitamin D (unit)', 'Vitamin E (value)', 'Vitamin E (unit)',
'Vitamin K (value)', 'Vitamin K (unit)', 'Water (value)', 'Water (unit)'])

i=0
for index, row in df.iterrows():
        each_item = json.loads(row.to_json())
        foodDetails.loc[i] = [each_item.get('food_id', None), each_item.get('food_name', None), each_item.get('food_type', None), each_item.get('brand_name', None)] 
        nutrientDetails.loc[i] = [each_item.get('food_id', None), each_item.get('serving_id', None),each_item.get('metric_serving_amount', None),each_item.get('number_of_units', None), each_item.get('measurement_description', None), each_item.get('serving_description', None), each_item.get('calories', None), 'calories', each_item.get('fat', None), 'g', each_item.get('saturated_fat', None), 'g', each_item.get('monounsaturated_fat', None), 'g', 
        each_item.get('polyunsaturated_fat', None), 'g', each_item.get('carbohydrate', None), 'g', each_item.get('fiber', None), 'g', each_item.get('sugar', None), 'g', each_item.get('protein', None), 'g',
        each_item.get('cholesterol', None), 'mg', each_item.get('sodium', None), 'mg', each_item.get('calcium', None), 'mg', each_item.get('magnesium', None), 'mg', each_item.get('potassium', None), 'mg',
        each_item.get('iron', None), 'mg', each_item.get('zinc', None), 'mg', each_item.get('phosphorus', None), 'mg', each_item.get('vitamin_a', None), 'mg', each_item.get('vitamin_c', None), 'mg',
        each_item.get('thiamin_b1', None), 'mg', each_item.get('riboflavin_b2', None), 'mg', each_item.get('niacin_b3', None), 'mg', each_item.get('vitamin_b6', None), 'mg', each_item.get('folate_equivalent', None), 'mg',
        each_item.get('folate', None), 'mg', each_item.get('folic_acid', None), 'mg', each_item.get('vitamin_b12', None), 'mg', each_item.get('vitamin_d', None), 'mg', each_item.get('vitamin_e', None), 'mg',
        each_item.get('vitamin_k', None), 'mg', each_item.get('water', None), 'g']
        i=i+1
    
foodDetails.to_excel('food_details.xlsx')
nutrientDetails.to_excel('nutrientDetails.xlsx')
