# tokenizers-neural-nets-2020-paper

<!--- [![DOI](https://zenodo.org/badge/285613872.svg)](https://zenodo.org/badge/latestdoi/285613872) --->

This repository contains every notebook, model, and pickled dataset and other supporting materials used during the research associated to the paper `Automated Source Code Generation and Auto-completion Using Deep Learning: Comparing and Discussing Current Language-Model-Related Approaches`

For more information about the purpose of each file and model, please refer to the paper.

## 📓 Notebooks

The notebooks related to the data cleaning and preparing are:

- `downloading_cleaning_codeSearchNetChallenge_dataset.ipynb`
- `preparing_csv_files_from_codeSearchNetChallenge_dataset.ipynb`

The notebooks related to the training of AWD-LSTM neural networks are:

- `20200811_word_model_training_lstm.ipynb`
- `20200811_unigram_model_training_lstm.ipynb`
- `20200811_bpe_model_training_lstm.ipynb`
- `20200811_char_model_training_lstm.ipynb`

The notebooks related to the training of AWD-QRNN neural networks are:

- `20200820_word_model_training_qrnn.ipynb`
- `20200820_unigram_model_training_qrnn.ipynb`
- `20200820_bpe_model_training_qrnn.ipynb`
- `20200820_char_model_training_qrnn.ipynb`

The notebooks related to the training of the Transformer models GPT-2, BERT and RoBERTa are:

- `20200813_gpt2.ipynb`
- `20200817_bert.ipynb`
- `20200824_roberta.ipynb`

## 📖 Models from tokenization

The models and vocab files resulting from each tokenization process and used for AWD-LSTM and AWD-QRNN neural nets are:

- `word_model.model`
- `word_model.vocab`
- `unigram_model.model`
- `unigram_model.vocab`
- `bpe_model.model`
- `bpe_model.vocab`
- `char_clean_code_challenge_model.model`
- `char_clean_code_challenge_model.vocab`

The models and vocab files used for GPT-2, BERT and RoBERTA are under the folders named:

- `20200813_gpt2-CodeSearchNet-fine-tuned`
- `20200817_fit_head_bert_model-CodeSearchNet`
- `20200817_fine_tuned_bert_model-CodeSearchNet`
- `20200813_roberta-CodeSearchNet_fit_head`
- `20200813_roberta-CodeSearchNet_fine_tuned`

There are another Python script for tokenization utils, used in some notebooks named `tokenizer_utils.py`.

## 🤖 Trained models

Every model trained using the [FastAI library](https://github.com/fastai/) is located under the Zenodo record [10.5281/zenodo.4293857](https://doi.org/10.5281/zenodo.4293857). The name of each one is consistent with the names used in the different notebooks above commented. The models stored using the [🤗HuggingFace's Transformers](https://github.com/huggingface/transformers) library are in the folders `20200813_gpt2-CodeSearchNet-fine-tuned`, `20200817_fit_head_bert_model-CodeSearchNet`, `20200817_fine_tuned_bert_model-CodeSearchNet`, `20200813_roberta-CodeSearchNet_fit_head`, and `20200813_roberta-CodeSearchNet_fine_tuned`.

## ✅ Results

The CSV files with results from training processes are located under the `results` folder. The associated notebook that analyzes them is `analyzing_results.ipynb`.
