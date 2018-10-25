/* E more than 300 total terms */
select count(*) 
from (
select docid, sum(count) 
from frequency E 
group by E.docid 
having sum(E.count) > 300
);

