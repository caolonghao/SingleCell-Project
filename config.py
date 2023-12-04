# config.py

config = {
    'input_train_mod1': './sample_data/openproblems_bmmc_multiome_starter/openproblems_bmmc_multiome_starter.train_mod1.h5ad',
    'input_train_mod2': './sample_data/openproblems_bmmc_multiome_starter/openproblems_bmmc_multiome_starter.train_mod2.h5ad',
    'input_test_mod1': "./sample_data/openproblems_bmmc_multiome_starter/openproblems_bmmc_multiome_starter.test_mod1.h5ad",
    'input_test_mod2': './sample_data/openproblems_bmmc_multiome_starter/openproblems_bmmc_multiome_starter.test_mod2.h5ad',
    'output': 'output/output.h5ad',
    'n_pcs': 4,
    'n_neighbors': 5,
    'save_predict': True,
    'method_name':"sample_model",
    'do_test':True,
    'write_result':True
}
