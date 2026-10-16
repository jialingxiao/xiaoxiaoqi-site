# -*- coding: utf-8 -*-
"""吐司日报 第180期 公众号排版版（复用179期深色主题CSS）"""
import re

BASE = "/Coze/Drive/吐司/所有对话/主对话/吐司日报"
with open(f"{BASE}/第179期/公众号排版_179期.html", encoding="utf-8") as f:
    old = f.read()

css = re.search(r"<style>(.*?)</style>", old, re.S).group(1).strip()

HEAD = "https://s.coze.cn/image/1Cce_eD5Ucs/"
A = ["https://s.coze.cn/image/hUTO0jYjwx0/", "https://s.coze.cn/image/drVxdTIRw7Y/",
     "https://s.coze.cn/image/T9keIimy-f8/", "https://s.coze.cn/image/hFuNBp6sPhw/"]
M = ["https://s.coze.cn/image/IoYnpSBRVH4/", "https://s.coze.cn/image/4NtJgBNKIbM/",
     "https://s.coze.cn/image/tmyI-9Aswcw/", "https://s.coze.cn/image/lD7jDzO5BEM/"]

def article(kind, no, img, alt, title, body, source):
    return f'''    <div class="article-card">
        <span class="article-number {kind}">{no}</span>
        <img class="article-image" src="{img}" alt="{alt}">
        <div class="article-content">
            <div class="article-title">{title}</div>
            <div class="article-body">
                {body}
            </div>
            <div class="article-source">{source}</div>
        </div>
    </div>'''

ai_cards = [
    article("ai", "NO.01", A[0], "RTX Spark个人智能体PC",
      "英伟达RTX Spark个人智能体PC全球开售：128GB统一内存本地跑1250亿参数，18999元起",
      "10月16日晚8点，全球首款专为个人智能体打造的Windows电脑<strong>NVIDIA RTX Spark</strong>全球开售，华硕、戴尔、联想、微软、微星五大OEM同步。集成Blackwell RTX GPU与Grace CPU，最高128GB统一内存、FP4下1 PFLOPS，本地可跑最高<strong>1250亿参数智能体</strong>、离线跑1200亿参数大模型，数据不出本机、零Token成本。华硕ProArt创16（37999元）首发迅速售罄。<strong>AI算力正从云端数据中心大规模下放至个人桌面。</strong>",
      "NVIDIA Newsroom · IT之家 · 智东西 · 2026-10-16"),
    article("ai", "NO.02", A[1], "微软MAI-Base-2模型",
      "微软自研MAI-Base-2完成预训练：2.8万亿MoE、性能超GPT-5.6 Sol基座，算力仅OpenAI的1/4",
      "微软10月15日宣布完成新一代SOTA基础模型<strong>MAI-Base-2</strong>预训练：MoE架构、总参数2.8万亿、激活800亿，在6000块GB200上训练38天，算力效率为DeepSeek-V4-Pro-Base的<strong>4-12倍</strong>，性能强于所有参测开源权重模型。AI主管苏莱曼称其已超越驱动GPT-5.6 Sol的模型（代号Spud），训练算力仅OpenAI同类的<strong>1/4</strong>，并已启动MAI-Base-3。<strong>微软正以高效自研模型降低对OpenAI的依赖。</strong>",
      "微软AI官方博客 · 财联社 · IT之家 · 2026-10-16"),
    article("ai", "NO.03", A[2], "人形机器人医院导诊",
      "智元机器人×蚂蚁阿福落地北大人民医院：人形导诊机器人66个工作日交互4.7万次，日均707次",
      "10月16日，智元机器人与蚂蚁阿福合作的智慧医院导诊项目正式落地<strong>北京大学人民医院</strong>。灵犀X2机器人接入阿福AI就医助理及医疗大模型、对接医院私有知识库，承接科室指引、就诊流程、医保政策、院内导航等咨询。截至9月30日累计服务66个工作日、交互<strong>46686次</strong>、日均约707次、单日峰值1420次。<strong>人形机器人在三甲医院公共服务场景的常态化落地能力得到验证。</strong>",
      "北京商报 · 2026-10-16"),
    article("ai", "NO.04", A[3], "技术出口管制",
      "商务部拟将40项关键技术纳入出口管制：AI占23项含大模型智能体算力集群，14项禁止出口",
      "10月16日商务部、科技部发布2026年第48号公告，就修订《中国禁止出口限制出口技术目录》公开征求意见，拟增列人工智能、生物医药、光伏三领域<strong>40项技术</strong>并同步实施出口前登记。AI领域涉大模型、智能体、算力集群、信息处理等<strong>23项</strong>；14项拟禁止出口、26项限制出口；已开源或发表论文进入公共领域的技术不纳入管理。生物医药涉细胞基因治疗、小核酸药等5项。<strong>前沿AI技术贸易进入常态化安全管控阶段。</strong>",
      "商务部官网 · 新华财经 · 中国经济网 · 2026-10-16"),
]

