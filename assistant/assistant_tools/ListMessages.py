from typing import Optional, Literal, Any
from pydantic import Field
from instructor import OpenAISchema


class ListMessages(OpenAISchema):
    """List messages between the user and the AI Assistant on a specific thread."""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")
    
    thread_id: str = Field(...,
        description="ID of the thread of messages to be listed.")
    
    limit: int = Field(default=20,
        description="Amount of messages to be listed. Limit can range between 1 and 100")
    
    order: Literal["asc", "desc"] = Field(default="desc",
        description="ascending or descending order of messages to be listed")
    
    after: Optional[str] = Field(default=None,
        description="A cursor for use in pagination. after is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.")
    
    before: Optional[str] = Field(default=None,
        description="A cursor for use in pagination. before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.")

    def run(self):
        thread_messages = self.client.beta.threads.messages.list(
            self.thread_id,
            limit = self.limit,
            order = self.order,
            after = self.after,
            before = self.before
            )
        return thread_messages
    
    def is_safe(self) -> bool:
        return True