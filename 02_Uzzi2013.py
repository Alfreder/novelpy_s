# Uzzi et al.(2013) Ref_Journals_sample
import tqdm
import indicators
for focal_year in tqdm.tqdm(range(1997, 1998), desc = "Computing indicator for window of time"):
    Uzzi = indicators.Uzzi2013(collection_name = "Ref_Journals_sample",
                                           id_variable = 'PMID',
                                           year_variable = 'year',
                                           variable = "c04_referencelist",
                                           sub_variable = "item",
                                           focal_year = focal_year,
                                           density = True)
    Uzzi.get_indicator()