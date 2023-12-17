from typing import Any
from pydantic import Field
from instructor import OpenAISchema

class RetrieveMessageFile(OpenAISchema):
    """Retrieve a file associated with a given message"""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")
    
    thread_id: str = Field(...,
        description="ID of the thread of messages associated with the file.")
    
    message_id: str = Field(...,
        description="ID of the message the file is associated with.")
    
    file_id: str = Field(...,
        description="The id representing the file to be retrieved.")

    def run(self):
        message_files = self.client.beta.threads.messages.files.retrieve(
            thread_id = self.thread_id,
            message_id = self.message_id,
            file_id = self.file_id
        )
        return message_files
    
    def is_safe(self) -> bool:
        return True