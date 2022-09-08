# Movie-Recommender-System-With-Deployment.
In This Project I am going to build a movie recommendation system project and then build a model and then deploy it on Heroku.

## What is a Recommendation System. 
Recommendation engines are a subclass of machine learning which generally deal with ranking or rating products / users. Loosely defined, a recommender system is a system which predicts ratings a user might give to a specific item.

## Who Uses Recommendation System.
Companies like Amazon, Netflix, Linkedin, and Pandora leverage recommender systems to help users discover new and relevant items (products, videos, jobs, music), creating a delightful user experience while driving incremental revenue.

## Types of Recommender System.
There are three main types of recommendation engines: collaborative filtering, content-based filtering – and a hybrid of the two. 
Collaborative filtering focuses on collecting and analyzing data on user behavior, activities, and preferences, to predict what a person will like, based on their similarity to other users.

## What Are the Types of Recommendation Engines?

There are three main types of recommendation engines: collaborative filtering, content-based filtering – and a hybrid of the two.

### Collaborative filtering

Collaborative filtering focuses on collecting and analyzing data on user behavior, activities, and preferences, to predict what a person will like, based on their similarity to other users.

To plot and calculate these similarities, collaborative filtering uses a matrix style formula. An advantage of collaborative filtering is that it doesn’t need to analyze or understand the content (products, films, books). It simply picks items to recommend based on what they know about the user.

( In short-- users interest based filtering )

### Content-based filtering

Content-based filtering works on the principle that if you like a particular item, you will also like this other item. To make recommendations, algorithms use a profile of the customer’s preferences and a description of an item (genre, product type, color, word length) to work out the similarity of items using cosine and Euclidean distances.  

The downside of content-based filtering is that the system is limited to recommending products or content similar to what the person is already buying or using. It can’t go beyond this to recommend other types of products or content. For example, it couldn’t recommend products beyond homeware if the customer had only brought homeware.

( In short-- content based filtering )

### Hybrid model

A hybrid recommendation engine looks at both the meta (collaborative) data and the transactional (content-based) data. Because of this, it outperforms both.

In a hybrid recommendation engine, natural language processing tags can be generated for each product or item (movie, song), and vector equations used to calculate the similarity of products. A collaborative filtering matrix can then be used to recommend items to users depending on their behaviors, activities, and preferences. Netflix is the perfect example of a hybrid recommendation engine. It takes into account both the interests of the user (collaborative) and the descriptions or features of the movie or show (content-based).  

( In short-- both content and users interest based filtering )

<b>***IN THIS PROJECT I AM GOING TO USE THE TECHNIQUE OF CONTENT-BASE FILTERING***</b>


## Our Project Work Flow :

### Step 1: Data collection.
### Step 2: Preprocessing Our Data.
### Step 3: Building Our Model for prediction.
### Step 4: Making it on website then
### Step 5: Deployment On Heroku.

## Our Page Will Look Like This :

![image](https://user-images.githubusercontent.com/90556877/189056984-88a14357-0841-4445-83d6-a67b5f33d341.png)

### 

## After Recommendations :

![image](https://user-images.githubusercontent.com/90556877/189057250-d10e2b44-f892-4aea-9b6d-aa99a9ee4212.png)

