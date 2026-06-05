# 《Ashish Vaswani 传记：Transformer 架构之父》

## Chapter 11：完整引用与延伸阅读

> **核心论点**：这一章不是"凑字数"——它是**可复现性**的基础。如果你读完这本传记，想"自己实现Transformer"，这一章给你**所有需要的资源**（论文、代码、教程、视频）。

---

## 📚 核心论文（必读）

### Transformer 原始论文

```
[1] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017).
    "Attention is All You Need".
    NeurIPS 2017.
    arXiv:1706.03762.
    🔗 https://arxiv.org/abs/1706.03762

    必读理由：
      → Transformer的原始论文（所有后续工作的基础）
      → 包含完整的数学推导和架构图
      → 引用100,000+（2026年）

推荐阅读顺序：
    1. 读**摘要**（1页）——了解"为什么要抛弃RNN"
    2. 读**模型架构**部分（3页）——理解Encoder-Decoder结构
    3. 读**实验部分**（2页）——了解在机器翻译任务上的结果
    4. 跳过**附录**（除非你要复现实验）
```

### Multi-Head Attention 详解

```
[2] Vaswani, A., et al. (2017).
    "Attention is All You Need" (Supplementary Material).
    🔗 https://arxiv.org/src/1706.03762/anc/Attention_Is_All_You_Need_Supplement.pdf

    必读理由：
      → 包含Multi-Head Attention的**完整推导**
      → 有**超参数设置**（6 layers, 8 heads, d_model=512）
      → 有**训练细节**（Adam optimizer, learning rate schedule）

[3] Shazeer, N. (2019).
    "Fast Transformer Decoding: One Write-Head is All You Need".
    arXiv:1911.02150.
    🔗 https://arxiv.org/abs/1911.02150

    必读理由：
      → 改进Multi-Head Attention的**解码速度**
      → 提出"Multi-Query Attention"（所有Head共享K/V）
      → 被Llama 2/3采用
```

### Positional Encoding

```
[4] Vaswani, A., et al. (2017).
    "Attention is All You Need" (Section 3.5: Positional Encoding).
    🔗 https://arxiv.org/abs/1706.03762

    必读理由：
      → 原始的正弦/余弦位置编码公式
      → 解释"为什么用正弦/余弦？"（外推性）

[5] Gehring, J., et al. (2017).
    "Convolutional Sequence to Sequence Learning".
    ICML 2017.
    🔗 https://arxiv.org/abs/1705.03122

    必读理由：
      → 提出"可学习位置编码"（与正弦/余弦编码对比）
      → BERT/GPT采用"可学习位置编码"

[6] Su, J., et al. (2021).
    "RoFormer: Enhanced Transformer with Rotary Position Embedding".
    arXiv:2104.09864.
    🔗 https://arxiv.org/abs/2104.09864

    必读理由：
      → 提出"旋转位置编码"（RoPE）
      → 被Llama/Mistral采用
```

---

## 📝 实现教程（推荐）

### 官方实现

```
[7] Google Brain. (2017).
    "TensorFlow Implementation of Transformer".
    GitHub: tensor2tensor.
    🔗 https://github.com/tensorflow/tensor2tensor

    推荐理由：
      → Transformer的**官方实现**（TensorFlow）
      → 包含**完整训练代码**和**预训练模型**
      → 适合"复现论文结果"

[8] Hugging Face. (2019).
    "PyTorch Implementation of Transformer (BERT/GPT-2/GPT-3)".
    GitHub: transformers.
    🔗 https://github.com/huggingface/transformers

    推荐理由：
      → 最流行的Transformer实现（PyTorch）
      → 包含**所有**Transformer变体（BERT、GPT、T5、Llama...）
      → 文档详细（有API说明和示例代码）
```

###  tutorial（初学者推荐）

```
[9] Harvard NLP. (2018).
    "The Annotated Transformer".
    🔗 http://nlp.seas.harvard.edu/annotated-transformer/

    推荐理由：
      → **逐行注释**的Transformer PyTorch实现
      → 适合"想理解每一行代码"的读者
      → 包含**训练示例**（机器翻译）

[10] Alammar, J. (2018).
     "The Illustrated Transformer".
     🔗 https://jalammar.github.io/illustrated-transformer/

     推荐理由：
       → **图文并茂**解释Transformer（有动画）
       → 适合"不喜欢数学公式"的读者
       → 有中文翻译版

[11] Karpathy, A. (2023).
     "Let's Build GPT: From Scratch".
     YouTube: Andrej Karpathy.
     🔗 https://www.youtube.com/watch?v=kCc8FmEb1w

     推荐理由：
       → **视频教程**（2小时），从零实现GPT
       → Karpathy是"代码之神"（Former Tesla AI Director）
       → 适合"视觉学习者"
```

---

## 🎥 视频讲座（深入理解）

### 课程视频

