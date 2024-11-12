from phi.agent import Agent
from phi.model.ollama import Ollama

extract_agent = Agent(
    model=Ollama(id="sroecker/nuextract-tiny-v1.5"),
)

def predict_nuextract(input_text):
    template = """
    {
        "Model": {
            "Name": "",
            "Number of parameters": "",
            "Number of max token": "",
            "Architecture": []
        },
        "Usage": {
            "Use case": [],
            "Licence": ""
        }
    }
    """
    template = f"""<|input|>\n### Template:\n{template}\n### Text:\n{input_text}\n\n<|output|>"""

    return template

example_text = """We introduce Mistral 7B, a 7–billion-parameter language model engineered for
superior performance and efficiency. Mistral 7B outperforms the best open 13B
model (Llama 2) across all evaluated benchmarks, and the best released 34B
model (Llama 1) in reasoning, mathematics, and code generation. Our model
leverages grouped-query attention (GQA) for faster inference, coupled with sliding
window attention (SWA) to effectively handle sequences of arbitrary length with a
reduced inference cost. We also provide a model fine-tuned to follow instructions,
Mistral 7B – Instruct, that surpasses Llama 2 13B – chat model both on human and
automated benchmarks. Our models are released under the Apache 2.0 license.
Code: <https://github.com/mistralai/mistral-src>
Webpage: <https://mistral.ai/news/announcing-mistral-7b/>"""

print(predict_nuextract(example_text))

extract_agent.print_response(predict_nuextract(example_text))
