import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import statsmodels

import matplotlib.ticker as mtick

from code_strings import code_1, code_2, code_3, code_4, code_5, code_6, code_7, code_8, code_9, code_10

with st.container():
    st.markdown("### Name : Bahige Saab")
    st.markdown("### AUB ID : 200402516")

with st.empty():
    st.markdown('# MSBA-370 Pre-Streamlit Exercise')


with st.container():
    st.markdown("## Exercise 1. Let's take a look at Nobel prize Laureates")
    paragraph1 = components.html("""
            <p><img style="float: right;margin:5px 20px 5px 1px; max-width:250px" src="https://www.nicepng.com/png/detail/11-111010_laurel-wreath-psd37402-laurel-wreath.png"></p>
            <p> In this exercise we will dive into the Nobel prize Laureats dataset by the Nobel Prize Foundation. This dataset lists all prize winners from the start of the prize in 1901 till 2016.</p>
            <p> The Nobel prize is one of the most famous and prestigious intellectual awards. It is awarded annually for 6 different categories. From Stockholm, the Royal Swedish Academy of Sciences confers the prizes for physics, chemistry, and economics, the Karolinska Institute confers the prize for physiology or medicine, and the Swedish Academy confers the prize for literature. The Norwegian Nobel Committee based in Oslo confers the prize for peace.</p>
            
            <p>A person or organization awarded the Nobel Prize is called a Nobel Laureate. The word "laureate" refers to the laurel wreath (إكليل الغار) that was considered as "a trophy" in ancient greek, given to victors of competitions (image to the right).</p><br>
            
            The aim of this exercise is to train you on handling dataframes with Pandas. Main visualization library used will be Seaborn (don't stick to it, focus later on Plotly please).
            """, height=400)


with st.container():
    st.markdown("### Part 1 - Setting up the environment and loading required libraries")
    st.markdown("1.1- Import Pandas, Seaborn and Numpy (as pd, sns and np)")
    st.markdown("1.2- Read in the dataset")
    st.markdown("1.3- Take a look at the first 10 laureates")

with st.empty():
    st.code(code_1, language="python")

nobel = pd.read_csv("datasets/nobel.csv")
nobel.head(10)
nobel.tail()

with st.container():
    st.dataframe(nobel.tail())

with st.container():
    st.markdown("### Part 2 - Which country had most laureates?")
    st.markdown("""
        Just looking at the first couple of prize winners, or Nobel laureates as they are also called, we already see a celebrity: Wilhelm Conrad Röntgen, the guy who discovered X-rays. And actually, we see that all of the winners in 1901 were guys that came from Europe. But that was back in 1901, looking at all winners in the dataset, from 1901 to 2016, which country is the most commonly represented? Also, when did it start to dominate the prize?
        """)
    st.markdown("(For country, we will use the column birth_country of the winner)")


with st.empty():
    st.code(code_2, language="python")

with st.container():
    st.write(f'{len(nobel)}')
    prizes_per_country_df = nobel["birth_country"].value_counts()
    st.dataframe(prizes_per_country_df.head(10))


with st.container():
    st.markdown("### Part 3 - USA-born laureats by decade")
    st.markdown("3.1 - Calculate the proportion of USA born winners per decade")
    st.markdown("3.2 - Display the proportions of USA born winners per decade")

with st.empty():
    st.code(code_3, language="python")

with st.container():
    nobel['usa_born_winner'] = nobel["birth_country"] == "United States of America"
    nobel['decade'] = (np.floor(nobel["year"] / 10) * 10).astype(int)
    prop_usa_winners = nobel.groupby("decade", as_index=False)["usa_born_winner"].mean()
    st.dataframe(prop_usa_winners)

with st.container():
    st.markdown("### Part 4 - USA laureates, visualized")
    st.markdown("A table is OK, but to see when the USA started to dominate the Nobel charts we need a plot!")
    st.markdown("Plot the proportion of USA born winners per decade.")
    st.markdown("4.1 - Use seaborn to plot prop_usa_winners with decade on the x-axis and usa_born_winner on the y-axis as an sns.lineplot. Assign the plot to ax.")
    st.markdown("4.2 - Fix the y-scale so that it shows percentages using PercentFormatter.")


with st.empty():
    st.code(code_4, language="python")


with st.container():
    line_fig = plt.figure(figsize=(11, 7))
    ax = sns.lineplot(data=prop_usa_winners, x='decade', y='usa_born_winner')
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    st.pyplot(line_fig)


with st.container():
    st.markdown("### Part 5 - What is the gender of a typical Nobel Prize winner?")
    st.markdown("So the USA became the dominating winner of the Nobel Prize first in the 1930s and had remained since. If we look at the gender of laureats, we see a clear imbalande. How significant is this imbalance? And is it better or worse within specific prize categories like physics, medicine, literature, etc.? Let's find out. We have to plot the proportions of female laureats by decade split by prize category.")
    st.markdown("5.1 - Add the female_winner column to nobel, where the value is True when sex is **Female**.")
    st.markdown("5.2 - Use groupby to group by both decade and category, setting as_index=False. Then isolate the female_winner column and take the mean(). Assign the resulting DataFrame to prop_female_winners.")
    st.markdown("5.3 - Copy and paste your seaborn plot from part 4 (including axis formatting code), but plot prop_female_winners and map the category variable to the **hue** parameter.")


