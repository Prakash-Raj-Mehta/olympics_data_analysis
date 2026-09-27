import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

st.markdown("""
<style>
    /* Hide Streamlit default header */
    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* Button container - fixed top right */
    .dev-profile-btn {
        margin-top: 80px;
        position: fixed;
        top: 18px;
        right: 28px;
        z-index: 9999;
    }

    .dev-profile-btn a {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 10px 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        text-decoration: none !important;
        font-family: 'Segoe UI', system-ui, sans-serif;
        font-size: 14px;
        font-weight: 600;
        
        border-radius: 50px;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        letter-spacing: 0.3px;
    }

    .dev-profile-btn a:hover {
        cursor: pointer;
        transform: translateY(-3px) scale(1.03);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.55);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }

    .dev-profile-btn a:active {
        transform: translateY(-1px) scale(0.98);
    }

    /* Optional subtle pulse animation on load */
    @keyframes softPulse {
        0% { box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4); }
        50% { box-shadow: 0 4px 22px rgba(102, 126, 234, 0.6); }
        100% { box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4); }
    }

    .dev-profile-btn a {
        animation: softPulse 2.5s ease-in-out infinite;
    }

    .dev-profile-btn a:hover {
        animation: none;
    }
</style>

<div class="dev-profile-btn">
    <a href="https://prakash-raj-mehta.github.io/portfolio/" target="_blank">
        👨‍💻 View Developer Profile
    </a>
</div>
""", unsafe_allow_html=True)

# ---- Your app content starts here ----
st.title("Welcome to My App")


df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')


df = preprocessor.preprocess(df,region_df)

st.sidebar.title('Olympics Analsis')
st.sidebar.image('olampic.jpg')

st.sidebar.title('Olympics Analysis')
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis'))




# st.dataframe(df)
if user_menu == 'Medal Tally':
    st.header('Medal Tally')

    # st.header('Medal Tally')
    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox('Select year',years)
    selected_country= st.sidebar.selectbox('Select country', country )
    medal_tally= helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title('Overall Analysis')
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title('Medal Tally in ' + str(selected_year) )
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title('Medal Tally in ' + selected_country)
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title('Medal Tally in ' + selected_country + str(selected_year) )
    select_mode = st.sidebar.selectbox('select one',('DataFrame','Table'))
    if select_mode == 'DataFrame':
        st.dataframe(medal_tally)
    if select_mode == 'Table':
        st.table(medal_tally)





if user_menu == 'Overall Analysis':
    user_color = st.sidebar.selectbox('Select color',('Blues','Greens','Reds','Oranges','Purples','Greys'))
    user_line = st.sidebar.selectbox('Select color', ('blue', 'green', 'red', 'orange', 'purple', 'grey'))
    editions = df['Year'].unique().shape[0]-1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    col1,col2,col3 = st.columns(3)
    with col1:
        st.header('editions')
        st.title(editions)

    with col2:
        st.header('Hosts')
        st.title(cities)
    with col3:
        st.header('Sport')
        st.title(sports)

    col1,col2,col3 = st.columns(3)
    with col1:
        st.header('Events')
        st.title(events)

    with col2:
        st.header('Nations')
        st.title(nations)
    with col3:
        st.header('Athletes')
        st.title(athletes)

    nations_over_time = helper.participating_nations_over_time(df)
    events_over_time = helper.data_over_time(df,col='Event')
    athletes_over_time = helper.data_over_time(df,col='Name')


    fig1 = px.line(nations_over_time,x = 'Edition',y = 'No of Countries')
    fig2 = px.line(events_over_time,x = 'Edition',y = 'Event')
    fig3 = px.line(athletes_over_time,x = 'Edition',y = 'Name')

    if user_line == 'blue':

        fig1.update_traces(line_color='blue')
        fig2.update_traces(line_color='blue')
        fig3.update_traces(line_color='blue')
    elif user_line == 'green':
        fig1.update_traces(line_color='green')
        fig2.update_traces(line_color='green')
        fig3.update_traces(line_color='green')
    elif user_line == 'red':
        fig1.update_traces(line_color='red')
        fig2.update_traces(line_color='red')
        fig3.update_traces(line_color='red')
    elif user_line == 'orange':
        fig1.update_traces(line_color='orange')
        fig2.update_traces(line_color='orange')
        fig3.update_traces(line_color='orange')
    elif user_line == 'purple':
        fig1.update_traces(line_color='purple')
        fig2.update_traces(line_color='purple')
        fig3.update_traces(line_color='purple')
    elif user_line == 'grey':
        fig1.update_traces(line_color='grey')
        fig2.update_traces(line_color='grey')
        fig3.update_traces(line_color='grey')




    st.title('Participating Nations Over Time')
    st.plotly_chart(fig1)

    st.title('Events over the years')
    st.plotly_chart(fig2)

    st.title('Events over the years')
    st.plotly_chart(fig3)
    st.title('No. of Events over time(Every Sport)')



    fig,ax = plt.subplots(figsize = (20,20))
    x = df.drop_duplicates(['Year','Sport','Event'])
    if user_color == 'Blues':
        ax = sns.heatmap(
            x.pivot_table(index="Sport", columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),cmap='Blues',
            annot=True)
    elif user_color == 'Greens':
        ax = sns.heatmap(
            x.pivot_table(index="Sport", columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),cmap='Greens',
            annot=True)
    elif user_color == 'Reds':
        ax = sns.heatmap(
            x.pivot_table(index="Sport", columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),cmap='Reds',
            annot=True)
    elif user_color == 'Oranges':
        ax = sns.heatmap(
            x.pivot_table(index="Sport", columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),cmap='Oranges',
            annot=True)
    elif user_color == 'Purples':
        ax = sns.heatmap(
            x.pivot_table(index="Sport", columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),cmap='Purples',
            annot=True)
    elif user_color == 'Greys':
        ax = sns.heatmap(
            x.pivot_table(index="Sport", columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),cmap='Grays',
            annot=True)


    st.pyplot(fig)


    st.title('Most successful Athletes')
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')
    selected_sport = st.selectbox('Select Sport',sport_list)
    x = helper.most_successful(df,selected_sport)
    st.table(x)

