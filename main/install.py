import subprocess, os

def find_path():
	raw_command = subprocess.check_output(['pip', 'show', 'requests']).decode('utf-8').split('\n')
	for i in raw_command:
		if i[0:8] == 'Location':
			return i[10:].strip()

path = find_path()
os.system(f'move imgc.py {path}')
print('Installed')