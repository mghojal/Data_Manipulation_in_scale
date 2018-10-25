import sys
import MapReduce

mr = MapReduce.MapReduce()

#Matrix Dimensions are 5x5 for A and B so the result will be also 5x5
Dim = 5

def mapper(records):
	key = records[0]
	i = records[1]
    	j = records[2]
    	value = records[3]

    	if key == "a":
        	mr.emit_intermediate(key, [i,j,value])
    	elif key == "b":
        	mr.emit_intermediate(key, [j,i,value])
    	else:
        	print "Error."

def reducer(key, list_of_values):
	A = {}
	B = {}
	result = 0
	if key == "a":
		for a in mr.intermediate["a"]:
			A[(a[0], a[1])] = a[2]
		for b in mr.intermediate["b"]:
			B[(b[0], b[1])] = b[2]
		# fill in zeros
		for i in range(0,Dim):
			for j in range(0,Dim):
				k = (i,j) 
				if k not in A.keys():
					A[k] = 0
				if k not in B.keys():
					B[k] = 0
		# now do the multiply.
		for i in range(0,Dim):
			for j in range(0,Dim):
				result = 0
				for k in range(0,Dim):
					result += A[(i,k)] * B[(j,k)]
				mr.emit((i,j,result))


inputData = open(sys.argv[1])
mr.execute(inputData,mapper,reducer)
