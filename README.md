# SheHacks Boston Project

## Goal
Create a solution that will help combat the fake news phenomena.

## Competing Categories
- **Google Cloud Platform**

*Google Cloud Platform Award! For the team with the best use of the Google Cloud Platform.*


- **Political Polarization**

*Create a solution that will help combat the fake news phenomena.*


- `She </LEARNS>`

*Beginner Hack Award! For the beginner team (where at least half of team members have never attended a hackathon before) with most ambitous hack.*

## Tools and APIs 
- Python
- Flask
- Google Cloud Natural Language API
- Google Cloud Custom Search API
- Google Cloud Compute Engine
- Google Cloud App Engine

## Implemented Solution
We heavily relied on the Google Cloud Natural Language API to use help us measure the semantic value of different news articles. Based on this semantic value, we can tell the tone of the articles which can help infer whether an article is more opinionated or factual. We created a website that uses many of the Google Cloud APIs that allows the user to enter a phrase, headline, or article; we then take the user's input and find the most relevant keywords to find other articles on the same topic. We search a total of 10 well-known news sources including Fox News, The New York Times, CNN, The Washington Post, Google News, The New Yorker, The Economist, NBC News, ABC News, and CBS News. 

To make this analysis easy to understand, we took the semantic values and made a pie graph to denote what percentages of the articles on the user's topic have a more positive, negative, or neutral tone. 



