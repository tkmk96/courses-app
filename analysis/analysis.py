import pandas as pd
pd.set_option('display.max_columns', None)

data_frame = pd.read_csv('../rest_api/api/csv/CourseUser.csv')

# ACTUAL RATINGS
data_frame\
    .groupby(['course']).mean()\
    .to_csv('actual ratings.csv')

# USER RATINGS COUNT
data_frame\
    .groupby(['user'])\
    .count()\
    .drop(columns=['course'])\
    .sort_values(by=['rating'], ascending=False)\
    .to_csv('user ratings count.csv')

# RATINGS COUNT
data_frame\
    .groupby(['user']).count()\
    .groupby(['rating']).count()\
    .rename(columns={'course': 'users'})\
    .to_csv('ratings count.csv')

# CATEGORY
data_frame = pd.read_csv('../rest_api/api/csv/Course.csv')

data_frame\
    .groupby(['name']).count()\
    .sort_values(by=['category'], ascending=False)\
    .rename(columns={'category': 'number of categories'})\
    .drop(columns=['description', 'ratings', 'number of lectures', 'difficulty', 'average rating', 'price'])\
    .to_csv('courses in categories.csv')

# CATEGORY COUNT
data_frame\
    .drop(columns=['ratings', 'number of lectures', 'difficulty', 'average rating', 'price'])\
    .groupby(['name']).count()\
    .groupby(['category']).count()\
    .rename(index=str, columns={'category': 'number of categories', 'description': 'courses'})\
    .to_csv('courses in categories count.csv')
