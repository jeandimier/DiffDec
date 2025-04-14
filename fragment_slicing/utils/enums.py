class DataframeColumnsEnum:
    SCAFFOLDS = "scaffolds"
    DECORATIONS = "decorations"
    ORIGINAL = "original"
    MAX_CUTS = "max_cuts"
    REACTION = "reaction"

    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

    # prohibit any attempt to set any values
    def __setattr__(self, key, value):
        raise ValueError("No changes allowed.")


class MolecularDescriptorsEnum:
    HEAVY_ATOM_COUNT = "heavy_atom_count"
    MOLECULAR_WEIGHT = "molecular_weight"
    CLOGP = "clogp"
    HYDROGEN_BOND_DONORS = "hydrogen_bond_donors"
    HYDROGEN_BOND_ACCEPTORS = "hydrogen_bond_acceptors"
    ROTATABLE_BONDS = "rotatable_bonds"
    RING_COUNT = "ring_count"


class RunningModeEnum:
    RANDOMIZATION = "data_randomization"
    REACTION_BASED_SLICING = "reaction_based_slicing"
    DUPLICATE_REMOVAL = "duplicate_removal"
    STATS_EXTRACTION = "stats_extraction"
    FILE_SHUFFLING = "file_shuffling"
    REACTION_VALIDATION = "reaction_validation"
    REAGENT_VALIDATION = "reagent_validation"
    VALIDATION_SCAFFOLD_SELECTION = "validation_scaffold_selection"
    TENSORBOARD_LOG_EXTRACTION = "tensorboard_log_extraction"
    SCAFFOLD_MEMORY_ANALYSIS = "scaffold_memory_analysis"
    DECORATION_SIMILARITY = "decoration_similarity"

    VALIDATION_SET_SIMILARITIES = "scaffold_similarity"
    VALIDATION_SET_FILTERING = "filtering"
    VALIDATION_SET_SLICED = "sliced_split"

    # try to find the internal value and return
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

    # prohibit any attempt to set any values
    def __setattr__(self, key, value):
        raise ValueError("No changes allowed.")
