import pandas as pd
from unittest import main

def calculate_demographic_data(print_data=True):
# Read data from file
    df = pd.read_csv('adult.data.csv')
    
    #df1 = df.set_index('salary').sort_index()
    #duplicate index, .loc not recommended
    
     # serveral hours not through because of case sensitivity!!! FK!
    
    #df2 = df1.loc[df1['salary'].isin(['<=50k'])]
    #df2 = df1.groupby(['salary'])
    #pass
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    
    race_count = df['race'].value_counts()
    #pass
    
    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(),1)
    #pass
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df['education'].value_counts(normalize=True)['Bachelors']*100,1)
    #pass
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    
    df2 = df[['salary','education']]#.value_counts(normalize=True)
    hec = df2.groupby('salary')['education'].value_counts().to_frame()
    
    hec = hec.rename(columns={'education':'count'})
    hec = hec.sort_values(by='education',ascending=False)
    hec = hec.reset_index(level='salary')
    
    higher_education = ['Bachelors','Masters','Doctorate']
    lower_education = set([item for item in hec.index.values.tolist() if item 
                            not in higher_education])
    
    add0 = hec.loc[higher_education]
    add0 = add0.loc[add0['salary'] == '>50K']['count'].sum()
    add1 = hec.loc[higher_education]['count'].sum()
    
    higher_education_rich = round(add0 / add1 *100, 1)   
    
    add0 = hec.loc[lower_education]
    add0 = add0.loc[add0['salary'] == '>50K']['count'].sum()
    add1 = hec.loc[lower_education]['count'].sum()
    
    lower_education_rich = round(add0 / add1 *100, 1)   
    
                 
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours]
    
    num_min_workers = num_min_workers.loc[num_min_workers['salary'] =='>50K']
                          
    
    rich_percentage = num_min_workers.value_counts(normalize=True).sum()*10
    
    # What country has the highest percentage of people that earn >50K?
    df2 = df[['salary','native-country']]#.value_counts(normalize=True)
    #countris = 
    #df2 = df2.set_index('salary')
    hec = df2.groupby('native-country')['salary'].value_counts(normalize=True).to_frame()
    hec = hec.rename(columns={'salary':'percent'})
    hec = hec.sort_values(by='percent',ascending=False)
    hec = hec.reset_index(level='salary')
    hec = hec.loc[hec['salary'] == '>50K']
    highest_earning_country = hec.index.values[0]
    highest_earning_country_percentage = round(hec['percent'][0]*100,1)
    
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[df['native-country'] == 'India']
    top_IN_occupation = top_IN_occupation.loc[top_IN_occupation['salary'] == '>50K']
    top_IN_occupation = top_IN_occupation['occupation'].value_counts().sort_values(ascending=False).index[0]
    
    # DO NOT MODIFY BELOW THIS LINE
    
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)
    
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

#main(module='test_module', exit=False)