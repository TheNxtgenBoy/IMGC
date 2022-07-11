from PIL import Image
import sys

class IMGC():
	def __init__(self):
		argument = sys.argv[-1]
		self.clone(argument)

	def clone(self, argument):
		try:
			if argument.split('.')[-1] in ['jpg', 'png']:
				original_image = Image.open(argument)
				clone_image = Image.new('RGB', original_image.size)
				clone_image.paste(original_image)
				name = argument.split('.')[-2] + '_IMGC.' + argument.split('.')[-1]
				clone_image.save(name)
				print('Success...')
			else:
				print('file not supported.....')
		except:
			print('Internal error')

if __name__ == "__main__":
	IMGC()