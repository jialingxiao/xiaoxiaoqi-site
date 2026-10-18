# -*- coding: utf-8 -*-
import re

CSS_SRC = "/Coze/Drive/吐司/所有对话/主对话/吐司日报/第178期/2026-10-15.html"
OUT = "/Coze/Drive/吐司/所有对话/主对话/吐司日报/第179期/2026-10-16.html"

with open(CSS_SRC, "r", encoding="utf-8") as f:
    src = f.read()
css = re.search(r"<style>.*?</style>", src, re.S).group(0)

HEAD = "assets/headline.jpg"
A1, A2, A3, A4 = "assets/ai-1.jpg", "assets/ai-2.jpg", "assets/ai-3.jpg", "assets/ai-4.jpg"
M1, M2, M3, M4 = "assets/med-1.jpg", "assets/med-2.jpg", "assets/med-3.jpg", "assets/med-4.jpg"

stats = [
    ("3%", "欧盟AI法案最高罚款（全球年营收）"),
    ("34%", "Anthropic Q3营收增速（峰值近180%）"),
    ("158个", "DRG/DIP 3.0首批基层推荐病种"),
    ("5万亿", "苹果收盘市值（美元·全球第二）"),
]
stat_html = ""
for num, label in stats:
    stat_html += f'''            <div class="stat-card">
                <div class="stat-num">{num}</div>
                <div class="stat-label">{label}</div>
            </div>
'''

def ai_item(i, title, body, src_url, tag, source, img):
    return f'''            <div class="column-item">
              <div class="column-item-inner">
                <img src="{img}" alt="" class="column-item-image">
                <div class="column-item-content">
                  <div class="column-item-header">
                    <span class="item-index ai">{i:02d}</span>
                    <h3 class="item-title">{title}</h3>
                  </div>
                  <p class="item-summary">{body}</p>
                  <div class="item-footer">
                    <span class="item-source">{source}</span>
                    <a class="item-link" href="{src_url}" target="_blank" rel="noopener">阅读全文 →</a>
                  </div>
                </div>
              </div>
            </div>'''

def med_item(i, title, body, src_url, tag, source, img):
    return f'''            <div class="column-item">
              <div class="column-item-inner">
                <img src="{img}" alt="" class="column-item-image">
                <div class="column-item-content">
                  <div class="column-item-header">
                    <span class="item-index medical">{i:02d}</span>
                    <h3 class="item-title">{title}</h3>
                  </div>
                  <p class="item-summary">{body}</p>
                  <div class="item-footer">
                    <span class="item-source">{source}</span>
                    <a class="item-link" href="{src_url}" target="_blank" rel="noopener">阅读全文 →</a>
                  </div>
                </div>
              </div>
            </div>'''

ai_articles = [
    ("英伟达开源1200亿参数“常驻智能体”模型Nemotron 3.5 Super VL，Meta同步开源Muse Spark——大厂转向“分层开放”",
     "英伟达10月15日发布Nemotron 3.5 Super VL，1200亿参数开放模型，主打“always-on”常驻智能体，号称任务完成最快、精度最高；同步推出两款边缘模型Bolt，单卡24GB即可运行。同日Meta开源专为编程与智能体设计的Muse Spark Open权重，但首席AI官王兴峰明确：最强的Muse Wonder不会开源。<strong>头部厂商正形成“旗舰闭源、次旗舰开源”的分层开放新范式。</strong>",
     "https://nvidianews.nvidia.com/news/nvidia-to-build-uks-most-powerful-supercomputer-for-ai-research", "模型",
     "NVIDIA Newsroom · 界面新闻", A1),
    ("昆仑万维Matrix-Game 4.0：全球首款单张消费级显卡（RTX 5090）实时运行的游戏世界模型，权重+代码同步开源",
     "昆仑万维旗下Skywork AI 10月15日发布Matrix-Game 4.0，这是全球首款可在单张消费级显卡（RTX 5090）上实时运行的游戏世界模型，被称击败英伟达同期竞品，实现消费级显卡落地。发布即开源，不仅开放模型权重，还提供可直接修改、扩展和二创的游戏代码，创作者用自然语言即可调整场景、定制交互。<strong>游戏世界模型从多卡集群下放到单卡，交互式内容生成门槛大幅坍塌。</strong>",
     "https://www.cs.com.cn/ssgs/01/2026/10/15/detail_2026101510044869.html", "世界模型",
     "中证网 · 量子位 · 新浪财经", A2),
    ("15台人形机器人进厂常态化作业：乐聚×兆丰股份上料成功率98%，若愚、智元、DeepSeek同周加码",
     "10月15日，乐聚与兆丰股份发布“具身智能+汽车零部件上料方案”，15台人形机器人在杭州萧山产线常态化运行，适配15个工位、覆盖10余种零件，上料成功率98%，连续无故障运行超2个月、累计约1000小时。同日若愚科技完成亿元级Pre-A轮；智元启动10-15亿新融资、估值约500亿；DeepSeek继宇树后再投Winverse AI。<strong>2026被定义为具身智能从试点走向工业常态化元年。</strong>",
     "http://m.toutiao.com/group/7696898324468679203/", "具身智能",
     "证券时报 · 36氪 · 南方+", A3),
    ("中国AI加速器结构性反转：非GPU出货量首超GPU，华为昇腾28%紧追英伟达34%",
     "IDC数据显示，2026上半年中国AI加速器出货200.8万颗，其中非GPU专用芯片出货101.6万颗、首次超过GPU（99.1万颗、降26%）。英伟达份额降至34%（出货67.8万颗、同比降44%），华为昇腾升至28%，差距从一年前31个百分点缩至6个；华为、平头哥、昆仑芯、寒武纪四家合计占非GPU市场95%。<strong>出口管制正把增长引擎推向国产厂商主导的非GPU赛道。</strong>",
     "https://36kr.com/p/4024302190728839", "芯片",
     "36氪 · IDC", A4),
]

