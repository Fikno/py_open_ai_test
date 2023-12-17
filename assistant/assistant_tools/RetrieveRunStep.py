from typing import Any
from pydantic import Field
from instructor import OpenAISchema


class RetrieveRunStep(OpenAISchema):

    """Retrieve a single step of a run."""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")

    thread_id: str = Field(...,
        description="ID of the thread the run was executed on.")
    
    run_id: str = Field(...,
        description="ID of the run the step will be retrieved from.")
    
    step_id: str = Field(...,
        description="ID of the step to be retrieved.")
    

    def retrieve_run_step(self, thread_id, run_id, step_id):
        run_step = self.client.beta.threads.runs.steps.retrieve(
            thread_id = thread_id,
            run_id = run_id,
            step_id = step_id
        )
        return run_step
    
    def is_safe(self) -> bool:
        return True