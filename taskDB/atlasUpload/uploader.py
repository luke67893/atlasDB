def writeFile(htmlObject, fileName):
	newFile = open('uploads/' + fileName, 'w')
	for line in htmlObject:
		newFile.write(line)
	newFile.close()