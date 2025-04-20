# from transformers import AutoTokenizer, AutoModelWithLMHead

# class T5Module:
#     def __init__(self):
#         self.tokenizer = AutoTokenizer.from_pretrained('t5-base')
#         self.model = AutoModelWithLMHead.from_pretrained('t5-base', return_dict=True)

#     def summarize(self, text: str, minlength: int, maxlength: int, truncation: bool) -> str:
#         inputs = self.tokenizer.encode("summarized: " + text,
#                                        return_tensors='pt',
#                                        max_length=512,
#                                        truncation=truncation)

#         summary_ids = self.model.generate(inputs, 
#                                           max_length=maxlength, 
#                                           min_length=minlength, 
#                                           length_penalty=5., 
#                                           num_beams=2)

#         summary = self.tokenizer.decode(summary_ids[0])
#         return summary
