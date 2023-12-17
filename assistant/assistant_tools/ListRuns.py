from typing import Optional, Literal, Any
from pydantic import Field
from instructor import OpenAISchema


class ListRuns(OpenAISchema):

    """List runs on a thread."""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")
    
    thread_id: str = Field(...,
        description="ID of the thread the runs to be listed were executed on.")
    
    limit: int = Field(default=20,
        description="Amount of runs to be listed. Limit can range between 1 and 100")
    
    order: Literal["asc", "desc"] = Field(default="desc",
        description="ascending or descending order of runs to be listed")
    
    after: Optional[str] = Field(default=None,
        description="A cursor for use in pagination. after is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.")
    
    before: Optional[str] = Field(default=None,
        description="A cursor for use in pagination. before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.")

    def run(self):
        runs = self.client.beta.threads.runs.list(
            thread_id = self.thread_id,
            limit = self.limit,
            order = self.order,
            after = self.after,
            before = self.before
        )
        return runs
    
    def is_safe(self) -> bool:
        return True