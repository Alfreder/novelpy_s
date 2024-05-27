import indicators
import tqdm
# networkx 报错 https://blog.csdn.net/Yukee_/article/details/132664000?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-132664000-blog-133126419.235%5Ev39%5Epc_relevant_default_base&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-132664000-blog-133126419.235%5Ev39%5Epc_relevant_default_base&utm_relevant_index=1


for focal_year in tqdm.tqdm(range(1997, 2000), desc = "Computing indicator for window of time"):
    Foster = indicators.Foster2015(collection_name = "Ref_Journals_sample",
                                           id_variable = 'PMID',
                                           year_variable = 'year',
                                           variable = "c04_referencelist",
                                           sub_variable = "item",
                                           focal_year = focal_year,
                                           starting_year = 1996,
                                           community_algorithm = "Louvain",
                                           density = True)
    Foster.get_indicator()