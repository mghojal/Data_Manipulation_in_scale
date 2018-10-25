/* Matrix Multiplication */
select A.row_num, B.col_num, sum(A.value * B.value)
from A, B
where A.col_num = B.row_num
--and a.row_num = 2 and b.col_num = 3
group by A.row_num, B.col_num;
