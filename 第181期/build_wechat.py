# -*- coding: utf-8 -*-
"""吐司日报 第181期 公众号排版版（复用179/180期深色主题CSS）"""
import re

BASE = "/Coze/Drive/吐司/所有对话/主对话/吐司日报"
with open(f"{BASE}/第179期/公众号排版_179期.html", encoding="utf-8") as f:
    old = f.read()

css = re.search(r"<style>(.*?)</style>", old, re.S).group(1).strip()

HEAD = "https://s.coze.cn/image/lptY1m9VA8c/"
A = ["https://s.coze.cn/image/QqmPgAzvI3c/", "https://s.coze.cn/image/LhNKVWXOHow/",
     "https://s.coze.cn/image/tvih5FJ2Hi4/", "https://s.coze.cn/image/G7WIjRIdJHo/"]
M = ["https://s.coze.cn/image/n5BXIXwlG_I/", "https://s.coze.cn/image/TnEzQ2LVvVA/",
     "https://s.coze.cn/image/SUlyU8ci288/", "https://s.coze.cn/image/KbOzVo8uaYw/"]

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
    article("ai", "NO.01", A[0], "DeepSeek V4.1-Flash-1017",
      "DeepSeek V4.1-Flash-1017发布：7630亿参数、主打“许愿式编程”，跑分超Claude Opus 5与GPT-5.6 Sol、费用反降61%",
      "10月17日16时，DeepSeek宣布V4.1 Flash升级至<strong>V4.1-Flash-1017</strong>，网页端、App与API同步切换，距9月10日首发仅一个多月。新模型参数<strong>763B</strong>（上版552B），通过自反馈强化学习显著增强从零构建完整项目能力——Terminal-Bench 4.0由31.2升至42.3、DeepSWE v1.1通过率达77.0%，可完成故宫3D建模、网页赛车游戏等“许愿式编程”任务。推理约250 tok/s，max档<strong>每任务平均费用由约3.3元降至约1.3元</strong>；权重MIT许可开放下载。<strong>参数更大、跑分更高，调用成本反而继续下探。</strong>",
      "机器之心 · 第一财经 · 智东西 · 2026-10-17"),
    article("ai", "NO.02", A[1], "Anthropic北极星项目",
      "Anthropic“北极星项目”曝光：600亿美元芯片债创纪录，黑石认购90亿次级债、票息10%，比公开市场高逾300基点",
      "据FT 10月17日报道，Anthropic正推进约<strong>600亿美元</strong>债务融资“北极星项目”，采购约1.5吉瓦谷歌TPU，将成史上最大芯片融资。结构为约420亿美元优先级债（博通担保残值）+180亿次级债；<strong>黑石承诺认购90亿次级债、票息10%</strong>，以未来五年芯片租赁付款支持。信用相近者公开市场仅约7%，6月“Big Sky”次级债利率约8.5%。高盛数据显示AI相关高收益债利差已扩至350基点以上；今年美国AI项目公司债发行1060亿美元，接近2025全年370亿的3倍。<strong>头部AI实验室正以前所未有的高杠杆为算力军备竞赛筹资。</strong>",
      "金融时报 · 财联社 · 新浪财经 · 2026-10-17"),
    article("ai", "NO.03", A[2], "禾赛Kosmo数据引擎",
      "禾赛发布三维世界数据引擎Kosmo：8K空间相机+AI云平台，从激光雷达厂商迈向物理AI核心基础设施",
      "禾赛科技近日发布三维世界数据引擎<strong>Kosmo</strong>，由全球首款8K超高清AI空间相机Kosmo One与AI驱动云平台Kosmo World组成。Kosmo One集成高空间分辨率激光雷达、8K影像、一英寸大底CMOS与高精度IMU，100平方米室内扫描约15分钟；底层自研Kosmo Spatial Core可从同一采集数据同步生成<strong>3DGS、mesh、depth</strong>三种sim-ready三维数据供机器人训练仿真。发布会上禾赛与银河通用、原力灵机签约，并展示与皮克斯、高德合作。李一帆称这是禾赛从零部件商走向物理AI基础设施提供商的第一步。<strong>物理世界数据的采集与重建，正成为具身智能的新入口。</strong>",
      "36氪 · 2026-10-17"),
    article("ai", "NO.04", A[3], "风清AI气象预报",
      "我国首个全自主可控气象AI“风清”投入业务运行：11天有效预报超欧洲中期天气预报中心，十万卡AI4S集群训练",
      "10月17日CCF HPC China 2026上，国家超算互联网宣布由国家气象中心牵头等研制的<strong>“风清”人工智能全球短中期集合天气预报系统V1.0</strong>通过业务化评审并投运。系统融合Swin Transformer与大气物理守恒约束，“数据+物理”双驱动，依托国家超算（天津）核心节点<strong>十万卡AI4S集群</strong>训练，数据、模型、算力全国产自主可控。其全球500hPa位势高度ACC大于0.6的<strong>有效预报时效达11天</strong>，综合效果及部分指标优于欧洲中期天气预报中心AIFS-CRPS，数分钟即可完成全球气象要素推演。<strong>中国AI气象预报达到世界先进水平。</strong>",
      "科创板日报 · IT之家 · 腾讯新闻 · 2026-10-17"),
]

