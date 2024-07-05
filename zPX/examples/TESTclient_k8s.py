from llama_agents import LlamaAgentsClient
import time


#client = LlamaAgentsClient("http://0.0.0.0:8001")
client = LlamaAgentsClient("http://control-plane.127.0.0.1.nip.io")
task_id = client.create_task("What is the secret fact?")
time.sleep(10)
task_result = client.get_task_result(task_id)
print(task_result.result)