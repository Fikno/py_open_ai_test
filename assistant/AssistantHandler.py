class AssistantHandler:

    """
    A class that provides methods for managing assistants and associated files
    using the OpenAI API.

    Parameters:
    - client (OpenAIAPI): An instance of the OpenAI API client.

    Methods:
    - retrieve_assistant(assistant_id): Retrieve information about a specific assistant.
    - delete_assistant(assistant_id): Delete a specific assistant.
    - list_all_assistants(): List all available assistants.
    - filtered_list_assistants(limit_param=20, order_param='desc', after_param=None, before_param=None):
        List assistants with optional filtering parameters.
    - file_uploader(file): Upload a file to be associated with assistants.
    - attach_file(assistant_id, file_id): Attach a file to a specific assistant.
    - retrieve_assistant_files(assistant_id, file_id): Retrieve information about a specific file associated with an assistant.
    - delete_assistant_file(assistant_id, file_id): Delete a specific file associated with an assistant.
    - list_assistant_files(assistant_id): List all files associated with a specific assistant.

    Note: Ensure that the OpenAI API client is instantiated before creating an instance of this class.
    """
    
    def __init__(self, client):
        self.client = client

    def retrieve_assistant(self, assistant_id):
        my_assistant = self.client.beta.assistants.retrieve(assistant_id)
        return my_assistant
        
    def delete_assistant(self, assistant_id):
        response = self.client.beta.assistants.delete(assistant_id)
        return response
        
    def list_all_assistants(self):
        all_assistants = self.client.beta.assistants.list(
            limit = 100
        )
        return all_assistants
        
    def filtered_list_assistants(self, limit_param=20, order_param='desc', after_param=None, before_param=None):
        filtered_list = self.client.beta.assistants.list(
            limit = limit_param,
            order = order_param,
            after = after_param,
            before= before_param
        )
        return filtered_list
    
    def file_uploader(self, file):
        file = self.client.files.create(
        file=open(file, "rb"),
        purpose='assistants'
        )

        return file
        
    def attach_file(self, assistant_id, file_id):
        assistant_file = self.client.beta.assistants.files.create(
        assistant_id = assistant_id,
        file_id = file_id
        )

        return assistant_file
        
        
    def retrieve_assistant_files(self, assistant_id, file_id):
        assistant_file = self.client.beta.assistants.files.retrieve(
        assistant_id = assistant_id,
        file_id = file_id
        )

        return assistant_file
    
    def delete_assistant_file(self, assistant_id, file_id):
        deleted_assistant_file = self.client.beta.assistants.files.delete(
        assistant_id = assistant_id,
        file_id = file_id
        )

        return deleted_assistant_file

    def list_assistant_files(self, assistant_id):
        assistant_files = self.client.beta.assistants.files.list(
        assistant_id = assistant_id
        )

        return assistant_files
