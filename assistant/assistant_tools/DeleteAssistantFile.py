from typing import Any
from pydantic import Field
from instructor import OpenAISchema

class DeleteAssistantFile(OpenAISchema):
    """
    Python Class constructor for storing the parameters for the function DeleteAssistantFile.
    This function will be used to delete a file associated with the AI assistant.
    """

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")
    
    assistant_id: str = Field(...,
        description="The id representing the assistant")
    
    file_id: str = Field(...,
        description="The id representing the file to be deleted.")
    
    def run(self):
        deleted_assistant_file = self.client.beta.assistants.files.delete(
            assistant_id=self.assistant_id,
            file_id=self.file_id
        )
        return deleted_assistant_file
    
    def is_safe(self) -> bool:
        return True