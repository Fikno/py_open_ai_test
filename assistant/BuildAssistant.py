class BuildAssistant:
    def __init__(self, client, name=None, description=None, model=None, instructions=None,
                 tools=None, file_ids=None):
        
        """
        Initialize a BuildAssistant object.

        Parameters:
        - client: object or None, Required
          Client object used for authentication with API.

        - name: str or None, Optional
          The name of the assistant. The maximum length is 256 characters.

        - description: str or None, Optional
          The description of the assistant. The maximum length is 512 characters.

        - model: Required
          ID of the model to use. You can use the List models API to see all of your available models,
          or see our Model overview for descriptions of them.

        - instructions: str or None, Optional
          The system instructions that the assistant uses. The maximum length is 32768 characters.

        - tools: list, Optional
          Defaults to an empty list.
          A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant.
          Tools can be of types code_interpreter, retrieval, or function.

        - file_ids: list, Optional
          Defaults to an empty list.
          A list of file IDs attached to this assistant. There can be a maximum of 20 files attached to the assistant.
          Files are ordered by their creation date in ascending order.

        - assistant: object, Optional
          Defaults to an empty dictionary.
          An object. This will not be assigned upon creation of an instance of this object,
          but when a later defined method of this class object is run.

        - assistant_id: str, Optional
          Defaults to an empty string.
          A string value representing the assistant id. This will not be assigned upon creation of an instance of this object,
          but when a later defined method of this class object is run.
        """

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