med_cards = [
    article("med", "NO.01", M[0], "丁汉院士谈AI医疗",
      "丁汉院士同济呼吸年会开讲：AI判百层CT仅3-5秒、敏感度超95%，“会用AI与不会用AI的医生差距会越来越大”",
      "10月17日湖北省呼吸内科专科联盟中期汇报暨同济呼吸学术年会上，中科院院士<strong>丁汉</strong>作《人工智能在医疗健康领域的应用现状及展望》报告。他以DeepMind 3秒完成乳腺癌筛查、误诊率低5.7%切入，指出AI对指定大小实性肺结节判读百层CT仅<strong>3-5秒、敏感度超95%</strong>，骨折识别准确率超90%，眼底图数秒完成糖网分级。但丁汉强调<strong>“医生永远是做决策的那个人”</strong>，AI不会让医生失业，如何用AI正拉开医生差距；并点出数据标准不统一、标注稀缺、跨院“水土不服”等瓶颈。<strong>医疗AI的价值在增强而非替代医生，落地应“先点、再线、后面”。</strong>",
      "健康日报 · 湖北大健康融媒 · 2026-10-17"),
    article("med", "NO.02", M[1], "京东健康精神心理大模型",
      "京东健康×重医附一院共建“心理康复与医疗智能体实验室”：发布全国精神心理知识图谱大模型，拟为2万学生提供AI筛查",
      "10月15日第三届精神领域学科融合与创新大会在重庆举行，京东健康与重医附一院签署AI医疗战略合作、共建<strong>“心理康复与医疗智能体实验室”</strong>，并发布全国精神心理知识图谱大模型。双方将在重庆及联盟中小学为<strong>不少于2万名学生</strong>免费提供“筛查—诊断—治疗”全周期评估的专病大模型心理筛查服务，并开展青少年心理健康筛查多中心研究。京东健康同步发布《AI时代中国医生执业与学习行为变迁（2026）》白皮书；平台已汇聚6000余名精神科医生、2000余名心理咨询师。<strong>AI心理服务从单点问答走向校院协同全周期闭环。</strong>",
      "上游新闻 · 2026-10-16"),
    article("med", "NO.03", M[2], "国产ANGPTL3单抗获批",
      "我国首款自研全人源ANGPTL3单抗“芮弗西拜单抗”获批：填补HoFH罕见病治疗空白；武田NT1对因新药开出中国首日处方",
      "据光明网10月16日报道，我国自主研发的<strong>芮弗西拜单抗</strong>正式获批，成为首款国产全人源ANGPTL3单克隆抗体，填补纯合子家族性高胆固醇血症（HoFH）长期缺乏有效治疗手段的空白。HoFH因先天LDL受体功能障碍致LDL-C显著升高，<strong>患者平均寿命不超过30岁</strong>，既往用药长期依赖进口。此外10月15日，武田全球首个1型发作性睡病（NT1）对因治疗药奥泽悦®（奥普雷顿片，口服高选择性OX2R激动剂）在国内多地开出首日处方，我国NT1患者约52万-56万人。<strong>罕见病药物自主研发与全球首发对因治疗同步突破。</strong>",
      "光明网 · 新民晚报 · 2026-10-16"),
    article("med", "NO.04", M[3], "第四批中成药集采",
      "第四批全国中成药集采落地：89种药品平均降幅超50%、OTC与独家品种首次全面纳入，院内院外价格加速并轨",
      "第四批全国中成药联盟集采（湖北省医保局组织）完整中选结果近日公布并加速落地。本轮设28个采购组、纳入<strong>89种</strong>临床常用中成药，覆盖市场规模超450亿元，全国超4万家公立医疗机构参与；344家企业就468个产品投标，243家企业310个规格中选，<strong>整体平均降幅超50%</strong>，部分OTC最高降幅达70%。首次大规模将OTC与独家品种全面纳入，护肝片、健胃消食片等常备药在列，采用“价格分60%+技术40%”综合评审及A/B分组竞争，告别“唯低价”。广西10月起执行集采药“三进”，定点药店中选药加成上限15%。<strong>院内院外价格体系被加速打通。</strong>",
      "GMT Eight · 搜药 · 中国新闻周刊 · 2026-10-17"),
]

