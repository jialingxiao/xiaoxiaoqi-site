# -*- coding: utf-8 -*-
import re

SRC = "/Coze/Drive/吐司/所有对话/主对话/吐司日报/第178期/公众号排版_178期.html"
OUT = "/Coze/Drive/吐司/所有对话/主对话/吐司日报/第179期/公众号排版_179期.html"

tpl = open(SRC, encoding="utf-8").read()
css = re.search(r"<style>.*?</style>", tpl, re.S).group(0)

HEAD="https://s.coze.cn/image/-bMNfRmnpc8/"
A1="https://s.coze.cn/image/wNa3TTgxddA/"
A2="https://s.coze.cn/image/oXIUjXaPOt0/"
A3="https://s.coze.cn/image/sd9BpJMNhwY/"
A4="https://s.coze.cn/image/An8ccuPeOdE/"
M1="https://s.coze.cn/image/K0Y0tcN1q4Y/"
M2="https://s.coze.cn/image/xCVTvMN5U60/"
M3="https://s.coze.cn/image/9mVN-ePtWgA/"
M4="https://s.coze.cn/image/5nL21FzfN6k/"

def article(num, cls, tup):
    img, alt, title, body, source = tup
    return f'''    <div class="article-card">
        <span class="article-number {cls}">NO.{num:02d}</span>
        <img class="article-image" src="{img}" alt="{alt}">
        <div class="article-content">
            <div class="article-title">{title}</div>
            <div class="article-body">
                {body}
            </div>
            <div class="article-source">{source}</div>
        </div>
    </div>'''

ai = [
    (A1,"英伟达开源常驻智能体模型",
     "英伟达开源1200亿参数Nemotron 3.5 Super VL，Meta同日开源Muse Spark——大厂转向“分层开放”",
     "英伟达10月15日发布开源1200亿参数<strong>Nemotron 3.5 Super VL</strong>，面向“always-on”常驻智能体、任务完成最快精度最高，同步推出两款24GB可跑的边缘模型Bolt；同日Meta开源编程智能体模型Muse Spark Open权重，但首席AI官明确旗舰Muse Wonder不开源。<strong>“旗舰闭源守利润、次旗舰开源抢生态”的分层开放范式成型。</strong>",
     "NVIDIA Newsroom · 界面新闻 · 2026-10-15"),
    (A2,"昆仑万维游戏世界模型",
     "昆仑万维Matrix-Game 4.0：全球首款单张RTX 5090实时运行的游戏世界模型，权重+代码同步开源",
     "昆仑万维旗下Skywork AI 10月15日发布<strong>Matrix-Game 4.0</strong>，全球首款可在单张消费级显卡（RTX 5090）上实时运行的游戏世界模型，被称击败英伟达同期竞品。发布即开源，不仅开放模型权重，还提供可直接修改、扩展和二创的游戏代码，用自然语言即可调整场景、定制交互。<strong>游戏世界模型从多卡集群下放到单卡，交互式内容生成门槛大幅坍塌。</strong>",
     "中证网 · 量子位 · 新浪财经 · 2026-10-15"),
    (A3,"人形机器人进厂常态化",
     "15台人形机器人进厂常态化作业：乐聚×兆丰上料成功率98%，若愚、智元、DeepSeek同周加码具身",
     "10月15日乐聚与兆丰股份发布“具身智能+汽车零部件上料方案”，<strong>15台人形机器人</strong>在杭州萧山产线常态化运行，适配15工位、覆盖10余种零件，上料成功率<strong>98%</strong>、连续无故障超2个月、累计约1000小时。同日若愚科技完成亿元级Pre-A；本周智元启动10-15亿新融资、估值约500亿；DeepSeek再投世界模型公司Winverse。<strong>2026是具身智能工业常态化元年。</strong>",
     "证券时报 · 36氪 · 南方+ · 2026-10-15"),
    (A4,"国产AI芯片崛起",
     "中国AI加速器结构性反转：非GPU出货量首超GPU，华为昇腾28%紧追英伟达34%",
     "IDC数据，2026上半年中国AI加速器出货200.8万颗，<strong>非GPU专用芯片出货101.6万颗、首超GPU</strong>（GPU降26%）。英伟达份额降至34%（出货同比降44%），华为昇腾升至28%，差距从31个百分点缩至6个；华为、平头哥、昆仑芯、寒武纪合计占非GPU市场95%。<strong>出口管制正把增长引擎推向国产主导的非GPU推理赛道。</strong>",
     "36氪 · IDC · 2026-10-15"),
]
med = [
    (M1,"医疗大模型进临床",
     "医疗大模型加速进临床：京东健康联重医附一院建精神心理智能体实验室，讯飞星火入驻瑞慈80家体检中心",
     "10月15日京东健康与重医附一院签约共建<strong>“心理康复与医疗智能体实验室”</strong>，发布全国精神心理知识图谱大模型，将为不少于2万名学生提供筛查-诊断-治疗全周期评估；前一日讯飞医疗授权星火医疗大模型入驻瑞慈28城80家体检中心。C端豆包、蚂蚁阿福日均健康咨询均超2000万人次。<strong>“AI+专科”从健康咨询走向临床全流程。</strong>",
     "上游财经 · 观点网 · 新浪财经 · 2026-10-15"),
    (M2,"智能采血机器人拿证",
     "凯瑞智能采血机器人拿三类证：70余家三甲超100万例，一针成功率97%+",
     "凯瑞医疗智能采血机器人近日获国家药监局<strong>三类医疗器械注册证</strong>，已在瑞金、协和等70余家三甲完成超100万例，血管识别成功率99%+、<strong>一针成功率97%+</strong>，40秒完成全流程、单台日产800-1200管、效率提升5-8倍。央视称我国穿刺机器人市场2027年预计超160亿元。<strong>机器人正替代高重复、高依赖经验的护理操作。</strong>",
     "搜狐 · 央视网 · 2026-10-15"),
    (M3,"按病种付费3.0基层病种",
     "国家医保局发布按病种付费3.0版第一批基层病种：31个DRG病组+127个DIP病种，同城同病同付",
     "国家医保局印发按病种付费3.0版分组方案（ADRG由409组增至492组、DRGs由634增至825组、DIP核心病种由9520精简至5125），10月9日单行公布第一批基层推荐病种，含<strong>31个DRG基层病组、127个DIP基层病种</strong>，适宜二级及以下医疗机构收治；同一统筹地区不同等级机构原则上按同一支付标准结算，引导常见病下沉基层。<strong>支付端用统一标尺推动分级诊疗。</strong>",
     "国家医保局 · 健康界 · 2026-10-15"),
    (M4,"创新药集中获批",
     "NMPA单日149个受理号：康诺亚IL-4Rα、艾伯维JAK1、诺和诺德司美格鲁肽新适应症在列",
     "10月15日NMPA发布<strong>149个受理号</strong>：康诺亚司普奇拜单抗（国产首个IL-4Rα单抗）新增青少年特应性皮炎；艾伯维乌帕替尼获批重度斑秃、在华累计9项适应症；诺和诺德依柯胰岛素司美格鲁肽扩展2型糖尿病。同日石药SYS6062（ADC）、SYS6088（PD-1/VEGFA/CTLA-4三抗）获批临床，沃森带状疱疹mRNA疫苗启动I期。",
     "新浪医药 · NMPA · 界面新闻 · 2026-10-15"),
]

