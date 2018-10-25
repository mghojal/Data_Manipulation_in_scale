import sys
import MapReduce

mr=MapReduce.MapReduce()
 	mr.emit( (pairs[1], pairs[0]) )

def mapper(record):
    # key: document identifier
    # value: document contents
    person = record[0]
    friend = record[1]
    mr.emit_intermediate((person,friend), 1)
    mr.emit_intermediate((friend,person), 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
   
   if len(list_of_values) < 2:
       mr.emit(key)


inputData = open(sys.argv[1])
mr.execute(inputData,mapper,reducer)
