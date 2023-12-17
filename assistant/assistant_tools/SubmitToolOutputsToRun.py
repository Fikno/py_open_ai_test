from typing import List, Dict, Any
from pydantic import Field
from instructor import OpenAISchema


class SubmitToolOutputsToRun(OpenAISchema):

    """Submit the tool ouputs for the tools called on for a run."""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")

    thread_id: str = Field(...,
        description="The id of the thread of messages between user and AI Assistant.")
    
    run_id: str = Field(...,
        description="ID of the run to submit tool outputs to.")
    
    tool_outputs: List[Dict[str, str]] = Field(...,
        description="list of dictionaries containing the function call id and function output. Example: 'tool_call_id': 'func_call_id', 'output': 'func_output'.")

    def run(self):
        run = self.client.beta.threads.runs.submit_tool_outputs(
            thread_id = self.thread_id,
            run_id = self.run_id,
            tool_outputs = self.tool_outputs
        )
        return run
    
    def is_safe(self) -> bool:
        return True