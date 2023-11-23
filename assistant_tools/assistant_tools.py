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
        self.assistant = ""
        self.assistant_id = ""
        


    def get_name(self):
        return self.name
    
    def get_instructions(self):
        return self.instructions
    
    def get_tools(self):
        return self.tools
    
    def get_model(self):
        return self.model
    
    def get_client(self):
        return self.client
    
    def get_assistant(self):
        return self.assistant
    
    def get_assistant_id(self):
        return self.assistant_id
    
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
        if self.assistant == "":
            if self.tools[0] == "":
                self.assistant = self.client.beta.assistants.create(
                    name=self.name,
                    instructions=self.instructions,
                    model=self.model
                )
                self.assistant_id = self.assistant.id
            else:
                self.assistant = self.client.beta.assistants.create(
                    name=self.name,
                    instructions=self.instructions,
                    tools=self.tools,
                    model=self.model
                )
                self.assistant_id = self.assistant.id

    def update_assistant_tools(self, new_tools):
        self.assistant = self.client.beta.assistants.update(
            self.assistant.id,
            tools=[new_tools],
        )
        self.set_tools(new_tools)



class AssistantComms:

    def __init__(self, assistant):
        self.client = assistant.get_client()
        self.assistant_id = assistant.get_assistant_id()
        self.thread_ids = []

    def get_client(self):
        return self.client
    
    def get_assistant_id(self):
        return self.assistant_id
    
    def get_thread_ids(self):
        return self.thread_ids

    def create_new_thread(self, thread_name):
        thread = self.client.beta.threads.create()
        self.thread_ids.append([thread_name, thread.id])

    def find_thread(self, thread_name):
        for thread in self.thread_ids:
            if thread[0] == thread_name:
                return thread[1]

    def create_run(self, thread_id, assistant_id):
        run = self.client.beta.threads.runs.create(
        thread_id = thread_id,
        assistant_id = assistant_id,
        )

        return run
    
    def wait_on_run(self, run, thread_id):
        while run.status == "queued" or run.status == "in_progress":
            run = self.client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run.id,
            )
            time.sleep(0.5)
        return run
    
    def submit_message(self, assistant_id, thread_id, user_message):
        self.client.beta.threads.messages.create(
            thread_id=thread_id, role="user", content=user_message
        )
        return self.create_run(thread_id, assistant_id)


    def get_response(self, thread_id):
        return self.client.beta.threads.messages.list(thread_id=thread_id, order="asc")
    
    def message_formater(self, messages):
        
        for m in messages:
            message = f"{m.role}: {m.content[0].text.value}"
            message_without_backslashes = message.replace("\\", "")
            return message_without_backslashes

    
    

if __name__ == "__main__":

    test = AssistantTools("Test Name", "Test Instructions", "Test Model", "Test Tools")
    print(str(test.get_name()))
    print(str(test.get_instructions()))
    print(str(test.get_model()))
    print(str(test.get_tools()))
    tester = test.key_test()

    if tester[0]:
        print(tester[1])

        #test_assist = AssistantTools(
            #"Math Tutor", 
            #"You are a personal math tutor. Write and run code to answer math questions.",
            #"gpt-3.5-turbo-1106"
                    #)
        
        #if test_assist.assistant == "":
            #print("Building Assistant...")
            #test_assist.build_assistant()
            #print("Assistant Built!")
        #else:
            #print("Assistant Already Built!")

        #test_assist.show_json(test_assist.assistant)
        #print("Updating Tools...")
        #test_assist.update_assistant_tools({"type": "code_interpreter"})
        #print(str(test_assist.get_tools()))
        #test_assist.show_json(test_assist.assistant)

        #commer = AssistantComms(test_assist)

        #test_thread = commer.create_new_thread("test_thread")
        #print(commer.find_thread("test_thread"))
        #test_run = commer.submit_message(commer.get_assistant_id(), commer.find_thread("test_thread"), "I need to solve the equation `3x + 11 = 14`. Can you help me?")
        #commer.wait_on_run(test_run, commer.find_thread("test_thread"))
        #commer.pretty_print(commer.get_response(commer.find_thread("test_thread")))

        assistant_list = []

        while True:
            user_input = input("User (enter 'quit' to exit): ")

            if user_input.lower() == "quit":
                break
            else:
                pass


    if not tester[0]:
        print(tester[1])
        exit()