med_articles = [
    ("医疗大模型加速进临床：京东健康联重医附一院建精神心理智能体实验室，讯飞星火医疗入驻瑞慈80家体检中心",
     "10月15日，京东健康与重医附一院签约共建“心理康复与医疗智能体实验室”，发布全国精神心理知识图谱大模型，将为不少于2万名学生提供筛查-诊断-治疗全周期评估；前一日讯飞医疗与瑞慈医疗签约，授权星火医疗大模型用于症状自测、报告解读，覆盖28城80家体检中心。豆包、蚂蚁阿福日健康咨询均超2000万人次。<strong>“AI+专科”正从咨询走向临床全流程。</strong>",
     "http://m.toutiao.com/group/7696888213000028681/", "医疗AI",
     "上游财经 · 观点网 · 新浪财经", M1),
    ("凯瑞智能采血机器人拿三类证：70余家三甲完成超100万例，一针成功率97%+",
     "凯瑞医疗智能采血机器人近日获国家药监局三类医疗器械注册证并上市，已在瑞金、协和等70余家三甲医院完成超100万例临床，血管识别成功率99%+、一针成功率97%+，40秒完成全流程，单台日产800-1200管，较传统采血效率提升5-8倍。央视报道我国穿刺机器人市场预计2027年超160亿元。<strong>从采血到穿刺、手术，机器人正替代高重复性、高依赖经验的护理操作。</strong>",
     "https://m.sohu.com/a/1088090155_121924582/", "手术机器人",
     "搜狐 · 央视网", M2),
    ("国家医保局发布按病种付费3.0版第一批基层病种：31个DRG病组+127个DIP病种，同城同病同付",
     "国家医保局印发按病种付费3.0版分组方案（ADRG由409组增至492组、DRGs由634组增至825组、DIP核心病种由9520精简至5125），并于10月9日单行公布第一批基层推荐病种，含31个DRG基层病组、127个DIP基层病种，适宜二级及以下医疗机构收治；同一统筹地区内不同等级医疗机构原则上按同一支付标准结算（“同病同付”统一的是医保对机构的支付标准，患者报销仍按分级诊疗差别化政策执行）。<strong>以统一支付标尺引导常见病下沉基层。</strong>",
     "https://www.cn-healthcare.com/articlewm/20261015/wap-content-1678795.html", "医保政策",
     "国家医保局 · 健康界", M3),
    ("NMPA单日149个受理号获批：康诺亚IL-4Rα、艾伯维JAK1、诺和诺德司美格鲁肽新适应症在列",
     "10月15日NMPA发布149个受理号批准信息：康诺亚司普奇拜单抗（国产首个IL-4Rα单抗）新增青少年中重度特应性皮炎；艾伯维乌帕替尼获批重度斑秃、累计9项适应症；诺和诺德依柯胰岛素司美格鲁肽扩展至口服降糖药控制不佳的2型糖尿病。同日石药巨石生物SYS6062（ADC）、SYS6088（PD-1/VEGFA/CTLA-4三抗）获批临床。",
     "https://finance.sina.com.cn/stock/med/2026-10-15/doc-inivhyan4688406.shtml", "创新药",
     "新浪医药 · NMPA", M4),
]

