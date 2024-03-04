dependencies = [
    "numpy",
    "pandas",
    "shap",
    "matplotlib",
    "seaborn",
    "imbalanced-learn",
    "plotly",
    "scikit-learn",
    "lightgbm",
    "xgboost"
]

# Write the dependencies to a requirements.txt file
with open("requirements.txt", "w") as f:
    for package in dependencies:
        f.write(package + "\n")
