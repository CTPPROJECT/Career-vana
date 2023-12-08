import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer  
import openai
import os
from openai import OpenAI
from PyPDF2 import PdfReader 
import requests
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())







data_visualize_K = pd.read_csv('data/LocalPayNYC.csv')
data_visualize_B = pd.read_csv('data/b_dataMod.csv')

tabs = st.sidebar.radio("Select a tab", ('Geographic', 'Psychographic', 'Demographic', 'Find Your Perfect Career Sector', 'Generate Cover Letter'))

# Main content
st.title("Careers influenced by various factors over the years")






# Psychographic tab
if tabs == 'Psychographic':
    st.header("Psychographic Section")
    
    # Create a list of available factors (columns) in the CSV file
    available_factors = data_visualize_B.columns.tolist()

    # Let the user choose factors (columns) from the CSV file
    col1, col2, col3 = st.columns(3)  # Create two columns for side-by-side display

    with col1:
        selected_factor1 = st.selectbox('Please select either Sector or Salary', available_factors, key='factor1')
        unique_values_factor1 = data_visualize_B[selected_factor1].unique()
        st.write(f"Unique values in the selected {selected_factor1} column:", unique_values_factor1)

    with col2:
        selected_factor2 = st.selectbox('Please select a Personality Attribute', available_factors, key='factor2')
        unique_values_factor2 = data_visualize_B[selected_factor2].unique()
        st.write(f"Unique values in the selected {selected_factor2} column:", unique_values_factor2)
        
    with col3:
        selected_factor3 = st.selectbox('Please select either Sector or Salary', available_factors, key='factor3')
        unique_values_factor3 = data_visualize_B[selected_factor3].unique()
        st.write(f"Unique values in the selected {selected_factor3} column:", unique_values_factor3)

    # Display box plots
    st.subheader("Box Plots")
    fig_box = px.box(data_visualize_B, x=selected_factor1, y=selected_factor2, color=selected_factor3, title=f"{selected_factor1} {selected_factor2}")
    st.plotly_chart(fig_box)

    # Display histogram
    st.subheader("Bar Chart")
    fig_bar = px.histogram(data_visualize_B,x=selected_factor1, y=selected_factor2, color=selected_factor3, title=f"Employment by {selected_factor1}", barmode='group')   
    st.plotly_chart(fig_bar)
    
    # Display line graph
    st.subheader("Line Graph")
    fig_line = px.line(data_visualize_B, x=selected_factor1, y=selected_factor2, color=selected_factor3, title=f"{selected_factor1} {selected_factor2}")
    st.plotly_chart(fig_line)
    
    # Display Scatter 3D graph
    st.subheader("Scatter 3D Plot")
    fig_scatter_3d = px.scatter_3d(data_visualize_B, x=selected_factor1, y=selected_factor2, z=selected_factor3, title=f"{selected_factor1} vs {selected_factor2} vs {selected_factor3}")
    fig_scatter_3d.update_layout(height=800, width=1000)
    st.plotly_chart(fig_scatter_3d)




elif tabs == 'Geographic':
    st.header("Geographic Section")

    # Load data
    df = pd.read_csv('data/mock_data.csv')

   
    sectors = st.multiselect('Select Employment Sectors', df['employment_sector'].unique())
    if not sectors:
        filtered_df = df
    else:
        filtered_df = df[df['employment_sector'].isin(sectors)]

    
    state_counts = filtered_df['state'].value_counts().reset_index()
    state_counts.columns = ['state', 'count']
    state_avg_salary = filtered_df.groupby('state')['salary'].mean().reset_index()


    map_color = st.selectbox('Select Map Color', ['Viridis', 'Cividis', 'Plasma', 'Inferno'])

    
    map_option = st.selectbox('Select what to display on the map', ['Number of Entries', 'Average Salary'])

    
    if map_option == 'Number of Entries':
        fig = px.choropleth(state_counts, 
                        locations='state', 
                        color='count',  
                        color_continuous_scale=map_color,
                        scope="usa",
                        title='Number of Entries per State')
        st.plotly_chart(fig)
    elif map_option == 'Average Salary':
        fig = px.choropleth(state_avg_salary, 
                        locations='state',  
                        locationmode="USA-states", 
                        color='salary',  
                        color_continuous_scale=map_color,
                        scope="usa",
                        title='Average Salary per State')
        st.plotly_chart(fig)



    

