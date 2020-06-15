import os
root_dir=os.getcwd()
print("Root directory: ", root_dir)

#dirname:[(subdir), info]
folder_structure = {'data':[('raw', 'processed', 'external'), 'from raw to proccesed data'], 'docs':[(), 'default sphinx docs'], 'notebooks':[(), 'jupyter notebooks'], 'references':[(),'data dictionaries, manuals'] , 'reports':[(), 'generated analysis'], 'src':[('etl', 'analysis'), 'source code for the project']}


def create_dir():
	for folder in folder_structure.keys():
		print (folder)
		try:
			#full_path = str(root_dir)+'/'+str(folder)
			os.makedirs(folder)
			print("Directory created: ", folder)
			if folder_structure[folder][0]:
				for subfolder in folder_structure[folder][0]:
					os.makedirs(str(folder+'/'+subfolder))
			else:
				continue
		except FileExistsError:
			print("Directory already exists: ", folder)
		except OSError:
			print ("Creation of the directory failed: ", folder)


if __name__ == '__main__':
	create_dir()


