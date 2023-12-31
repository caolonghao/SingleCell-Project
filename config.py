# config.py

subtask = 'openproblems_bmmc_multiome_phase2_mod2'

config = {
    'input_train_mod1': f'./data/{subtask}/{subtask}.censor_dataset.output_train_mod1.h5ad',
    'input_train_mod2': f'./data/{subtask}/{subtask}.censor_dataset.output_train_mod2.h5ad',
    'input_test_mod1': f'./data/{subtask}/{subtask}.censor_dataset.output_test_mod1.h5ad',
    'input_test_mod2': f'./data/{subtask}/{subtask}.censor_dataset.output_test_mod2.h5ad',
    'root': './data',
    'subtask': subtask,
    'output': 'output/output.h5ad',
    'n_pcs': 4,
    'n_neighbors': 5,
    'save_predict': True,
    'method_name':"sample_model",
    'do_test':True,
    'write_result':True
}
