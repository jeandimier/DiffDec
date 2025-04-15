from dataclasses import dataclass
from typing import List, Optional, Tuple

from rdkit.Chem import Mol
from rdkit.Chem.rdChemReactions import ChemicalReaction


@dataclass
class FilteringConditionDTO:
    name: str
    min: Optional[float] = None
    max: Optional[float] = None
    equals: Optional[float] = None


@dataclass
class GeneralConfiguration:
    run_type: str
    parameters: dict


@dataclass
class ReactionDTO:
    reaction_smarts: str
    chemical_reaction: ChemicalReaction


@dataclass
class ReactionOutcomeDTO:
    reaction_smarts: str
    reaction_outcomes: List[Tuple[Mol]]
    targeted_molecule: Mol


@dataclass
class ReactionBasedSlicingConfig:
    input_file: str
    output_path: str
    output_smiles_file: str
    conditions_file: str
    reactions_file: str
    max_cuts: int = 4
    number_of_partitions: int = 1000
    validate_randomization: bool = True


@dataclass
class SlicingConditionsDTO:
    scaffold: List[FilteringConditionDTO]
    decoration: List[FilteringConditionDTO]
