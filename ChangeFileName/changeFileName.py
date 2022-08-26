import os
path = '/home/victor/Videos/进击的巨人/S4'

filename_list = os.listdir(path)

a = 0
for i in filename_list:
	old_name = path + '/' + filename_list[a]
	x = old_name.find('-')
	x = x+1
	# x = old_name.find('[',x+1)
	# y = old_name.find(']',x)
	# new_name = path + '/' + old_name[x+1:y] + '.mp4'
	new_name = path + '/' + old_name[x:]
	# new_name = new_name.replace(')','')
	os.rename(old_name,new_name)
	print(new_name)
	a += 1


