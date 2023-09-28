# Created or modified on May 2022
# Author: 임일
# CB기반 추천

import pandas as pd

# Data 읽기
movies = pd.read_csv('C:/RecoSys/Data/movies_metadata.csv', encoding='latin-1', low_memory=False)
movies = movies[['id', 'title', 'overview']]
movies.head(10)
len(movies)

# 데이터 전처리
movies = movies.drop_duplicates()
movies = movies.dropna()
movies['overview'] = movies['overview'].fillna('')
len(movies)

# 불용어를 english로 지정하고 tf-idf 계산
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])

# Cosine 유사도 계산
from sklearn.metrics.pairwise import cosine_similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
cosine_sim = pd.DataFrame(cosine_sim, index=movies.index, columns=movies.index)

# index-title을 뒤집는다
indices = pd.Series(movies.index, index=movies['title'])

# 영화제목을 받아서 추천 영화를 돌려주는 함수
def content_recommender(title, n_of_recomm):
    # title에서 영화 index 받아오기
    idx = indices[title]
    # 주어진 영화와 다른 영화의 similarity를 가져온다
    sim_scores = cosine_sim[idx]
    # similarity 기준으로 정렬하고 n_of_recomm만큼 가져오기 (자기자신은 빼기)
    sim_scores = sim_scores.sort_values(ascending=False)[1:n_of_recomm+1]
    # 영화 title 반환
    return movies.loc[sim_scores.index]['title']

# 추천받기
print(content_recommender('The Lion King', 5))
print(content_recommender('The Dark Knight Rises', 10))
