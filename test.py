from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://172.18.227.71:8000/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
completion = client.completions.create(model="/archive/shared/sim_center/shared/mixtral/data/Mixtral-8x7B-Instruct-v0.1",
                                      prompt="San Francisco is a")
print("Completion result:", completion)
