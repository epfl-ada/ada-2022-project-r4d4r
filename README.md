ada-2022-project-r4d4r
---

Readme.md file containing the detailed project proposal (up to 1000 words). Your README.md should contain:

    Title
    Abstract: A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?
    Research Questions: A list of research questions you would like to address during the project.
    Proposed additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.
    Methods
    Proposed timeline
    Organization within the team: A list of internal milestones up until project Milestone P3.
    Questions for TAs (optional): Add here any questions you have for us related to the proposed project.



# Success or Failure? Predict the success of your future movie!

## Abstract
---
How can we make a successful movie? The script? The plot? The genre? Luck? In this project we want to see if we can find figure out what elements influence the success of a film. Studios would kill to know the secret formula that determines the success or failure of their future films, so let’s see if we can find it. 
The main character: Who is the main character? Main characters come in many shapes and sizes but can they make the movie sink or swim? With the increase in recent controversial casting choices such as Liam Hemsworth to replace Henry Cavill for the Witcher, we want to see how much it matters. Furthermore, the goal of this project is to discover the hidden links between the elements, for instance, what does the main character need to look like when it’s a romantic film vs an adventure film?

We want to look at the effect of the factors individually and when combined, (eg. 30 year old man as the main character for an action film compared to a 20 year old woman for a sci-fi film)


## Research Questions
---
- Who is the main character? 
- What is the most popular type of main character? (Characteristics such height and age)
- How does it vary among genres and which one is the most successful?
- What characteristics of the main character can influence the success of a movie?
- Does the time period of release of the movie affect its success?
- Can we use regression to predict if a movie will be successful?
- Does the gender of the main character influence the success?



## Proposed additional datasets
---
Use of **Cinemagoer**, a python package for retrieving and managing the data of the **IMDb movie database**. This package is used to gain more complete information about the characters in each movie in order to maximise the accuracy rate when finding the main character, as the IMDb database is more complete. We will match the IMDb movies to the Wikipedia using the titles of the movies.

## Methods
---
To find the main character we are making the assumption that the name that appears the most in the synopsis represents the main character. We will find the character who’s first name or last name appears the most with natural language processing. 
To analyse correlation we will use t-test to correlate factors/attributes to success. We will also check the correlation among the attributes as well using the same method. We will also perform a logistic regression trained with the dataset to see if we are able to estimate the box office success of the movie and see which attributes affect it the most.

## Proposed timeline
---


## Organization within the team 
---