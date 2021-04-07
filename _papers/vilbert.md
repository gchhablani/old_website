---
layout: paper
date: 2021-02-26
title: 'ViLBERT: Pretraining Task-Agnostic Visiolinguistic
Representations for Vision-and-Language Tasks'
permalink: /papers/vilbert
usemathjax: true
venue: NeurIPS
year:  2019
topics: 
  - Multi-modal ML
  - BERT
  - Visuo-Linguistic Models
authors:
  - name: Jiaseen Lu
  - name: Dhruv Batra
  - name: Devi Parikh
  - name: Stefan Lee
paperurl: https://papers.nips.cc/paper/2019/file/c74d97b01eae257e44aa9d5bade97baf-Paper.pdf
---

### Problem Statement
- Learning groundings between vision and language is pretrainable and transferable like NLP tasks.

### Approach
- Use self-supervised learning in a fashion similar to BERT in order to learn groundings.
- Separate streams to process visual and linguistic modes in a different fashion:
  - NOT single stream - ["discretizing the space of visual inputs via clustering"](#doubts), treat the visual 'tokens' like text. Issues:
    - Information loss.
    - Identical processing of both modes.
    - Potential to damage pre-trained BERT weights.
  -  Use Transformer blocks(TRM), and **co-attentional transformer layers** (Co-TRM)(proposed):
    - Co-TRM :
      - Combine embeddings from visual and linguistic parts using co-attention.
      <img alt = "ViLBERT CoTRM layer" src="/images/papers/vilbert_cotrm.png" width="500"/>

  - Longer processing for textual part, few extra transformer layers before Co-TRM+TRM blocks.

- Image Representation: 
  - Extract bounding boxes and visual features FastRCNN trained on Visual Genome.
  - Spatial location: 5-d vector from region: normalized top-left coordinates, bottom right coordinates,fraction of area covered, projected to match dimension of visual feature and then summed.(<span style="color:blue">Projected how? linearly?</span>)
  - [IMG] token for start of image features - mean-pooled visual features with a spacial encoding for entire image.

- Two proxy tasks:
  - Masked Multi-modal Modelling:
    - Visual: KL Divergence between prediction softmax distribution, and the Fast-RCNN prediction softmax distribution.
      - Reasons:
        - Language is unlikely to be able to reconstruct exact features.
        - Applying a regression loss could make it difficlut to balance losses incurred by marked image and text inputs.
    - Linguistic: Cross-Entropy, similar to BERT's MLM.

  - Multi-modal Alignment Prediction
    - Whether caption matches the image or not.
    - Output is linear Projection on hadamard product of $h_{[IMG]}$ and $h_{[CLS]}$.
    - Negative Sampling for negative examples.


### Datasets
**Conceptual Captions**
- 3.3 M samples

### Training

**Hyperparams**: 

### Analysis & Results

### Doubts
