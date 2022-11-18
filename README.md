# Success or Failure? Predict the success of your future movie!
### Abstract

How can we make a successful movie? The script? The plot? The genre? Luck? And how has that changed over time? In this project we want to see how the movie characteristics have evolved over time. For instance, we will look at the main character, who are they? What is their gender? Age? What do the distributions look like and can those characteristics influence the success of the film. We will also look at other factors such as genre and runtime. Furthermore, the goal of this project is to discover hidden correlations between the elements and success, for instance, what does the main character need to look like when it’s a romantic film vs an adventure film in order to perform well in the box-office?


### Research Questions

- How has the production of movies changed over time? What kind of features (genre, runtime, main character gender, etc) were in produced movies?
- How have those features impacted the box office over time?
- How well can we correlate production and success?
- Using these insights, can we predict future production and/or the future box office of arbitrary productions?



### Proposed additional datasets

Use of **Cinemagoer**, a python package for retrieving and managing the data of the **IMDb movie database**. This package is used to gain more complete information about the characters in each movie in order to maximise the accuracy rate when finding the main character, as the IMDb database is more complete. We will match the IMDb movies to the Wikipedia using the titles of the movies and release date.

### Methods

How has the production of movies changed over time? What kind of features (genre, runtime, main character gender, etc) were in produced movies?

### How have those features impacted the box office over time?
We will first complete the dataset with imdb box office data. Using this data, we will analyze the impact of previously identified features on the box office.

### How well can we correlate production and success?

### Using these insights, can we predict future production and/or the future box office of arbitrary productions?



We evaluated the kind of movies contained in this dataset. 
Our dataset contains films with decent box office 
The type of films were well distributed and seem to represent the industry.
From the analysis of the country of release we have mainly USA, some from India and UK, as expected, so the analysis will relate to the popularity in the USA, which seems to match the most popular language release: English, Hindu, Spanish and French.

The movie releases represented are mainly from the beginning of the 20th century but overall it is well distributed. Dataset contains some errors, we know this, because we checked the maximum running time (eg. zero tolerance does not last 1079281 minutes) but the IQR look good so it can be corrected with some ease. We corrected the outliers by using the IMDb dataset from Cinemagoers.

#### Finding the main character
To find the main character we are making the assumption that the name that appears the most in the synopsis represents the main character. We will find the character who’s first name or last name appears the most with natural language processing. If no main character is found the movie will be discarded. 

#### Correlation analysis and predicting future production/box office
To analyse correlation we will use t-test to correlate factors/attributes to success. We will also check the correlation among the attributes as well using the same method. We will also perform a logistic regression trained with the dataset to see if we are able to estimate the box office success of the movie and see which attributes affect it the most.

#### Dealing with the sparsity of the data
To handle the amount of missing data we will use IMDb to complete our dataset when needed, in a similar fashion as the methods at the end of the notebook. We start with more than 80000 movies, of those we keep 42204 movies with plot summary and 37779 with at least one character. The 4000 films that do not have any character are considered artifacts so we will drop them from the dataset.



### Proposed timeline and Organization within the team 

`A list of internal milestones up until project Milestone P3.`
Assess the validity of hypothesis of name most mentioned in synopsis equals main character.
Perform the t-test on the various attributes
Perform the regression, while varying the attributes given to see which is the most accurate regression
Evaluate if instead of taking just one main character we should evaluate the most popular ones and consider them the main characters (eg. If the most popular characters appears 11 times, 10 times and 9 times, considering all three)
Determine on the box-office revenue we have 73340 information missing but we are trying to complete it. Either we replace everything with IMDb or replace only some but the revenue is for now and not then. 
We need to adjust the the box office success with the rate of inflation.
Complete the dataset with the boxoffices revenue from IMDb, this is a large dataset, so it will need to run for approximately a week on servers. (to do by Edouard)




## Questions for TAs (optional): 

`Add here any questions you have for us related to the proposed project.`
The 4000 films that do not have any character are considered artifacts so we will drop them from the dataset. Would this be acceptable?
For the pipeline pre-processing we find that some of the questions can be independently answered (no need to remove the movies that do not have a main character from the dataset to see which movie genre is most succesful)


