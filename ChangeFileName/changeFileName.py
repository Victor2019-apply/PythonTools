import os
path = '/home/victor/Downloads/公正Justice：一场思辨之旅（中英字幕全12集）'

filename_list = os.listdir(path)

a = 0
for i in filename_list:
	old_name = path + '/' + filename_list[a]
	x = old_name.find('P')
	x = old_name.find('.',x+1)
	y = old_name.find('：',x+4)
	new_name = path + '/' + old_name[x+1:y] + '.mp4'
	# new_name = new_name.replace(')','')
	os.rename(old_name,new_name)
	print(new_name)
	a += 1


