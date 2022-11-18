# Success or Failure? Predict the success of your future movie!
### Abstract

How can we produce a successful movie? The script? The plot? The genre? Luck? And how has that changed over time? In this project we want to see how the movie characteristics have evolved over time. For instance, we will look at the main character, who are they? What is their gender? Age? Do those characteristics influence the success of the film? We will also look at other factors such as genre and runtime. Furthermore, the goal of this project is to discover correlations between the characteristics and success. For instance, what does the main character need to look like when it’s a romantic film vs an adventure film in order to perform well in the box-office?

### Research Questions

- How has the production of movies changed over time? What kind of features (genre, runtime, main character gender, etc) were in produced movies?
- How have those features impacted the box office over time?
- How well can we correlate production and success?
- Using these insights, can we predict future production and/or the future box office of arbitrary productions?



### Proposed additional datasets

Use of **Cinemagoer**, a python package for retrieving and managing the data of the **IMDb movie database**. This package is used to gain more complete information about the characters in each movie in order to maximise the accuracy rate when finding the main character, as the IMDb database is more complete. We will match the IMDb movies to the Wikipedia using the titles of the movies and release date.

### Methods

#### Step 1: Preprocessing, data scraping
Importing the different dataset and finding a way to retrieve data from IMDB API. Evaluating the kind of movies contained in this dataset. Our dataset contains a decent amount of films with box office values, the type of films were well distributed and seem to represent the industry. From the analysis of the country of release we have mainly USA, some from India and UK, as expected, so the analysis will relate to the popularity in the USA, which seems to match the most popular language release: English, Hindu, Spanish and French. The movie releases represented are mainly from the beginning of the 21th century but overall it is well distributed. Dataset contains some errors, we know this, because we checked the maximum running time (eg. zero tolerance does not last 1079281 minutes) but the IQR look good so it can be corrected with some ease. We can correct the outliers by using the IMDb dataset from Cinemagoers.

#### Step 2: Investigating the evolution of movie production over time and finding main character
To find the main character we are making the assumption that the name that appears the most in the synopsis represents the main character. We will find the character who’s first name or last name appears the most with natural language processing. If no main character is found the movie will be discarded.
Plot the evolution of the main chosen features over time, discretize movies in period of time if relevant.
    
#### Step 3: Box office feature analysis
We will first complete the dataset with imdb box office data using Cinemagoer, as describe at the end of the notebook. Using this data, we will analyze the impact of previously analysed features on the box office. For that we will notably use the χ2 test, to select the most relevant one.
    
#### Step 4: Finding correlation
To analyze correlation between the identified features and success rate of the movies we will use the t-test. We will also check the correlation among the attributes using the same method.
    
    
#### Step 5: Predicting future production and box office
We will perform a linear regression trained with the dataset to see if we are able to estimate the box office value of the movie and see which attributes affect it the most. For this part, we will also use time series forecasting tools such as the Granger causality test, which determines whether one time series contains information to forecast another, or the ARIMA Model, another time series forcasting model.
    
#### Step 6: Final visualisation of the datastory

## Proposed timeline
- Step 2: 25/11/22
- Step 3 and 4: 02/12/22
- Step 5: 09/12/22
- Step 6: 16/12/22

## Organization within the team
- Step 2: Teammate 1 and 2
- Step 3: Teammate 1 and 2
- Step 4: Teammate 3 and 4
- Step 5: Teammate 3 and 4
- Step 6: Teammate 1, 2, 3 and 4

Teammate 1: Blanche<br>
Teammate 2: Martin<br>
Teammate 3: Edouard<br>
Teammate 4: Malena<br>
