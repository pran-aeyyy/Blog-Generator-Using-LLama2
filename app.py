import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

#function to get response from LLAMA2 model

def getLlamaResponse(input_text, no_words, blog_style):
    # Llama2 model
    llm= CTransformers(model = r'C:\Users\Pranay\OneDrive\Desktop\Blog_generation\model\llama-2-7b-chat.ggmlv3.q8_0.bin',
                       model_type = 'llama',
                       config = {'max_new_tokens':256,
                                 'temperature': 0.01})
    
    ##Prompt Template
    template = """
    Write a blog for {blog_style} job profile for the given topic {input_text}
    within the given {no_words} limit of words. 
    """
    
    prompt = PromptTemplate(input_variables=['input_text', 'no_words', 'blog_style'],
                            template= template)
    
    ## Geerate the response from the llama2 model
    response = llm(prompt.format(blog_style = blog_style, no_words = no_words, input_text = input_text))
    print(response)
    return response


st.set_page_config(page_title="Blog Generation",
                   page_icon='💯',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header('Generate My blogs')

input_text = st.text_input("Enter the Blog Topic")

#cReating two more coloumns for additional fields

col1, col2 = st.columns([5,5])

#1st coloumn can be used to set the limit of number of words for the blog
with col1:
    no_words = st.text_input("Enter the Number of Words...")

#the 2nd coloumn can be used to select the style of the blog which can be selected from the dropdown
with col2:
    blog_style = st.selectbox('Writing the blog for...', ('Researchers', 'Data Scientist', 'Common People'), index=0)
    
submit = st.button('Generate')

##Final Response
if submit:
    st.write(getLlamaResponse(input_text, no_words, blog_style))