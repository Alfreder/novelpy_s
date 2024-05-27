import utils
ref_cooc1 = utils.cooc_utils.create_cooc(
                 collection_name = "Ref_Journals_sample",
                 year_var="year",
                 var = "c04_referencelist",
                 sub_var = "item",
                 time_window = range(1996, 2000),
                 weighted_network = True, self_loop = True)

ref_cooc1.main()



