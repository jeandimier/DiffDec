python sample_single_for_specific_context.py \
    --scaffold_smiles_file ./data/examples/scaf.smi \
    --protein_file ./data/examples/protein.pdb \
    --scaffold_file ./data/examples/scaf.sdf \
    --task_name exp \
    --data_dir ./data/examples \
    --checkpoint ./ckpt/diffdec_single.ckpt \
    --samples_dir samples_exp \
    --n_samples 1 \
    --device cuda:0