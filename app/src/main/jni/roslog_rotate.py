#log_dir.py
import os
import time
from pprint import pprint

def get_logrotate_conf(path):
	current_files = os.listdir(path)
	content = ''
	for file_name in current_files:
		pprint(file_name)
		olddir = '/data/media/0/ros/log_old/' + file_name;
		if os.path.exists(olddir) == False:
			os.mkdir(olddir)

		content = content + os.path.join(path, file_name, '*')
		content = content + '{ \n'
		content = content + '    hourly\n'
		content = content + '    rotate 5\n'
		content = content + '    olddir ' + olddir + '\n'
		content = content + '    nocompress\n'
		content = content + '} \n'

	return content

def write_conf(path, content):
	file_object = open(path, 'w')
	file_object.write(content)
	file_object.close


now_time = time.time()
last_time = 0
while True:
	if (now_time - last_time) > 3600:
		conf = get_logrotate_conf('/data/media/0/ros/log')
		write_conf('logrotate.conf', conf)
		os.system('log_rotate logrotate.conf')
		last_time = now_time
	now_time = time.time()