from typing import Any, Optional, Dict
from pydantic import Field
from instructor import OpenAISchema

class ModifyThread(OpenAISchema):
    """Modify existing thread for communication between user and AI Assistant"""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")
    
    thread_id: str = Field(default="",
        description="The id of the thread to be Modified.")
    
    metadata: Optional[Dict[str, Any]] = Field(default={},
        description="Optional metadata to be set by the user")
    
    def run(self):
        my_thread = self.client.beta.threads.update(self.thread_id)
        return my_thread
    
    def is_safe(self) -> bool:
        return True