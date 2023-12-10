from typing import Any
from pydantic import Field
from instructor import OpenAISchema

class AttachFileOpenAI(OpenAISchema):
    """
    Python Class constructor for storing the parameters for the function AttachFileOpenAI.
    This function will be used to attach, or make available, a file to an AI assistant. This file will be used
     by an AI assistant to complete the task(s).
    """

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")
    
    assistant_id: str = Field(...,
        description="The id representing the assistant")
    
    file_id: str = Field(...,
        description="The id representing the file to be attached to assistant associated with the assistant_id attribute")
    
    def run(self):
        assistant_file = self.client.beta.assistants.files.create(
            assistant_id=self.assistant_id,
            file_id=self.file_id
        )
        return assistant_file
    
    def is_safe(self) -> bool:
        return True