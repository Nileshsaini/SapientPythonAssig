import sys

def read_data(filename):
	lines=[]
	fh=None
	try:
		fh = open(filename, encoding="utf8")
		for line in fh:
			if line.strip():
				lines.append(line)
	except (IOError, OSError) as err:
		print(err)
		return []
	finally:
		if fh is not None:
			fh.close
	return lines

#file=sys.argv[0]

#print(read_data(file))
for file in sys.argv[1:]:
	lines=read_data(file)
	print(lines)

