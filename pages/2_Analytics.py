import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Plotting Demo")

st.title('Analytics')

# Load data
new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text = pickle.load(open('datasets/feature_text.pkl', 'rb'))


# ---------------------------------------------------------
# Sector Price per Sqft Geomap
# ---------------------------------------------------------

group_df = new_df.groupby('sector')[
    ['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']
].mean()

st.header('Sector Price per Sqft Geomap')

fig = px.scatter_map(
    group_df,
    lat="latitude",
    lon="longitude",
    color="price_per_sqft",
    size="built_up_area",
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    map_style="open-street-map",
    width=1200,
    height=700,
    hover_name=group_df.index,
    center={
        "lat": group_df["latitude"].mean(),
        "lon": group_df["longitude"].mean()
    }
)

st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------------------------
# Features Wordcloud
# ---------------------------------------------------------

st.header('Features Wordcloud')

wordcloud = WordCloud(
    width=800,
    height=800,
    background_color='black',
    stopwords=set(['s']),
    min_font_size=10
).generate(feature_text)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)

st.pyplot(plt)


# ---------------------------------------------------------
# Area Vs Price
# ---------------------------------------------------------

st.header('Area Vs Price')

property_type = st.selectbox(
    'Select Property Type',
    ['flat', 'house']
)

if property_type == 'house':

    fig1 = px.scatter(
        new_df[new_df['property_type'] == 'house'],
        x="built_up_area",
        y="price",
        color="bedRoom",
        title="Area Vs Price"
    )

    st.plotly_chart(fig1, use_container_width=True)

else:

    fig1 = px.scatter(
        new_df[new_df['property_type'] == 'flat'],
        x="built_up_area",
        y="price",
        color="bedRoom",
        title="Area Vs Price"
    )

    st.plotly_chart(fig1, use_container_width=True)


# ---------------------------------------------------------
# BHK Pie Chart
# ---------------------------------------------------------

st.header('BHK Pie Chart')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0, 'overall')

selected_sector = st.selectbox(
    'Select Sector',
    sector_options
)

if selected_sector == 'overall':

    fig2 = px.pie(
        new_df,
        names='bedRoom'
    )

    st.plotly_chart(fig2, use_container_width=True)

else:

    fig2 = px.pie(
        new_df[new_df['sector'] == selected_sector],
        names='bedRoom'
    )

    st.plotly_chart(fig2, use_container_width=True)


# ---------------------------------------------------------
# Side by Side BHK Price Comparison
# ---------------------------------------------------------

st.header('Side by Side BHK price comparison')

fig3 = px.box(
    new_df[new_df['bedRoom'] <= 4],
    x='bedRoom',
    y='price',
    title='BHK Price Range'
)

st.plotly_chart(fig3, use_container_width=True)


# ---------------------------------------------------------
# Side by Side Distplot for Property Type
# ---------------------------------------------------------

st.header('Side by Side Distplot for property type')

fig4 = plt.figure(figsize=(10, 4))

sns.distplot(
    new_df[new_df['property_type'] == 'house']['price'],
    label='house'
)

sns.distplot(
    new_df[new_df['property_type'] == 'flat']['price'],
    label='flat'
)

plt.legend()

st.pyplot(fig4)