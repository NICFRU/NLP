from transformers import pipeline

def zeroshotNLP(text):
    zeroshot = pipeline(task= "zero-shot-classification", 
                      model= "valhalla/distillbart-mnli-12-1",)
    return zeroshot(text)[0]