# Demographic tab
elif tabs == 'Demographic':
    st.header("Demographic Section")
    selected_factor = st.selectbox('Select a factor', ['gender', 'ethnicity', 'race'])
    if selected_factor == 'gender':
        data_visualize_K.loc[~data_visualize_K['gender'].isin(['Male', 'Female']), 'gender'] = 'Other gender'
        description_box = "Observations: People identifying as male tend to have the highest salaries followed by women and other genders."
        description_bar = "Observations: Highest percentage of all genders are professionals which could also mean that there is just more data on professionals. Some noteworthy comparisons is that there are more men in skilled craft than female and other gender. women least common professions are skilled craft and service maintenance. men least common are technicians and protective service while other genders least common are administrative support, technicians and skilled craft  "
    elif selected_factor == 'ethnicity':
        description_box = "Non-hispanic or latino tend to be paid the highest. there may be data bias because of the people choosing not to report their ethnicity"
        description_bar = "Ignoring the common professionals,Non-hispanic or latino populations tend to work as paraprofessionals and officials/administrators and least in protective service and skilled craft. while hispanic or latinos are generally the same the difference in paraprofessionals and officials in less which means either of those categories are more common, while in non-hispanic/latinos more tend to lean towards paraprofessionals than officials/administrators   "
    elif selected_factor == 'race':
        description_box = "highest paid race is White while lowest being native hawaian. again this could just correspond to their populations in the US. Moreover this the chart is only showing upper pay bound the average pay could be a different story."
        description_bar = "some notable observations would be white working more in skilled craft than other races, asians and black winning the technicians profession, asians and white significantly more administrators/officials than paraprofessionals. "


        

    # Display box plot and pie chart
    st.subheader("Box Plot")
    fig_box = px.box(data_visualize_K, x=selected_factor, y="upper_pay_band_bound", title=f"Pay Distribution by {selected_factor}")
    st.write(description_box)
    st.plotly_chart(fig_box)

    st.subheader("Bar Plot")
    fig_bar = px.bar(data_visualize_K, x=selected_factor,color="job_category", barmode ="group",title=f"Distribution of Job Categories by {selected_factor}")
    st.write(description_bar)
    st.plotly_chart(fig_bar)

# Find Your Perfect Career Sector tab
elif tabs == 'Find Your Perfect Career Sector':
    monster_df = pd.read_csv('data/monster.csv')

    # Load the model and initialize TfidfVectorizer
    filename = 'pickled_models/finalized_model.sav'
    filename2 = 'pickled_models/finalized_vector.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    loaded_vector = pickle.load(open(filename2,'rb'))
   

    # Define functions for text preprocessing
    def make_lower(a_string):
        return a_string.lower()

    def remove_punctuation(a_string):    
        a_string = re.sub(r'[^\w\s]', '', a_string)
        return a_string

  
    # Text preprocessing function using TfidfVectorizer
    def text_pipeline(input_string):
        input_string = make_lower(input_string)
        input_string = remove_punctuation(input_string) 
        return input_string

    # Streamlit app section
    st.title("Find Your Perfect Career Sector")

    # Text input area
    user_input = st.text_area("Enter your text here:")

    if st.button("Predict"):
        # Process the user input
        processed_input = text_pipeline(user_input)
        X = loaded_vector.transform([processed_input])
        predictions_proba = loaded_model.predict_proba(X)
        classes = loaded_model.classes_
        proba = predictions_proba[0]
        combined = list(zip(classes, proba))
        sorted_combined = sorted(combined, key=lambda x: x[1], reverse=True)
        top_predictions = sorted_combined[:3]
        for i, (predicted_class, probability) in enumerate(top_predictions, start=1):
            st.write(f"Prediction {i}: Career path '{predicted_class}'")

            # Filter dataset by predicted sectors
        selected_sectors = [pred[0] for pred in top_predictions]
        filtered_df = monster_df[monster_df['sector'].isin(selected_sectors)]
        st.subheader("Top States in Predicted Sectors")
        for sector in selected_sectors:
            sector_df = filtered_df[filtered_df['sector'] == sector]
            states_count = sector_df['location'].apply(lambda x: x.split(',')[1].strip() if len(x.split(',')) >= 2 else x.strip()).value_counts()
            top_states = states_count.head(10)
        
        # Create pie chart
            fig_pie = px.pie(values=top_states.values, names=top_states.index, title=f"Top 10 States in '{sector}'")
            st.plotly_chart(fig_pie)
 
     # Display top 10 job titles in each predicted sector
        st.subheader("Top 10 Job Titles in Predicted Sectors")
        for sector in selected_sectors:
            top_jobs = filtered_df[filtered_df['sector'] == sector]['job_title'].value_counts().head(10)
            st.write(f"Top 10 Job Titles in '{sector}':")
            st.write(top_jobs)
    

