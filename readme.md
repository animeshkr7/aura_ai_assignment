#### Running the FastAPI backend 
uvicorn backend:app --reload 


### Running the Front End

streamlit run app.py



To use it :
- Setup the environment
`` python -m venv myenv

`` myenv\Scripts\activate

- install dependencies

`` pip install -r requirements.txt

- create .env file and write the key for :

WEAVIATE_API_KEY = ''

WEAVIATE_CLUSTER =  ''

HUGGINGFACE_TOKEN = ''

for this assignment i have uploaded the link on google drive you can copy paste it( I will delete after 10-15 days):
env link :  https://drive.google.com/file/d/13b2htb0z9QNKk6f5XXKHjEVnxwvWeA8-/view?usp=sharing

- run backend and wait for it to load

`` uvicorn backend:app --reload 

- run frontend :

`` streamlit run app.py

- select the documents(pdf only here) -> upload it to backend -> store the embedding in Vector DB -> write the topic you want to create a question and press to create the question

## NOTE :
 it will provide answer along with the relevent chunk which is used as context for generatio