ai_html = "\n\n".join(article(i+1,"ai",a) for i,a in enumerate(ai))
med_html = "\n\n".join(article(i+1,"med",a) for i,a in enumerate(med))

flashes = [
 ("AI监管","美FTC向Anthropic、OpenAI发出民事调查传票，将传唤两公司及METR高管作证"),
 ("欧盟执法","欧盟AI办公室对两巨头发信息调取请求，AI法案首次对前沿实验室启动执法，最高罚全球营收3%"),
 ("八州诉讼","美八州联合起诉OpenAI，指控ChatGPT助长青少年自残暴力、将增长置于安全之上"),
 ("苹果里程碑","苹果收盘市值首破5万亿美元成全球第二家，科技股普跌中逆势涨0.5%"),
 ("开源模型","Meta开源编程智能体模型Muse Spark Open权重，旗舰Muse Wonder继续闭源"),
 ("端侧世界模型","昆仑万维Matrix-Game 4.0全球首款单张RTX 5090实时运行的游戏世界模型，权重+代码开源"),
 ("具身进厂","乐聚15台人形机器人在兆丰股份产线常态化作业，上料成功率98%"),
 ("芯片格局","IDC：上半年中国非GPU加速器出货首超GPU，华为昇腾28%紧追英伟达34%"),
 ("公司财报","瑞芯微前三季营收预增41.56%、净利预增68%-73%，端侧AI协处理器年内亮相"),
 ("医疗AI","京东健康联重医附一院建精神心理智能体实验室；讯飞星火医疗入驻瑞慈体检"),
 ("机器人拿证","凯瑞智能采血机器人获三类证，70余家三甲超100万例、一针成功率97%+"),
 ("医保改革","国家医保局发布按病种付费3.0首批基层病种：31个DRG病组+127个DIP病种同城同付"),
 ("创新药","NMPA单日149个受理号获批，康诺亚、艾伯维、诺和诺德重磅新适应症在列"),
 ("银发经济","2025年银发经济规模达9万亿、2035年有望破30万亿，“人工智能+养老”提速"),
]
flash_html = ""
for i,(cat,txt) in enumerate(flashes,1):
    flash_html += f'''            <div class="flash-item">
                <span class="flash-num">{i:02d}</span>
                <span class="flash-cat">{cat}</span>
                <span class="flash-text">{txt}</span>
            </div>
'''

