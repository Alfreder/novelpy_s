import utils
# 第一步  构建pkl文件 预处理
cooc = utils.create_citation_network(
            collection_name = "Citation_net_sample",
            id_variable = "PMID",
            variable = "refs_pmid_wos"
)
# cooc.id2citedby()
# cooc.update_db()

# 预处理结束


# 结果在result文件夹中
import indicators

year = 1996
# 第二步，开始执行
disruptiveness = indicators.Disruptiveness(
                      collection_name = 'Citation_net_sample_cleaned',
                      focal_year = year,
                      id_variable = 'PMID',
                      refs_list_variable ='refs',
                      cits_list_variable = 'cited_by',
                      year_variable = 'year')

# disruptiveness.get_indicators()