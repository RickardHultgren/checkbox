varbegin = False

def regfunc(string):
	with open("in_file.txt","r") as fo: 
		pat=re.compile(r'^([^\n]*?blocks are definitely lost in loss record.*?loss record)', re.S | re.M)
		for i, block in pat.finditer(of.read()):
			# deal with each block

if regstring == "begin":
	varbegin = True
	regfunc(regstring)
elif regstring == "end":
	varbegin = False

vardic={name:value}
