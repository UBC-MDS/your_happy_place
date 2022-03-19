# Proposal

Group number: 29

Members : Aldo Saltao Barros (\@aldojasb), Rada Wilinofsky(\@Radascript), Yair Guterman(\@gutermanyair).

For this reflection, we will describe **both dashboard-python and dashboard-R**, and we will use the template and questions from the lectures notes.

Our app is designed to help new graduates find their ideal US county to live in. We have implemented a dashboard that users are abe to select US counties of their liking and then compare certain characteristics about those selected cities in order to find the best fit for themselves.


# Dashboard-python

**what you have implemented in your dashboard so far** 

Up to now, we have implemented two drop dropdowns to select the state and the cities within them. We also have the bottom to "add" cities and the bottom to "reset" the cities. Moreover, we have implemented the fivicon and 10 different plots so that 4 are bar charts and 6 are line charts.

We also implemented six improvements from the feedback of the last milestones (both TA's and users):

1.  Based on peer review suggestions: we made the time x-axis nicer and more meaningful, and they now have month names for scale.

2.  Based on peer review suggestions: We implemented users' suggestions of putting different charts on different tabs. we sorted them into "Social charts" and "Climate charts." That was a great idea - any future charts can be classified, too.

3.  We added titles and subtitles to sections (now tabs).

4.  Based on peer review suggestions: We implemented users' suggestion that the bar plots would look better horizontal rather than vertical.

5.  Improved padding of everything so the app looks less jammed, and added little thin borders.

6.  Added "for DSCI532" and "by" sections below the title, with links to our team's git profiles.

**Has it been easy to use your app?**

According to the user's feedback, the app is user-friendly and it is capable to generate insights about the cities that they have the interest to move to. It's possible to navigate without any previous assistance and the plots are straightforward about what they want to communicate and compare.

**What differences are there between the DashR and DashPy app?**

Given that python, dash version is pretty much user friendly than the r-version, and the fact that we had more time to work on it, the python dashboard has more fancy implementations than the r-version. Generally speaking, the plots from python libraries are best designed than r-plots and they are also more intuitive and easier to implement.

**Are there reoccurring themes in your feedback on what is good and what can be improved?**

No.

**Is there any feedback (or other insight) that you have found particularly valuable during your dashboard development?**

Generally speaking, the python version of the dashboard seems to be more relevant and more intuitive to work on. There are tons of applications to explore in the interface between python and dash, but there is a shortage of time for it. We would suggest spending less time in the r-version and putting more effort into the python-version of dash.

# Dashboard-R

**what you have implemented in your dashboard so far**

Up to now, we have implemented 10 different plots so that 4 are bar charts and 6 are line charts. Basically, the bar charts are comparing the percentage of unemployed people, population density, percentage of young people (under 17) and percentage of aged people (above 65) for each selected city in the dropdown bar. For the line charts, we have the features meant temperature, precipitation, max temperature, rain, minimum temperature, and snow for each selected city.

**Has it been easy to use your app?**

Generally speaking, the app is easy to use. The user can select the cities in the dropdown bar and compare those 10 features among the selected cities. These features are able to address the core question for a user to decide where he or she wants to move and build a good life, according to his/her values and requirements.

**What differences are there between the DashR and DashPy app?**

As we had less time to work on the R-version and the R-version has a peculiar way to work, making it more difficult to code than the pyhton-version, we chose to deploy a simplified version here. However, it is still possible to answer all the user questions about the best city to live. We faced many problems deploying this R-version on Heroku. But, fortunately, we made it.

**Are there reoccurring themes in your feedback on what is good and what can be improved?**

We don't have review so far for the R-version.

**Is there any feedback (or other insight) that you have found particularly valuable during your dashboard development?**

As general feedback, we should focus more on the python dashboard and don't spend too much time in the R-version. The level of complexity to re-build the python dashboard in R and to deploy it is quite high and it seems it isn't worth it. Maybe we could do only the individual assignment in R and put more time in the python version.
