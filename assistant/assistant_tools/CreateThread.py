from typing import Any
from pydantic import Field
from instructor import OpenAISchema

class CreateThread(OpenAISchema):
    """Creates a new thread for communication between user and AI Assistant."""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")
    
    messages: str = Field(default="",
        description="A list of messages to start the thread with.")

    def run(self):
        thread = self.client.beta.threads.create(
            messages = [
                    {"role": "user", "content": self.messages}
                ]
        )
        return thread
    
    def is_safe(self) -> bool:
        return True