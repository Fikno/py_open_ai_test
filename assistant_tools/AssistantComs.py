import time
import openai

class AssistantComs:

    def __init__(self, assistant):
        self.client = assistant.get_client()
        self.assistant_id = assistant.get_assistant_id()
        self.thread_ids = []

    def get_client(self):
        return self.client
    
    def get_assistant_id(self):
        return self.assistant_id
    
    def get_thread_ids(self):
        return self.thread_ids

    def create_new_thread(self, thread_name):
        thread = self.client.beta.threads.create()
        self.thread_ids.append([thread_name, thread.id])

    def find_thread(self, thread_name):
        for thread in self.thread_ids:
            if thread[0] == thread_name:
                return thread[1]

    def create_run(self, thread_id, assistant_id):
        run = self.client.beta.threads.runs.create(
        thread_id = thread_id,
        assistant_id = assistant_id,
        )

        return run
    
    def wait_on_run(self, run, thread_id):
        while run.status == "queued" or run.status == "in_progress":
            run = self.client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run.id,
            )
            time.sleep(0.5)
        return run
    
    def submit_message(self, assistant_id, thread_id, user_message):
        self.client.beta.threads.messages.create(
            thread_id=thread_id, role="user", content=user_message
        )
        return self.create_run(thread_id, assistant_id)


    def get_response(self, thread_id):
        return self.client.beta.threads.messages.list(thread_id=thread_id, order="asc")
    
    def file_uploader(self, file):
        self.client.files.create(
            file=open(
            str(file),
            "rb",
            ),
            purpose="assistants",
        )
    
    def message_formater(self, messages):
        
        for m in messages:
            message = f"{m.role}: {m.content[0].text.value}"
            message_without_backslashes = message.replace("\\", "")
            print(message_without_backslashes)