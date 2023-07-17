# To help construct our Chat Messages
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
 
# We will be using ChatGPT model (gpt-3.5-turbo)
from langchain.chat_models import ChatOpenAI
 
# To parse outputs and get structured data back
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
 
#To Separtion on Special Json Character[ \n \t (*.)]
import re

# To Converting String into JSON String 
import json

openai_api="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"
        
def generating_mcq(chunks):
        response_schemas = [
        ResponseSchema(name="Question", description="A multiple choice question generated."),
        ResponseSchema(name="Options", description="Possible choices for the multiple choice question."),
        ResponseSchema(name="Answer", description="Correct answer for the question.")
        ]

        # The parser that will look for the LLM output in my schema and return it back to me
        output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

        # The format instructions that LangChain makes. Let's look at them
        format_instructions = output_parser.get_format_instructions()


        # create ChatGPT object
        chat_model = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo',openai_api=openai_api)


        prompt = ChatPromptTemplate(
        messages=[
             
            SystemMessagePromptTemplate.from_template("""The multiple choice question should be in three level, In first level easy,In second level medium, In third level hard """),
            HumanMessagePromptTemplate.from_template("""Generate 10 multiple choice questions from it along with the correct answer. \n 
            {format_instructions} \n
            {user_prompt}
            """)  
        ],
        
        input_variables=["user_prompt"],
        partial_variables={"format_instructions": format_instructions}
        )

        # Passing single chunks 
        for chunk in chunks[:1]:
             
            user_query = prompt.format_prompt(user_prompt = chunk)
            user_query_output =chat_model(user_query.to_messages())

            markdown_text = user_query_output.content

            json_string = re.search(r'```json\n(.*?)```', markdown_text,re.DOTALL).group(1)
            # Convert JSON string to Python list
            python_list = json.loads(f'[{json_string}]')
        
        return python_list