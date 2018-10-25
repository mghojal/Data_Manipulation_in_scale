import sys
import MapReduce

mr=MapReduce.MapReduce()

def mapper(record):
	key = record[1]
    	mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
	lines = []
    	order = []
   	for v in list_of_values:
		if v[0] == "order":
			order = v
		else:
			lines.append(v)
   	for line in lines:
		mr.emit(order + line)	

inputData = open(sys.argv[1])
mr.execute(inputData,mapper,reducer)
