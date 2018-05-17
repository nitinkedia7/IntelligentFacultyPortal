import re

def mailscan(mail):
	info = {}
	subject = mail['subject']
	for word in subject.split():
		if "paper" in word:
			info['type'] = 'journal'
			break
		elif "designation" in word:
			info['type'] = 'promotion'
			break
		elif "responsibility" in word:
			info['type'] = 'adminres'
			break
		elif "Project" in word:
			info['type'] = 'project'
			break
		else:
			info['type'] = 'none'
		
	content = mail['body']
	words = re.findall('"([^"]*)"', str(content))
	if info['type'] == 'journal':			
		info['title'] = words[0]
		info['contrib'] = words[1]
		info['paper'] = words[2]
	elif info['type'] == 'promotion':			
		info['designation'] = words[0]
	elif info['type'] == 'adminres':
		info['responsibility'] = words[0]
		info['from'] = words[1]
	elif info['type'] == 'project':
		info['sponsor'] = words[0]
		info['title'] = words[1]
		info['budget'] = words[2]
		info['role'] = words[3]
	return info