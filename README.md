# Data-Analysis-Task-1
Mall Customers – Data Cleaning & preprocessing 

A Python (Pandas) script that takes a raw customer dataset and runs it through a full data-cleaning pipeline: handling missing values, removing duplicates, standardizing text, fixing data types, and cleaning up column names — producing an analysis-ready CSV plus a change log.

📌 Objective

Clean and prepare a raw dataset for downstream analysis (e.g. customer segmentation), following standard data-cleaning best practices used in real-world data analyst workflows.

📂 Dataset

Mall Customer Segmentation Data (Kaggle)


200 rows, 5 columns: CustomerID, Gender, Age, Annual Income (k$), Spending Score (1-100)


🛠️ Tools Used


Python 3
Pandas
NumPy


🔧 What the Script Does

StepTechniqueLoad datapd.read_csv()Clean column headersRegex-based conversion to lowercase snake_case (e.g. Annual Income (k$) → annual_income_k)Detect missing values.isnull().sum()Handle missing valuesNumeric columns → filled with median; text columns → filled with modeRemove duplicates.drop_duplicates()Standardize text.str.strip() + .str.title(), plus manual mapping for inconsistent category labels (e.g. M/Man → Male)Handle date formatsAuto-detects any date-like column and converts to a consistent dd-mm-yyyy format using pd.to_datetime()Fix data typesForces numeric columns to proper Int64 type using pd.to_numeric()Save outputExports cleaned dataset to CSV + writes a full text log of every change made

📊 Results

The dataset was found to already be well-structured:


0 missing values
0 duplicate rows
2 consistent gender categories (Male, Female) after standardization
All numeric columns confirmed and cast to proper integer types
Column headers converted to clean snake_case format


Even though this particular dataset needed minimal fixes, the script is built generically — it will detect and correct nulls, duplicates, inconsistent text, and mixed date formats automatically if present, making it reusable on messier real-world datasets.

📁 Repository Structure

├── clean_data.py                  # Main cleaning script
├── requirements.txt                # Dependencies (pandas, numpy)
├── Mall_Customers.csv              # Raw input dataset
├── Mall_Customers_cleaned.csv      # Cleaned output dataset
└── cleaning_summary.txt            # Log of every change made

▶️ How to Run

bashpip install -r requirements.txt
python clean_data.py

This generates Mall_Customers_cleaned.csv and cleaning_summary.txt in the same folder.

🎯 Key Learnings


Built a reusable, generic data-cleaning pipeline rather than a one-off manual fix
Practiced core Pandas operations: .isnull(), .fillna(), .drop_duplicates(), .astype(), pd.to_datetime()
Understood the difference between removing missing data (dropna()) vs. imputing it (fillna())
Learned why consistent column naming and data types matter for downstream analysis and modeling
Practiced debugging real setup issues (file paths, running scripts from the correct working directory)
