from typing import Optional, List, Literal, Dict, Any, Type

from pydantic import Field
from instructor import OpenAISchema

class Assistant(OpenAISchema):
    """
    Python class for the creation of OpenaiAPI Assistants. 
    Each Assistant created using this class should be specialized to do one role.
    """

    chain_of_thought: str = Field(default='',
        description="Think step by step to determine the correct actions that are needed to be taken in order to complete the task.")
    
    client: Any = Field(default="",
            description="Open AI Client to be set by the user.")
    
    name: str = Field(...,
        description="A descriptive name of the assistant. Must be between 5 and 80 characters in length.")
    
    description: str = Field(...,
        description="A short description of the assistant")
    
    model: Literal['gpt-3.5-turbo-1106', 'gpt-4-1106-preview'] = Field(...,
        description="The model to be used for the assistant")

    instructions: str = Field(...,
        description="""Concise instructions on what the assistant's job is and how it should be carried out.""")
    
    tools: Optional[List[Dict[str, Any]]] = Field(default=[],
        description="A list of tools available to the assistant to be used to complete task. The list's max length is 128")
    
    file_ids: Optional[List[str]] = Field(default=[],
        description="A list of file ids representing the file(s) containing information the assistant can use to complete the task")
    
    assistant: Optional[Type[object]] = Field(default="",
        description="An instance of the assistant created using the 'build_assistant' method")
    
    assistant_id: Optional[str] = Field(default="",
        description="The id representing the assistant")
    
    
    def run(self):
        self.assistant = self.client.beta.assistants.create(
                name=self.name,
                description=self.description,
                instructions=self.instructions,
                tools=self.tools,
                model=self.model,
                file_ids=self.file_ids,
                )
        self.assistant_id = self.assistant.id

    def update_assistant_tools(self, new_tools):
        self.tools.extend(new_tools)
        self.assistant = self.client.beta.assistants.update(
            self.assistant_id,
            tools=self.tools,
        )

    def is_safe(self) -> bool:
        return True

