---
layout: post
title: 'A Gated Self-attention Memory Network for Answer Selection'
permalink: /papers/gsamn
usemathjax: true
---

### Problems with Compare-Aggregate:
- Encode Question-Candidate pairs into context vector representation separately.
### Approach
-	Gated Self-attention Memory Networks for Answer Selection

	-	Builds upon two main ideas:
		-	Gated-Attention Mechanism from GAReaders (Dhingra et al., 2017)

			-	**Regular Attention**: Given a context vector $ \mathbf{c} $ and an input sequence vector representation $X = \begin{bmatrix}\mathbf{x_{1}\dots x_{n}}\end{bmatrix}$:

			$$\alpha_{i} = \frac{\exp{(\mathbf{c}^{T}\mathbf{x}_{j})}}{\sum_{j\in \begin{bmatrix} 1\dots n\end{bmatrix}}{\exp{(\mathbf{c}^{T}\mathbf{x}_{j})}}}

			$$

			-	**Gated Attention**: Instead of calculating a single attention value for each component and combining, make a vector for each.

			$$
			\mathbf{g}_{i} = \sigma(f(\mathbf{c},\mathbf{x}_{i})) $$

			- **Gated Self-Attention Mechanism**(Proposed): The gating in gated attention is done based on context vector and single input vector. They want - self-attention + entire sequences as well. Hence, a different kind of vector is calculated as follows:

			$$ \mathbf{v}^{j} = \mathbf{W}\mathbf{x}_{j} + \mathbf{b} ; \mathbf{v}^{c} = \mathbf{W}\mathbf{c} + \mathbf{b} \\

			s^{j}_{i} = \mathbf{x}_{i}^{T}\mathbf{v}^{j}; s^{j}_{i} = \mathbf{x}_{i}^{T}\mathbf{v}^{c} \\

			\alpha_{i}^{j} = \frac{\exp{(s_{i}^{j})}}{\sum_{k\in \begin{bmatrix} 1\dots n\end{bmatrix}}{\exp{(s_{i}^{k})}+\exp{(s_{i}^{c})}}}\\

			\alpha_{i}^{c} = \frac{\exp{(s_{i}^{c})}}{\sum_{k\in \begin{bmatrix} 1\dots n\end{bmatrix}}{\exp{(s_{i}^{k})}+\exp{(s_{i}^{c})}}} \\

			\begin{align*}
			\mathbf{g}_{i} = & f_{i}(c, X)\\
			 = & \sigma \left( \sum_{j}(\alpha_{i}^{j}\mathbf{x}^{j}) + \alpha_{i}^{c}\mathbf{c}  \right)
			\end{align*}

			$$

		- Memory-Networks (Sukhbaatar et al., 2015)
			- They try to overcome the limitation of having a single control vector at every hop by combining GSAM with memory network architecture. Thus, creating the GSAMN. Let $\mathbf{k}$ denote the $k^{th}$ reasoning hop, the memory cells are updated as:

			$$
				\mathbf{g}_{i} = f_{i}(\mathbf{c}_{k},X)\\

				\mathbf{x}_{i}^{k+1} = \mathbf{g}_{i} \odot \mathbf{x}_{i}^{k}\\
			$$

			- Update the controller using this gated self-attention and traditional aggregation update, assume no weighting is required as self-attention is enough :

			$$
			\mathbf{g}_{c} = f_{c}(\mathbf{c}_{k},X)\\

			\mathbf{c}_{k+1} = \mathbf{g}_{c} \odot \mathbf{c}_{k} + \frac{1}{n} \sum_{i}\mathbf{x}_{i}^{k+1}\\ \color{red}{\text{(Error in this notation, should be}\ \mathbf{c}^{k}\text{)}}
			$$

### Datasets :
- Crawled StackExchange QnAs for pre-training.
	- Preprocessing:
		- Remove non-relevant answers for positive examples (upvotes<2) $\color{blue}{\text{Why 2?}}$
		- Random answers for negative.
	- Code: https://github.com/laituan245/StackExchangeQA
	- 628706 positive and 9874758 negative examples.
- TrecQA
	- Preprocessing:
		- Clean Version : Remove no answer/ only pos/neg answer questions.
	- 1229/65/68 questions, 53417/1117/1442 Q-A pairs. (train/dev/test)
- WikiQA
	- Preprocessing:
		- Remove questions with no answer
	- 873/126/243 Q, 8627/1130/2351 Q-A pairs.


### Training
- Convert the problem to binary-classification: They train concatenate the answer in the question and then predict 1 or 0, based on whether the answer is correct or not. They use the final context/controller state $\mathbf{c}_{T}$ as a representation, and do a sigmoid on it's linear transform (one neural netowk layer).

- Controller state is randomly intialized. Input vectors are taken from any embedding. Can be GloVe, ElMo, etc. They use BERT (base)



#### Metrics
- Mean Average Precision
- Mean Reciprocal Rank


#### Hyperparameters
Tuning on dev set:
- Fine-tune BERT embeddings during training.
- 2 Hops (probably due to small sized datasets - TrecQA and WikiQA) $\color{blue}{\text{But they fine-tuned, didn't they? Is there a possible problem with pre-training, then?}}$
- Adam - lr: 1e-5; betas = [0.9,0.999];
- L2 decay : 0.01
- Warmup first 10% of total
- Linear Decay of LR.

### Analysis & Results
- **Previous Methods**
	- BERT + GSAMN + Transfer Learning is better than just BERT
- **Ablation Analysis**
	- Both better than BERT, combination best:
		- BERT + GSAMN
		- BERT + Transfer Learning	 
- **GSAMN vs Transformers**
	- Check whether not due to just extra parameters : ${color{green}{\text{Nice}}}$
		- Stack 6 Transformer layers on Top of BERT.
			- Didn't perform as well, even with Transfer Learning.
- **GSAMN vs Compare-Aggregate**
	- ElMo + Compare Aggregate
		- ElMo because word-level representations needed for Compare Aggregate and dynamic-clip attention.
		- Say tried with BERT + Comapre-Aggregate too but was worse. $\color{blue}{\text{If that is actually the case, why not show it in their table?}}$
- BERT + GSAMN + Transer : 0.914 MAP on TrecQA, 0.857 MAP on WikiQA
- BERT + GSAMN : 0.914 MAP on TrecQA, 0.857 MAP on WikiQA

### Doubts
- Meaning of the sentence : "We use affine-transformed inputs v and x
to calculate the self-attention instead of just x to
break the attention symmetry phenomenon." (2.1)
