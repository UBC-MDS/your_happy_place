# Proposal

Group number: 29

Members : Aldo Saltoa Barros (\@aldojasb), Rada Wilinofsky(\@Radascript), Yair Guterman(\@gutermanyair).

## Motivation and Purpose

Our role: American startup specializing in finding customers their ideal living locations

Target audience: New graduates looking to find where to settle down.

When Finishing university, deciding on a place to live can be daunting and scary. There are so many factors to consider when deciding on a city to settle down in. You need to consider things such as cost of living, temperature, rainfall, snow, health issues, social issues, education, and so many more factors. To help new grads find their 'happy place' we are proposing building a web app where new graduates will be able to interact and filter for the things that they would be looking for in a new home. The app will then narrow down their search and leave the new graduates with good options of US cities for them to live in. Our app will show users where people similar to them have settled and show them through great visualizations how different regions, states or cities differ from one another. We plan to have our app captures many factors such as environmental factors, social factors, demographic factors, and health factors. We pride ourselves on making sure everything that goes into finding a place to settle down will be included in our app..

## Description of the data

We will be visualizing a dataset of approximately 40,000 rows of information from US states. Each row has 50 features for a given state in a given month of the year 2020. Those features can be grouped into the following five clusters:

1.  [WEATHER]{.ul}: `mean_temp`; `max_temp`; `min_temp`; `rain`; `snow`; `hail`; `precipitation`;

2.  [LIVING CONDITIONS]{.ul}: `population_density_per_sqmi`; `presence_of_water_violation`; `percent_severe_housing_problems`; `percent_severe_housing_cost_burden`

3.  [HEALTH]{.ul}: `percent_fair_or_poor_health`; `average_number_of_physically_unhealthy_days`; `average_number_of_mentally_unhealthy_days`; `percent_frequent_physical_distress`; `percent_frequent_mental_distress`; `percent_insufficient_sleep`; `percent_smokers`; `food_environment_index`; `percent_with_access_to_exercise_opportunities`; `percent_excessive_drinking`; `chlamydia_rate`; `primary_care_physicians_rate`; `dentist_rate`; `mental_health_provider_rate`; `preventable_hospitalization_rate`; `percent_vaccinated`

4.  [SOCIAL ISSUES]{.ul}: `life_expectancy`; `child_mortality_rate`; `teen_birth_rate`; `high_school_graduation_rate`; `percent_some_college`; `percent_unemployed_CHR`; `percent_long_commute_drives_alone`; `percent_children_in_poverty; percent_food_insecure`; `violent_crime_rate`; `homicide_rate`; `median_household_income`; `per_capita_income`; `percent_below_poverty`; `percent_unemployed_CDC`; `segregation_index`

5.  [DEMOGRAPHIC]{.ul}: `percent_less_than_18_years_of_age`; `percent_age_17_and_younger`; `percent_65_and_over`; `percent_age_65_and_older`; `percent_disabled`; `percent_non_hispanic_white`; `percent_minorities`; `percent_no_vehicle`

Using this data we will be able to produce insights about what state has the preferable features according to the personal preferences of each person/client of the startup. Those data will fulfill the plots that we will discuss in the README session.

## Research questions and usage scenarios

Jenna has just finished her master's in biology and is looking for her first full-time job as a biologist. She has lived her whole life in Denever Colorado but is wanting to find her 'happy place' and settle somewhere new. She loves warm weather but hates the rain. Additionally, she wants to live in a chill place without crowded centers. Jenna also appreciates the idea of having a good health system around her, it means a place with physicians and facilities for sports and exercises. Another relevant point for Jenna is living in a site where the governmental authorities "does their respective jobs". In other words, she is looking for a state where the government is able to guarantee a healthy economy with jobs opportunities, respecting also the children's rights, and keep the people safe against general crimes. Last but not the least, Jenna also enjoys the idea of multicultural places and would love to see people from other cultures living around her.

When Jenna uses the dash startup's dashboard, she will see information about the weather - average temperature information and rain perspectives -, living conditions such as population density, health such as primary care physicians rate and percent of the population with access to exercise. Finally, she will be able to check the social issues of the states like the percentage of unemployed, crime rates, and demographic factors like the percentage of minorities in the state.

Having all those information, Janne will be able to choose the best state that can fulfill her personal desires for a happy place to live.
