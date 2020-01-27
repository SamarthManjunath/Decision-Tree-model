#Samarth Manjunath
#1001522809
#program to print a decision tree

import math
import random 
trrt = .8
class C45:

	#c45 algo to create a decision tree
	def __init__(sf, pttda,pttna):
		sf.fpd = pttda
		sf.fpn = pttna
		sf.data = []
		sf.td = [] 
		sf.cls = []
		sf.numatt = -1 
		sf.attva = {}
		sf.att = []
		sf.tree = None
# function to retreive data
	def data_retrieve(sf):
		with open(sf.fpn, "r") as file:
			cls = file.readline()
			sf.cls = [x.strip() for x in cls.split(",")]
			for line in file:
				[attbe, values] = [x.strip() for x in line.split(":")]
				values = [x.strip() for x in values.split(",")]
				sf.attva[attbe] = values
		sf.numatt = len(sf.attva.keys())
		sf.att = list(sf.attva.keys())
		with open(sf.fpd, "r") as file:
			for line in file:
				row = [x.strip() for x in line.split(",")]
				
				if row != [] or row != [""]:
					if random.random() < trrt:
						sf.data.append(row)
					else:
						sf.td.append(row)
		
		# function to preprocess the data
	def preprocesstd(sf):
		flag = 0
		
		for index,row in enumerate(sf.td):
			if (sf.cls).__contains__(row[0]):
				flag = 1
				if flag == 1:
					val = row[0]
					sf.td[index].remove(row[0])
					sf.td[index].append(val)
					flag = 0

#function to preprocess the data
	def ppd(sf):
		for index,row in enumerate(sf.data):
			for attr_index in range(sf.numatt):
				if(not sf.iad(sf.att[attr_index])):
					sf.data[index][attr_index] = float(sf.data[index][attr_index])
		flag = 0
		for index,row in enumerate(sf.data):
			if (sf.cls).__contains__(row[0]):
				flag = 1
				if flag == 1:
					data = row[0]
					sf.data[index].remove(row[0])
					sf.data[index].append(data)
					flag = 0
		sf.preprocesstd()

		
	def pt(sf):
		sf.pn(sf.tree)

#function to build the tree
	def pn(sf, node, indent=""):
		if not node.isLeaf:
			if node.thld is None:
				for index,child in enumerate(node.children):
					if child.isLeaf: 
						a = []
						a = sf.attva.get(node.label)
						print(indent + node.label + " = " + str(a[index]) + " : " + child.label) 
					else:
						a = []
						a = sf.attva.get(node.label)
						print(indent + node.label + " = " + str(a[index])  + " : ")
						sf.pn(child, indent + "	")
			else:
				leftChild = node.children[0]
				rightChild = node.children[1]
				if leftChild.isLeaf:
					print(indent + node.label + " <= " + str(node.thld) + " : " + leftChild.label)
				else:
					print(indent + node.label + " <= " + str(node.thld)+" : ")
					sf.pn(leftChild, indent + "	")

				if rightChild.isLeaf:
					print(indent + node.label + " > " + str(node.thld) + " : " + rightChild.label)
				else:
					print(indent + node.label + " > " + str(node.thld) + " : ")
					sf.pn(rightChild , indent + "	")


	def gt(sf):
		sf.tree = sf.rcusgt(sf.data, sf.att)

	def rcusgt(sf, crdt, curatt):
		allSame = sf.asc(crdt)
		if len(crdt) == 0:
			return nd(True, "Fail", None)
		elif allSame is not False:
			return nd(True, allSame, None)
		elif len(curatt) == 0:
			majClass = sf.gmc(crdt)
			return nd(True, majClass, None)
		else:
			(best,best_thld,splt) = sf.spatt(crdt, curatt)
			remainingatt = curatt[:]
			remainingatt.remove(best)
			node = nd(False, best, best_thld)
			node.children = [sf.rcusgt(subset, remainingatt) for subset in splt]
			return node

	def gmc(sf, crdt):
		freq = [0]*len(sf.cls)
		for row in crdt:
			index = sf.cls.index(row[-1])
			freq[index] += 1
		maxInd = freq.index(max(freq))
		return sf.cls[maxInd]


	def asc(sf, data):
		if len(data) == 0:  
			return False
		else:
			for row in data:
				if row[-1] != data[0][-1]:
					return False
			return data[0][-1]

	def iad(sf, attbe):
		if attbe not in sf.att:
			raise ValueError("Att not there")
		elif len(sf.attva[attbe]) == 1 and sf.attva[attbe][0] == "continuous":
			return False
		else:
			return True

			#function to calculate information gn
	def gn(sf,unst, sbts):
		S = len(unst)
		imbsplt = sf.entp(unst)
		wts = [len(subset)/S for subset in sbts]
		imasplt = 0
		for i in range(len(sbts)):
			imasplt += wts[i]*sf.entp(sbts[i])
		totg = imbsplt - imasplt
		return totg

	def spatt(sf, crdt, curatt):
		splt = []
		maxEnt = -1*float("inf")
		bstatt = -1
		best_thld = None
		for attbe in curatt:
			iofatt = sf.att.index(attbe)
			if sf.iad(attbe):
				valfatt = sf.attva[attbe]
				sbts = [[] for a in valfatt]
				for row in crdt:
					for index in range(len(valfatt)):
						if row[iofatt] == valfatt[index]:   
							sbts[index].append(row)
							break
				e = sf.gn(crdt, sbts) 
				if e > maxEnt:
					maxEnt = e
					splt = sbts
					bstatt = attbe
					best_thld = None
			else:
				crdt.sort(key = lambda x: x[iofatt])
				for j in range(0, len(crdt) - 1):
					if crdt[j][iofatt] != crdt[j+1][iofatt]:
						thld = (crdt[j][iofatt] + crdt[j+1][iofatt]) / 2
						less = []
						greater = []
						for row in crdt:
							if(row[iofatt] > thld):
								greater.append(row)
							else:
								less.append(row)
						e = sf.gn(crdt, [less, greater])
						if e >= maxEnt:
							splt = [less, greater]
							maxEnt = e
							bstatt = attbe
							best_thld = thld
		return (bstatt,best_thld,splt)

