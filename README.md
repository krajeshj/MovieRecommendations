# MovieRecommendations
This respository is for Movie Recommendation using KNN algorithm. The GroupLens Research Project is a research group in the Department of Computer Science and Engineering at the University of Minnesota. Members of the GroupLens Research Project are involved in many research projects related to the fields of information filtering, collaborative filtering, and recommender systems. The project is lead by professors John Riedl and Joseph Konstan. The project began to explore automated collaborative filtering in 1992, but is most well known for its world wide trial of an automated collaborative filtering system for Usenet news in 1996.  The technology developed in the Usenet trial formed the base for the formation of Net Perceptions, Inc., which was founded by members of GroupLens Research. Since then the project has expanded its scope to research overall information filtering solutions, integrating in content-based methods as well as improving current collaborative filtering technology.
### Data source :
<Permalink: http://grouplens.org/datasets/movielens/100k/>


### Data Set information : 
This data set consists of:
1.100,000 ratings (1-5) from 943 users on 1682 movies. 
2.Each user has rated at least 20 movies. 
3.Simple demographic info for the users (age, gender, occupation, zip)
 
### Problem 
"Based on user preferences, can we predict and recommend with user will like which movies? "

### Client
The client can be streaming movie companies such as Netflix who would be  interested in proposing recommendations for their customers

### Approach 
This is a K-Nearest neighbour problem.
Similarity of user to user prefence is measured as a distance( Pearson distance) to predict a users' preference
For a user, the movies he/she likes will be predicted.
Cross correlation of Users likes and Movies ratings will be used.
 

### Files and Directories
#### Diretories
|Directories | Description|
|:---:|:---|
|.| contains  this README.md file and the python notebook
|code| sub-directory to hold the Python code saved from Jupyter notebook
|data| sub-directory to hold movie lens data 
|rpts| reports and documents|
#### Files
|File|Description
|---------|-------------------------------------------------------------------------------------------------------------------
|code/MovieRecommendations.ipynb| Jupyter notebook viewable with nbviewer|
|code/MovieRecommendations.py | Main python program  file saved from notebook
|data/10k_diabetes.csv| Exporatory csv file  containing a subset of data 
|data/dataset_diabetes/IDs_mapping.csv | csv file with Ids descrption
|data/dataset_diabetes/diabetic_data.csv | This is the data from UCI machine learning repository
|data/ml-100k/u.data |    -- The full u data set, 100000 ratings by 943 users on 1682 items.Each user has rated at least 20 movies.  Users and items arenumbered consecutively from 1.  The data is randomlyordered. This is a tab separated list of user id | item id | rating | timestamp. The time stamps are unix seconds since 1/1/1970 UTC   
|data/ml-100k/u.info |The number of users, items, and ratings in the u data set.
|data/ml-100k/u.item  |Information about the items (movies); this is a tab separated list of movie id | movie title | release date | video release date |IMDb URL | unknown | Action | Adventure | Animation |Children's | Comedy | Crime | Documentary | Drama | Fantasy |Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |Thriller | War | Western |The last 19 fields are the genres, a 1 indicates the movie is of that genre, a 0 indicates it is not; movies can be is several genres at once.The movie ids are the ones used in the u.data data set.
|data/ml-100k/u.genre  | A list of the genres.
|data/ml-100k/u.user   | Demographic information about the users; this is a tab separated list ofuser id | age | gender | occupation | zip codeThe user ids are the ones used in the u.data data set.
|data/ml-100k/u.occupation | A list of the occupations.
|data/ml-100k/u1.base   |  The data sets u1.base and u1.test through u5.base and u5.test
|data/ml-100k/u1.test   |    are 80%/20% splits of the u data into training and test data.
|data/ml-100k/u2.base   |    Each of u1, ..., u5 have disjoint test sets; this if for
|data/ml-100k/u2.test   |    5 fold cross validation (where you repeat your experiment
|data/ml-100k/u3.base   |     with each training and test set and average the results).
|data/ml-100k/u3.test   |    These data sets can be generated from u.data by mku.sh.
|data/ml-100k/u4.base   |
|data/ml-100k/u4.test   |
|data/ml-100k/u5.base   |
|data/ml-100k/u5.test   |
|data/ml-100k/ua.base   | The data sets ua.base, ua.test, ub.base, and ub.test
|data/ml-100k/ua.test   |    split the u data into a training set and a test set with
|data/ml-100k/ub.base   |   exactly 10 ratings per user in the test set.  The sets
|data/ml-100k/ub.test   |   ua.test and ub.test are disjoint.  These data sets can be generated from u.data by mku.sh.
|data/ml-100k/allbut.pl | The script that generates training and test sets where all but n of a users ratings are in the training data.
|data/ml-100k/mku.sh    | A shell script to generate all the u data sets from u.data.


 ### ACKNOWLEDGEMENTS
 1. Prof. Sudhir Wadhwa, Chief Technology Officer, Viridis and Adjunct Lecturer, Santa Clara University
 
 ### Reference
 |Sl. no. |Reference | Details |
 |:---|:---|:----|
 1.|Paper |Herlocker, J., Konstan, J., Borchers, A., Riedl, J.. An Algorithmic Framework for Performing Collaborative Filtering. Proceedings of the 1999 Conference on Research and Development in Information Retrieval. Aug. 1999
 2.|Download Data|< https://grouplens.org/datasets/movielens/100k/>
 3.|Citation |  F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets:History and Context. ACM Transactions on Interactive IntelligentSystems (TiiS) 5, 4, Article 19 (December 2015), 19 pages.DOI=http://dx.doi.org/10.1145/2827872
 4.|ContactGroupLens |<grouplens-info@cs.umn.edu>. 

 
 

 
 
