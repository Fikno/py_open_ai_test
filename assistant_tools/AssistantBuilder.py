import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()

class AssistantBuilder:
    def __init__(self, name, instructions, model, description = None, tools=[], file_ids=[]):
        self.name = name
        self.description = description
        self.instructions = instructions
        self.model = model
        self.tools = tools
        self.file_ids = file_ids
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(
            api_key=self.api_key
        )
        self.assistant = ''
        self.assistant_id = ''

    def get_name(self):
        return self.name

    def get_instructions(self):
        return self.instructions

    def get_model(self):
        return self.model

    def get_tools(self):
        return self.tools

    def get_assistant(self):
        return self.assistant

    def get_assistant_id(self):
        return self.assistant_id
    
    def get_description(self):
        return self.description
    
    def get_client(self):
        return self.client

    def show_json(self, obj):
        print(json.loads(obj.model_dump_json()))

    def get_or_build_assistant(self, assistants_list):
        for assistant_dict in assistants_list:
            if self.name in assistant_dict:
                return assistant_dict[self.name]
        self.assistant = self.client.beta.assistants.create(
                name=self.name,
                description=self.description,
                instructions=self.instructions,
                tools=self.tools,
                model=self.model,
                file_ids=self.file_ids,
                )
        self.assistant_id = self.assistant.id
        return self.assistant_id
    
    def update_assistant_tools(self, new_tools):
        self.assistant = self.client.beta.assistants.update(
            self.assistant.id,
            tools=[new_tools],
        )
        self.tools = new_tools

    def update_assistant_file_ids(self, new_file_ids):
        self.assistant = self.client.beta.assistants.update(
            self.assistant.id,
            file_ids=[new_file_ids],
        )
        self.file_ids = new_file_ids