flashes = [
    ("开源升级", "DeepSeek V4.1-Flash-1017：763B参数、跑分超Opus 5与GPT-5.6 Sol，单任务费用3.3元降至1.3元"),
    ("搜索开放", "DeepSeek开放自研Search/Fetch API，统一5元/千次，11月1日起服务端调用计费"),
    ("组织调整", "DeepSeek整合多团队成立产品部，原Harness负责人崔添翼出任负责人"),
    ("高息融资", "Anthropic“北极星项目”600亿美元芯片债，黑石认购90亿次级债、票息10%"),
    ("海外扩张", "Anthropic首签加拿大数据中心租约，EverWind拟投超100亿加元建420MW园区"),
    ("AI立法", "Anthropic向美国会推介AI安全法案草案，模型致超50人死伤或10亿美元损失可被叫停"),
    ("物理AI", "禾赛发布三维世界数据引擎Kosmo，联手银河通用、皮克斯、高德"),
    ("AI气象", "全国产“风清”AI集合预报系统投运，11天有效预报超欧洲中期天气预报中心"),
    ("安全并购", "Proofpoint拟约63亿美元、每股49.75美元收购数据与AI安全公司Varonis"),
    ("AI制药IPO", "英伟达投资的AI药企Iambic募资约1.5亿登陆纳斯达克（IAM）"),
    ("芯片代工", "KeyBanc称英特尔拿下博通、谷歌、苹果、AMD、微软、英伟达六家部分代工订单"),
    ("智能体网络", "紫金山实验室等发布确定性网络智能体互联平台AXP，跨4000公里寻址"),
    ("AI就业", "Anthropic内部报告：初级技术新聘占比27%降至9%，智能体工时达人类6倍"),
    ("AI量子", "Anthropic联合哈佛让Claude设计量子电路，椭圆曲线方案门数量降至约1/17"),
    ("院士观点", "丁汉院士：AI判百层CT仅3-5秒、肺结节敏感度超95%，医生仍是最终决策者"),
    ("心理AI", "京东健康×重医附一院共建心理康复医疗智能体实验室，发布精神心理知识图谱大模型"),
    ("罕见病新药", "首款国产全人源ANGPTL3单抗芮弗西拜单抗获批；武田NT1新药开出中国首日处方"),
    ("中成药集采", "第四批89种平均降幅超50%、OTC与独家品种首入；广西药店中选药加成上限15%"),
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
    ("趋势一 · “半分钱一次”对上“10%高息”，AI两种增长哲学同框",
     "10月17日极具象征意味。一边，DeepSeek把<strong>7630亿参数</strong>新模型跑分做到超越Claude Opus 5和GPT-5.6 Sol，同时把单任务费用从3.3元砍到1.3元，还把索引千亿网页的搜索能力以5元/千次（单次半分钱）开放、权重MIT开源；另一边，FT曝出Anthropic为买1.5GW谷歌TPU，向黑石支付<strong>10%票息</strong>、撬动600亿美元债务，而同类融资4个月前只要8.5%、信用相近的普通高收益债更只要7%。<strong>这不是简单的“中美差距”，而是两种增长函数的分叉：前者用工程效率和开源摊薄边际成本把市场做大，后者用资本杠杆前置锁定算力、赌未来收入覆盖利息。</strong>“算力回报率”第一次成为比“模型跑分”更硬的考题。"),
    ("趋势二 · 从“训模型”到“喂数据”，物理世界数据成为AI下半场稀缺资产",
     "本期两则新闻指向同一趋势。禾赛发布Kosmo，不再只卖激光雷达，而是用8K空间相机把真实房间扫描成3DGS/mesh/depth三种“可训练”三维资产，把自己重新定义为物理AI的数据基础设施；“风清”气象系统则证明，当视觉Transformer加上大气物理约束、再喂以国家级超算集群处理的海量观测数据，中国团队能在11天预报时效上超过欧洲老牌数值中心。<strong>大模型文本/代码红利正在见顶，下一阶段壁垒从“谁的参数多”转向“谁能把物理世界——空间、天气、生命——高保真地转化为机器可学习的数据”。</strong>"),
    ("趋势三 · 医疗AI从“能不能看病”走向“如何嵌入体系”，决策留给医生",
     "丁汉院士“医生永远是做决策的人”与京东健康把精神心理大模型送进2万学生筛查闭环，看似一守一攻，实则勾勒出医疗AI真实落位：<strong>不取代医生，而是重做“高频、重复、可标准化”的环节</strong>——AI把百层CT压到3-5秒、肺结节敏感度超95%，把青少年心理筛查做成多中心循证工具，而诊断权、责任与人文关怀仍留在医生一侧。制度侧同步收口：ANGPTL3单抗补上罕见病短板，第四批中成药集采和药店15%加成上限把院内院外价格打通。<strong>外资械企与创新药企需同时回答——能否进入AI驱动的诊疗闭环，以及能否在价值付费新账本里证明硬ROI。</strong>"),
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
    <title>吐司日报 · 第181期 · 2026-10-18</title>
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
            <div class="cover-en">VOL.181 · 2026.10.18 · SUN</div>
            <img class="cover-image" src="{HEAD}" alt="AI两条路线：开源普惠与高杠杆扩张">
            <div class="cover-meta">
                <span>📅 2026年10月18日</span>
                <span>📖 阅读约10分钟</span>
                <span>🔢 第181期</span>
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
            <div class="headline-title">AI的“两条路线”同框：DeepSeek开源7630亿参数、单任务费用砍到1.3元、5元/千次开放搜索API；Anthropic却被曝为600亿美元芯片债向黑石支付10%高息——开源普惠与高杠杆扩张的分野前所未有地清晰</div>
            <img class="headline-img" src="{HEAD}" alt="AI两条路线：开源普惠与高杠杆扩张">
            <div class="headline-summary">
                10月17日16时，国产大模型龙头DeepSeek宣布V4.1 Flash升级至<strong>V4.1-Flash-1017</strong>，网页端、App与API同步切换，模型名沿用deepseek-flash、调用方式与API单价不变。新模型参数规模达<strong>7630亿（763B）</strong>，在DeepSWE v1.1、Automation-Bench、Agents' Last Exam等智能体与多模态基准上拿下最高分，领先Claude Opus 5、GPT-5.6 Sol等海外旗舰；max档<strong>每任务平均费用从上一版约3.3元降至约1.3元</strong>。同日DeepSeek正式开放自研<strong>Search/Fetch搜索API，统一价5元/千次（单次半分钱）</strong>，索引全球千亿级网页、日处理数亿次请求。权重以MIT许可开放下载。<br><br>
                几乎同一时刻，AI产业另一端呈现截然相反的资本画像。英国《金融时报》17日报道，Anthropic正推进代号<strong>“北极星项目”的约600亿美元芯片债务融资</strong>，采购约1.5吉瓦谷歌定制TPU，将成史上最大芯片融资；其中约420亿优先级债（博通残值担保）、180亿次级债，<strong>黑石承诺认购90亿美元次级债、票息高达10%</strong>，而信用相近者公开市场只需约7%——四个月前“Big Sky”次级债利率还约8.5%。同日Anthropic首次在加拿大签下数据中心长期租约。一边开源、降价、把能力以半分钱一次开放；一边以两位数高息为天量算力加杠杆。<strong>当AI进入“算账阶段”，中国式效率路线与美国式资本路线的分野，在这个周末被摆到同一张桌面上。</strong>
            </div>
            <div class="headline-source">澎湃新闻 · 第一财经 · 机器之心 · 金融时报 · 财联社 · 新浪财经 · 2026-10-17</div>
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
            第181期 · 2026年10月18日<br>
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

OUT = f"{BASE}/第181期/公众号排版_181期.html"
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print("公众号版生成:", OUT)
print("字节:", len(html.encode("utf-8")), "图片:", html.count("<img"), "快讯:", len(flashes))
