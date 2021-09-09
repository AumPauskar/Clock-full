def GiveLayout():
	import json
	with open('settings.json', 'r') as file:
		data = json.load(file)
		return data['layout']