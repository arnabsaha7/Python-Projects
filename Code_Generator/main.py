from datasets import load_from_disk
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments

# Load the Tokenizer & Model
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono")

# Set the pad_token to eos_token (Or add a new pad token)
tokenizer.pad_token = tokenizer.eos_token

# Load the dataset
dataset = load_from_disk("data/")
print("Dataset has been loaded successfully!!!")

dataset = dataset.train_test_split(test_size=0.1)
def preprocess_function(examples):
    inputs = tokenizer(examples['code'], truncation=True, padding='max_length', max_length=512)
    inputs['labels'] = inputs['input_ids']
    return inputs

tokenized_datasets = dataset.map(preprocess_function, batched=True)

# Model fine-tuning
training_args = TrainingArguments(
    output_dir='./results',
    per_device_train_batch_size=1,  # Keeping this low to save memory
    num_train_epochs=1,
    save_steps=10_000,
    save_total_limit=2,
    logging_dir='./logs',  # Log directory
    logging_steps=100,  # Adjust logging frequency to reduce I/O overhead
    gradient_accumulation_steps=4,  # Accumulate gradients to effectively increase batch size
    fp16=True,  # Enable mixed precision if using a compatible environment
    evaluation_strategy="epoch",  # Evaluate at the end of each epoch
)

# Training the model with the new tunings
trainer = Trainer(
    model = model,
    args = training_args,
    train_dataset = tokenized_datasets['train'],
    eval_dataset = tokenized_datasets['test']
)
trainer.train()

# define a function to generate code using the fine-tuned model
def generate_code(prompt, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs['input_ids'],
        attention_mask=inputs['attention_mask'],  # Include the attention mask
        max_length=max_length,
        pad_token_id=tokenizer.eos_token_id  # Ensure pad_token_id is set
    )
    generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_code

# test the model with a code generation prompt
prompt = "Code print fibonacci series upto 10"
generated_code = generate_code(prompt)

print("Generated Code:")
print(generated_code)