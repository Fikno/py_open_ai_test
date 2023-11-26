class AssistantHandler:
    def __init__(self, client):
        self.client = client

    def retrieve_assistant(self, assistant_id):
        my_assistant = self.client.beta.assistants.retrieve(assistant_id)
        return my_assistant
        
    def delete_assistant(self, assistant_id):
        response = self.client.beta.assistants.delete(assistant_id)
        return response
        
    def list_all_assistants(self):
        all_assistants = self.client.beta.assistants.list()
        return all_assistants
        
    def filtered_list_assistants(self, limit_param=20, order_param='desc', after_param=None, before_param=None):
        filtered_list = self.client.beta.assistants.list(
            limit = limit_param,
            order = order_param,
            after = after_param,
            before= before_param
        )
        return filtered_list