# python app/reto2.py
import read_csv
import charts

#Country/Territory

def graph_word_population():
  data = read_csv.read_csv('./app/data.csv')

  world_population_percent = list(map(lambda item: item['World Population Percentage'], data))
  countrys = list(map(lambda item: item['Country/Territory'], data))
  
  charts.generate_pie_chart(countrys,world_population_percent)

def graph_word_population_by_continent(continent):
  data = read_csv.read_csv('./app/data.csv')
  data = list(filter(lambda item: item['Continent'] == continent, data)) 
  world_population_percent = list(map(lambda item: item['World Population Percentage'], data))
  countrys = list(map(lambda item: item['Country/Territory'], data))

  charts.generate_pie_chart(countrys,world_population_percent)
  
    

  #print (data[0])


if __name__ == '__main__': 
  #graph_word_population()
  #South America
  continent = input('Ingrese el continente: ')
  graph_word_population_by_continent(continent)
  
  