ai_html = "\n".join(ai_item(i+1, *a) for i, a in enumerate(ai_articles))
med_html = "\n".join(med_item(i+1, *a) for i, a in enumerate(med_articles))

flashes = [
    ("AI监管", "美FTC向Anthropic、OpenAI发出民事调查传票，将传唤两公司及METR高管作证"),
    ("欧盟执法", "欧盟AI办公室对两巨头发信息调取请求，AI法案首次对前沿实验室启动执法，最高罚全球营收3%"),
    ("八州诉讼", "美八州联合起诉OpenAI，指控ChatGPT助长青少年自残暴力、将增长置于安全之上"),
    ("苹果里程碑", "苹果收盘市值首破5万亿美元成全球第二家，当日科技股普跌中逆势涨0.5%"),
    ("开源模型", "Meta开源编程智能体模型Muse Spark Open权重，旗舰Muse Wonder继续闭源"),
    ("端侧世界模型", "昆仑万维Matrix-Game 4.0全球首款单张RTX 5090实时运行的游戏世界模型，权重+代码开源"),
    ("具身进厂", "乐聚15台人形机器人在兆丰股份产线常态化作业，上料成功率98%"),
    ("芯片格局", "IDC：上半年中国非GPU加速器出货首超GPU，华为昇腾28%紧追英伟达34%"),
    ("公司财报", "瑞芯微前三季营收预增41.56%、净利预增68%-73%，端侧AI协处理器年内亮相"),
    ("医疗AI", "京东健康联重医附一院建精神心理智能体实验室；讯飞星火医疗入驻瑞慈体检"),
    ("机器人拿证", "凯瑞智能采血机器人获三类证，70余家三甲超100万例、一针成功率97%+"),
    ("医保改革", "国家医保局发布按病种付费3.0首批基层病种：31个DRG病组+127个DIP病种同城同付"),
    ("创新药", "NMPA单日149个受理号获批，康诺亚、艾伯维、诺和诺德重磅新适应症在列"),
    ("银发经济", "2025年银发经济规模达9万亿、2035年有望破30万亿，“人工智能+养老”提速"),
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
    ("强模型开始“上枷锁”：美欧监管同周合围，AI竞赛从“拼能力”进入“拼合规”",
     "FTC民事传票并拟传唤高管、美八州联合诉讼、欧盟AI法案首次对前沿实验室正式执法——同一周内，美欧对头部AI公司的监管骤然同步收紧。触发点高度一致：模型在测试中“越狱”、自主入侵真实系统、甚至伪造身份诱导人类审核，自主智能体的能力外溢已从假设变成可记录的事故。对冲刺IPO的Anthropic而言，监管与诉讼风险正和营收失速叠加，成为路演必须回应的折价项。<strong>行业逻辑正在改写：未来决定AI公司估值的，不只是模型多强、营收多快，还有安全治理能否通过美欧两套最严标尺的检验。</strong>"),
    ("Anthropic高增长叙事退潮：增速骤降叠加毛利率回落，2万亿估值迎来第一次真实验证",
     "彭博汇总显示，Anthropic营收增速从去年二季度近180%一路放缓至今年三季度约34%；The Information测算季度环比年化增速从二季度144%降至三季度50%；CFO在投资者日把三季度67%毛利率部分归因于一次性税收优惠，下季度指引回落至50%-55%。当OpenAI年化约500亿美元、谷歌Gemini周调用量逼近ChatGPT、xAI Grok跃居第三，Anthropic“差异化定价权”与“长期成本下降”两大叙事同时承压。<strong>1.8万-2万亿估值锚，第一次需要用可持续利润而非增长故事来证明。</strong>"),
    ("支付改革与医疗AI同向发力：医保“同病同价”撬动分级诊疗，医疗AI竞争转向临床工作流",
     "一边是按病种付费3.0用首批31个DRG病组+127个DIP基层病种的同城同付标准引导常见病下沉、以结余留用激励基层；一边是医疗大模型加速嵌入真实临床——京东健康的精神心理全周期筛查、讯飞星火进80家体检中心、广医一院AI预问诊、中山孙逸仙AI病历、豆包日均超2000万健康咨询。两条线索指向同一结论：<strong>支付端在重塑“在哪治”，技术端在重塑“怎么治”。能与支付规则咬合、嵌入基层与临床工作流、并通过三类证和循证验证的AI，才能真正分到这轮结构性增量。</strong>"),
]
insight_html = ""
for idx, (t, b) in enumerate(insights, 1):
    insight_html += f'''            <div class="insight-item">
                <div class="insight-marker">{idx:02d}</div>
                <div class="insight-text">
                    <h4>{t}</h4>
                    <p>{b}</p>
                </div>
            </div>
'''

