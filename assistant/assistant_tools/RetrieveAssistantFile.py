from typing import Any
from pydantic import Field
from instructor import OpenAISchema

class RetrieveAssistantFile(OpenAISchema):
    """
    Python Class constructor for storing the parameters for the function RetrieveAssistantFile.
    This function will be used to retrieve a file associated with the AI assistant.
    """

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")
    
    assistant_id: str = Field(...,
        description="The id representing the assistant")
    
    file_id: str = Field(...,
        description="The id representing the file to be retrieved.")
    
    def run(self):
        assistant_file = self.client.beta.assistants.files.retrieve(
            assistant_id=self.assistant_id,
            file_id=self.file_id
        )
        return assistant_file
    
    def is_safe(self) -> bool:
        return True