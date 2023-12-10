from typing import Any
from pydantic import Field
from instructor import OpenAISchema

class RetrieveAssistant(OpenAISchema):
    """
        Python Class constructor for storing the parameters for the function RetrieveAssistant.
        This function will be used to make an api call to the Openai API and return a single 
        instance of an assistant represented by assistant_id.
    """

    client: Any = Field(default="",
            description="Open AI Client to be set by the user.")
    
    assistant_id: str = Field(...,
        description="The id representing the assistant")
    
    def run(self):
        my_assistant = self.client.beta.assistants.retrieve(self.assistant_id)
        return my_assistant
    

    def is_safe(self) -> bool:
        return False