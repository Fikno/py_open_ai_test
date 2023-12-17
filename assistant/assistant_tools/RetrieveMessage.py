from typing import Any
from pydantic import Field
from instructor import OpenAISchema


class RetrieveMessage(OpenAISchema):
    """Retrieve a message from specified thread."""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")
    
    message_id: str = Field(...,
        description="ID of the message to be retrieved.")
    
    thread_id: str = Field(...,
        description="ID of the thread the message will be retrieved from.")

    def run(self):
        message = self.client.beta.threads.messages.retrieve(
            message_id=self.message_id,
            thread_id=self.thread_id,
        )
        return message
    
    def is_safe(self) -> bool:
        return True