import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(records):
   	nucleotides = records[1][:-10]
    	mr.emit_intermediate(nucleotides, 1)

def reducer(key,list_of_values):
	 mr.emit(key)

inputData = open(sys.argv[1])
mr.execute(inputData,mapper,reducer)
