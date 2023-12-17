from typing import Any
from pydantic import Field
from instructor import OpenAISchema


class CancelRun(OpenAISchema):

    """Cancel a run on a thread"""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")

    thread_id: str = Field(...,
        description="The id of the thread of messages between user and AI Assistant.")
    
    run_id: str = Field(...,
        description="ID of the run to be canceled.")

    def run(self):
        run = self.client.beta.threads.runs.cancel(
            thread_id = self.thread_id,
            run_id = self.run_id
        )
        return run
    
    def is_safe(self) -> bool:
        return True