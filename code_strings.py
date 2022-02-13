code_1 = '''
        # 1.1- Import Pandas, Seaborn and Numpy (as pd, sns and np)
        import pandas as pd
        import seaborn as sns
        import numpy as np

        #  1.2- Read in the dataset
        # Hint: Use pd.read_csv to read in datasets/nobel.csv and save it into a dataframe "nobel"
        nobel = pd.read_csv("datasets/nobel.csv")

        # 1.3- Take a look at the first 10 laureats
        # Hint: use the method head()
        nobel.head(10)
        nobel.tail()
'''


code_2 = """
        # Display the number of (possibly shared) Nobel Prizes handed between 1901 and 2016.
        # Hint: Count the number of rows/prizes using the len() function. Use the display() function to display the result.
        display(len(nobel))
        
        # Count the number of prizes for each birth_country using value_counts() and show the top 10. Do not use display().
        prizes_per_country_df = nobel["birth_country"].value_counts()
        prizes_per_country_df.head(10)
        """

code_3 = """
        # 3.1 - Add a usa_born_winner column to nobel, where the value is True when birth_country is "United States of America".
        nobel['usa_born_winner'] = nobel["birth_country"]  == "United States of America"
        
        # Add a decade column to nobel for the decade each prize was awarded. Here, np.floor() will come in handy. Ensure the decade column is of type int64.
        # Hint: astype(int)
        # check this example: 
        ## year = pd.Series([1843, 1877, 1923])
        ## decade = (np.floor(year / 10) * 10).astype(int)
        ## decade is now 1840, 1870, 1920
        
        # nobel['decade'] = nobel["year"].apply(lambda year: np.floor(year/10)*10).astype(int)
        nobel['decade'] = (np.floor(nobel["year"]/10)*10).astype(int)
        
        
        # 3.2- Display the proportions of USA born winners per decade
        # Hint: Use groupby to group by decade, setting as_index=False. Then isolate the usa_born_winner column and take the mean(). Assign the resulting DataFrame to prop_usa_winners.
        
        prop_usa_winners= nobel.groupby("decade", as_index=False)["usa_born_winner"].mean()
        prop_usa_winners
        """

code_4 = """
        # Setting the plotting theme (done for you)
        sns.set()
        # and setting the size of all plots. (done for you)
        import matplotlib.pyplot as plt
        plt.rcParams['figure.figsize'] = [11, 7]  # try different numbers once you have the plot
        
        # Plotting USA born winners 
        ax = sns.lineplot(data=prop_usa_winners, x='decade', y='usa_born_winner')
        
        # Adding %-formatting to the y-axis (done for you)
        import matplotlib.ticker as mtick
        from matplotlib.ticker import PercentFormatter
        
        # Use Percent formatter method here
        #Hint: Check this: https://stackoverflow.com/questions/31357611/format-y-axis-as-percent/36319915#36319915
        ax.yaxis.set_major_formatter(mtick.PercentFormatter())
        """

code_5 = """
        # 5.1 - Calculating the proportion of female laureates per decade
        nobel['female_winner'] = nobel["sex"] =="Female"
        
        # 5.2 - Grouping by both decade and category
        #Hint_link: https://stackoverflow.com/questions/17679089/pandas-dataframe-groupby-two-columns-and-get-counts
        prop_female_winners= nobel.groupby(["decade","category"], as_index=False)["female_winner"].mean()
        prop_female_winners
        
        # 5.3 - Plotting USA born winners with % winners on the y-axis (refer to what you did in part 4)
        ax = sns.lineplot(data=prop_female_winners, x='decade', y='female_winner', hue="category")
        ax.yaxis.set_major_formatter(mtick.PercentFormatter())
        """

code_6 = """
        # 6.1 - Select only the rows of 'Female' winners in nobel.

        female_winners = nobel[nobel["sex"]=="Female"]
        female_winners
        
        #6.2 - Using the nsmallest() method with its n and columns parameters, pick out the first woman to get a Nobel Prize.
        # Hint: DataFrame.nsmallest(self, n, columns, keep='first')
        # Hint_link: https://www.w3resource.com/pandas/dataframe/dataframe-nsmallest.php
        #Another Hint_link: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nsmallest.html
        
        female_winners.nsmallest(1, 'year', keep='first')
        """

code_7 = """
        # Selecting the laureates that have received 2 or more prizes.
        twice_or_more_winners = nobel.groupby("full_name").filter(lambda group: len(group) >= 2)
        # twice_or_more_winners = nobel.groupby("full_name").apply(lambda item: print(item))
        twice_or_more_winners
        # Hint: Here is an example of how to use groupby together with filter. This would keep only those rows with birth countries that have had 50 or more winners:
        # nobel.groupby('birth_country').filter(lambda group: len(group) >= 50)
         """

code_8 = """
        # 8.1 - Converting birth_date from String to datetime
        nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])
        nobel.info()
        # Hint: https://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime
        
        # 8.2 - Calculating the age of Nobel Prize winners
        nobel['age'] = nobel['year']-nobel['birth_date'] .dt.year
        nobel.head()
        
        # 8.3 - Plotting the age of Nobel Prize winners: Use sns.lmplot (not sns.lineplot) to make a plot with year on the x-axis and age on the y-axis.
        # To make the plot prettier, add the arguments lowess=True, aspect=2, and line_kws={'color' : 'black'}.
        sns.lmplot(data=nobel, x='year', y='age', lowess=True, aspect=2, line_kws={'color' : 'black'})
        # Hint_link: https://seaborn.pydata.org/generated/seaborn.lmplot.html
        """

code_9 = """
        # As before, use sns.lmplot to make a plot with year on the x-axis and age on the y-axis. But this time, make one plot per prize category by setting the row argument to 'category'
        # Hint: Copy and paste your solution from task 8 and then add the argument row='category' to the function call..
        sns.lmplot(data=nobel, x='year', y='age', lowess=True, aspect=2, line_kws={'color' : 'black'},row='category')
        # Scroll down to see the several plots. One by category. Beautiful!
        """

code_10 = """
          # The oldest winner of a Nobel Prize as of 2016
          # Hint: Use nlargest() to pick out and display the row of the oldest winner.
          nobel.nlargest(1, 'age', keep='first')
        
        # The youngest winner of a Nobel Prize as of 2016
        # Hint: Use nsmallest() to pick out and display the row of the youngest winner.
        nobel.nsmallest(1, 'age', keep='first')
        """