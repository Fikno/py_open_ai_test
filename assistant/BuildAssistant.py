class BuildAssistant:

    """
    A class for building and managing OpenAI ChatGPT Assistants.

    Parameters:
    - client (OpenAIAPI): An instance of the OpenAI API client.
    - name (str): The name of the assistant.
    - description (str): A brief description of the assistant.
    - model (str): The language model used by the assistant.
    - instructions (str): Instructions for the assistant.
    - tools (list): A list of tools to be associated with the assistant.
    - file_ids (list): A list of file IDs to be associated with the assistant.

    Attributes:
    - client (OpenAIAPI): The OpenAI API client instance.
    - name (str): The name of the assistant.
    - description (str): A brief description of the assistant.
    - model (str): The language model used by the assistant.
    - instructions (str): Instructions for the assistant.
    - tools (list): A list of tools associated with the assistant.
    - file_ids (list): A list of file IDs associated with the assistant.
    - assistant (str): The created assistant instance.
    - assistant_id (str): The ID of the created assistant.

    Methods:
    - get_name(): Get the name of the assistant.
    - get_description(): Get the description of the assistant.
    - get_model(): Get the language model used by the assistant.
    - get_instructions(): Get the instructions for the assistant.
    - get_tools(): Get the list of tools associated with the assistant.
    - get_file_ids(): Get the list of file IDs associated with the assistant.
    - get_assistant(): Get the created assistant instance.
    - get_assistant_id(): Get the ID of the created assistant.
    - set_tools(tools): Set the list of tools associated with the assistant.
    - set_file_ids(file_ids): Set the list of file IDs associated with the assistant.
    - update_assistant_tools(new_tools): Update the list of tools associated with the assistant.
    - build_assistant(): Create a new assistant with the specified parameters and store its information.

    Note: Ensure that the OpenAI API client is instantiated before creating an instance of this class.
    """
    
    def __init__(self, client, name=None, description=None, model=None, instructions=None,
                 tools=None, file_ids=None):

        self.client = client
        self.name = name
        self.description = description
        self.model = model
        self.instructions = instructions
        self.tools = tools if tools is not None else []
        self.file_ids = file_ids if file_ids is not None else []
        self.assistant = ''
        self.assistant_id = ''

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_model(self):
        return self.model

    def get_instructions(self):
        return self.instructions

    def get_tools(self):
        return self.tools

    def get_file_ids(self):
        return self.file_ids

    def get_assistant(self):
        return self.assistant

    def get_assistant_id(self):
        return self.assistant_id
    
    def set_tools(self, tools):
        self.tools = tools

    def set_file_ids(self, file_ids):
        self.file_ids = file_ids

    def update_assistant_tools(self, new_tools):
        self.tools.append(new_tools)
        self.assistant = self.client.beta.assistants.update(
            self.assistant_id,
            tools=self.tools,
        )
    
    def build_assistant(self):
        self.assistant = self.client.beta.assistants.create(
                name=self.name,
                description=self.description,
                instructions=self.instructions,
                tools=self.tools,
                model=self.model,
                file_ids=self.file_ids,
                )
        self.assistant_id = self.assistant.id