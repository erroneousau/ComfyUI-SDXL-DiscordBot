import asyncio
import configparser

from comfy_script.runtime import load

async def server_is_started() -> bool:
    while True:
        try:
            config = configparser.ConfigParser()
            config.read("config.properties")
            load(f"http://localhost:{config['EMBEDDED']['SERVER_PORT']}")
            break
        except:
            asyncio.sleep(3)
    # do api call to check if server is started
    from comfy_script.runtime import client
    try:
        print(len(client.get_nodes_info()))
        return len(client.get_nodes_info()) > 0
    except:
        return False

def get_models():
    from comfy_script.runtime.nodes import Checkpoints
    models = [model.value for model in Checkpoints]
    return models

def get_loras():
    from comfy_script.runtime.nodes import Loras
    loras = [lora.value for lora in Loras]
    return loras

def get_samplers():
    from comfy_script.runtime.nodes import Samplers
    samplers = [sampler.value for sampler in Samplers]
    return samplers
