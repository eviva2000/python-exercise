def to_rna(dna_strand):
    """Return the RNA complement of a DNA strand.

    Each nucleotide is replaced with its RNA complement:
    G -> C, C -> G, T -> A, and A -> U.

    Args:
        dna_strand (str): A DNA sequence containing A, C, G, and T.

    Returns:
        str: The corresponding RNA sequence.
    """
    complements = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }
    return "".join(complements[nucleotide] for nucleotide in dna_strand)