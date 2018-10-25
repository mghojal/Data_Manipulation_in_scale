/* D count the number of documents containing the word "parliament" */
select count(*) 
from (
select * 
from frequency D 
where D.term = 'parliament'
);

