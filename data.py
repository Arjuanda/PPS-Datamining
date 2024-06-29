import pandas as pd
import numpy as np
import openpyxl

# Base data extracted from the image (manually represented here for demonstration)
data = {
    "No": range(1, 61),
    "Nama": ["Chika", "Amelia", "Jodie", "Dian", "Dea", "Flo", "Dhesta", "Gladys", "Cacaa", "Rismat", "Abda", "Ana", "Theo", "Selsa", "Rouf", 
             "TIM", "Mitha", "Eri", "Lidya", "Nisa", "Fadhillah", "Heno", "Rizki", "Eldora", "Janice", "Tere", "Teresa", "faiq", "Marshel", 
             "Wuri", "Naura", "Wima", "Ahya", "Feby", "Dewi", "Nyimas", "Mitha", "Rosi", "Deva", "Fiqih", "Ameng", "Mega", "Rayi", "anggi", 
             "Salsa", "Selvi", "Rafi", "Eka", "Melati", "Lulu", "Aiman", "Deris", "Afifah", "nadi", "Rozy", "Syelin", "Dhea", "Dyah", "Yuni", "Anto"],
    "X1": np.random.randint(75, 100, 60),
    "X2": np.random.randint(75, 100, 60),
    "X3": np.random.randint(75, 100, 60),
    "X4": np.random.uniform(50, 95, 60).round(2),
    "X5": np.random.uniform(50, 95, 60).round(2),
    "X6": np.random.uniform(50, 95, 60).round(2),
    "X7": np.random.randint(50, 100, 60),
    "X8": np.random.randint(50, 100, 60),
    "X9": np.random.randint(50, 100, 60),
    "X10": np.random.randint(50, 100, 60),
    "Target": np.random.choice(["IF", "AK", "MS", "GM", "ABT", "LPI", "MK", "TRPL", "KP", "RPE", "AN", "WE", "TPPU", "RKS", "TRE", "TRM", "EM", "AM"], 60)
}

# Create initial DataFrame
df_initial = pd.DataFrame(data)

# Generate additional rows (200 total)
additional_rows = 140
new_data = {
    "No": range(61, 61 + additional_rows),
    "Nama": [f"Student{i}" for i in range(61, 61 + additional_rows)],
    "X1": np.random.randint(75, 100, additional_rows),
    "X2": np.random.randint(75, 100, additional_rows),
    "X3": np.random.randint(75, 100, additional_rows),
    "X4": np.random.uniform(50, 95, additional_rows).round(2),
    "X5": np.random.uniform(50, 95, additional_rows).round(2),
    "X6": np.random.uniform(50, 95, additional_rows).round(2),
    "X7": np.random.randint(50, 100, additional_rows),
    "X8": np.random.randint(50, 100, additional_rows),
    "X9": np.random.randint(50, 100, additional_rows),
    "X10": np.random.randint(50, 100, additional_rows),
    "Target": np.random.choice(["IF", "AK", "MS", "GM", "ABT", "LPI", "MK", "TRPL", "KP", "RPE", "AN", "WE", "TPPU", "RKS", "TRE", "TRM", "EM", "AM"], additional_rows)
}

# Create DataFrame for new data and concatenate
df_new = pd.DataFrame(new_data)
df_combined = pd.concat([df_initial, df_new], ignore_index=True)

# Save to Excel
output_file_path = 'DataNilai.xlsx'
df_combined.to_excel(output_file_path, index=False)
