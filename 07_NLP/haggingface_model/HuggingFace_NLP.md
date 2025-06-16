# 🤗 Hugging Face for NLP 
**By Abid Hussain**
---

## 📘 What is Hugging Face

- A hub for **NLP models, datasets, and tools**
- Hosts the `transformers` library for state-of-the-art LLMs
- Pretrained models, fine-tuning, and dataset sharing
- Community-driven and open source

---

## 🧠 Why Use Hugging Face

✅ Access models like BERT, GPT-2, RoBERTa  
✅ 1000s of public NLP datasets  
✅ Easy pipelines for tasks  
✅ Fine-tune your own models  
✅ Urdu NLP support 🇵🇰

---

## 🛠️ Install & Import

```bash
# create conda environment
conda create -n hfp_env python=3.10 -y
conda activate hfp_env
# install transformers and datasets
pip install transformers datasets ipykernel
pip install torch torchvision torchaudio
pip install --upgrade pip
pip install tensorflow
```

```python
from transformers import pipeline
```

---

## 🧪 Sentiment Analysis (English)

```python
classifier = pipeline("sentiment-analysis")
classifier("Pakistan’s cricket team is amazing!")
```

✅ Output: Positive with high confidence

---

## 🌍 Urdu Sentiment (Pakistani Model)

```python
classifier = pipeline("text-classification", model="asafaya/bert-base-urdu")
classifier("پاکستان ایک خوبصورت ملک ہے۔")
```

✅ Urdu language support from pretrained model

---

## 📚 Urdu Dataset

```python
from datasets import load_dataset
dataset = load_dataset("urduhack/urdu_sentiment_corpus")
print(dataset["train"][0])
```

✅ 7,000+ Urdu sentences with sentiment labels

---

## 🧩 Supported Tasks

| Task               | Description |
|--------------------|-------------|
| `sentiment-analysis` | Positive/Negative detection |
| `translation`         | Multilingual translation |
| `question-answering`  | QA from context |
| `summarization`       | Shorten text |
| `ner`                 | Named Entity Recognition |
| `text-generation`     | Language generation |

---

## 💬 Urdu Text Generation

```python
generator = pipeline("text-generation", model="aubmindlab/urdu-bert-base-uncased")
generator("پاکستان میں", max_length=20)
```

---

## 🧠 Pakistani Use Cases

- Urdu news summarization 📰  
- Social media sentiment analysis 📱  
- Chatbots and FAQs 🤖  
- Bilingual website NLP 🔁  
- Localized classification tasks 📦

---

## 🌐 Search Hugging Face

🔍 Explore at:  
- https://huggingface.co/models  
- https://huggingface.co/datasets  

Search terms: `Urdu`, `Pakistan`, `transformers`, `T5`, `BERT`

---

## ✅ Summary

✅ Hugging Face makes NLP easy  
✅ Urdu/Pakistani models & datasets available  
✅ Reuse, fine-tune, deploy quickly  
✅ Big opportunity for local AI builders 🇵🇰

---