with st.empty():
    st.code(code_5, language="python")


with st.container():
    nobel['female_winner'] = nobel["sex"] == "Female"
    prop_female_winners = nobel.groupby(["decade", "category"], as_index=False)["female_winner"].mean()

    line_fig_categories = plt.figure(figsize=(11, 7))
    ax = sns.lineplot(data=prop_female_winners, x='decade', y='female_winner', hue="category")
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    st.pyplot(line_fig_categories)
    st.dataframe(prop_female_winners)


with st.container():
    st.markdown("### Part 6 - The first woman to win the Nobel Prize")
    st.markdown("Who was the first woman to receive a Nobel Prize? And in which category?")
    st.markdown("6.1 - Select only the rows of 'Female' winners in nobel.")
    st.markdown("6.2 -Using the nsmallest() method with its n and columns parameters, pick out the first woman to get a Nobel Prize.")


with st.empty():
    st.code(code_6, language="python")

with st.container():
    female_winners = nobel[nobel["sex"] == "Female"]
    smallest = female_winners.nsmallest(1, 'year', keep='first')
    st.dataframe(smallest)


with st.container():
    st.markdown("### Part 7 - Some won more than 1 ! ")
    st.markdown("Who are these few?")
    st.markdown("Extract and display the rows of repeat Nobel Prize winners. Use 'groupby' to group nobel by 'full_name'. Use the 'filter' method to keep only those rows in nobel with winners with 2 or more prizes.")

with st.empty():
    st.code(code_7, language="python")


with st.container():
    twice_or_more_winners = nobel.groupby("full_name").filter(lambda group: len(group) >= 2)
    st.dataframe(twice_or_more_winners)


with st.container():
    st.markdown("### Part 8 - How old are you when you get the prize?")
    st.markdown("Several laureates have received the Nobel prize twice. Marie Curie got the prize in physics for discovering radiation and in chemistry for isolating radium and polonium. John Bardeen got it twice in physics for transistors and superconductivity, Frederick Sanger got it twice in chemistry, and Linus Carl Pauling got it first in chemistry and later in peace for his work in promoting nuclear disarmament. Two organizations also got the prize twice : the Red Cross and the UNHCR.")
    st.markdown("But how old are Laureates generally when they get the prize?")
    st.markdown("Calculate and plot the age of each winner when they won their Nobel Prize.")
    st.markdown("8.1 - Convert the nobel['birth_date'] column to datetime using pd.to_datetime.")
    st.markdown("8.2 - Add a new column nobel['age'] that contains the age of each winner when they got the prize. That is, year of prize win minus birth year.")
    st.markdown("8.3 - Use sns.lmplot (not sns.lineplot) to make a plot with year on the x-axis and age on the y-axis.")


with st.empty():
    st.code(code_8, language="python")

with st.container():
    nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])
    nobel['age'] = nobel['year'] - nobel['birth_date'].dt.year
    fig = sns.lmplot(data=nobel, x='year', y='age', lowess=True, aspect=2, line_kws={'color': 'black'})
    st.pyplot(fig)


with st.container():
    st.markdown("### Part 9 - Age differences between prize categories")
    st.markdown("From the plot above, we can see that people used to be around 55 when they received the prize, but nowadays the average is closer to 65.")
    st.markdown("We can also see that the density of points is much high nowadays than befor, and since the number of prizes is still the same (+1), then this means that nowadays many more of the prizes are shared between several people. We can also see the small gap in prizes around the Second World War (1939 - 1945).")
    st.markdown("Let's look at age trends within different prize categories (use sns.lmplot).")
    st.markdown("You have to Plot how old tha laureats are, within the different price categories.")


with st.empty():
    st.code(code_9, language="python")

with st.container():
    categories = list(nobel["category"].unique())
    category = st.selectbox("Choose a nobel prize category", categories)
    fig_two = sns.lmplot(data=nobel[nobel["category"] == category], x='year', y='age', lowess=True, aspect=2, line_kws={'color': 'black'}, row="category")
    st.pyplot(fig_two)


with st.container():
    st.markdown("### Part 10 - Oldest and youngest winners")
    st.markdown("Who are the oldest and youngest people ever to have won a Nobel Prize? Pick out the rows of the oldest and the youngest winner of a Nobel Prize.")


with st.empty():
    st.code(code_10, language="python")

with st.container():
    st.dataframe(nobel.nlargest(1, 'age', keep='first'))
    st.dataframe(nobel.nsmallest(1, 'age', keep='first'))

with st.container():
    st.markdown("## Done. Nobel Prize in Analytics !")
    image = components.html(""" 
    <p><img style="float: center;margin:5px 20px 5px 1px; max-width:250px" src="https://www.nicepng.com/png/detail/11-111010_laurel-wreath-psd37402-laurel-wreath.png"></p>
    """, height=250)