```
[12] Stanford CS224N. (2017).
     "Lecture 14: Transformers and Self-Attention".
     Instructor: Christopher Manning.
     🔗 https://www.youtube.com/watch?v=ptuGllU5SQQ

     推荐理由：
       → Stanford的NLP课程（全球Top 1）
       → 详细讲解Self-Attention的数学推导
       → 有**作业**（实现Transformer做机器翻译）

[13] MIT 6.S094. (2018).
     "Deep Learning for Self-Driving Cars (Lecture 3: Transformer)".
     Instructor: Lex Fridman.
     🔗 https://www.youtube.com/watch?v=KzKhIIDlbEQ

     推荐理由：
       → 用"自动驾驶"案例讲解Transformer
       → 有**可视化**（Attention权重的热力图）
```

### 作者亲自讲解

```
[14] Vaswani, A. (2017).
     "Attention is All You Need" (NeurIPS 2017 Oral Presentation).
     🔗 https://www.youtube.com/watch?v=K07rUmWUmUw

     推荐理由：
       → **第一作者亲自讲解**Transformer
       → 了解"Vaswani当时怎么想的"
       → 有Q&A环节（回答"为什么抛弃RNN？"）

[15] Shazeer, N. (2019).
     "Fast Transformer Decoding" (Google AI Talk).
     🔗 https://www.youtube.com/watch?v=Z_lS8T-xoEg

     推荐理由：
       → 第二作者讲解"如何加速Transformer推理"
       → 了解"工业界视角"（Google的实战经验）
```

---

## 📊 基准数据集（实验必用）

### 机器翻译

```
[16] WMT 2014 English-to-German.
     🔗 http://www.statmt.org/wmt14/

     用途：
       → Transformer论文的**主要实验数据集**
       → 包含4.5M句对（训练集）
       → BLEU分数是主要评估指标

[17] IWSLT 2016 English-to-German.
     🔗 https://wit3.fbk.eu/

     用途：
       → **小规模数据集**（178K句对）
       → 适合"快速原型验证"（2小时训练完）
       → Transformer论文的**消融实验**用这个数据集
```

### 语言模型

```
[18] Penn Treebank (PTB).
     🔗 https://catalog.ldc.upenn.edu/LDC99T42

     用途：
       → 语言模型的标准基准
       → 包含~1M词（训练集）
       → Perplexity是主要评估指标

[19] WikiText-103.
     🔗 https://huggingface.co/datasets/salesforce/wikitext

     用途：
       → 大规模语言模型基准（~100M词）
       → GPT/GPT-2的训练数据集
```

---

## 🔗 延伸阅读（进阶）

### Transformer 变体

```
[20] Devlin, J., et al. (2018).
     "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding".
     NAACL 2019.
     arXiv:1810.04805.
     🔗 https://arxiv.org/abs/1810.04805

     必读理由：
       → **只用Encoder**的Transformer（抛弃Decoder）
       → 提出"Masked Language Modeling"预训练任务
       → 引用80,000+（2026年）

[21] Radford, A., et al. (2018).
     "Improving Language Understanding by Generative Pre-Training".
     OpenAI Blog.
     🔗 https://openai.com/blog/language-unsupervised/

     必读理由：
       → **只用Decoder**的Transformer（抛弃Encoder）
       → 提出"自回归语言模型"预训练任务
       → GPT系列的基础

[22] Raffel, C., et al. (2019).
     "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer".
     JMLR 2020.
     arXiv:1910.10683.
     🔗 https://arxiv.org/abs/1910.10683

     必读理由：
       → **完整Encoder-Decoder**的Transformer
       → 将所有NLP任务统一成"文本到文本"
       → T5的基础
```

### 多模态 Transformer

```
[23] Dosovitskiy, A., et al. (2020).
     "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale".
     ICLR 2021.
     arXiv:2010.11929.
     🔗 https://arxiv.org/abs/2010.11929

     必读理由：
       → **Vision Transformer (ViT)** 的原始论文
       → 把图像分成"patches"，当成"词"处理
       → 在ImageNet上达到SOTA

[24] Radford, A., et al. (2021).
     "Learning Transferable Visual Models From Natural Language Supervision".
     ICML 2021.
     arXiv:2103.00020.
     🔗 https://arxiv.org/abs/2103.00020

     必读理由：
       → **CLIP** 的原始论文
       → 同时训练"文本编码器"和"图像编码器"
       → 零样本图像分类惊艳
```

---

## ⚠️ 风险披露

- 本章的引用列表是**精选**（不是所有相关论文），可能遗漏重要工作。
- 链接（URL）可能在2026年后失效（建议用Internet Archive备份）。
- "必读理由"是**作者观点**，非学术共识。
- 作者可能持有AI相关股票（如NVDA、GOOGL），存在利益冲突可能。

---

*Chapter 11 完成。下一章（最终章）：Chapter 12 — 总结：Vaswani留给世界的礼物*
