from typing import Optional, Dict, Any
from pydantic import Field
from instructor import OpenAISchema


class ModifyMessage(OpenAISchema):
    """Modify a specific message from a specific thread."""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")
    
    message_id: str = Field(...,
        description="ID of the message to be modified.")
    
    thread_id: str = Field(...,
        description="ID of the thread of the message that will be modified.")
    
    metadata: Optional[Dict[str, Any]] = Field(default={},
        description="Optional metadata to be set by the user")

    def run(self):
        message = self.client.beta.threads.messages.update(
            message_id = self.message_id,
            thread_id = self.thread_id,
            metadata = self.metadata,
        )
        return message
    
    def is_safe(self) -> bool:
        return True