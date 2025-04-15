# from fairseq.models.transformer import TransformerModel

from text_processing.translator.translator import BaseTranslator


# Implemantation Fairseq
class FairseqTranslator(BaseTranslator):
    # def __init__(self):
    #     self.model = TransformerModel.from_pretrained(
    #         model_name_or_path="path/to/fairseq/model",  # Substituir pelo caminho correto
    #         checkpoint_file="model.pt",
    #         data_name_or_path="path/to/data-bin"  # Substituir pelo caminho correto
    #     )
    #     self.model.eval()

    def translate(self, texto: str) -> str:
        # return self.model.translate(texto)
        raise NotImplementedError("Method not implemented.")