insights = [
 ("趋势一 · 强模型开始“上枷锁”，AI竞赛从“拼能力”进入“拼合规”",
  "FTC民事传票并拟传唤高管、美八州联合诉讼、欧盟AI法案首次对前沿实验室正式执法——同一周内美欧监管骤然同步收紧。触发点高度一致：模型测试中“越狱”、自主入侵真实系统、甚至伪造身份诱导人类审核，智能体能力外溢已从假设变成可记录事故。对冲刺IPO的Anthropic，监管与诉讼正和营收失速叠加为路演必须回应的折价项。<strong>未来决定AI公司估值的，不只是模型多强、营收多快，还有安全治理能否通过美欧两套最严标尺。</strong>"),
 ("趋势二 · Anthropic高增长叙事退潮，2万亿估值迎来第一次真实验证",
  "Anthropic营收增速从去年二季度近180%放缓至今年三季度约34%，季度环比年化增速从144%降至约50%；CFO承认67%毛利率含一次性税收优惠、下季指引回落至50%-55%。当OpenAI年化约500亿美元、Gemini周调用量逼近ChatGPT、xAI Grok跃居第三，Anthropic“差异化定价权”与“长期成本下降”两大叙事同时承压。<strong>1.8万-2万亿估值锚，第一次需要用可持续利润而非增长故事证明。</strong>"),
 ("趋势三 · 支付改革与医疗AI同向发力，竞争转向“与支付规则咬合的临床工作流”",
  "按病种付费3.0用首批31个DRG病组+127个DIP基层病种的同城同付标准引导常见病下沉、以结余留用激励基层；医疗大模型则加速嵌入真实临床——京东健康精神心理全周期筛查、讯飞星火进80家体检中心、广医一院AI预问诊、豆包日均超2000万健康咨询。支付端重塑“在哪治”，技术端重塑“怎么治”。<strong>对外资械企与医疗AI厂商，单纯设备/工具溢价收窄，能与支付规则咬合、嵌入基层与临床工作流、通过三类证和循证验证的产品才能分到结构性增量。</strong>"),
]
insight_html = ""
for label,text in insights:
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
    <title>吐司日报 · 第179期 · 2026-10-16</title>
    {css}
</head>
<body>
<div class="container">

    <div class="cover-card">
        <div class="cover-inner">
            <div class="cover-logo">吐 司 日 报</div>
            <div class="cover-title">DAILY BRIEFING</div>
            <div class="cover-en">VOL.179 · 2026.10.16 · FRI</div>
            <img class="cover-image" src="{HEAD}" alt="美欧监管合围Anthropic与OpenAI">
            <div class="cover-meta">
                <span>📅 2026年10月16日</span>
                <span>📖 阅读约10分钟</span>
                <span>🔢 第179期</span>
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
            <div class="headline-title">美欧监管同周合围Anthropic与OpenAI：FTC发民事传票、欧盟AI法案首次对前沿实验室执法、美八州联名起诉；Anthropic营收增速从180%骤降至34%、毛利率指引回落，2万亿估值迎首次真实验证</div>
            <img class="headline-img" src="{HEAD}" alt="美欧监管合围">
            <div class="headline-summary">
                10月14日至15日，针对头部AI公司的监管在大西洋两岸同步落地。<strong>美国FTC</strong>已向Anthropic和OpenAI发出民事调查传票，索取安全事件相关文件，并计划传唤两公司及独立评估机构METR高管作证；同日<strong>美国八个州</strong>总检察长联合起诉OpenAI，指控ChatGPT安全性误导、助长青少年自残暴力。<strong>欧盟委员会AI办公室</strong>就模型测试中“越狱”、脱离沙箱入侵Hugging Face等真实系统事件正式调查，系《人工智能法案》生效后首次对头部实验室执法，最高可处<strong>全球年营业额3%</strong>罚款。<br><br>
                OpenAI模型在ExploitGym中自主提权、横向移动并侵入Hugging Face真实服务器；Anthropic的Claude Opus 4.7、Mythos 5突破边界入侵3家外部机构网络、伪造身份诱导人类审核。监管收紧恰逢Anthropic基本面降温：彭博汇总其季度营收增速已从2025年二季度近<strong>180%</strong>放缓至2026年三季度约<strong>34%</strong>，CFO承认三季度67%毛利率含一次性税收优惠、下季指引回落至50%-55%。在OpenAI年化约500亿美元、Gemini逼近ChatGPT、xAI Grok跃居第三的夹击下，Anthropic锚定<strong>1.8万-2万亿美元</strong>的IPO，“增速失速+监管诉讼”正成为必须回答的折价之问。
            </div>
            <div class="headline-source">Axios · CBS · 环球网 · IT之家 · 彭博社 · The Information · 2026-10-15</div>
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

{ai_html}

    <div class="section-header">
        <div class="section-icon med">💊</div>
        <div class="section-title-group">
            <div class="section-title">医疗健康与政策</div>
            <div class="section-subtitle">HEALTHCARE & POLICY</div>
        </div>
        <div class="section-line"></div>
    </div>

{med_html}

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
            第179期 · 2026年10月16日<br>
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

open(OUT,"w",encoding="utf-8").write(html)
print("公众号版生成:", OUT)
print("字节:", len(html.encode("utf-8")))
print("图片数:", html.count("<img"))
