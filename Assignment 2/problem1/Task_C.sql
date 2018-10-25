/* C πterm(σdocid=10398_txt_earn and count=1(frequency)) U πterm(σdocid=925_txt_trade and count=1(frequency)) */
select count(*) 
from (
select term 
from frequency C1 
where C1.docid = '10398_txt_earn'and C1.count=1 
union select term 
from frequency C2 
where C2.docid = '925_txt_trade' and C2.count=1
);