med_cards = [
    article("med", "NO.01", M[0], "蚂蚁阿福入选时代最佳发明",
      "蚂蚁阿福入选《时代》2026年度最佳发明：今年唯一上榜中国AI应用，1.5亿用户、日咨询近2000万",
      "北京时间10月15日晚，美国《时代》周刊揭晓2026年度“全球最佳发明”，蚂蚁集团健康AI<strong>“蚂蚁阿福”</strong>入选，为今年唯一上榜中国AI应用（去年为DeepSeek）。截至9月阿福App用户达<strong>1.5亿</strong>、单日健康咨询近2000万次，连接5000家医院、30万名真人医生，三线及以下用户超8400万、中老年超30%，并推出方言与长辈模式。<strong>对比ChatGPT Health仍停留问答层，中国AI已打通挂号、问诊、医保结算全链路。</strong>",
      "澎湃新闻 · 第一财经 · 2026-10-16"),
    article("med", "NO.02", M[1], "人形机器人进三甲",
      "人形机器人进三甲同日，信通院报告：上半年全球出货超2.2万台、同比近300%，中国产业链高度集中",
      "在智元×蚂蚁阿福落地北大人民医院同日，中国信通院联合清华大学发布《具身智能发展报告（2026）》：2026上半年全球人形机器人出货超<strong>2.2万台</strong>、同比增长近<strong>300%</strong>；文娱商演与科教数采占比超60%、导览导购约19%、智能制造约13%；中国产业链企业高度集中于京粤沪苏浙，前五省市占比超八成。<strong>具身智能正从展示体验走向真实使用、从单点验证走向规模应用。</strong>",
      "中国新闻网 · 北京商报 · 2026-10-16"),
    article("med", "NO.03", M[2], "创新药获批",
      "NMPA批准中药创新药紫花温肺止嗽颗粒上市，苑东生物第三代白血病靶向药泊那替尼获药品注册证",
      "10月16日国家药监局批准中药创新药<strong>紫花温肺止嗽颗粒</strong>上市并列入创新药品名录；同日苑东生物公告第三代BCR-ABL酪氨酸激酶抑制剂<strong>泊那替尼片</strong>获《药品注册证书》，用于经一/二代TKI耐药及伴T315I突变的慢性髓细胞白血病、费城染色体阳性急性淋巴细胞白血病成人患者。此外泰恩康聚多卡醇注射液获批、西藏药业PCSK9体内基因编辑药ART002g1获美国FDA临床许可。<strong>中药创新与高端化药、基因治疗管线同步推进。</strong>",
      "国家药监局 · 金融界 · 2026-10-16"),
    article("med", "NO.04", M[3], "AI自主开处方",
      "全球首例：美国犹他州批准AI无医生把关直接“新诊断+首开处方”，Doctor in the Loop边界再被试探",
      "据36氪报道，美国犹他州今年9月批准一个新项目，AI系统将首次在<strong>没有人类医生把关</strong>的情况下为患者作出新诊断并开具处方。此前该州仅允许AI为病情稳定的慢性病患者续开“老药”，不得下新诊断或调整剂量，所有改变须经医生审核。新项目把AI权限推进到“新诊断+首处方”，全球首次越过人在回路红线，引发医疗责任与安全广泛讨论。<strong>医疗AI自主权边界正从“医生审核”向“有限自主”谨慎试探。</strong>",
      "36氪 · 2026-10-15"),
]

