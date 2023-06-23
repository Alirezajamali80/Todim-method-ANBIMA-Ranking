# Todim-method-ANBIMA-Ranking
I used one of the MCDM methods, named Todim, to help ranking financial institutions in brazil using ANBIMA Ranking.


This repository contains Python code that performs TODIM (an acronym for Thomson's Ordinal Decision Making) analysis on a given dataset. TODIM is a multi-criteria decision-making method used to rank alternatives based on a set of criteria.

Requirements :
- Python 3
- pandas
- numpy

Usage:
1. Clone the repository or download the code files.
2. Install the required Python libraries by running the following command:

_pip install pandas numpy_

3. Prepare your dataset in Excel format with the following structure:

  - The first column contains the basic ranking based on the algebraic sum of investments of each institution.
  - The second column contains the names of alternatives.
  - The subsequent columns except the last one represent the decision matrix, where each cell represents the performance score of an alternative for a specific criterion.
  - The last column shows the algebraic sum of investments of each institution. In the excel file you see this column with the name of "Total".
   
4. Update the file path in the code to point to your Excel dataset:

  _df = pd.read_excel('path/to/your/dataset.xlsx')_

5. Run the Python script:

  _python todim_analysis.py_

6. The script will calculate the global dominance values for each alternative, sort them in descending order, and display the ranked results.

**Output :**
The output of the script will be a DataFrame displaying the alternatives along with their global dominance values and ranks.

**References:**
Gomes, L. F. A. M., Machado, M. A. S., & Sallum, F. S. V. 2020. "Title of the Article." Int. J. Business and Systems Research, Volume 14, No. 1
