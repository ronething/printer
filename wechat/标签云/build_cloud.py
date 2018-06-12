# coding:utf-8
# 生成词云
import re
tList = []

# 拼接字符串
text = """
不够冷静机智"hello.howareyou...Givemybest！！！您好，有事请留言，我会尽快回复您人生在世，相惜于品，相敬于德，相交于情，相随于义。与你一个喜欢给你们分享美好事物的女孩<="Entschudigung不要觉得弱小是理所当然不以物喜，不以己悲！做IT界的金融家..以我绝美之刃弑你凡尘之羽愿吾万事胜意<="2764"</学会微笑！【我喜欢我是玫瑰色的，】音为爱·音为你上善若水。不要怂就是干！！我会努力做到
承君一诺，必守一生
以剑之名，以月之名3年后看到吧！既然选择了远方，就要风雨兼程！君以国士待我，我当以国士报之。Lackofpassionisfatal.只有你，让我的体温上升0.5度自己过得好，才是真的好，难听了点，却是真理^_^^_^是远方有琴，愀然空灵，声声催天雨新号码：15710633371可能真的在乎吧，所以就很在意天气转凉，记德添衣想在泛泛之众做一个酷酷的少女～LittleYan<="偷偷的变kiang缘分是本书翻的不经意会错过读的太认真会流泪。。喜欢下雨，还有雨后的阳光。最终目标：环游世界好人行好路在所有人事已非的景色里

我最喜欢妳永远只为争一口气，为自己活得更好逐梦翎雀浴火重生但行好事莫问前程但问耕耘莫问收获铭寶倫酒庄，你的私人酒庄，出售各类红酒，价格经济实惠！YYYYYYY(´･_･`)努力学英语中。。。。。。。。Withtheoriginalhearttodoforever.热线：13794416368高举自身者必为人贬抑，贬抑自身者必为人高举这家伙很懒，什么都没有留下Nozuonodie！记得也好最好忘掉圆通恢复，急事来电15017559653恩恩我也想有个店长！<="祝生意兴隆<="donotregret-Lifewillbebetter原来。唯自由为上潮汕特色食品百太，你的潮流口袋waiting一切众生，若干种心，如来悉知悉见。没有无缘无故的好，只有不冷不淡的关怀。收拾旧山河，朝天阙做人:菩萨心肠！办事:屠夫手段！莫见乎隐，莫显乎微，故君子慎其独也。也许是我太过渴望人只要放好心态没有什么事会挺不过去的，把一次困难当做一场锻炼喵<="
世界和平不乱于心不困于情不畏将来不念过往阳光下像个孩子风雨里像个大人再见了，大家请认准呢只莹我想，我等，我期待。世界上没有绝对的绝缘体，只有不努力的电压。I'mheretoletyouknow
I'mheretoletyougo散落风中的约定<="我祈祷拥有一颗透明的心灵你主动点我们就有故事。微笑恐惧症O_oComebacktome.若有些人当你一摊烂泥，那么你也只好在他们面前开出花朵。醒来觉得甚是爱你<="2764"</认真且怂从一而终心是孤独的猎手哪会怕有一天只你共我紫罗兰把它的香气留在那踩扁了它的脚踝上，这就是宽恕。隐约雷鸣阴霾天空红满堂人工智能，开心就人工，忙不过来就智障呗，别问，单身如果再见不能红着眼是否还能红着脸FreiheitalsAutonomie.复合吧我有一个哥哥
可以温暖整个世界我弄丢了我的热情。别问“在不在”，这不是QQ我的心借了你的光是明是暗腹有诗书气自华我给你最后的疼爱是手放开手机已扔急事<="发现了一个崭新的世界。…回忆是一条没有尽头的路…下个目标。谨言慎行
非常酷不闲聊
孤独且帅气一本傻逼却扮得酷酷滴方寸之间，一步万象<="Insolitude,beamultitudetoyourself..
♡.♡.♡우리같이늙자♡GD◡̈⃝腹有诗书气自华养生！想要怎样的生活，就去创造！别胆怯，去突破！Theyallwanttokillyou，kissyou，
ortobeyou.
''以后你死了，我要叫我们的子孙把我安乐死''愚人生若只如初见，何事秋风悲画扇。大风吹大风吹看我朋友圈
看我打不打死你Ifnotme，who？Ifnotnow，when？此人常年挂机非常不走心。不敢想那一刻的到来累
二月的你
四月的风
刚刚好我也喜欢壁纸纹理释怀后蛮舒服的孤独且帅气成长中每一次低头，都是对自己的肯定Booyah，Booyah，whathef*Boo微斯人，吾谁与归不打扰是我的倔强哭我为了感动谁
笑又为了碰着谁由于各种原因微信不常在线
"""

# jieba分词
import jieba
wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)

# wordcloud词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os
import numpy as np
import PIL.Image as Image


d = os.path.dirname(__file__)
alice_coloring = np.array(Image.open(os.path.join(d, "alice_color.png")))
my_wordcloud = WordCloud(width=300,height=200,background_color="black", max_words=2000, mask=alice_coloring,
                         max_font_size=40, random_state=42,
                         font_path='C:/Python27/Lib/site-packages/wordcloud/msyh.ttf')\
    .generate(wl_space_split)

image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
