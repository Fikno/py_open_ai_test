from typing import Optional, List, Literal, Dict, Any
from pydantic import Field
from instructor import OpenAISchema


class CreateRun(OpenAISchema):

    """Represents an execution run on a thread."""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")

    thread_id: str = Field(...,
        description="ID of the thread the run will be executed on.")
    
    assistant_id: str = Field(...,
        description="The id representing the AI assistant used for this run.")
    
    model: Optional[Literal['gpt-3.5-turbo-1106', 'gpt-4-1106-preview']] = Field(default=None,
        description="The model to be used by the assistant in this run.")
    
    instructions: Optional[str] = Field(default=None,
        description="""Concise instructions on what the assistant's job is on this run and how it should be carried out.""")
    
    tools: Optional[List[Dict[str, Any]]] = Field(default=[],
        description="A list of tools available to the assistant to be used in this run to complete task. The list's max length is 128")
    
    metadata: Optional[Dict[str, Any]] = Field(default={},
        description="Optional metadata to be set by the user")
    


    def run(self):
        run = self.client.beta.threads.runs.create(
            thread_id = self.thread_id,
            assistant_id = self.assistant_id,
            model = self.model,
            instructions = self.instructions,
            tools = self.tools,
            metadata = self.metadata
        )
        return run
    
    def is_safe(self) -> bool:
        return True