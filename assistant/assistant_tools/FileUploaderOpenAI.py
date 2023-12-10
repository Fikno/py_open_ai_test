from typing import Any
from pydantic import Field
from instructor import OpenAISchema

class FileUploaderOpenAI(OpenAISchema):
    """
    Python Class constructor for storing the parameters for the function FileUploaderOpenAI.
    This function will be used to upload a file to OpenAI using the API. This file will be used
     by an AI assistant to complete the task(s).
    """

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")
    
    file: str = Field(...,
        description="Name of the file to be uploaded to OpenAI to be used by an Assistant. Must include the file extension")
    
    def run(self):
        file = self.client.files.create(
            file=open(self.file, "rb"),
            purpose='assistants'
        )
        return file
    

    def is_safe(self) -> bool:
        return True