import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(records):
	key = records[0]
	mr.emit_intermediate(key,1)

def reducer(key,list_of_values):
	count = 0
	for value in list_of_values:
		count+=value
	mr.emit((key,count))


inputData = open(sys.argv[1])
mr.execute(inputData,mapper,reducer)
