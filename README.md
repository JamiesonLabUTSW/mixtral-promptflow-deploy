## vLLM-promptflow-deploy
This repo is a short guide to 
- Hosting your own state-of-the-art open-source LLM's such as Mixtral 8x7B using the vLLM inference engine
- Using your hosted model in prompt-flow to develop your custom LLM flows and applications

**vLLM** is a flexible and efficient library for large language model (LLM) inference that makes it easy to host and serve LLM's. vLLM provides:
- Seamless integration with popular HuggingFace models
- OpenAI compatible API server 

**promptFlow** is a set of development tools designed to streamline prototyping, testing, deployment and monitoring of LLM apps. 

### Installation
1. Create new conda environment 
```sh
conda create -n myenv python=3.9 -y
conda activate myenv
```
2. Install vllm, ray and prompt-flow 
```sh
pip install vllm
pip install promptflow promptflow-tools
```

### Launch vLLM inference server 

This repo contains a demo for running an OpenAI protocol compatible API server using vLLM that runs the Mixtral 8X7B MOE model - one of the most peformant open source LLMs available as of Jan '24. Using the OpenAI API protocol makes it easy to swap OpenAI models that you may already be using in your applications with models that are self-hosted or from other providers. 

The Mixtral model can run with `float16` precision on 1 GPU4v100 node on BioHPC. 

To launch your inference server, you can either

   - Use a bash script `serve_mixtral.sh` (recommended)
   - Request an interactive node and launch your server on it

If you decide to run or test your server on an interactive node, make sure your request 4 gpus in the SLURM command
```sh
srun -p GPU4v100 --gres=gpu:4 --pty /bin/bash

python -m vllm.entrypoints.openai.api_server \
  --model /archive/shared/sim_center/shared/mixtral/data/Mixtral-8x7B-Instruct-v0.1 \
  --chat-template /archive/shared/sim_center/shared/mixtral/vllm/template_mistral.jinja \
  --trust-remote-code --dtype float16 --tensor-parallel-size 4 --max-model-len 8192
```
#### Parameters Explanation

python -m vllm.entrypoints.openai.api_server: This starts the API server.

--model <path>: Specifies the path to the model directory. In this case, it is /archive/shared/sim_center/shared/mixtral/data/Mixtral-8x7B-Instruct-v0.1.

--chat-template <path>: Defines the path to the chat template file. Here, it's set to /archive/shared/sim_center/shared/mixtral/vllm/template_mistral.jinja.

--trust-remote-code: This flag indicates that the server should trust and run remote code.

--dtype float16: Sets the data type for tensors in the model to float16. This is the default precision for the full Mixtral model

--tensor-parallel-size 4: Specifies the size of the tensor parallelism. This shows over how many GPU's the model is being shared.

--max-model-len 8192: This is the max number of tokens that the model can support. In this case, Mixtral can support process a context window of 8192 tokens.

### Testing your server

To get the ip-address of the node that your server is running at. For BioHPC, the node name may look something like `Nucleus162`
```sh
ssh <node-name> hostname -i
```

To test whether the server running your models is running, you can query the server with
```sh
curl http://<ip-address>:8000/v1/models
```

If using BioHPC - you may need to first specify a proxy server for HTTP connections. To do this run 
```sh
export HTTPS_PROXY=http://proxy.swmed.edu:3128
export https_proxy=http://proxy.swmed.edu:3128
```
You can also add these lines to your `./bashrc` file in your home directory and manually execute it or restart your terminal. 
```sh
source ~/.bashrc
```

### Querying your server
You can run either of 
```sh
python test_chat.py
python test.py
```
to query your LLM. Make sure that you replace the model path and ip-address with the model path and ip-address of your vLLM server.

Alternatively, you can query it from the terminal: 
```sh
curl http:/<ip-address>:8000/generate \
            -d '{
                     "prompt": "San Francisco is a",
                                "use_beam_search": false, "max_tokens": 300,
                                 "n": 4, "temperature": 0.5}'

```

### prompt-flow

Read the README file in the /promptflow directory


## Authors
Ameer Hamza Shakur

Michael Holcomb

