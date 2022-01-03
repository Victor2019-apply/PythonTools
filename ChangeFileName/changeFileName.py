import os
path = '/home/victor/Downloads/course'

filename_list = os.listdir(path)

a = 0
for i in filename_list:
	old_name = path + '/' + filename_list[a]
	x = old_name.find('.')
	new_name = path + '/' + old_name[x+1:]
	os.rename(old_name,new_name)
#	print(new_name)
	a += 1


