# Lee et al.(2015) Ref_Journals_sample
import tqdm
import indicators
for focal_year in tqdm.tqdm(range(1996, 1997), desc = "Computing indicator for window of time"):
    Lee = indicators.Lee2015(collection_name = "Ref_Journals_sample",
                                           id_variable = 'PMID',
                                           year_variable = 'year',
                                           variable = "c04_referencelist",
                                           sub_variable = "item",
                                           focal_year = focal_year,
                                           density = True)
    Lee.get_indicator()