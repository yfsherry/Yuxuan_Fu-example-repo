

select t2.owner_id, o.owner_name, t2.different_category_count from 
(
    select owner_id, count(distinct category_id) as different_category_count from
    (select a.article_id, a.owner_id, m.category_id from article a
    left join category_article_mapping m
    on a.article_id = m.article_id) t 
    group by owner_id
) t2
left join owner o 
on o.owner_id = t2.owner_id

