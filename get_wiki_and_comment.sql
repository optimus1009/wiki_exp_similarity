select
	concat_ws('$&&$',string(T1.wiki_id),T1.wiki_content,concat_ws('|',collect_list(T2.comment)))
from
(
	select
		wiki_id --知识id
		,content as wiki_content --知识内容
	from ods.ods_bf09_forum_wiki_content_s_d
	where pt = 20170911
) T1
inner join
(
	select * 
	from
	(
	select 
			id  --经验id
			,wiki_id --知识id
			,regexp_replace(content,'|','') as comment --经验内容
		from
		(
			select
				id
				,wiki_id
			from ods.ods_bf09_forum_wiki_comment_s_d
			where pt = 20170911
		) t1
		left outer join
		(
			select
				comment_id
				,content
			from ods.ods_bf09_forum_wiki_comment_content_s_d  
			where pt = 20170911
		) t2
		on t1.id = t2.comment_id 
	 ) t3
	 where length(comment) > 40
) T2
on T1.wiki_id = T2.wiki_id 
group by T1.wiki_id,T1.wiki_content
