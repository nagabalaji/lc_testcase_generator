from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_test_cases(user_story, acceptance_criteria):
    llm = openai.OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=['user_story', 'acceptance_criteria'],
        template="You can do better. Write two positive and two negative Gherkin Scenarios with testable examples for the user story, {user_story} and for the acceptance criteria, {acceptance_criteria} with testable examples.",
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name,output_key="test_cases")

    response = name_chain({'user_story': user_story, 'acceptance_criteria': acceptance_criteria})
    return response

if __name__ == "__main__":
    print(generate_test_cases("As a user, I want to log in to saucedemo.com website", "Verify that the login functionality works correctly"))