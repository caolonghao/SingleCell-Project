# config.py

config = {
    'input_train_mod1': './data/openproblems_bmmc_cite_phase2_rna/openproblems_bmmc_cite_phase2_rna.censor_dataset.output_train_mod1.h5ad',
    'input_train_mod2': './data/openproblems_bmmc_cite_phase2_rna/openproblems_bmmc_cite_phase2_rna.censor_dataset.output_train_mod2.h5ad',
    'input_test_mod1': "./data/openproblems_bmmc_cite_phase2_rna/openproblems_bmmc_cite_phase2_rna.censor_dataset.output_test_mod1.h5ad",
    'input_test_mod2': './data/openproblems_bmmc_cite_phase2_rna/openproblems_bmmc_cite_phase2_rna.censor_dataset.output_test_mod2.h5ad',
    'root': './data',
    'subtask': 'openproblems_bmmc_cite_phase2_rna',
    'output': 'output/output.h5ad',
    'n_pcs': 4,
    'n_neighbors': 5,
    'save_predict': True,
    'method_name':"sample_model",
    'do_test':True,
    'write_result':True
}