#function to calculate entropy
	def entp(sf, dataSet):
		S = len(dataSet)
		if S == 0:
			return 0
		num_cls = [0 for i in sf.cls]
		for row in dataSet:
			classIndex = list(sf.cls).index(row[-1])
			num_cls[classIndex] += 1
		num_cls = [x/S for x in num_cls]
		ent = 0
		for num in num_cls:
			ent += num*sf.log(num)
		return ent*-1


	def log(sf, x):
		if x == 0:
			return 0
		else:
			return math.log(x,2)

	def gtn(sf):
		return sf.tree
	
	def gettd(sf):
		return sf.td

	def tstn(sf):
		print(sf.att)
		success = 0
		for row in sf.td:
			success += sf.tstr(row)
		print ("Welldone, Success : ", success)
		print ("Total : ", len(sf.td))
		print ("Actual Ratio  : ", float(success)/len(sf.td))

	def tstd(sf,row):
		node = sf.tree
		for index,value in enumerate(row):
			if not node.isLeaf:
				if list(sf.attva[node.label]).__contains__(value):
					val = list(sf.attva[node.label]).index(value)
					if node.label == sf.att[index]:
						node = node.children[val]
					else:
						print ("Sorry, Failure")
						return 0
				else:
					continue
			else:
				print (node.label)
				if row[-1] == node.label:
					print ("Welldone, Success")
					return 1
				else:
					print ("Sorry, Failure")
					return 0
#function to print nodes
	def printMyNODE(sf,node,indent):
		if not node.isLeaf:
			print (indent,"[", node.label, ",",node.thld,",",len(node.children),"]")
			for child in node.children:
				sf.printMyNODE(child,"    " + indent)
		else:
			print (indent,"[", node.label, ",",node.thld,",",len(node.children),"]")



	def tstnum(sf,row,node):
		if not node.isLeaf:
			aI = sf.att.index(node.label)
			if row[aI] >= node.thld:
				node = node.children[0]
				return sf.tstnum(row,node)
			else:
				node = node.children[1]
				return sf.tstnum(row,node)
		else:
			print (node.label)
			if node.label == row[-1]:
				print ("Welldone, Success")
				return 1
			else:
				print ("Sorry, Failure")
				return 0
		return 0

	def tstr(sf,row):
		node = sf.tree
		print (row)
		if node.thld is None:
			return sf.tstd(row)

		else:
			return sf.tstnum(row,node)
		
		print ("Sorry, Failure")
		return 0

class nd:
	def __init__(sf,isLeaf, label, thld):
		sf.label = label
		sf.thld = thld
		sf.isLeaf = isLeaf
		sf.children = []
		#end of function