import os
import openai
import json
import time
from dotenv import load_dotenv

load_dotenv()

class AssistantTools:
    def __init__(self, name, instructions, model, tools=""):
        self.name = str(name)
        self.instructions = str(instructions)
        self.tools = [tools]
        self.model = str(model)
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(
            api_key=self.api_key
        )
        self.assistant = "No Assistant Built Yet"


    def get_name(self):
        return self.name
    
    def get_instructions(self):
        return self.instructions
    
    def get_tools(self):
        return self.tools
    
    def get_model(self):
        return self.model
    
    def set_name(self, name):
        self.name = name

    def set_instructions(self, instructions):
        self.instructions = instructions

    def set_tools(self, tools):
        self.tools = [tools]

    def set_model(self, model):
        self.model = model


    def key_test(self):
        if not self.api_key or not isinstance(self.api_key, str):
            return (False,"No API key saved to 'OPENAI_API_KEY' inside .env file or key not saved as string")
        else:
            return (True,"API key saved to 'OPENAI_API_KEY")
        
    def show_json(self, obj):
        print(json.loads(obj.model_dump_json()))

    def build_assistant(self):
        if self.tools[0] == "":
            self.assistant = self.client.beta.assistants.create(
                name=self.name,
                instructions=self.instructions,
                model=self.model
            )
        else:
            self.assistant = self.client.beta.assistants.create(
                name=self.name,
                instructions=self.instructions,
                tools=self.tools,
                model=self.model
            )





if __name__ == "__main__":

    test = AssistantTools("Test Name", "Test Instructions", "Test Model", "Test Tools")
    print(str(test.get_name()))
    print(str(test.get_instructions()))
    print(str(test.get_model()))
    print(str(test.get_tools()))
    tester = test.key_test()

    if tester[0]:
        print(tester[1])

        test_assist = AssistantTools(
            "Math Tutor", 
            "You are a personal math tutor. Write and run code to answer math questions.",
            "gpt-3.5-turbo-1106"
                    )
        
        test_assist.build_assistant()
        test_assist.show_json(test_assist.assistant)
    if not tester[0]:
        print(tester[1])
        exit()


