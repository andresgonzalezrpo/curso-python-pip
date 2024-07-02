# python app/reto.py
# []
import read_csv

data = read_csv.read_csv('./app/data.csv')

country = list(filter(lambda item: item['Country/Territory'] == 'Colombia', data ))

dict_country = country[0]


result = {key: value for (key, value) in dict_country.items() if key in ['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population']}

#unique = {c: c.upper() for c in text if c in 'aeiou'}
print(result)
