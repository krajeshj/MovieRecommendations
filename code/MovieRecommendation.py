
# coding: utf-8

# In[1]:

import pandas as pd 
r_cols = ['user_id', 'movie', ]
#C:\Users\Rajesh\Documents\GitHub\MovieLens\ml-100k

import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv(r'C:\Users\Rajesh\Documents\GitHub\MovieLens\ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv(r'C:\Users\Rajesh\Documents\GitHub\MovieLens\ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

ratings.head()


# Now we'll pivot this table to construct a nice matrix of users and the movies they rated.
# NaN indicates missing data, or movies that a given user did not watch:

# In[2]:

userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
userRatings.head()


# Now the magic happens - pandas has a built-in corr() method that will compute a correlation score for every column pair in the matrix! This gives us a correlation score between every pair of movies (where at least one user rated both movies - otherwise NaN's will show up.) That's amazing!

# In[3]:

corrMatrix = userRatings.corr()
corrMatrix.head()


# However, we want to avoid spurious results that happened from just a handful of users that happened to rate the same pair of movies. In order to restrict our results to movies that lots of people rated together - and also give us more popular results that are more easily recongnizable - we'll use the min_periods argument to throw out results where fewer than 100 users rated a given movie pair

# In[4]:

corrMatrix = userRatings.corr(method='pearson', min_periods=100)
corrMatrix.head()


# Now let's produce some movie recommendations for , Nancy, user ID 0, who I manually added to the data set as a test case.
# 
# Assuing Nancy likes Star Wars and The Empire Strikes Back, but hated Gone with the Wind.
# 

# In[7]:

NancyRatings = userRatings.loc[1].dropna()
NancyRatings


# Now, let's go through each movie Nancy rated one at a time, and build up a list of possible recommendations based on the movies similar to the ones Nancy rated.
# 
# So for each movie Nancy rated, I'll retrieve the list of similar movies from our correlation matrix. I'll then scale those correlation scores by how well Nancy rated the movie they are similar to, so movies similar to ones Nancy liked count more than movies similar to ones Nancy hated:

# In[8]:

simCandidates = pd.Series()
for i in range(0, len(NancyRatings.index)):
    print ("Adding sims for " + NancyRatings.index[i] + "...")
    # Retrieve similar movies to this one that I rated
    sims = corrMatrix[NancyRatings.index[i]].dropna()
    # Now scale its similarity by how well I rated this movie
    sims = sims.map(lambda x: x * NancyRatings[i])
    # Add the score to the list of similarity candidates
    simCandidates = simCandidates.append(sims)


# This is starting to look like something useful! Note that some of the same movies came up more than once, because they were similar to more than one movie I rated. We'll use groupby() to add together the scores from movies that show up more than once, so they'll count more:
# 

# In[10]:

simCandidates = simCandidates.groupby(simCandidates.index).sum()


# In[11]:

simCandidates.sort_values(inplace = True, ascending = False)
simCandidates.head(8)


# In[ ]:



