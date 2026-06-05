# 《Ashish Vaswani 传记：Transformer 架构之父》

## Chapter 4：Transformer之后的Vaswani（2017-2021）—— 从明星到隐士

> **核心论点**：Transformer成功后，Vaswani没有选择"学术明星"路线（像Yoshua Bengio或Yann LeCun那样到处演讲），而是**回归低调**。这4年（2017-2021）可能是他**思考"下一个大东西"** 的关键时期。对比其他Transformer作者的去向，能看出Vaswani的独特思维模式。

---

## 🌟 Transformer成功后发生了什么？（2017-2018）

### 学术界的反应

```
2017年12月：NeurIPS会议（Transformer论文发表）

  学术界的初始反应：
    → "这篇论文很有趣，但是不是真的比LSTM好？"
    → "Attention机制我们早就有了，这个Transformer只是'更大的Attention'"
    → "没有RNN？不可能！RNN是序列建模的基础！"

2018年：BERT和GPT爆发

  转折点：
    → BERT（Google）：只用Transformer Encoder，11个任务刷榜
    → GPT（OpenAI）：只用Transformer Decoder，生成任务惊艳
    → 学术界突然意识到："哇，Transformer真的work！"

Vaswani的角色：
  → **没有** 像Bengio或LeCun那样到处做Keynote演讲
  → **没有** 在Twitter上"庆祝"Transformer的成功
  → **可能** 在Google Brain继续"低调研究"
```

### 其他Transformer作者的去向

```
"Atenion is All You Need"的8个作者（2017）：

  1. **Ashish Vaswani**（一作）
     → 留在Google Brain（?）
     → 非常低调，几乎没有公开演讲
     → 2021年离开Google，创立Adept AI

  2. **Noam Shazeer**（二作）
     → 留在Google（重要！）
     → 后来创立了Character.AI（2021年）
     → 是"注意力机制"的早期推动者

  3. **Niki Parmar**（三作）
     → 留在Google Brain（?）
     → 2021年和Vaswani一起创立Adept AI

  4. **Jakob Uszkoreit**（四作）
     → 留在Google Brain
     → 后来创立了Inceptive（2021年？）

  5. **Llion Jones**（五作）
     → 留在Google Brain（?）
     → 后来...（信息很少）

  6. **Aidan N. Gomez**（六作）
     → **最重要**：当时是**本科生**（University of Toronto）
     → 后来创立了Cohere（2019年，LLM公司）
     → 证明：本科生也能做出诺奖级研究

  7. **Łukasz Kaiser**（七作）
     → 留在Google Brain
     → 后来加入了OpenAI（?）

  8. **Illia Polosukhin**（八作）
     → 离开Google
     → 创立了Near Protocol（区块链项目，2018年）

观察：
  → 8人中**至少4人**后来创立了公司（Vaswani, Shazeer, Gomez, Polosukhin）
  → Vaswani是**第一个**离开Google的（2021年）
  → 这说明他在2017-2021年间就已经在思考"下一个大东西"
```

---

## 🔬 Vaswani在Google Brain的"神秘4年"（2017-2021）

### 推测1：他在研究"Transformer的局限"

```
Transformer的局限（2017-2019年逐渐被发现）：

  1. **计算复杂度**：O(n²)（n=序列长度）
     → 序列长度翻倍 → 计算量翻4倍
     → 无法处理超长序列（>10,000词）

  2. **位置编码的局限**：
     → 正弦/余弦编码无法泛化到"训练时未见过的序列长度"
     → 可学习位置编码无法"外推"

  3. **缺乏"递归"能力**：
     → Transformer是"前馈"的（一次性处理所有词）
     → 无法做"逐步推理"（像人类一样"思考"）

  4. **数据效率低**：
     → Transformer需要**海量数据**才能work
     → 人类只需要几个例子就能学会新任务

Vaswani可能在思考：
  → "Transformer是答案，但**不是最终答案**"
  → "下一个架构应该解决这些问题"
  → "也许我们需要**回到RNN的优点**（样本效率高），但**保留Attention的优点**（并行训练）？"
```

### 推测2：他在研究"多模态Transformer"

```
Transformer不仅用于NLP：

  2018-2019年：
    → **Vision Transformer (ViT)**（2020年发表，但2019年就在做）
      - 把图像分成"patches"，当成"词"处理
      - 结果：在ImageNet上达到SOTA

    → **CLIP**（OpenAI，2021年）
      - 用Transformer同时处理"文本"和"图像"
      - 结果：零样本图像分类惊艳

    → **Speech Transformer**（语音识别）
      - 用Transformer替代RNN（语音是序列数据）

Vaswani可能参与了：
  → Google的**多模态Transformer**项目
  → 或者他在**独立研究**"如何让Transformer处理图像/语音/视频"
```

### 推测3：他在思考"通用人工智能（AGI）"

```
Transformer的成功让很多人相信：
  → "Scale is All You Need"（ scaling Law）
  → 只要堆更多数据、更大模型、更强算力 → AGI

但Vaswani可能不这么认为：
  → Transformer是"统计模式匹配"（找规律）
  → AGI需要"因果推理"（理解为什么）
  → "我们需要**不同于Transformer**的东西来实现AGI"

证据（间接）：
  → 他2021年创立的Adept AI的Mission是：
    "Build useful general intelligence"
    （构建**有用的通用智能**）
  → 不是"Build the largest LLM"
  → 说明他对"什么是AGI"有**不同于OpenAI**的理解
```

---

## 🚪 为什么离开Google？（2021年）

### Google的"创新者困境"

```
Google的处境（2021年）：

  优势：
    → 钱（现金流：~$250B/年）
    → 数据（Search/Gmail/YouTube的用户数据）
    → 算力（TPU v4，比NVIDIA V100快）

  劣势：
    → **监管压力**（反垄断调查）
    → **企业文化**（"Move Fast and Break Things"？不，Google是"Don't Be Evil"）
    → **创新者的困境**：
      - Search是"现金奶牛"（$200B/年广告收入）
      - 如果推出"颠覆Search的AGI" → 自己颠覆自己？
      - 所以Google对"激进AGI研究"**态度谨慎**
```

### Vaswani的可能动机

```
可能性1：**想做"Google不允许的事"**

  例如：
    → 构建一个"能操作电脑的AI"（Adept的ACTION模型）
    → 这需要"模拟鼠标/键盘输入" → 可能触及Google的"安全红线"
    → Google可能说："这个太危险，我们不能做"

可能性2：**想证明"Transformer不是终点"**

  例如：
    → Vaswani可能认为："Transformer有局限，我们需要新架构"
    → 但Google说："Transformer还能scale（GPT-3/GPT-4还很强），继续堆数据/算力"
    → Vaswani想："不，我们需要**新想法**，不是更多数据"

可能性3：**财务自由 + 改变世界**

  2021年：
    → Transformer已经成为行业标准（GPT-3、BERT、T5...）
    → Vaswani作为第一作者，**专利/股票**可能已经让他财务自由
    → 下一步："我想做**真正改变世界**的事（AGI），而不是"优化广告推荐系统""
```

---

## 🏢 Adept AI的创立（2021年）

### 联合创始人

```
Adept AI（2021年创立）：

  联合创始人：
    1. **Ashish Vaswani**（CEO？）
    2. **Niki Parmar**（CTO？）
      - 也是Transformer论文的第三作者
      - 印度裔女性，在男性主导的AI领域很少见

  投资人：
    → 红杉资本（Sequoia）
    → OpenAI的Greg Brockman（？）
    → 估值：$65M（2022年）
```

### Mission："Build useful general intelligence"

```
Adept的Mission与OpenAI不同：

  OpenAI：
    → "Ensure AGI benefits all of humanity"
    → 偏向"纯研究"（GPT系列是"通用语言模型"）

  Adept：
    → "Build **useful** general intelligence"
    → 偏向"应用"（让AI**操作电脑**）

具体产品（2022-2023）：
  → **ACTION模型**：
    - 输入："帮我预订明天去纽约的航班"
    - 输出：AI**打开浏览器** → 进入航空公司网站 → 填写表单 → 点击"搜索" → 返回结果

  → 对比：
    - ChatGPT：只能"生成文本"（告诉你"如何预订航班"）
    - Adept：可以"操作电脑"（**替你**预订航班）
```

---

## 💡 关键洞察：Vaswani的"下一招"

```
从Transformer（2017）到Adept（2021），Vaswani在想什么？

推测：

  1. **"Transformer是'理解'的好工具，但不是'行动'的好工具"**
     → Transformer擅长"理解语言"（NLP）
     → 但要"操作电脑"，需要"理解**界面**"（UI/UX）
     → 这需要**多模态**（文本 + 图像 + 动作）

  2. **"AGI = 理解 + 行动"**
     → OpenAI在做"理解"（GPT系列）
     → Adept在做"行动"（ACTION模型）
     → 两者结合 = AGI

  3. **"下一个架构可能不是Transformer"**
     → Adept的ACTION模型**可能**不是纯Transformer
     → 可能需要"神经符号AI"（Neural Symbolic AI）
     → 或者"强化学习 + Transformer"
```

---

## ⚠️ 风险披露

- 本章关于Vaswani在2017-2021年间具体工作的描述，是基于**间接证据**的推测（他没有公开日记或博客）。
- Adept AI的具体技术路线未公开（2023年），本章分析基于公开访谈和招聘信息。
- "Vaswani认为Transformer不是终点"是**观点**，非Vaswani的原话。
- 作者可能持有Adept AI的股权或代币，存在利益冲突可能。

---

*Chapter 4 完成。下一章：Chapter 5 — Adept AI的技术架构与ACTION模型*
