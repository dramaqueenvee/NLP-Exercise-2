"""
Code to quantitative and qualitatively assessing accuracy of the model in both 2024 and 1997
"""

# We open the files
files = [
    'noms_nadons_1997_clean_mod.txt',
    'noms_nadons_2024_clean_mod.txt',
    'noms_generats_1997.txt',
    'noms_generats_2024.txt'
]

# 1. We load it and put all files in a dictionary and clean the data
files_loaded = {}
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        # .strip() eliminates any white space or jump
        files_loaded[file] = [line.strip() for line in f.readlines()]

# 2. We then use sets to find the intersection
set_generats_2024 = set(files_loaded['noms_generats_2024.txt'])
set_reals_2024 = set(files_loaded['noms_nadons_2024_clean_mod.txt'])
set_generats_1997 = set(files_loaded['noms_generats_1997.txt'])
set_reals_1997 = set(files_loaded['noms_nadons_1997_clean_mod.txt'])


# The symbol & finds the intersection, and the - symbol finds the non-intersection
matches_2024 = list(set_generats_2024 & set_reals_2024)
matches_1997 = list(set_generats_1997 & set_reals_1997)
non_matches_2024 = list(set_generats_2024 - set_reals_2024)
non_matches_1997 = list(set_generats_1997 - set_reals_1997)

# 3. We finally print the output

# QUANTITATIVE ANALYSIS
print("QUANTITATIVE ANALYSIS:")
print(f"There is a match of {len(matches_2024)}% as for 2024 names.")
print(f"There is a match of {len(matches_1997)}% as for 1997 names.")

# QUALITATIVE ANALYSIS
print("QUALITATIVE ANALYSIS")
print(f"Matches 2024: {matches_2024}")
print(f"Non-Matches 2024: {non_matches_2024}")
print(f"Matches 1997: {matches_1997}")
print(f"Non-Matches 1997: {non_matches_1997}")