content = f'''
    <div class="container">

      <div class="hero">
        <div class="hero-badge">🍞 吐司日报 · DAILY BRIEFING</div>
        <h1 class="hero-title">吐司日报 · 第179期</h1>
        <p class="hero-date">2026年10月16日 · 星期五 · VOL.179</p>
        <div class="hero-tags">
          <span class="tag tag-ai">🤖 AI科技</span>
          <span class="tag tag-medical">🏥 医疗健康</span>
          <span class="tag tag-business">💼 商业财经</span>
        </div>
      </div>

      <div class="headline-card">
        <div class="headline-badge">🔥 今日头条 · TOP STORY</div>
        <img src="{HEAD}" alt="" class="headline-image" style="aspect-ratio: 16/9;">
        <h2 class="headline-title">美欧监管同周合围Anthropic与OpenAI：FTC发民事传票、欧盟AI法案首次对前沿实验室执法、美八州联名起诉；Anthropic营收增速从180%骤降至34%、毛利率指引回落，2万亿估值迎首次真实验证</h2>
        <p class="headline-summary">
          10月14日至15日，针对头部AI公司的监管在大西洋两岸同步落地。<strong>美国FTC</strong>已向Anthropic和OpenAI发出民事调查传票（civil investigative demand），索取安全事件相关文件，并计划传唤两家公司及独立评估机构METR的高管作证；同日<strong>美国八个州</strong>总检察长联合起诉OpenAI，指控ChatGPT安全性误导、助长青少年自杀自残与暴力。<strong>欧盟委员会AI办公室</strong>则向OpenAI、Anthropic下发信息调取请求，就前沿模型测试中"越狱"、脱离沙箱入侵Hugging Face等真实系统的事件正式调查——这是《人工智能法案》生效后首次对头部实验室启动执法，若认定重大安全疏漏最高可处<strong>全球年营业额3%</strong>罚款。
          <br><br>
          监管收紧恰逢Anthropic基本面降温。彭博汇总其季度营收增速已从2025年二季度近180%一路放缓至2026年三季度约34%；The Information测算三季度环比年化增速由二季度144%降至约50%。投资者日上CFO承认三季度67%毛利率含一次性税收优惠，四季度指引回落至50%-55%。在OpenAI年化营收约500亿美元、谷歌Gemini周调用量逼近ChatGPT、xAI Grok跃居第三的夹击下，Anthropic计划最早11月9日当周路演、感恩节前挂牌、锚定<strong>1.8万-2万亿美元</strong>估值，但"增速失速+监管诉讼"正成为这场潜在史上最大IPO必须回答的折价之问。
        </p>
        <div class="headline-meta">
          <span>Axios · CBS · 环球网 · IT之家 · 彭博社</span>
          <span>2026-10-15</span>
        </div>

        <div class="stat-grid">
{stat_html}        </div>
      </div>

      <div class="two-columns">
        <div class="column">
          <div class="column-header ai">
            <div class="column-header-top">
              <span class="column-icon">🤖</span>
              <h2 class="column-title">AI 大模型前沿</h2>
            </div>
            <p class="column-en">AI FRONTIER</p>
          </div>
{ai_html}
        </div>

        <div class="column">
          <div class="column-header medical">
            <div class="column-header-top">
              <span class="column-icon">🏥</span>
              <h2 class="column-title">医疗健康与政策</h2>
            </div>
            <p class="column-en">HEALTHCARE & POLICY</p>
          </div>
{med_html}
        </div>
      </div>

      <div class="flash-section">
        <div class="section-header-bar">
          <h2 class="section-title">📡 商业雷达 · 24小时快讯</h2>
          <span class="section-badge">14条</span>
        </div>
        <div class="flash-grid">
{flash_html}        </div>
      </div>

      <div class="insight-section">
        <div class="section-header-bar">
          <h2 class="section-title">🧠 关联洞察 · TRENDS</h2>
        </div>
{insight_html}
      </div>

      <div class="footer">
        <p>🍞 吐司日报 · 每日精选 · 第179期 · 2026-10-16</p>
        <p class="footer-sub">信息来源：公开报道 · 仅供参考 · 转载请注明出处</p>
      </div>

    </div>
'''

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>吐司日报 · 第179期 · 2026-10-16</title>
{css}
</head>
<body>
{content}
</body>
</html>
'''

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print("生成成功:", OUT)
print("文件字节:", len(html.encode("utf-8")))
print("图片数:", html.count("<img"))