if user_menu == 'Country-wise Analysis':
    user_color = st.sidebar.selectbox('Select color', ('Blues', 'Greens', 'Reds', 'Oranges', 'Purples', 'Greys'))
    st.sidebar.title('Country wise Analysis')
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()
    selected_country = st.sidebar.selectbox('Select Region',country_list)
    country_df = helper.yearwise_medal_tally(df,selected_country)
    fig = px.line(country_df,x ="Year",y = "Medal")
    st.title("EMedal tally over the years")
    st.plotly_chart(fig)


    st.title(selected_country + 'excels in the following sports')
    pt = helper.country_event_heatmap(df,selected_country)
    fig,ax = plt.subplots(figsize = (20,20))
    x = df.drop_duplicates(['Year','Sport','Event'])
    if user_color == 'Blues':
        ax = sns.heatmap(
            x.pivot_table(index="Sport", columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),cmap='Blues',
            annot=True)
    elif user_color == 'Greens':
        ax = sns.heatmap(
            x.pivot_table(index="Sport", columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),cmap='Greens',
            annot=True)
    elif user_color == 'Reds':
        ax = sns.heatmap(
            x.pivot_table(index="Sport", columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),cmap='Reds',
            annot=True)
    elif user_color == 'Oranges':
        ax = sns.heatmap(
            x.pivot_table(index="Sport", columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),cmap='Oranges',
            annot=True)
    elif user_color == 'Purples':
        ax = sns.heatmap(
            x.pivot_table(index="Sport", columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),cmap='Purples',
            annot=True)
    elif user_color == 'Greys':
        ax = sns.heatmap(
            x.pivot_table(index="Sport", columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),cmap='Grays',
            annot=True)


    st.pyplot(fig)

    st.title('Top 10 athletes os' + selected_country)
    top10_df = helper.most_successful_countrywise(df,selected_country)
    st.table(top10_df)

if user_menu == 'Athlete wise Analysis':
    athlete_df =df.drop_duplicates(subset = ['Name','region'])
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()
    fig = ff.create_distplot([x1, x2, x3, x4],['Over all Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'], show_hist=False, show_rug=False)
    fig.update_layout(autosize = False,width = 1000,height= 600)
    st.title('Distribution of Age')
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports =['Basketball', 'Judo', 'Football', 'Tug-Of-War', ' Athletics', 'Swimming', 'Badminton', 'Sailing', 'Gymnastics', 'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling', 'Water Polo', 'Hockey', 'Rowing', 'Fencing', 'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing', 'Tennis', 'Golf', 'Softball', 'Archery', 'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball', 'Rhythmic Gymnastics', 'Rugby Sevens', 'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        age_data = temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna()
        if len(age_data) > 0:
            x.append(age_data)
            name.append(sport)


    fig = ff.create_distplot(x,name,show_hist= False, show_rug= False)
    fig.update_layout(autosize = False,width = 1000,height= 600)
    st.title('Distribution of Age wrt Sport(Gold Medalist)')
    st.plotly_chart(fig)
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Weight vs Height')
    selected_sport = st.selectbox('Select Sport', sport_list)
    temp_df =helper.weight_v_height(df,selected_sport)
    fig,ax = plt.subplots()
    ax = sns.scatterplot(data = temp_df,x = 'Weight' , y='Height', hue='Medal',style='Sex',s =60)
    st.pyplot(fig)

    st.title('Men vs Women')
    final  = helper.men_vs_women(df)
    fig = px.line(final,x ='Year',y=['Male','Female'])
    st.plotly_chart(fig)
