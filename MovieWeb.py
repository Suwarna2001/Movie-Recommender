import streamlit as st
import pickle as pk
import pandas as pd
from PIL import Image
import requests
from io import BytesIO


#to read the model
#here movies contain id,title and tags now I want links also so bring new pkl
movies_list=pk.load(open('movies.pkl','rb'))
movies_list=movies_list['title'].values
pkl_file1 = pk.load(open('movies_dict_final.pkl', 'rb'))
pkl_file=pd.DataFrame(pkl_file1)
similarity_pkl=pk.load(open('similarity_1.pkl','rb'))
st.title('Movie Recommender')
st.subheader('')

def recommend(movie):
     movie_index = pkl_file[pkl_file['title'] == movie].index[0]
     distances = similarity_pkl[movie_index]
     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

     recommended_movies=[]
     recommended_poster=[]
     for i in movies_list:
          movie_id = i[0]
          #fetch poster will be available from api
          recommended_movies.append(pkl_file.iloc[i[0]].title)
          recommended_poster.append(pkl_file.iloc[i[0]].Posters)
     return recommended_movies,recommended_poster


def recommended(movie):
    movie_index = pkl_file[pkl_file['title'] == movie].index[0]
    distances = similarity_pkl[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    #recommended_poster = []
    for i in movies_list:
        movie_id = i[0]
        # fetch poster will be available from api
        recommended_movie.append(pkl_file.iloc[i[0]].title)
        #recommended_poster.append(pkl_file.iloc[i[0]].Posters)
    return recommended_movie

st.subheader('Please select which movie would you like to see?')
option = st.selectbox('',movies_list)
st.write('You selected:', option)


if st.button('Show Recommendation'):
  recommendations = recommended(option)
  for i in recommendations:
     st.write(i)
if st.button('Show Recommendation with posters'):

       recommended_movie_names,recommended_movie_posters = recommend(option)
       col1, col2,col3 = st.columns(3)
       col5,col4, col6= st.columns(3)

       with col1:

          st.write(recommended_movie_names[0])
          try:
             url=recommended_movie_posters[0]
             response = requests.get(url)
             img = Image.open(BytesIO(response.content))
             resizedImg = img.resize((625, 525), Image.Resampling.LANCZOS)
             st.image(resizedImg)
          except:
               st.text("Poster not available in DB")
       with col2:
          st.write(recommended_movie_names[1])
          try:
             url=recommended_movie_posters[1]
             response = requests.get(url)
             img = Image.open(BytesIO(response.content))
             resizedImg = img.resize((625, 525), Image.Resampling.LANCZOS)
             st.image(resizedImg)
          except:
               st.text("Poster not available in DB")

       with col3:
          st.write(recommended_movie_names[2])
          try:
             url=recommended_movie_posters[2]
             response = requests.get(url)
             img = Image.open(BytesIO(response.content))
             resizedImg = img.resize((625, 525), Image.Resampling.LANCZOS)
             st.image(resizedImg)
          except:
               st.text("Poster not available in DB")
       with col4:
          st.write(recommended_movie_names[3])
          try:
             url=recommended_movie_posters[3]
             response = requests.get(url)
             img = Image.open(BytesIO(response.content))
             resizedImg = img.resize((625, 525), Image.Resampling.LANCZOS)
             st.image(resizedImg)
          except:
               st.text("Poster not available in DB")
       with col5:
          st.write(recommended_movie_names[4])
          try:
              url = recommended_movie_posters[4]
              response = requests.get(url)
              img = Image.open(BytesIO(response.content))
              resizedImg = img.resize((625, 525), Image.Resampling.LANCZOS)
              st.image(resizedImg)
          except:
              st.text("Poster not available in DB")
       with col6:
           st.write(' ')





# def fetch_poster(movie_id):
#     url = "https://imdb-scraper.p.rapidapi.com/top250".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path




#st.image(filteredImages, width=150, caption=caption)
# for image in filteredImages:
#     r = requests.get(image)
#     img = Image.open(BytesIO(r.content))
#     resizedImg = img.resize((225, 325), Image.ANTIALIAS)
#     resizedImages.append(resizedImg)
# with st.beta_container():
#      for col in st.beta_columns(4):
#           col.image(filteredImages, width=150)



# url='https://image.tmdb.org/t/p/w300_and_h300_face/n9dwu1p5G4qJ4DI5eHJMUbAdOfA.jpg'
# response = requests.get(url)
# img = Image.open(BytesIO(response.content))
# resizedImg = img.resize((225, 325), Image.ANTIALIAS)
#
# st.text('Inception')
# st.image(resizedImg)
# st.text('Inception')
# st.image(resizedImg)
# st.text('Inception')
# st.image(resizedImg)
#
# # for image in filteredImages:
# #     r = requests.get(image)
# #     img = Image.open(BytesIO(r.content))
# #     resizedImg = img.resize((225, 325), Image.ANTIALIAS)#5 movie ko append kerkeimage lagange
# #     resizedImages.append(resizedImg)
#
# with st.container():
#      for col in st.columns(4):
#           col.image(resizedImg, width=160, caption='MOvie')

