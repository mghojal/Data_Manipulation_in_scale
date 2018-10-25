/* B πterm(σdocid=10398_txt_earn and count=1(frequency)) */
select count(*) 
from (
select term 
from frequency B 
where B.docid = '10398_txt_earn' and B.count = 1
);


