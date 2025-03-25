import torch
from rdkit import Chem
from tqdm import tqdm

split_by_name = torch.load("data/split_by_name.pt")
path_prefix = "data/crossdocked_pocket10/"
f = open("data/train_smi.smi", "w")
for i in tqdm(range(len(split_by_name["train"]))):
    ligand_filename = path_prefix + split_by_name["train"][i][1]
    mol = next(iter(Chem.SDMolSupplier(ligand_filename, removeHs=True)))
    smi = Chem.MolToSmiles(mol, isomericSmiles=False, canonical=True)
    f.write(smi + "\n")
f.close()
f = open("data/test_smi.smi", "w")
for i in tqdm(range(len(split_by_name["test"]))):
    ligand_filename = path_prefix + split_by_name["test"][i][1]
    mol = next(iter(Chem.SDMolSupplier(ligand_filename, removeHs=True)))
    smi = Chem.MolToSmiles(mol, isomericSmiles=False, canonical=True)
    f.write(smi + "\n")
f.close()
