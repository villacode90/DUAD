import csv


video_game__list = [
	{
		'Nombre': 'Grand Theft Auto IV',
		'Genero': 'Acción',
		'Desarrollador': 'RockStar Games',
		'Clasificación ESEB': 'M',
	},
	{
		'Nombre': 'The Elder Scrolls IV: Oblivion',
		'Genero': 'RPG',
		'Desarrollador': 'Bethesda',
		'Clasificación ESEB': 'M',
	},
	{
		'Nombre': 'Tony Hawk´s',
		'Genero': 'Deportes',
		'Desarrollador': 'Activision',
		'Clasificación ESEB': 'T',
	},
]

general_headers = (
	'Nombre',
	'Genero',
	'Desarrollador',
	'Clasificación ESEB',
)

def write_csv_file(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, headers)
    writer.writeheader()
    writer.writerows(data)

write_csv_file('./videoGames.csv', video_game__list, general_headers)