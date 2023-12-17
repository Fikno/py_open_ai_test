import time
from typing import Any
from pydantic import Field
from instructor import OpenAISchema

from assistant_tools import LazyLoadModule, RetrieveRun, CancelRun, SubmitToolOutputsToRun


class WaitOnRun(OpenAISchema):

    """Wait on a run on a thread and submit tool ouputs to the run if needed."""

    client: Any = Field(default="",
        description="Open AI Client to be set by the user.")

    thread_run : Any = Field(...,
        description="The run to be executed")
    
    thread: Any = Field(...,
        description="The thread the run is excuted on")
    
    def run(self):

        while self.thread_run.status != "completed":

            if self.thread_run.status == "failed":
                print("Run Failed")
                break

            if self.thread_run.status == "cancelled":
                print("Cancelled")
                break

            get_run = RetrieveRun(
                client=self.client,
                thread_id=self.thread.id,
                run_id=self.thread_run.id)
            
            self.thread_run = get_run.run()

            time.sleep(0.2)
            print(self.thread_run.status)
            print()

            if self.thread_run.status == "requires_action":
                function_entries = self.thread_run.required_action.submit_tool_outputs.tool_calls
                functions_info = []
                functions_returns = []

                for entry in function_entries:
                    function_call_id = entry.id
                    function_name = entry.function.name
                    arguments_str = entry.function.arguments

                    functions_info.append((function_call_id, function_name, arguments_str))

                for function in functions_info:
                    inst = LazyLoadModule(function[1], **eval(function[2]))

                    if 'client' in inst.model_dump():
                        inst.client = self.client

                    func_is_safe = inst.is_safe()

                    if not func_is_safe:
                        want_to_run = input(f"do you want to run function: {function[1]}, with the following arguments: {function[2]}?: (y/n)")
                        if want_to_run.lower() != "y":
                            can_run = CancelRun(
                                client=self.client,
                                thread_id=self.thread.id,
                                run_id=self.thread_run.id)
                            can_run.run()
                            print("Cancelled")

                    result = inst.run()

                    functions_returns.append({"tool_call_id": function[0], "output": str(result)})

                if functions_returns:
                    submit = SubmitToolOutputsToRun(
                        client=self.client,
                        thread_id=self.thread.id,
                        run_id=self.thread_run.id,
                        tool_outputs=functions_returns)
                    
                    submit.run()

        return self.thread_run
    

    def is_safe(self) -> bool:
        return True

