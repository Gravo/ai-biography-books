# -*- coding: utf-8 -*-
"""Yann LeCun书籍PDF转换脚本"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import re

# 注册中文字体
pdfmetrics.registerFont(TTFont('msyh', 'C:/Windows/Fonts/msyh.ttc', subfontIndex=0))

def create_pdf():
    doc = SimpleDocTemplate(
        "C:/Users/Gao Wei/.qclaw/workspace/lecun-book/yann-lecun-book.pdf",
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    styles = getSampleStyleSheet()
    
    # 自定义样式
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontName='msyh',
        fontSize=24,
        spaceAfter=30,
        alignment=1
    )
    
    h1_style = ParagraphStyle(
        'CustomH1',
        parent=styles['Heading1'],
        fontName='msyh',
        fontSize=18,
        spaceBefore=20,
        spaceAfter=12
    )
    
    h2_style = ParagraphStyle(
        'CustomH2',
        parent=styles['Heading2'],
        fontName='msyh',
        fontSize=14,
        spaceBefore=15,
        spaceAfter=8
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontName='msyh',
        fontSize=11,
        leading=18,
        spaceAfter=8
    )
    
    quote_style = ParagraphStyle(
        'CustomQuote',
        parent=styles['Normal'],
        fontName='msyh',
        fontSize=11,
        leading=18,
        leftIndent=20,
        textColor=colors.HexColor('#555555'),
        spaceAfter=10
    )
    
    story = []
    
    # 标题
    story.append(Paragraph("Yann LeCun: $1B Bet Against LLMs", title_style))
    story.append(Paragraph("世界模型之父的豪赌", ParagraphStyle('Subtitle', parent=body_style, fontSize=14, alignment=1)))
    story.append(Spacer(1, 30))
    
    # 第一章
    story.append(Paragraph("第一章：深度学习教父", h1_style))
    story.append(Paragraph("1.1 从巴黎到纽约", h2_style))
    story.append(Paragraph("Yann LeCun(杨立昆)，1960年出生于法国巴黎郊区。他是卷积神经网络(CNN)的发明者、深度学习三巨头之一、2018年图灵奖得主。", body_style))
    
    story.append(Paragraph("关键里程碑：", body_style))
    milestones = [
        ["年份", "事件"],
        ["1960", "出生于法国巴黎"],
        ["1987-1988", "在AT&T贝尔实验室开发LeNet"],
        ["1998", "发表CNN开创性论文"],
        ["2003", "加入纽约大学"],
        ["2013", "加入Facebook(现Meta)"],
        ["2018", "获得图灵奖"],
        ["2025.11", "离开Meta，创办AMI Labs"],
        ["2026.3", "完成10.3亿美元种子轮融资"]
    ]
    t = Table(milestones, colWidths=[3*cm, 10*cm])
    t.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'msyh'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4472C4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t)
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("1.2 卷积神经网络之父", h2_style))
    story.append(Paragraph("LeCun最著名的贡献是卷积神经网络(CNN)：", body_style))
    story.append(Paragraph("LeNet-5(1998)：首个成功的CNN架构，用于手写数字识别", body_style))
    story.append(Paragraph("反向传播算法：与Hinton等人共同推广", body_style))
    story.append(Paragraph("深度学习基础：奠定了现代AI视觉技术的基础", body_style))
    
    # 第二章
    story.append(PageBreak())
    story.append(Paragraph("第二章：LLM的四大致命缺陷", h1_style))
    story.append(Paragraph("2.1 2025达沃斯预言", h2_style))
    story.append(Paragraph("2025年冬季达沃斯技术辩论现场，LeCun抛出震撼观点：", body_style))
    story.append(Paragraph("当前的大语言模型(LLM)范式将在3-5年内被淘汰。", quote_style))
    story.append(Paragraph("LLM就像从未接触过物理世界的数字婴儿。", quote_style))
    
    story.append(Paragraph("2.2 四大核心缺陷", h2_style))
    story.append(Paragraph("缺陷一：缺乏对物理世界的理解", body_style))
    story.append(Paragraph("LLM通过文本学习，从未真正看见或触摸过世界。它们知道球会掉落这个词组，却不理解重力是什么。", body_style))
    
    story.append(Paragraph("缺陷二：缺乏持久记忆", body_style))
    story.append(Paragraph("尽管GPT-4 Turbo支持128k tokens上下文，但本质仍是滑动窗口式记忆。", body_style))
    
    story.append(Paragraph("缺陷三：缺乏推理能力", h2_style))
    story.append(Paragraph("LLM擅长操控语言，但并不擅长思考。", quote_style))
    
    story.append(Paragraph("缺陷四：缺乏复杂规划能力", body_style))
    story.append(Paragraph("LLM无法进行多步骤、长期规划。人类能规划去超市买菜的完整流程，LLM只能逐词生成。", body_style))
    
    # 第三章
    story.append(PageBreak())
    story.append(Paragraph("第三章：世界模型愿景", h1_style))
    story.append(Paragraph("3.1 什么是世界模型？", h2_style))
    story.append(Paragraph("世界模型(World Model)是LeCun提出的下一代AI核心概念：一个能学习并理解物理世界结构与规律的AI系统。", body_style))
    
    capabilities = [
        ["能力", "说明"],
        ["物理理解", "懂重力、懂因果、懂空间关系"],
        ["预测能力", "能模拟如果这样做，会发生什么"],
        ["规划能力", "能制定多步骤行动计划"],
        ["持久记忆", "能积累经验并复用"]
    ]
    t2 = Table(capabilities, colWidths=[3*cm, 10*cm])
    t2.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'msyh'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4472C4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t2)
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("3.2 JEPA架构", h2_style))
    story.append(Paragraph("联合嵌入预测架构(JEPA)是LeCun提出的技术方案：", body_style))
    story.append(Paragraph("不预测下一个token，而是预测抽象表示", body_style))
    story.append(Paragraph("通过观察视频和与环境交互来学习世界如何运行", body_style))
    story.append(Paragraph("分层结构支持更抽象、更长期的预测", body_style))
    
    jepa_versions = [
        ["模型", "时间", "特点"],
        ["I-JEPA", "2023.6", "图像联合嵌入预测"],
        ["V-JEPA", "2024", "视频联合嵌入预测"],
        ["V-JEPA 2", "2025.6", "比英伟达Cosmos快30倍"]
    ]
    t3 = Table(jepa_versions, colWidths=[3*cm, 3*cm, 7*cm])
    t3.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'msyh'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4472C4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t3)
    story.append(Spacer(1, 15))
    
    # 第四章
    story.append(PageBreak())
    story.append(Paragraph("第四章：离开Meta", h1_style))
    story.append(Paragraph("4.1 离职背景", h2_style))
    story.append(Paragraph("2025年11月19日，LeCun宣布将在年底离开效力十年的Meta，创办自己的AI公司。", body_style))
    
    story.append(Paragraph("离职原因：", body_style))
    story.append(Paragraph("1. 技术路线分歧：LeCun长期主张LLM无法实现人类水平智能", body_style))
    story.append(Paragraph("2. 商业化冲突：学术路线与公司产品化战略冲突", body_style))
    story.append(Paragraph("3. 独立愿景：想更快、更便宜、更好地实现世界模型", body_style))
    
    story.append(Paragraph("这玩意儿我自己干，能更快更便宜更好。", quote_style))
    
    # 第五章
    story.append(PageBreak())
    story.append(Paragraph("第五章：AMI Labs与$1B豪赌", h1_style))
    story.append(Paragraph("5.1 公司概况", h2_style))
    
    company_info = [
        ["维度", "信息"],
        ["成立时间", "2025年11月"],
        ["创始人", "Yann LeCun"],
        ["CEO", "Alexandre Lebrun"],
        ["使命", "让系统能理解物理世界、拥有持久记忆、具备推理能力"],
        ["技术路线", "世界模型 + JEPA架构"],
        ["团队规模", "约12人"]
    ]
    t4 = Table(company_info, colWidths=[3*cm, 10*cm])
    t4.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'msyh'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4472C4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t4)
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("5.2 10.3亿美元种子轮", h2_style))
    story.append(Paragraph("2026年3月10日，AMI Labs宣布完成约10.3亿美元种子轮融资：", body_style))
    
    funding_info = [
        ["项目", "数据"],
        ["融资金额", "10.3亿美元"],
        ["投前估值", "35亿美元"],
        ["投资轮次", "种子轮"],
        ["历史意义", "欧洲有史以来最大种子轮"]
    ]
    t5 = Table(funding_info, colWidths=[3*cm, 10*cm])
    t5.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'msyh'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4472C4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t5)
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("投资方阵容：", body_style))
    story.append(Paragraph("领投方：凯辉创新基金、Greycroft、Hiro Capital、HV Capital、Jeff Bezos Expeditions", body_style))
    story.append(Paragraph("跟投方：淡马锡、英伟达、Toyota Ventures、三星、Eric Schmidt、Tim Berners-Lee等", body_style))
    
    story.append(Paragraph("5.3 为什么是$1B Bet Against LLMs？", h2_style))
    
    comparison = [
        ["传统LLM路线", "LeCun的世界模型路线"],
        ["预测下一个token", "预测物理世界状态"],
        ["文本训练", "视频+交互训练"],
        ["语言智能", "物理智能"],
        ["ChatGPT、Claude、LLaMA", "JEPA、V-JEPA、AMI Labs"]
    ]
    t6 = Table(comparison, colWidths=[6.5*cm, 6.5*cm])
    t6.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'msyh'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4472C4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t6)
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("我认为五年内，没有人会再把当下的LLM模式当作AI系统的核心组件使用。", quote_style))
    
    # 第六章
    story.append(PageBreak())
    story.append(Paragraph("第六章：学术贡献与合作", h1_style))
    story.append(Paragraph("6.1 何恺明合作：无需归一化的Transformer", h2_style))
    story.append(Paragraph("2025年CVPR收录论文：何恺明(MIT副教授)与LeCun合作提出无需归一化的Transformer。归一化层长期以来被认为是神经网络的必要组件，这项发现挑战了传统认知。", body_style))
    
    # 第七章
    story.append(Paragraph("第七章：观点与争议", h1_style))
    story.append(Paragraph("7.1 对LLM的持续批判", h2_style))
    story.append(Paragraph("核心论点：", body_style))
    story.append(Paragraph("1. LLM无法超越训练数据，无法创造新概念", body_style))
    story.append(Paragraph("2. 自回归生成导致缺乏全局规划", body_style))
    story.append(Paragraph("3. 文本只是世界的符号表示，真正的智能需要理解物理世界", body_style))
    
    story.append(Paragraph("7.2 六个月后预言", h2_style))
    story.append(Paragraph("六个月后，每家公司都会自称是世界模型来筹集资金。", quote_style))
    
    # 第八章
    story.append(PageBreak())
    story.append(Paragraph("第八章：未来展望", h1_style))
    story.append(Paragraph("8.1 世界模型的应用前景", h2_style))
    
    applications = [
        ["领域", "应用场景"],
        ["机器人", "家务机器人、工业机器人可靠操控"],
        ["自动驾驶", "更可靠的物理场景预测"],
        ["医疗", "手术机器人精确操控"],
        ["仿真", "高保真物理模拟"]
    ]
    t7 = Table(applications, colWidths=[3*cm, 10*cm])
    t7.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'msyh'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4472C4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t7)
    story.append(Spacer(1, 15))
    
    # 结语
    story.append(PageBreak())
    story.append(Paragraph("结语：一场豪赌的意义", h1_style))
    story.append(Paragraph("LeCun的$1B豪赌，不只是资金，更是信念：", body_style))
    story.append(Paragraph("他在赌：", body_style))
    story.append(Paragraph("LLM不是AI的终点", body_style))
    story.append(Paragraph("理解物理世界才是智能的核心", body_style))
    story.append(Paragraph("世界模型将在5年内取代LLM成为AI系统的核心", body_style))
    
    story.append(Paragraph("如果赌对了：", body_style))
    story.append(Paragraph("开启机器人技术新纪元", body_style))
    story.append(Paragraph("AI能真正帮助人类处理物理世界的任务", body_style))
    story.append(Paragraph("欧洲AI产业翻盘", body_style))
    
    story.append(Spacer(1, 20))
    story.append(Paragraph("正如LeCun所说：", body_style))
    story.append(Paragraph("LLM能通过律师资格考试，但清不了一张餐桌。", quote_style))
    story.append(Paragraph("他赌的是一个能真正干活的AI。", body_style))
    
    # 时间线
    story.append(PageBreak())
    story.append(Paragraph("附录：时间线", h1_style))
    timeline = [
        ["年份", "事件"],
        ["1960", "出生于法国巴黎"],
        ["1987-88", "开发LeNet"],
        ["1998", "发表CNN开创性论文"],
        ["2003", "加入纽约大学"],
        ["2013", "加入Meta"],
        ["2018", "获得图灵奖"],
        ["2022", "提出分层JEPA架构"],
        ["2023.6", "发布I-JEPA"],
        ["2025.1", "达沃斯预言LLM将在3-5年被淘汰"],
        ["2025.6", "发布V-JEPA 2"],
        ["2025.11.19", "宣布离开Meta"],
        ["2026.3.10", "完成10.3亿美元种子轮"]
    ]
    t8 = Table(timeline, colWidths=[3*cm, 10*cm])
    t8.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'msyh'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4472C4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t8)
    
    # 生成PDF
    doc.build(story)
    print(f"PDF: C:/Users/Gao Wei/.qclaw/workspace/lecun-book/yann-lecun-book.pdf")

if __name__ == "__main__":
    create_pdf()
