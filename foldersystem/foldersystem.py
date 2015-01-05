__author__ = 'niels van Schooten'
import os

class directory:
	"""
		objectify the foldersystem
	"""

	def __init__(self, path):
		self.basepath = self.makepath()+path
		self.index = len(self.makepath(False))
		if not self.exists():
			self.makedirectory()

	def __str__(self):
		return self.basepath

	def __repr__(self):
		return repr(str(self.basepath))


	def makepath(self, string=True):
		path = os.path.dirname(__file__)
		path = path.replace("\\", "/")
		pathsplit = path.split("/")
		correctDir = ""
		# if "/" in path[0]:
			# correctDir += "/"

		for i in range(0, ((len(pathsplit) - 1))):
				correctDir += pathsplit[i] + "/"

		if string:
			return correctDir
		else:
			return pathsplit

	def exists(self):
		""" check if the directory exists """
		return os.path.exists(self.basepath)

	def makedirectory(self):
		if not self.exists():
			print("making the folder with write permissions")
			try:
				oriMask = os.umask(0)
				os.makedirs(self.basepath, 0o777)
			finally:
				os.umask(oriMask)
			return True
		else:
			if self.getaccespermissions(os.W_OK):
				print("access permissions correct")
				return True
			else:
				print("setting access permission")
				self.setaccespermissions()
				return  True

	def checkfile(self, filename):
		return  os.path.isfile(self.basepath+"/"+filename)

	def getfilepath(self, name):
		return  self.basepath+"/"+name


	def getaccespermissions(self, permission):
		""" get the acces permission of the folder """
		return os.access(self.basepath, permission)

	def setaccespermissions(self):
		""" set the acces permissions of the folder """
		os.chmod(self.basepath, 0o777)


	def getFiles(self):
		direct = os.listdir(self.basepath)
		dirlist = []
		for file in direct:
			dirlist.append(self.basepath+"/"+file)
		return dirlist
