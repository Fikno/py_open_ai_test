from typing import Any
from pydantic import Field
from instructor import OpenAISchema

class ListAssistantFiles(OpenAISchema):
    """
    Python Class constructor for storing the parameters for the function ListAssistantFiles.
    This function will be used to list all files associated with the AI assistant.
    """

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")

    assistant_id: str = Field(default="",
        description="The id representing the assistant")
    
    def run(self):
        assistant_files = self.client.beta.assistants.files.list(
            assistant_id=self.assistant_id
        )
        return assistant_files
    
    def is_safe(self) -> bool:
        return True