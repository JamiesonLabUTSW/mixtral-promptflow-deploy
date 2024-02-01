### Installation

- Make sure your environment has the required packages installed. Using `python=3.9` is recommended.
```sh
pip install promptflow promptflow-tools
```
- Install the vscode extension from the <a href="https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow">visualstudio marketplace</a>.

### Create a flow

- Create a demo-flow in promptflow - for example using something like this. 
```sh
pf flow init --flow ./my_chatbot --type chat
```
- You can also use the visual editor to create a simple flow with input, llm and output nodes
    - Open flow.dag.yaml, hover and click on 'visual editor' on the top left and click on '+' to add the type of nodes you want 

### Using Mixtral, or any other open-source model 
1. Setup the vllm server running your model (follow the steps in the parent directory)

2. Edit create_connection.py and
    - Update the 'base_url' field to the ip address of the machine running your vllm server 
    - Update the 'model' field to the path of the folder containing the model that was used to inititate the vllm server

3. Run the python script to create a connection in prompt-flow to the model
```sh
python create_connection.py
```

4. Go to the promptflow vscode extension on the side-bar and click on 'Connections'. There should be a new connection titled 'Mixtral' under the OpenAI connections.

4. Use the promptflow extensions visual editor to create a new LLM node in your demo app if not already created

5. Select connection name 'Mixtral' and completions api. Choose any model from the list of OpenAI models and save your file.

6. Update the model name in the yaml file of your demo flow. 

- Open flow.dag.yaml
- Update the model field under nodes -> llm-node -> inputs -> model: to the 'model' field in create_connection.py in step 2(i)

7. Go back to the visual editor. The right model name should now show up in the model field.
    
