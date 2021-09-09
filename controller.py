def GiveLayout():
	import json
	with open('settings.json', 'r') as file:
		data = json.load(file)
		return data['layout']

def GiveMainClockFont():
	import json
	with open('settings.json', 'r') as file:
		data = json.load(file)
	word = data['font-clock-main']
	temp = ''
	for a in range(len(word)):
		if a == 0 or a == len(word)-1:
			pass
		else:
			temp += word[a]
	return temp

import json
with open('settings.json', 'r') as file:
	data = json.load(file)
word = data['font-clock-main']
temp = ''
for a in range(len(word)):
	if a == 0 or a == len(word)-1:
		pass
	else:
		temp += word[a]
print(temp)

def Convert(hours, minutes, seconds):
	# these two if statements are executed to convert the times in the correct form
	# eg if seconds == 3600 then hour ==1 and minutes, seconds are reduced to 0
	if seconds >= 60:
		temp = seconds // 60
		seconds = seconds % 60
		minutes += temp
	if minutes >= 60:
		temp = minutes // 60
		minutes = minutes % 60
		hours += temp

	# these two if statements does not allow for minutes and seconds to be of length 1
	seconds = str(seconds); minutes = str(minutes); hours = str(hours)
	if len(seconds) == 1:
		seconds = '0' + seconds
	if len(minutes) == 1:
		minutes = '0' + minutes

	return hours, minutes, seconds