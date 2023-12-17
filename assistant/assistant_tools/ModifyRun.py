from typing import Optional, Dict, Any
from pydantic import Field
from instructor import OpenAISchema


class ModifyRun(OpenAISchema):

    """Modify a run on a thread."""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")

    thread_id: str = Field(...,
        description="ID of the thread the run was executed on.")
    
    run_id: str = Field(...,
        description="ID of the run to be modified.")
    
    metadata: Optional[Dict[str, Any]] = Field(default={},
        description="Optional metadata to be set by the user")

    def run(self):
        run = self.client.beta.threads.runs.update(
            thread_id = self.thread_id,
            run_id = self.run_id,
            metadata = {self.metadata},
        )
        return run
    
    def is_safe(self) -> bool:
        return True