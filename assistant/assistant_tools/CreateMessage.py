from typing import Optional, Dict, Any, List
from pydantic import Field
from instructor import OpenAISchema

class CreateMessage(OpenAISchema):
    """Create a new message from the user to the AI Assistant."""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")
    
    thread_id: str = Field(...,
        description="The id of the thread of messages between user and AI Assistant this message will be added to.")
    
    user_message: str = Field(...,
        description="Message from user to AI assistant.")
    
    file_ids: Optional[List[str]] = Field(default=[],
        description="A list of file ids representing the file(s) containing information the assistant can use to complete the task")
    
    metadata: Optional[Dict[str, Any]] = Field(default={},
        description="Optional metadata to be set by the user")

    def run(self):
        message = self.client.beta.threads.messages.create(
            self.thread_id,
            role = "user",
            content = self.user_message,
            file_ids = self.file_ids,
            metadata = self.metadata
        )
        return message
    
    def is_safe(self) -> bool:
        return True