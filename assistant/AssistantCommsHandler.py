import time
import json
from FunctionManager import FunctionManager

class AssistantCommsHandler:
    """
    A class that provides methods for interacting with communication threads and runs
    using the OpenAI API.

    Parameters:
    - client (OpenAIAPI): An instance of the OpenAI API client.

    Methods:
    - create_thread(messages=None): Create a new communication thread.
    - retrieve_thread(thread_id): Retrieve information about a specific thread.
    - modify_thread(thread_id): Modify the properties of a specific thread.
    - delete_thread(thread_id): Delete a specific thread.
    - create_message(thread_id, user_input, file_ids=None, metadata=None): Create a new message in a thread.
    - retrieve_message(message_id, thread_id): Retrieve information about a specific message in a thread.
    - modify_message(message_id, thread_id, metadata=None): Modify the properties of a specific message in a thread.
    - list_messages(thread_id, limit=20, order="desc", after=None, before=None): List messages in a thread.
    - retrieve_message_file(thread_id, message_id, file_id): Retrieve information about a file attached to a message.
    - list_message_files(thread_id, message_id, limit=20, order="desc", after=None, before=None): List files attached to a message.
    - create_run(thread_id, assistant_id, model=None, instructions=None, tools=None, metadata=None): Create a new run in a thread.
    - retrieve_run(thread_id, run_id): Retrieve information about a specific run in a thread.
    - modify_run(thread_id, run_id, metadata=None): Modify the properties of a specific run in a thread.
    - list_runs(thread_id, limit=20, order="desc", after=None, before=None): List runs in a thread.
    - submit_tool_outputs_to_run(thread_id, run_id, tool_outputs={}): Submit tool outputs to a specific run in a thread.
    - cancel_run(thread_id, run_id): Cancel a specific run in a thread.
    - create_thread_and_run(assistant_id, user_input): Create a new thread and run with a user input message.
    - retrieve_run_step(thread_id, run_id, step_id): Retrieve information about a specific step in a run.
    - list_run_steps(thread_id, run_id, limit=20, order="desc", after=None, before=None): List steps in a run.
    - wait_on_run(run, thread): Wait for a run to complete before proceeding.

    Note: Ensure that the OpenAI API client is instantiated before creating an instance of this class.
    """

    def __init__(self, client, dbhost, dbname, dbuser, dbpassword, dbport):
        self.client = client
        self.dbhost = dbhost
        self.dbname = dbname
        self.dbuser = dbuser
        self.dbpassword = dbpassword
        self.dbport = dbport

    def create_thread(self, messages = None):
        thread = self.client.beta.threads.create(
            messages = [messages]
        )
        return thread
    
    def retrieve_thread(self, thread_id):
        my_thread = self.client.beta.threads.retrieve(thread_id)
        return my_thread
    
    def modify_thread(self, thread_id):
        my_thread = self.client.beta.threads.update(thread_id)
        return my_thread
    
    def delete_thread(self, thread_id):
        response = self.client.beta.threads.delete(thread_id)
        return response
    
    def create_message(self, thread_id, user_input, file_ids = [], metadata = {}):
        message = self.client.beta.threads.messages.create(
            thread_id,
            role = "user",
            content = user_input,
            file_ids = file_ids,
            metadata = metadata
        )

        return message
    
    def retrieve_message(self, message_id, thread_id):
        message = self.client.beta.threads.messages.retrieve(
            message_id=message_id,
            thread_id=thread_id,
        )

        return message
    
    def modify_message(self, message_id, thread_id, metadata = {}):
        message = self.client.beta.threads.messages.update(
            message_id = message_id,
            thread_id = thread_id,
            metadata=metadata,
        )

        return message
    
    def list_messages(self, thread_id, limit = 20, order = "desc", after = None, before = None):
        thread_messages = self.client.beta.threads.messages.list(
            thread_id,
            limit = limit,
            order = order,
            after = after,
            before = before
            )
        
        return thread_messages
    
    def retrieve_message_file(self, thread_id, message_id, file_id):
        message_files = self.client.beta.threads.messages.files.retrieve(
            thread_id = thread_id,
            message_id = message_id,
            file_id = file_id
        )

        return message_files
    
    def list_message_files(self, thread_id, message_id, limit = 20, order = "desc", after = None, before = None):
        message_files = self.client.beta.threads.messages.files.list(
            thread_id = thread_id,
            message_id = message_id,
            limit = limit,
            order = order,
            after = after,
            before = before
        )

        return message_files
    
    def create_run(self, thread_id, assistant_id, model=None, instructions=None, tools=None, metadata=None):
        run = self.client.beta.threads.runs.create(
            thread_id = thread_id,
            assistant_id = assistant_id,
            model = model,
            instructions = instructions,
            tools = tools,
            metadata = metadata
        )

        return run
    
    def retrieve_run(self, thread_id, run_id):
        run = self.client.beta.threads.runs.retrieve(
            thread_id = thread_id,
            run_id = run_id
        )

        return run
    
    def modify_run(self, thread_id, run_id, metadata = None):
        run = self.client.beta.threads.runs.update(
            thread_id = thread_id,
            run_id = run_id,
            metadata = {metadata},
        )

        return run
    
    def list_runs(self, thread_id, limit = 20, order = "desc", after = None, before = None):
        runs = self.client.beta.threads.runs.list(
            thread_id = thread_id,
            limit = limit,
            order = order,
            after = after,
            before = before
        )

        return runs
    
    def submit_tool_outputs_to_run(self, thread_id, run_id, tool_outputs = {}):
        run = self.client.beta.threads.runs.submit_tool_outputs(
            thread_id = thread_id,
            run_id = run_id,
            tool_outputs=tool_outputs
        )

        return run
    
    def cancel_run(self, thread_id, run_id):
        run = self.client.beta.threads.runs.cancel(
            thread_id = thread_id,
            run_id = run_id
        )

        return run
    
    def create_thread_and_run(self, assistant_id, user_input):
        run = self.client.beta.threads.create_and_run(
            assistant_id = assistant_id,
            thread={
                "messages": [
                    {"role": "user", "content": user_input}
                ]
            }
        )

        return run
    
    def retrieve_run_step(self, thread_id, run_id, step_id):
        run_step = self.client.beta.threads.runs.steps.retrieve(
            thread_id = thread_id,
            run_id = run_id,
            step_id = step_id
        )

        return run_step
    
    def list_run_steps(self, thread_id, run_id, limit = 20, order = "desc", after = None, before = None):
        run_steps = self.client.beta.threads.runs.steps.list(
            thread_id = thread_id,
            run_id = run_id,
            limit = limit,
            order = order,
            after = after,
            before = before
        )

        return run_steps
    
    def wait_on_run(self, run, thread):
        functions_returns = []

        while run.status != "completed":
            run = self.retrieve_run(
                thread_id=thread.id,
                run_id=run.id,
            )
            time.sleep(0.5)
            #print(run.status)

            if run.status == "requires_action":
                data = json.loads(run.model_dump_json())
                function_entries = data["required_action"]["submit_tool_outputs"]["tool_calls"]
                functions_info = []

                for entry in function_entries:
                    function_call_id = entry["id"]
                    function_name = entry["function"]["name"]
                    arguments_str = json.loads(entry["function"]["arguments"])

                    functions_info.append((function_call_id, function_name, arguments_str))

                function_manager = FunctionManager(self.dbhost, self.dbname, self.dbuser, self.dbpassword, self.dbport)

                for function in functions_info:
                    function_info_from_db = function_manager.retrieve_function_is_safe_by_name(function[1])
                    db_function = function_info_from_db[0]
                    db_is_safe = function_info_from_db[1]
                    exec_result = {}

                    print(f"Function Call ID: {function[0]}, Function Name: {function[1]}, Arguments: {function[2]}")

                    if not db_is_safe:
                        want_to_run = input(f"do you want to run function: {function[1]}, with the following arguments: {function[2]}?: (y/n)")
                        if want_to_run.lower() != "y":
                            self.cancel_run(thread.id, run.id)
                            print("Canceled")

                    exec(db_function, exec_result)

                    db_to_py_function = exec_result.get(function[1])
                    result = db_to_py_function(function[2])

                    functions_returns.append({"tool_call_id": function[0], "output": str(result)})

                function_manager.close_connection()

                if functions_returns:
                    self.submit_tool_outputs_to_run(thread.id, run.id, functions_returns)
                    print("Returns")
                    functions_returns.clear()
                #self.wait_on_run(run, thread)

        # Keep this return
        return run