flashes = [
    ("估值回调", "Anthropic部分投资者转向约1.5万亿美元估值，Q3营收168亿、环比增45%但增速大幅放缓"),
    ("IPO承压", "Anthropic拟募资约1000亿美元冲击史上最大IPO，消息传出后美光、SK海力士等AI硬件股盘前跳水"),
    ("算力账本", "黄仁勋称几万亿美元AI基建压力不该全压在OpenAI身上，CoreWeave五年期CDS利差升破1190基点"),
    ("云信用风险", "黄仁勋表态英伟达无需为CoreWeave财务兜底，其部分债券收益率升至15%-16%"),
    ("端侧AI", "NVIDIA RTX Spark个人智能体PC全球开售，本地跑1250亿参数，五大PC品牌同步推出"),
    ("自研模型", "微软MAI-Base-2完成预训练：2.8万亿MoE、800亿激活，性能超GPT-5.6 Sol基座"),
    ("开源模型", "Meta Muse Spark Open开放8160亿参数权重（激活420亿、100万上下文），联手苹果MLX本地部署"),
    ("出口管制", "商务部拟增列40项关键技术出口管制，AI占23项，已开源技术不纳入"),
    ("量子计算", "谷歌《科学》论文：Willow验证“魔态培育”，量子错误率降低约40倍、T态保真度99.99%"),
    ("AI数学", "OpenAI与Anthropic联西蒙斯基金会投1500万美元，资助数学家评估AI研究成果"),
    ("AI Infra", "无问芯穹完成23亿元C轮、累计43亿，已保密递表港交所；硅基流动毛利率转负"),
    ("医疗AI荣誉", "蚂蚁阿福入选《时代》2026年度最佳发明，为今年唯一上榜中国AI应用"),
    ("具身落地", "智元×蚂蚁阿福导诊机器人落地北大人民医院，66个工作日交互4.7万次"),
    ("行业数据", "信通院：上半年全球人形机器人出货超2.2万台、同比近300%，中国产业链高度集中"),
    ("创新药", "NMPA批准中药创新药紫花温肺止嗽颗粒；苑东生物泊那替尼片获药品注册证"),
    ("AI自主处方", "美国犹他州批准全球首个AI无医生把关的“新诊断+首开处方”项目"),
]
flash_html = ""
for i, (cat, txt) in enumerate(flashes, 1):
    flash_html += f'''            <div class="flash-item">
                <span class="flash-num">{i:02d}</span>
                <span class="flash-cat">{cat}</span>
                <span class="flash-text">{txt}</span>
            </div>
'''

insights = [
    ("趋势一 · Anthropic的“估值折价时刻”：史上最大IPO撞上AI基建信用焦虑",
     "承接上期叙事，Anthropic投资者日效应持续：部分投资者把估值锚从约2万亿下调至约<strong>1.5万亿美元</strong>，Q3营收168亿、环比增速由Q2超100%回落至45%。尽管单季首次调整后盈利、自由现金流转正、每1美元算力换回1.7美元收入，但未来十年5180亿美元不可取消的云算力承诺，让市场第一次用“可持续利润”而非“增长故事”为其定价。情绪外溢：CoreWeave五年期CDS利差破1190基点、美光与SK海力士盘前跳水。<strong>AI产业正从“不计成本建算力”切换到“追问每一块钱算力的回报率”，这场IPO将成为整个AI牛市的压力测试。</strong>"),
    ("趋势二 · 云端焦虑与端侧爆发同框，AI算力分配开始重构",
     "10月16日出现意味深长的对照——一边是黄仁勋回应AI基建能否支撑天量资本开支、CoreWeave信用警报拉响；另一边是NVIDIA RTX Spark开售，把1 PFLOPS算力、128GB统一内存和1250亿参数本地智能体塞进18999元起的笔记本。叠加微软以1/4算力训出超越GPT-5.6 Sol基座的MAI-Base-2、Meta开放8160亿参数权重，<strong>“云端集中训练+端侧分布式推理”新分工成型：敏感数据与高频推理下沉本地，云端回归超大模型训练与重负载。</strong>"),
    ("趋势三 · 医疗AI“中国式可及性”被世界看见，评价标尺从参数转向普惠",
     "蚂蚁阿福成为今年唯一入选《时代》最佳发明的中国AI应用，靠的不是最大参数，而是1.5亿用户、近2000万次日咨询、连通5000家医院与30万医生，以及覆盖县城、村医、方言和老人的真实可及性；同一天智元机器人接入阿福能力进北大人民医院承担日均707次导诊。而美国犹他州却在反向试探“AI无医生直接开处方”的自主权红线。<strong>决定医疗AI价值的不再是模型“能飞多高”，而是能否嵌入真实就医与支付闭环、在保证人在回路安全的前提下“接住更多人”。</strong>"),
]
insight_html = ""
for label, text in insights:
    insight_html += f'''            <div class="insight-item">
                <div class="insight-label">{label}</div>
                <div class="insight-text">{text}</div>
            </div>
'''

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>吐司日报 · 第180期 · 2026-10-17</title>
    <style>
{css}
    </style>
