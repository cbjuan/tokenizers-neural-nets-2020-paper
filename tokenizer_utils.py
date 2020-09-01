from fastai.text import (BaseTokenizer, ifnone, defaults, ListRules)
from typing import List, Collection, Callable
import sentencepiece as spm


class SPTokenizer(BaseTokenizer):
    "Wrapper around a SentncePiece tokenizer to make it a `BaseTokenizer`."

    def __init__(self, model_prefix: str):
        self.tok = spm.SentencePieceProcessor()
        self.tok.load(f'{model_prefix}.model')

    def tokenizer(self, t: str) -> List[str]:
        return self.tok.EncodeAsPieces(t)


class CustomTokenizer():
    '''Wrapper for SentencePiece toeknizer to fit into Fast.ai V1'''

    def __init__(self, tok_func: Callable, model_prefix: str,
                 pre_rules: ListRules = None):
        self.tok_func, self.model_prefix = tok_func, model_prefix
        self.pre_rules = ifnone(pre_rules,  defaults.text_pre_rules)

    def __repr__(self) -> str:
        res = (f'Tokenizer {self.tok_func.__name__} using '
               f'`{self.model_prefix}` model with the following rules:\n')
        for rule in self.pre_rules:
            res += f' - {rule.__name__}\n'
        return res

    def process_text(self, t: str, tok: BaseTokenizer) -> List[str]:
        "Processe one text `t` with tokenizer `tok`."
        for rule in self.pre_rules:
            t = rule(t)
        toks = tok.tokenizer(t)
        # post rules?
        return toks

    def _process_all_1(self, texts: Collection[str]) -> List[List[str]]:
        'Process a list of `texts` in one process'
        tok = self.tok_func(self.model_prefix)
        return [self.process_text(t, tok) for t in texts]

    def process_all(self, texts: Collection[str]) -> List[List[str]]:
        "Process a list of `texts`."
        return self._process_all_1(texts)
