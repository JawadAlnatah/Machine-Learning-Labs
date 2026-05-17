import json

nb_path = r'c:\Users\jawad\Desktop\University\IAU\level 6\ML\ML labs\Machine-Learning-Labs\Lab-6\ARTI308 Lab6.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Fix cell 41 - Data Cleaning markdown (backtick names were stripped by bash)
nb['cells'][41]['source'] = (
    "### Step 3: Data Cleaning\n\n"
    "The columns `Email`, `Address`, and `Avatar` are text fields that cannot be used "
    "directly by the Linear Regression model, so we will drop them."
)

# Fix cell 43 - Feature Engineering markdown (em dash was broken)
nb['cells'][43]['source'] = (
    "### Step 4: Feature Engineering\n\n"
    "No additional feature engineering is needed -- the numeric columns are already in "
    "suitable form. Let us check correlations to understand which features are most predictive."
)

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Fixed cells 41 and 43")
print("Cell 41:", nb['cells'][41]['source'][:80])
print("Cell 43:", nb['cells'][43]['source'][:80])
