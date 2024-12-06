from phi.tools import Toolkit
from phi.model.ollama import Ollama
from phi.utils.log import logger

class NuExtractTools(Toolkit):
    def __init__(self, json_template: str):
        super().__init__(name="nuextract_tools")
        self.json_template = json_template
        self.extract_agent = Agent(
            model=Ollama(id="sroecker/nuextract-tiny-v1.5", host=OLLAMA_HOST, options={"temperature": 0}),
            markdown=False,
            structured_outputs=True
        )
        self.register(self.predict_nuextract)

        
    def predict_nuextract(self, input_text: str) -> str:
        """Extracts structured information and returns JSON.
        
        Args:
            input_text (str): The input text to extract information from.
        Returns:
            str: The output in JSON.
        """
        template = f"""<|input|>\n### Template:\n{self.json_template}\n### Text:\n{input_text}\n\n<|output|>"""
        logger.info(f"Extracting structured data according to schema: {self.json_template}")
        output_json = self.extract_agent.run(template, stream=False)
        
        return output_json.content
