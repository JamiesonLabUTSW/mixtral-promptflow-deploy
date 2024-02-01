"""This script creates an OpenAI type connection in prompt-flow named 'Mixtral'"""

from promptflow import PFClient
from promptflow.entities import OpenAIConnection

# client can help manage your runs and connections.
client = PFClient()

# Initialize an OpenAIConnection object
# The 'base_url' field is the ip address at which the vllm server running the Mixtral model is hosted 
# The 'model' field contains the path to the model (this is the default model name in vllm)
connection = OpenAIConnection(
    model="/archive/shared/sim_center/shared/mixtral/data/Mixtral-8x7B-Instruct-v0.1",
    name="Mixtral",
    api_key="EMPTY",
    base_url="http://172.18.227.71:8000/v1",
)
# Create the connection, note that api_key will be scrubbed in the returned result
result = client.connections.create_or_update(connection)
print(result)