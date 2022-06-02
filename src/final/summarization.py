from transformers import AutoModelForSeq2SeqLM, T5TokenizerFast

MODEL_NAME = "UrukHan/t5-russian-summarization"
MAX_INPUT = 512

tokenizer = T5TokenizerFast.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def summarize_text(text_to_summarize) -> list:
    if type(text_to_summarize) != list:
        text_to_summarize = [text_to_summarize]
    encoded = tokenizer(
        [sequence for sequence in text_to_summarize],
        padding="longest",
        max_length=MAX_INPUT,
        truncation=True,
        return_tensors="pt",
    )["input_ids"]
    predicts = model.generate(encoded)
    return tokenizer.batch_decode(predicts, skip_special_tokens=True)
