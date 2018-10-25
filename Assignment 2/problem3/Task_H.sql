/* H Similarity Matrix */
select H 
from (
select A.docid, B.docid, sum(A.count * B.count) as H 
from frequency as A 
join frequency as B 
on A.term = B.term 
where A.docid < B.docid 
and A.docid = '10080_txt_crude' 
and B.docid = '17035_txt_earn' 
group by A.docid, B.docid
);

