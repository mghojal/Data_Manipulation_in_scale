/* A select σdocid=10398_txt_earn(frequency) */ 
select count(*) 
from (
select * 
from frequency A 
where A.docid = '10398_txt_earn'
);

