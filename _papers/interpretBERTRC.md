---
layout: post
date: 2021-01-09
title: 'Towards Interpreting BERT for Reading Comprehension Based QA'
permalink: /papers/interpretBERTRC
usemathjax: true
---

### Problem Statement
- BERT layers do not have pre-defined roles unlike previous Reading Comprehension QA architectures. Need model interpretability.

- Previous BERT analyze approaches use attention and train on sentiment classification, tags prediction, etc. Nothing has been done for RCQA.

### Approach
- BERT base, with official code and pre-trained checkpoints.

- [Integrated Gradients](https://arxiv.org/abs/1703.01365) per layer to find out word(token)-wise importance given by each layer in BERT.

- For a given passage $P$ with $n$ words $\[w_{1}, w_{2},\dots, w_{n}\]$, query $Q$, and model $f$ with $\theta$ parametes, answer prediction (start,end positions) is :

$$

p(w_{s}, w_{c}) = f(w_{s},w_{c}\vert P,Q,\theta)

$$

- For each layer:

$$

p(w_{s}, w_{c}) = f_{l}(w_{s},w_{c}\vert E_{l-1}(P),E_{l-1}(Q),\theta)

$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;where $f_{l}$ if forward propagation from layer l and $E_{l}(.)$ is previous layer output.

- The Integrated Gradients for a Model $M$, a passage word $w_{i}$ embedded as $x_{i} \in \mathbf{R}^{L}$ is defined as :

$$

IG(x_{i}) = \int_{\alpha = 0}^{1} \frac{\partial M(\tilde{x} + \alpha(x_{i}-\tilde{x}))}{\partial x_{i}}\partial \alpha

$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;where $\tilde{x}$ is a zero vector.

- Algorithm used in layer for every layer to get $I_{l}$ probability distribution over the passage words: <span style="color:red">(Refresh the page if the algorithm doesn't render.)</span>

{% include pseudocode.html id="LWIG" code="
\begin{algorithm}
\caption{Layer-Wise Integrated Gradients}
\begin{algorithmic}

\STATE $\tilde{p}=0 \hspace{1em}//zero baseline$
\STATE $m=50$
\STATE $G_{l}(p) = \frac{1}{m}\sum_{k=1}^{m} \frac{\partial f_{l}(\tilde{p}+\frac{k}{m}(p-\tilde{p}))}{\partial E_{l}}$
\STATE $IG_{l}(p) = [(p-\tilde{p})\times G_{l}(p)]$
\STATE //Computer squared norm for each word
\STATE $\tilde{I_{l}}([w_{1},\dots,w_{n}]) = \lVert IG_{l}(p)\rVert \in R^{k}$
\STATE Normalize $\tilde{I_{l}}$ to a probability distribution $I_{l}$
\end{algorithmic}
\end{algorithm}
" %}

- Define roles for layers based on these importances.


- Use [Jensen-Shannon Divergence](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence) between corresponding importance distribution $I_{x}, I_{y}$ :

  $$

  D_{JS}(P\lVert Q) = \frac{1}{2}D_{KL}(P\lVert M) + \frac{1}{2}D_{KL}(Q\lVert M)

  $$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;where $M = \frac{1}{2}(P+Q)$.  

- [Kullback-Leibler Divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence) is:

    $$

    D_{KL}(P \lVert Q) = \sum_{x\in X}P(x)\log(\frac{P(x)}{Q(x)})

    $$

- Analyze the distribution in two parts : Retain top-k words, zero out rest, and vice-versa. Re-normalize to get a probability distribution. Build heatmaps out of both cases. Average for 1000 samples in each case. More difference is observed in first case between layers. Hence, they conclude that they need to focus on top-k words.

- Use t-SNE visualizations for relevant words per layer.


### Datasets :
**SQuAD v1.1**
- 90k/10k train/dev

**DuoRC**
- SelfRC: 60k/13k train/dev


### Training
- BERT models fine-tuned to achieve F1 scores of 88.73 and 54.80 on their repective dev-splits.
- **Metrics**
  - F1 for finetuning.

- **Hyperparameters**
  - Epochs: 2

### Analysis & Results

**Probing Layers: QA functionality**
- Separate passage words into three categories: answer words, supporing words (within window size 5<span style="color:red">??</span> of the answer), query words.
- Check top-5 words in each layer distribution $I_{l}$. See category-wise percentages in top-5 words.

- **POS Tags**
  - Based on layer's functionality $I_{l}$, analyze top-5 important words in each layer on the basis of POS tags. 10% importance to punctuations and stopwords each, same as verbs and adjectives. Even when answer spans in SQuAD are 82.04% and in DuoRC are 79.78% entities.



- **Model first tries to identify part of the passage where question words are present, and then the question words' importances decrease gradually**

- **Qualitative Example**: Plot heatmap for each layer of top-5 words for an example. See all layers focus on answer words(<span style="color:blue;">Some of the examples have '.' as important in top 5, why?</span>). Initial layers incorporate interaction between the query and passage, later layers enchance and verify the prediction.

**Visualizing Word Representations**

- Visualize the t-SNE plot for one such passage -> answer, supporting words, query words, special tokens. Use the word representations. Gray out others.

- Across layers:
  - Numbers are always together.
  - Similar words are closer to each other in the initial layers - stop-words, team names, etc.
  - Question separates from answer and supporting words in later layers.
  - Model still predicts numbers correctly. Don't know why.

- **Quantifier Questions** :
  - Separate out quantifies questions.<span style="color:red">How?</span>. 799 and 310 questions in SQuAD and DuoRC.
  - Find out number of words that are numerical in top-5, and in the entire passage. Computer the ratio.
  - Ratio increases as we go to the later layers. Meaning the model gets more "confused". Still it manages to predict the answer for such questions with one numerical entity in the passage vs non-quantifier questions.




### Doubts
- Other training details : Optimizers, Schedulers, etc.
- Base for JS Divergence Log? Units?
- How do they combine the representations if a word was broken into multiple tokens?
