import pandas as pd
import os

excel_files = [
    "ex2/noms_nadons_2024.xlsx",
    "ex2/noms_nadons_1997.xlsx"
]

folder = "ex2"  

for file in excel_files:
    df = pd.read_excel(file, header=None)
    df = df[0].str.split(",", expand=True)
    names = df[2].str.lower()
    
    # Make output path in the same folder
    base_name = os.path.basename(file).replace(".xlsx", "_clean.txt")
    output_file = os.path.join(folder, base_name)
    
    names.to_csv(output_file, index=False, header=False)
    print(f"Processed {file} → {output_file}")

print("Done")
