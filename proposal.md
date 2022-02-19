# Proposal

Group number: 29

Members : Aldo Saltoa Barros (\@aldojasb), Rada Wilinofsky(\@Radascript), Yair Guterman(\@gutermanyair).

## Motivation and Purpose

Our role: American startup specializing in finding customers their ideal living locations

Target audience: New graduates looking to find where to settle down.

When Finishing university, deciding on a place to live can be daunting and scary. There are so many factors to consider when deciding on a city to settle down in. You need to consider things such as cost of living, temperature, rainfall, snow, health issues , social issues, education, and so many more factors. To help new grads find their 'happy place' we are proposing building a web app where new graduates will be able to interact and filter for the things that they would be looking for in a new home. The app will then narrow down their search and leave the new graduates with good options of US cities for them to live in. Our app will show users where people similar to them have settled and show them through great visualizations how different regions , states or cities differ from one another. We plan to have our app captures many factors such as environmental factors, social factors, demographic factors, and health factors. We pride ourselves on making sure everything that goes into finding a place to settle down will be included in our app.

## Description of the data

We will be visualizing a dataset of approximately 40,000 rows of information from US states. Each rows has 50 features for a given state in a given month of the year 2020. Those features can be grouped in the folowing five clusters:

1.  [WEATHER]{.ul}: `mean_temp`; `max_temp`; `min_temp`; `rain`; `snow`; `hail`; `precipitation`;

2.  [LIVING CONDITIONS]{.ul}: `population_density_per_sqmi`; `presence_of_water_violation`; `percent_severe_housing_problems`; `percent_severe_housing_cost_burden`

3.  [HEALTH]{.ul}: `percent_fair_or_poor_health`; `average_number_of_physically_unhealthy_days`; `average_number_of_mentally_unhealthy_days`; `percent_frequent_physical_distress`; `percent_frequent_mental_distress`; `percent_insufficient_sleep`; `percent_smokers`; `food_environment_index`; `percent_with_access_to_exercise_opportunities`; `percent_excessive_drinking`; `chlamydia_rate`; `primary_care_physicians_rate`; `dentist_rate`; `mental_health_provider_rate`; `preventable_hospitalization_rate`; `percent_vaccinated`

4.  [SOCIAL ISSUES]{.ul}: `life_expectancy`; `child_mortality_rate`; `teen_birth_rate`; `high_school_graduation_rate`; `percent_some_college`; `percent_unemployed_CHR`; `percent_long_commute_drives_alone`; `percent_children_in_poverty; percent_food_insecure`; `violent_crime_rate`; `homicide_rate`; `median_household_income`; `per_capita_income`; `percent_below_poverty`; `percent_unemployed_CDC`; `segregation_index`

5.  [DEMOGRAPHIC]{.ul}: `percent_less_than_18_years_of_age`; `percent_age_17_and_younger`; `percent_65_and_over`; `percent_age_65_and_older`; `percent_disabled`; `percent_non_hispanic_white`; `percent_minorities`; `percent_no_vehicle`

Using this data we will be able to produce insights about what state has the preferable features according to the personal preferences of each person/client of the startup. Those data will fullfil the plots that we will discuss in the README session.

## Research questions and usage scenarios

Jenna has just finished her masters in biology and is looking for her first full time job as a biologist. She has lived her whole life in Denever Colorado but is wanting to find her 'happy place' and settle somewhere new. She loves warm weather but hates the rain. she also ......... etc etc

Aldo: can you please finish the persona. thanks

Example from discription please delete later:

*Mary is a policy maker with the Canadian Ministry of Health and she wants to understand what factors lead to missed appointments in order to devise an intervention that improves attendance numbers. She wants to be able to \[explore\] a dataset in order to \[compare\] the effect of different variables on absenteeism and \[identify\] the most relevant variables around which to frame her intervention policy. When Mary logs on to the “Missed Appointments app”, she will see an overview of all the available variables in her dataset, according to the number of people that did or did not show up to their medical appointment. She can filter out variables for head-to-head comparisons, and/or rank patients according to their predicted probability of missing an appointment. When she does so, Mary may notice that “physical disability” appears to be a strong predictor missing appointments, and in fact patients with a physical disability also have the largest number of missed appointments. She hypothesizes that patients with a physical disability could be having a hard time finding transportation to their appointments, and decides she needs to conduct a follow-on study since transportation information is not captured in her current dataset.*
