from typing import Optional, Any
from pydantic import Field
from instructor import OpenAISchema

class CreateThreadAndRun(OpenAISchema):

    """Create a new thread and initialize a run on the thread"""

    client: Any = Field(default="",
            description="Open AI Client to be set by the user.")

    assistant_id: str = Field(...,
        description="The id representing the assistant")
    
    user_input: Optional[str] = Field(default="",
        description="initial user message on a new thread")

    def run(self):
        run = self.client.beta.threads.create_and_run(
            assistant_id = self.assistant_id,
            thread={
                "messages": [
                    {"role": "user", "content": self.user_input}
                ]
            }
        )
        return run
    
    def is_safe(self) -> bool:
        return True