---
layout: paper
date: 2021-04-07
title: 'THE CURIOUS CASE OF
NEURAL TEXT DeGENERATION'
permalink: /papers/curious_case
usemathjax: true
venue: ICLR
year:  2020
topics: 
  - Text Generation
  - Degeneration
  - Nucleus Sampling
authors:
  - name: Ari Holtzman
  - name: Jan Buys
  - name: Li Du
  - name: Maxwell Forbes
  - name: Yejin Choi
paperurl: https://arxiv.org/pdf/1904.09751.pdf
---
## Short Summary

This paper proposes a better alternative for open-domain text decoding/generation called "Nucelus Sampling".

There are few popular approaches that have been discussed for decoding, in general:

1. Greedy Decoding: Taking most probably token/term at every step.
2. Beam Search: A beam of width B is used and at each time step top B terms are expanded, and the total probability (product so far) is maximized, choosing B at every step.
3. Pure Sampling: In this, at each time step, the entire distribution is used, and a token is sampling based on the probabilities in the distribution at every step.
4. Top-K Sampling: In this, at each time step, the top-k tokens are chosen and then the distribution is re-normalized and is used for sampling. The value of k is difficult to choose. If k is small, then there is a risk of generating generic, probably repetitive, text. If k is large, risk of incoherent text.
5. Using Temperature: In this the "logits" are dividied by a temperature factor T before . Lowering the T makes the distribution more skewed.

The two main problems with the existing approaches is:

1. Repetition: Mostly happens in approaches like Beam Search, which attempt to maximize the likelihood of the text.
2. Incoherence: Happens during pure sampling, top-k sampling in which the sentences don't make sense together. This happens due to the "unreliable" tail of the distribution, which is considered during the sampling.

The authors suggest Nucleus Sampling, which takes the smallest set of tokens with probability sum greater than a hyperparameter P, i.e. the nucleus.

They use perplexity, % of repetition, Self-BLEU, Zipf coefficient and HUSE metrics for comparison.

The findings of the paper can be summarized in the following lines :

- Perplexity: Text with lower perplexity tends to have low diversity and get stuck in repttiive loops. Ideally, the perplexity should be same as that of human text.
    - Greedy~Beam<Top-k=40, t= 0.7<Top-k=40<Sampling t=0.9<Human<Nucleus p=0.95<Top-k=640<Pure Sampling

- Natural language does not maximize probability: Per-token probability of natural text is muchl lower than the generated text by beam search. The human language is not very probably/predictable. Models tend to assign high probabilities to beam search.
- Vocabulary distribution in terms of closeness, pure sampling is closest to human but has much higher perplexity. It oversamples rare word, which can explain both the observations. Lowering the temperature is a solution to fix this.
    - b=16<k=40<k=640<p=0.95<Gold<t=1.0
- A lower Self-BLEU means higher diversity in the text. Common values of temperature t in [0.5,1] and k in [1,100] result in very high self-similarity. Normal values of p [0.9,1) closely match the human text. This aligns with Zipfian measure.
- The percentage of generations resulting in repetition varies. Greedy decoding has a very high percentage of repetition.
    - Nucleus sampling repetition is lowest after a point, and matches with human.
    - For top-k sampling, the percentages are low always. Nucelus sampling and top-k, and regular sampling are closest to human.
    - Reducing temperature makes the text more repetitive as the distribution gets more skewed.
    - Beam search has a different, kind of a linear relation, the higher the beam width, the lower the percentage of repetition. However, very large beam sizes are required to bring the text closer to human % of repetition.
- HUSE metric: Nucelus is best, followed by top-k = 640, followed by sampling with t=0.9.

## References

- Diverse Beam Search: Decoding Diverse Solutions from Neural Sequence Models ([https://arxiv.org/abs/1610.02424](https://arxiv.org/abs/1610.02424))
- Unsupervised Text Generation by Learning from Search ([https://arxiv.org/abs/2007.08557](https://arxiv.org/abs/2007.08557))
- HUSE ([https://arxiv.org/abs/2007.08557](https://arxiv.org/abs/2007.08557))
- Temperature Sampling Example: [https://lena-voita.github.io/nlp_course/language_modeling.html#generation_strategies_temperature](https://lena-voita.github.io/nlp_course/language_modeling.html#generation_strategies_temperature)
- Grice's Maxims: [https://www.sas.upenn.edu/~haroldfs/dravling/grice.html#:~:text=The maxim of quantity%2C where,is not supported by evidence](https://www.sas.upenn.edu/~haroldfs/dravling/grice.html#:~:text=The%20maxim%20of%20quantity%2C%20where,is%20not%20supported%20by%20evidence).
