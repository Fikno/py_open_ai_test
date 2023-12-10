from pydantic import Field
from instructor import OpenAISchema
from typing import Optional

class PythonFileWriter(OpenAISchema):
    """
    Python file with an appropriate name, containing code that can be saved and executed locally at a later time. This environment has access to all standard Python packages and the internet.
    """
    chain_of_thought: str = Field(default="",
        description="Think step by step to determine the correct actions that are needed to be taken in order to complete the task.")
    file_name: str = Field(
        ..., description="The name of the file including the extension"
    )
    body: str = Field(..., description="Correct contents of a file")

    def run(self) -> str:
        with open(self.file_name, "w") as f:
            f.write(self.body)

        return "File written to " + self.file_name
    
    def is_safe(self):
        return False
