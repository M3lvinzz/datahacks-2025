# datahacks-2025
Project for Datahacks 2025

## Link to Streamlit Website
https://video-game-classification.streamlit.app/

## Inspiration
Due to the sudden emergence of indie games toppling the video game charts over the past couple of years, we had a rough idea of trying to do a project based on video games. We were inspired after looking at a couple of reviews from looking at one of the biggest video game distributors in the world Steam. 

## What it does
We created a classification model that took in any review that we type in and it would generate a video game genre that would best fit that review description. 

## How we built it
We used Kaggle to find two datasets that contained video game reviews of all sorts of games and used pandas to wrangle and clean the data. Then, we picked different genres for our model to classify reviews into and used sklearn to create and train our data. 

## Challenges we ran into
When we were structuring our genres, there were a lot of concatenation of other genres causing us to have to decide on which genre should take precedence or find a way to work multiple genres into our model. Additionally, choosing the genres that the model would take was another challenge because if we used a genre that was too broad like "Adventure" or "Action" would cause our prediction model to either default to those two genres and nothing else.

## Accomplishments that we're proud of
Getting hands on experience with streamlit, sklearn, and pandas

## What we learned
How to make a more completed product
## What's next for Video Game Genre Classifier 
