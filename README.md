# Write a function to select the rows where the score is missing, i.e. is NaN.

Define a function that takes in a dictionary as a parameter and converts it into a DataFrame.
The function should return those rows where the 'score' column's value is missing(i.e. NaN).

_Example:_

**Input:**



    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    

**Output:**
    
    
    
         attempts   name   qualify    score
    3         3    James      no      NaN
    7         1    Laura      no      NaN