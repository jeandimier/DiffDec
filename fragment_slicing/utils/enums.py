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
