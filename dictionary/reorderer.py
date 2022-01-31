words=[]
current=""
already=[]
with open("En.yaml",encoding="utf-8") as fp:
	line = fp.readline()
	while line:
		if not line[0] =="#":
			if not line[0] ==" ":
				current=line.replace(":\n","")
				if current in already or True:
					print(current)
				already.append(current)
				words.append("")
			if "dupl:" in line:
				if not current.replace("__","_").replace("__","_").replace("__","_").replace(" ","") == line.replace(" ","").replace("\n","").replace("dupl:","").replace("<69105>",""):
					print(current, line)
			words[-1]+=line
		line = fp.readline()
def sortBy(x):
	i=0
	for y in x:
		if y not in 'abcdefghıȷklmnopqrstuvwxyz ́':
			x=x.replace(y,"")
	if x[0] in "aeıouvy":
		x=" "+x
	y=0
	while i<len(x):
		y+='abcdefghıȷklmnoprqstuvwxyz ́'.index(x[i])/(100**i)
		i+=1
	return y
words.sort(key=sortBy)

new=open("e2n.yaml","w+",encoding="utf-8")
new.write("")
new.close()
new=open("e2n.yaml","a+",encoding="utf-8")
for word in words:
	new.write(word)
new.close()