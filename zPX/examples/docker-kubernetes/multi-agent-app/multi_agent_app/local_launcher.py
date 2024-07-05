from llama_agents import ServerLauncher

from multi_agent_app.core_services.message_queue import message_queue
from multi_agent_app.core_services.control_plane import control_plane
from multi_agent_app.agent_services.secret_agent import (
    agent_server as secret_agent_server,
)
from multi_agent_app.agent_services.funny_agent import (
    agent_server as funny_agent_server,
)
from multi_agent_app.additional_services.human_consumer import human_consumer_server

from llama_agents import ServerLauncher, CallableMessageConsumer

## added by zPX
# Additional human consumer
def handle_result(message) -> None:
    print(f"Got result:", message.data)


human_consumer = CallableMessageConsumer(
    handler=handle_result, message_type="human"
)


# launch it
launcher = ServerLauncher(
    [secret_agent_server, funny_agent_server],
    control_plane,
    message_queue,
    additional_consumers=[human_consumer_server.as_consumer(), human_consumer],
)


if __name__ == "__main__":
    launcher.launch_servers()
