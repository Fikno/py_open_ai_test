from typing import Any
from pydantic import Field
from instructor import OpenAISchema

class RetrieveThread(OpenAISchema):
    """Retrieve existing thread for communication between user and AI Assistant"""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")
    
    thread_id: str = Field(default="",
        description="The id of the thread to be retrieved")
    
    def run(self):
        my_thread = self.client.beta.threads.retrieve(self.thread_id)
        return my_thread
    
    def is_safe(self) -> bool:
        return True