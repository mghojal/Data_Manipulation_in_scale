/* I Keyword search */
create view if not exists keywords as 
select * 
from frequency 
union select 'q' as docid, 'washington' as term, 1 as count 
union select 'q' as docid, 'taxes' as term, 1 as count 
union select 'q' as docid, 'treasury' as term, 1 as count;

select A.docid, B.docid, sum(A.count * B.count) as similarity
from keywords A join keywords B on A.term = B.term 
where A.docid = 'q' and B.docid != 'q'
group by A.docid, B.docid
order by similarity desc;