elif tabs == 'Generate Cover Letter':
    API_URL = "https://api-inference.huggingface.co/models/Sachinkelenjaguri/resume_classifier"
    API_TOKEN = os.getenv('API_TOKEN')  
    openai.api_key  = os.getenv('OPENAI_API_KEY')
    client = OpenAI()
    MAX_SEQUENCE_LENGTH = 512


    st.subheader('Add your Resume and job description to get a tailored cover letter')
    
    job_desc = st.text_area("Copy paste the job description you're interested in")

   
    uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])
    # Mapping of labels to sector names
   
    # Function to get sector name from label
    def get_sector_name(label):
        label_to_sector = {
            'LABEL_0': 'Advocate',
            'LABEL_1': 'Arts',
            'LABEL_2': 'Automation Testing',
            'LABEL_3': 'Blockchain',
            'LABEL_4': 'Business Analyst',
            'LABEL_5': 'Civil Engineer',
            'LABEL_6': 'Data Science',
            'LABEL_7': 'Database',
            'LABEL_8': 'DevOps Engineer',
            'LABEL_9': 'DotNet Developer',
            'LABEL_10': 'ETL Developer',
            'LABEL_11': 'Electrical Engineering',
            'LABEL_12': 'HR',
            'LABEL_13': 'Hadoop',
            'LABEL_14': 'Health and fitness',
            'LABEL_15': 'Java Developer',
            'LABEL_16': 'Mechanical Engineer',
            'LABEL_17': 'Network Security Engineer',
            'LABEL_18': 'Operations Manager',
            'LABEL_19': 'PMO',
            'LABEL_20': 'Python Developer',
            'LABEL_21': 'SAP Developer',
            'LABEL_22': 'Sales',
            'LABEL_23': 'Testing',
            'LABEL_24': 'Web Designing'
        }
        return label_to_sector.get(label, 'Unknown')

    

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        reader = PdfReader(uploaded_file)
        page = reader.pages[0]
        text = page.extract_text()

    
            # Function to extract top 5 classifications
    def extract_top_5(classification_responses):
        top_5_classifications = []
        for response in classification_responses:
            response_json = response.json()
            response_json.sort(key=lambda x: x['score'], reverse=True)  # Sort responses based on score
            top_5_classifications.extend(response_json[:5]) 
            
        top_5_classifications.sort(key=lambda x: x['score'], reverse=True)
        top_5_with_sectors = [{'sector': get_sector_name(classification['label']), 'score': classification['score']} for classification in top_5_classifications[:5]]
        return top_5_with_sectors  


    
    if st.button("Generate Cover Letter"):
         if job_desc and uploaded_file is not None:
            prompt = f"Take this job description: {job_desc} and resume: {text} and write a cover letter tailored to it. Extract previous experience, skills, education, email, address from the resume and extract the company name and what they require from the job description"
            messages = [{"role": "user", "content": prompt}]
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0
            )
            st.write(f"Generated Cover Letter: {response.choices[0].message.content}")

         else:
            st.write("Please fill in the job description and upload a resume before generating a cover letter.")



    if st.button("Classify your Resume"):
        if uploaded_file is not None:
            if len(text) > MAX_SEQUENCE_LENGTH:
                chunks = [text[i:i+MAX_SEQUENCE_LENGTH] for i in range(0, len(text), MAX_SEQUENCE_LENGTH)]
                responses = []
                for chunk in chunks:
                    data = {"text": chunk}  # Adjust payload structure as per API requirements
                    response = requests.post(API_URL, headers={"Authorization": f"Bearer {API_TOKEN}"}, json=data)
                    responses.append(response)
               
                top_5_classifications = extract_top_5(responses)  # Function to extract top 5 classifications
                st.write(f"Top 5 Resume Classifications:")
                for classification in top_5_classifications:
                    st.write(f"Sector: {classification['sector']}, Score: {classification['score']}")
          

                
              
            else:
                 data = {"text": text}
                 response = requests.post(API_URL, headers={"Authorization": f"Bearer {API_TOKEN}"}, json=data)
                 st.write(f"Resume Classification: {response.text}")

        else:
            st.write("Please upload a resume first.")
        











   






   
        