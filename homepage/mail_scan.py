import re

def mailscan():
	info = {}
	with open("mail.txt", 'r', encoding='utf-8') as mail:
		subject = mail.readline()
		for word in subject.split():
			if "paper" in word:
				info['type'] = 'journal'
			elif "designation" in word:
				info['type'] = 'promotion'
			else:
				info['type'] = 'none'
		
		content = mail.readlines()
		words = re.findall('"([^"]*)"', str(content))
		if info['type'] == 'journal':			
			info['title'] = words[0]
			info['paper'] = words[1]
		elif info['type'] == 'promotion':			
			info['designation'] = words[0]
			info['from'] = words[1]
		return info