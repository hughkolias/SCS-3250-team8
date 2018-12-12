#Creating gif file based all images in current folder 

import os,sys
import datetime
import imageio
from pprint import pprint
import time
import datetime
e=sys.exit
 
def create_gif(filenames, duration):
	images = []
	for filename in filenames:
		images.append(imageio.imread(filename))
	output_file = 'gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
	imageio.mimsave(output_file, images, duration=duration)
 
if __name__ == "__main__":
	script = sys.argv.pop(0)

	duration = 0.7
	extension = '.png'

	filenames = sorted(filter(os.path.isfile, [x for x in os.listdir() if x.endswith(extension)]), key=lambda p: os.path.exists(p) and os.stat(p).st_mtime or time.mktime(datetime.now().timetuple()))
	create_gif(filenames, duration)
