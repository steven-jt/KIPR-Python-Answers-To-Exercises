'''
Practicing with Lists and Strings, Control Flow, and Modules and Libraries
'''
"""
#1 - #3: DNA Problems
"""

def GC_content(dna_str):
    """
    Returns the proportion of the DNA strings that is a Guanine (G) or
    Cytosine (C) base
    :param dna_str: the DNA sequence being analyzed
    :return: the proportion of guanine or cytosine bases in the DNA sequence
    """
    dna_str = str(dna_str).upper()
    cg_bases = dna_str.count("C") + dna_str.count("G")
    return cg_bases / len(dna_str)

def list_complement(dna_str):
    """
    Return the complement of the DNA sequence (formatted as a string)
    :param dna_str: the DNA sequence being converted
    :return: the DNA sequence's complement (as a string)
    """
    dna_str = str(dna_str).upper()
    complement = ""
    for base in dna_str:
        complement += convert_base(base)
    return complement

def complement(dna_list):
    """
    Return the complement of the DNA sequence (formatted as a string)
    :param dna_str: the DNA sequence being converted
    :return: the DNA sequence's complement (as a string)
    """
    for base in range(len(dna_list)):
        dna_list[base] = convert_base(dna_list[base])

def convert_base(str):
    """
    (This is a recommended function)
    Returns the complement base of a given base:
       Guanine <-> Cytosine
       Adenine <-> Thymine
    :param str: the base as a string
    :return: the complement of the base
    """
    if str == "A":
        return "T"
    elif str == "T":
        return "A"
    elif str == "G":
        return "C"
    elif str == "C":
        return "G"
    return ""