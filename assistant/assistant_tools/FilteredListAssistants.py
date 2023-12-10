from typing import Optional, Any, Literal
from pydantic import Field
from instructor import OpenAISchema

class FilteredListAssistants(OpenAISchema):
        """
        Python Class constructor for storing the parameters for the function FilteredListAssistants.
        This function will be used to make an api call to the Openai API and return a filtered list of 
        Assistants based off of the parameters provided.
        """

        client: Any = Field(default="",
            description="Open AI Client to be set by the user.")
        limit_param: int = Field(default=20, 
            description= "The maximum number of Assistants to return.Min is 1 Max is 100")
        order_param: Literal["asc", "desc"] = Field(default="desc", 
            description= "order in which the list of Assistants will be returned")
        after_param: Optional[str] = Field(default=None, 
            description= "A cursor for use in pagination. after is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.")
        before_param: Optional[str] = Field(default=None, 
            description= "A cursor for use in pagination. before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.")

        def run(self):
            filtered_list = self.client.beta.assistants.list(
                limit=self.limit_param,
                order=self.order_param,
                after=self.after_param,
                before=self.before_param
            )
            return filtered_list
        
        def is_safe(self) -> bool:
            return True