</head>
<body>
<div class="container">

    <div class="cover-card">
        <div class="cover-inner">
            <div class="cover-logo">吐 司 日 报</div>
            <div class="cover-title">DAILY BRIEFING</div>
            <div class="cover-en">VOL.180 · 2026.10.17 · SAT</div>
            <img class="cover-image" src="{HEAD}" alt="AI估值折价与端侧算力爆发">
            <div class="cover-meta">
                <span>📅 2026年10月17日</span>
                <span>📖 阅读约10分钟</span>
                <span>🔢 第180期</span>
            </div>
            <div class="cover-tags">
                <span class="cover-tag">AI科技</span>
                <span class="cover-tag">医疗健康</span>
                <span class="cover-tag">商业财经</span>
            </div>
        </div>
    </div>

    <div class="headline-section">
        <div class="headline-banner">
            <span>🔥</span>
            <span class="headline-banner-text">今日头条</span>
        </div>
        <div class="headline-body">
            <div class="headline-title">AI的“估值折价时刻”：Anthropic潜在估值从2万亿下修至1.5万亿、Q3环比增速腰斩至45%，CoreWeave信用警报拉响；同日RTX Spark把千亿模型塞进个人电脑，云端焦虑与端侧爆发同框</div>
            <img class="headline-img" src="{HEAD}" alt="AI估值折价与端侧算力爆发">
            <div class="headline-summary">
                路透社10月15日报道，Anthropic投资者日披露最新财务数据后，部分现有及潜在IPO投资者正考虑下调估值，三名知情人士称旧金山会场出现约<strong>1.5万亿美元</strong>讨论价，明显低于此前约2万亿。其Q3营收<strong>168亿美元</strong>、环比增长约<strong>45%</strong>，单季首次实现调整后盈利与正向自由现金流，但增速较Q2超100%大幅回落；招股材料披露未来十年与谷歌、亚马逊、微软、博通等算力及设备承诺至少<strong>5180亿美元</strong>、约八成不可取消。<br><br>
                估值焦虑外溢至AI基建链：英伟达支持的云厂商<strong>CoreWeave五年期CDS利差盘中升至1194.5基点</strong>、部分债券收益率15%-16%，黄仁勋紧急表态“无需为其财务兜底”，美光、SK海力士等硬件股盘前跳水。然而几乎同时，10月16日晚<strong>NVIDIA RTX Spark</strong>个人智能体PC全球开售，最高128GB统一内存、本地跑1250亿参数智能体；微软同日宣告以1/4算力训成2.8万亿参数MAI-Base-2、性能超GPT-5.6 Sol基座。<strong>云端为算力账单焦虑、端侧把算力下放个人桌面，成为AI产业进入“算账阶段”最鲜明的同框对比。</strong>
            </div>
            <div class="headline-source">路透社 · 每经 · 证券时报 · 36氪 · 财联社 · 2026-10-16</div>
        </div>
    </div>

    <div class="section-header">
        <div class="section-icon ai">🚀</div>
        <div class="section-title-group">
            <div class="section-title">AI大模型前沿</div>
            <div class="section-subtitle">AI FRONTIER</div>
        </div>
        <div class="section-line"></div>
    </div>

{chr(10).join(ai_cards)}

    <div class="section-header">
        <div class="section-icon med">💊</div>
        <div class="section-title-group">
            <div class="section-title">医疗健康与政策</div>
            <div class="section-subtitle">HEALTHCARE &amp; POLICY</div>
        </div>
        <div class="section-line"></div>
    </div>

{chr(10).join(med_cards)}

    <div class="insight-section">
        <div class="insight-header">
            <span>🧠</span>
            <span class="insight-header-text">关联洞察</span>
        </div>
        <div class="insight-body">
{insight_html}
        </div>
    </div>

    <div class="news-flash">
        <div class="flash-header">
            <span>⚡</span>
            <span class="flash-title">商业雷达 · 快讯</span>
        </div>
        <div class="flash-list">
{flash_html}        </div>
    </div>

    <div class="footer-card">
        <div class="footer-logo">🍞 吐司日报</div>
        <div class="footer-info">
            第180期 · 2026年10月17日<br>
            DAILY BRIEFING · 每日精选
        </div>
        <div class="footer-divider"></div>
        <div class="footer-info" style="font-size:10px;">
            AI科技 · 医疗健康 · 商业财经
        </div>
        <div class="footer-disclaimer">
            本内容基于公开信息整理，仅供参考，不构成投资建议
        </div>
    </div>

</div>
</body>
</html>
'''

OUT = f"{BASE}/第180期/公众号排版_180期.html"
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print("公众号版生成:", OUT)
print("字节:", len(html.encode("utf-8")), "图片:", html.count("<img"), "快讯:", len(flashes))
