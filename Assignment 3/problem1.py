import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
	key = record[0]
	value = record[1]

	for word in value.split():
		mr.emit_intermediate(word,key)

def reducer(key, list_of_values):
	result=[]
	for document_ID in list_of_values:
		if document_ID not in result:
			result.append(document_ID)
	mr.emit((key, result))

inputdata = open(sys.argv[1])
mr.execute(inputdata,mapper,reducer)
