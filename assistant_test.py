import os
import openai
import json
import time
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

# Reading API key from environment variables and setting it
API_KEY = os.getenv("OPENAI_API_KEY")


client = openai.OpenAI()

def show_json(obj):
    print(json.loads(obj.model_dump_json()))
   

def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Answer questions briefly, in a sentence or less.",
    model="gpt-3.5-turbo-1106",
)

# show_json(assistant, "Assistant JSON")

# thread = client.beta.threads.create()

# show_json(thread, "Thread JSON")

# message = client.beta.threads.messages.create(
    # thread_id=thread.id,
   # role="user",
    # content="I need to solve the equation `3x + 11 = 14`. Can you help me?",
# )

# show_json(message, "Message JSON")

# run = client.beta.threads.runs.create(
  #  thread_id=thread.id,
   # assistant_id=assistant.id,
#)
#show_json(run, "Run JSON")


# run = wait_on_run(run, thread)
# show_json(run, "Run JSON ASYNC")

# messages = client.beta.threads.messages.list(thread_id=thread.id)
# show_json(messages, "Messages JSON")

MATH_ASSISTANT_ID = assistant.id

def submit_message(assistant_id, thread, user_message):
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )


def get_response(thread):
    return client.beta.threads.messages.list(thread_id=thread.id, order="asc")

def create_thread_and_run(user_input):
    thread = client.beta.threads.create()
    run = submit_message(MATH_ASSISTANT_ID, thread, user_input)
    return thread, run

def pretty_print(messages):
    print("# Messages")
    for m in messages:
        print(f"{m.role}: {m.content[0].text.value}")
    print()

thread1, run1 = create_thread_and_run(
    "I need to solve the equation `3x + 11 = 14`. Can you help me?"
)
thread2, run2 = create_thread_and_run("Could you explain linear algebra to me?")
thread3, run3 = create_thread_and_run("I don't like math. What can I do?")

# Wait for Run 1
run1 = wait_on_run(run1, thread1)
pretty_print(get_response(thread1))

# Wait for Run 2
run2 = wait_on_run(run2, thread2)
pretty_print(get_response(thread2))

# Wait for Run 3
run3 = wait_on_run(run3, thread3)
pretty_print(get_response(thread3))

# Thank our assistant on Thread 3 :)
run4 = submit_message(MATH_ASSISTANT_ID, thread3, "Thank you!")
run4 = wait_on_run(run4, thread3)
pretty_print(get_response(thread3))