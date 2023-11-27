import time

class AssistantCommsHandler:
    def __init__(self, client):
        self.client = client

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
    
    def create_message(self, thread_id, user_input, file_ids = None, metadata = None):
        message = self.client.beta.threads.messages.create(
            thread_id,
            role = "user",
            content = user_input,
            file_ids = [file_ids],
            metadata = {metadata}
        )

        return message
    
    def retrieve_message(self, message_id, thread_id):
        message = self.client.beta.threads.messages.retrieve(
            message_id=message_id,
            thread_id=thread_id,
        )

        return message
    
    def modify_message(self, message_id, thread_id, metadata = None):
        message = self.client.beta.threads.messages.update(
            message_id = message_id,
            thread_id = thread_id,
            metadata={metadata},
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
            tool_outputs=[tool_outputs]
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
        while run.status == "queued" or run.status == "in_progress":
            run = self.client.beta.threads.runs.retrieve(
             thread_id=thread.id,
                run_id=run.id,
            )
            time.sleep(0.2)
        return run


