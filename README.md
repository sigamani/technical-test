# Technical test

Each question tests aspects of what we require from our data scientists at Qudo. All are important to the growth of our business. Furthermore, these are tasks that are very much part of our current workflow. Choose the question that you feel is your strong point so we get an understanding of where your interests lie. Alternatively, if you want to challenge yourself on something you find more interesting this also helps us understand more about you.

**Please choose one and only one question to answer. You must use python as the core programming language. You may submit your solution however you like (i.e. Github/GitLab repo, compressed folder). The questions are meant to be challenging and somewhat open-ended - Be creative. You must submit your work no later 10 AM (GMT) on Monday the 25th of October.**

## 1. Exploratory Data Analysis ([statista](https://github.com/sigamani/technical-test/tree/main/statista) folder)
Here we have two waves of a consumer survey conducted in the UK between 2020 and 2021. An hotel company has come to you wanting to understand the various dynamics of the UK market when it comes to travel and hospitality. They would like to start a chain of hotels next year in the UK. What can we tell them just based on the data we have? Things to explore (for ideas but feel free to choose your own):
- Clustering to find groups which are based on their travel habits. 
- Are there any distinct audiences you can see to target on Google/Social Media?
- Can you spot anything interesting in terms of trends when you look at the two waves?
- Anything else you think is interesting?
- Are there questions you think are missing that would be useful?

Furthermore, please create a supervised classification model using as the target the "v0154_etra_travelbookings#1" variable. You can go about it however you like using whatever features you want. The survey data is in Travel_survey.csv, ID_ItemLabel_dict.json will map column headings to the actual question text, and MP_Columns_dict.json will map column heading options to their actual text values. 

**What's being tested:** Your ability to sift through data to find answers to the question at hand. Your ability to think of questions not asked by the client. We are also looking at the depth of your statistical knowledge and analytical skills. The final thing we want to see is a strong ability to tell a compelling story using data visualization tools. Knowledge of dashboard platforms is a bonus (Tableau, Plotly). If not, please use a neatly formatted Jupyter Notebook or a slide deck as your output. The quality of your code will also be assessed so feel free to augment this with additional data you think useful if you like (macroeconomic factors, census info) 

**Tech. you should consider:** Jupyter Notebook, Plotly, Tableau, GitHub, GitLab

## 2. Core Python Development ([pipeline-code](https://github.com/sigamani/technical-test/tree/main/pipeline-code) folder)
We would like you to refactor the current analysis pipeline and deploy using a cloud provider of your choice (Heroku is a free and easy solution). The pipeline should be a web app with a run button that runs and outputs a particular segmentation of your choice (rules-based or k-modes). If using Heroku is difficult, simply give instructions to deploy using localhost. 

Things to consider when refactoring: Can we replace our CSV input using a suitable database (MongoDB, PostgreSQL)? Would we be better served using some internally defined business object logic for the storage of our survey data? Can you optimise some of the longer parts of the analysis, such as cost function optimisation for the k-modes algorithm? Are we missing some unit tests? Could we refactor the code to be simpler and easier to read? Could we reorganise the folders and file structure to be neater? You will not be judged on the aesthetics of your web app, this s a python development exercise.

Outside of the refactored code you provide us, please write down any ideas you did not have time to implement you would like to share with us. 

**What's being tested:** The depth of your python development knowledge (classes, testing, clean coding, optimal data storage methods, optimal data object definitions, full-stack development, database queering, refactoring, simplification, optimisation (time and memory), DevOps.

**Tech. you should consider:** Python, Pytest, Heroku, AWS, docker

## 3. Automated Literature Review using NLP
Our company performs market research for clients. After being approached with a problem, we usually spend a considerable amount of time (2-4 weeks) performing a literature review. The aim of the literature review is to distill the goal of the study into a set of survey questions that we think will achieve the required insight. This is a time-consuming process and requires a trained research expert. We are trying to automate some of these steps, but we are very much still in our infancy (as a company and the state-of-the-art in general). Your task is to take this example question from a client:

"Given that we are an online betting company in India, how can we better understand our target market and aquire more customers?"

and create a model that would output a set of key questions to get at the question above. For example, some questions could be "what are the most important things to you when you gamble online?" Alternatively, one could extract a set of higher-level factors, which could then be expanded to questions (i.e. gambling platform preference, desires when betting). The idea here is to leverage the vast amounts of data online alongside deep learning NLP tools to either automate the thought processes of a researcher. Or perhaps just save some time for the early stages. Perhaps the goal could be to one-day outperform a human. 

Things to think about: How transferable is your model? For example would it work it was the same question for the UK or any other country? What if it was a travel agency instead? You are also allowed to use other peoples models with data you've found if you find it applicable (Kaggle or GitHub tend to be good resources) but make sure to cite your sources.

Outside of the model you submit, please write down any ideas you did not have time to implement you would like to share with us.

**What's being tested:** The depth of your ability to identify useful data sources given a problem, data scraping, processing large datasets, the ability to take a large concept and simplify it into some sensible core components, the extent of your Deep Learning knowledge/NLP knowledge.

**Tech. you should consider:** Apart from using python libraries code, it's up to you (some ideas though: knowledge graphs, knowledge extraction, AllenNLP, Wikipedia, Wikidata, Reddit, Q&A forums).
