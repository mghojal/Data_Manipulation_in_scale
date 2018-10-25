/* F unique documents that contain both the word 'transactions' and the word 'world' */
select count(*) 
from (
select F1.docid 
from frequency F1 
inner join frequency F2 on F1.docid = F2.docid 
where F1.term = 'transactions' and F2.term = 'world'
);
