from pydantic import Field
from typing import Any
from instructor import OpenAISchema

class DeleteAssistant(OpenAISchema):
    """
    Python Class constructor for storing the parameters for the function DeleteAssistant.
    This function will be used to make an API call to the Openai API and delete a single 
    instance of an assistant to be represented by assistant_id.
    """
    
    client: Any = Field(default="",
            description="Open AI Client to be set by the user.")
    
    assistant_id: Any = Field(...,
        description="The id representing the assistant")
    
    def delete_assistant(self):
        response = self.client.beta.assistants.delete(self.assistant_id)
        return response
    
    def run(self) -> Any:
        self.delete_assistant()

    def is_safe(self) -> bool:
        return False
