# used this module for retriving relent context 
# and generating response from Mistral AI using HuggingFace
# retiver and generator both inside same componet (ie.e  rag chain)


"""
METHODS 
1) create_prompts(query , context)
2) retriver_and_LLM_Generation

"""


from langchain.prompts import ChatPromptTemplate
from langchain import HuggingFaceHub
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()





def create_prompts():

    template = """

    You are an assistant for a question-generation task.

    Using the retrieved context, generate a relevant question related to the provided topic.
    If the context is insufficient, gererate response for insufficient context.
    Ensure that all questions stay strictly within the topic scope.
    After generating the questions, provide the respective answers from the context.

    Topic: RAG {query}
    Context_RAG: {context}

    Format the output as follows:
    
    
    ALL questions (In numeric order):
    ALL answers( In numeric Order)
    



    """

    prompt = ChatPromptTemplate.from_template(template)

    return prompt




def retriever_and_LLM_Generation(vector_db, prompt, query):
    huggingface_api_token = os.getenv("HUGGINGFACE_TOKEN")

    model = HuggingFaceHub(
        huggingfacehub_api_token=huggingface_api_token,
        repo_id='mistralai/Mistral-7B-Instruct-v0.3',
        model_kwargs={'temperature': 1, 
                      "max_length": 500
                      }
    )

    output_parser = StrOutputParser()
    retriever = vector_db.as_retriever()

    rag_chain = (
        {'context': retriever, 'query': RunnablePassthrough()}
        | prompt
        | model
        | output_parser
    )

    output = rag_chain.invoke(query)

    # Optional: Extract the context from the output if needed
    # Assuming that the output includes both the context and the answer
    index = output.find('ALL questions (In numeric order):')
    answer = output[index:]

    # If you want to return the context as well, you may need to adjust this based on your implementation
    context_index = output.find('Context_RAG')
    context_end_index = output.find('Format the output as follows:')
    
    context = output[context_index:context_end_index] if context_index != -1 else "No context retrieved."
    context = context

    return answer , context