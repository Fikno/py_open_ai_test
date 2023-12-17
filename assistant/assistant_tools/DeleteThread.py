from typing import Any
from pydantic import Field
from instructor import OpenAISchema

class DeleteThread(OpenAISchema):
    """Delete existing thread for communication between user and AI Assistant"""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")
    
    thread_id: str = Field(default="",
        description="The id of the thread to be Deleted.")
    
    def run(self):
        response = self.client.beta.threads.delete(self.thread_id)
        return response
    
    def is_safe(self) -> bool:
        return True