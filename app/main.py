import utils
import read_csv
import charts
# python app/main.py

user_options = ('population_by_country', 'population_by_continent' ,'word_population')


def run(option):

  data = read_csv.read_csv('data.csv')
  
  if option == 'population_by_country':
    country = input('Type country => ')    
    result = utils.population_by_country(data, country)
    if len(result) > 0:
      country_dict = result[0]      
      labels, values = utils.get_population(country_dict)      
      charts.generate_bar_chart(country,labels,values)
    else:
      print('Country not found') 
      
  elif option == 'population_by_continent':
    continent = input('Ingrese el continente: ')
    result = utils.population_by_continent(data, continent)
    world_population_percent = list(map(lambda item: item['World Population Percentage'], result))   
    countrys = list(map(lambda item: item['Country/Territory'], result))
    charts.generate_pie_chart(continent,countrys,world_population_percent)

  elif option == 'word_population':
    world_population_percent = list(map(lambda item: item['World Population Percentage'], data))
    countrys = list(map(lambda item: item['Country/Territory'], data))
    charts.generate_pie_chart(countrys,world_population_percent)

  
if __name__ == '__main__': # Esto es para que se ejecute como script #cuando lo llamemos desde la terminal
  print(user_options)
  
  while True:
    option = input('Select an option => ')    
    
    if option not in user_options:
      print('Invalid option')
      continue
    else:
      run(option)
      
    