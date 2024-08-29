import pandas as pd

scores = pd.read_csv('scores.csv')
# print(scores['Scores'].max())
# print(scores['Scores'].min())
# print(scores['Scores'].mean())
# print(scores['Scores'].sum())
print(scores['Hours'].sort_values())
print(scores['Hours'].sort_values(),ascending = False)
# print(scores)
# print(scores.shape) # (rows*cols)
# print(scores.count())

import pandas as pd

# scores = pd.read_csv('scores.csv')
# # print(scores['Scores'].max())
# # print(scores['Scores'].min())
# # print(scores['Scores'].mean())
# # print(scores['Scores'].sum())
# # print(scores['Hours'].sort_values())
# # print(scores['Hours'].sort_values(),ascending = False)
# # print(scores)
# # print(scores.shape) # (rows*cols)
# # print(scores.count())

# # print(scores.head())  # prints top 5 rows
# # print(scores.tail())  # prints last 5 rows
# print(scores[scores['Hours'] == 2.5])

scores = pd.read_csv('student-scores.csv')
# print(scores.head())

# print(scores[scores['english_score'] > 90

#! Topper of geography from boys

# print(scores[scores['gender'] == 'male']['geography_score'].max())

#! Cateogry based on geography_score

# A_grade = scores[scores['geography_score'] > 85]
# B_grade = scores[scores['geography_score'].between(70,85)]
# C_grade = scores[scores['geography_score'].between(60,70)]
# D_grade = scores[scores['geography_score'] < 60]

# total_A_grade = A_grade.shape[0]

#! Cateogry based on geography_score and gender 'male'
# total_A_grade = scores[(scores['geography_score'] > 85) & (scores['gender']=='male')].shape[0]

# print(total_A_grade)

#! print bio, eng and geo scores of A grade students each
# subjects =['biology_score','english_score','geography_score']

# for sub in subjects:
#   print(sub, '->',scores[(scores[sub] > 85) & (scores['gender']=='male')].shape[0])

#! print total number of (count) scores of students with above average scores in geography_score

# avg = scores['geography_score'].mean()
# print(scores[scores['geography_score'] > avg].shape[0])

#! groupby returns a dictionary where the key is the unique value from the column and the value is a list of the data
print(scores.groupby('gender'.groups))