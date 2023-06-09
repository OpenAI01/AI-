# 结合input、字典、if判断，做一个查阅流行语的电子字典程序
slang_dict={"栓Q":"这一条其实是一组流行语，虽然字面有个“谢（栓）”，这一条其实是一组流行语，虽然字面有个“谢（栓）”，但实际上主要用来表达大无语状态或是非常厌烦的情绪，并非真的用来表示对他人的感谢。“栓Q”源于某抖音用户在2022年2月的一条宣传遇龙河竹筏漂流小视频的末尾所说的“Thank you.”，其中“thank”的发音酷似shuān。发音虽然不标准，但他说“Thank you.”确实表达感谢。不过“栓Q”被创造出来后，含义、用法就大为不同了。",
            "PUA":"在一段网络采访视频中，受访者因口误将“PUA”说成“CPU”，网友们觉得有趣而开始玩梗，故意将“PUA”说成“CPU”或者“KTV”“PPT”“ICU”。“PUA”是“Pick-up Artist”（搭讪艺术家）的简称，源于美国，原指男性为了增强异性交往中的魅力而学习提高情商、增加互动的技巧，如今在网络语境中泛指人际关系中一方通过洗脑、打压的方式，对另一方进行情感、思想控制的行为，存在于恋爱、职场、家庭、校园等多种场景中。"}
slang_dict["冤种"]="“冤种”一词来自东北地区方言，原指因为蒙受委屈而闷闷不乐的人，如今网络中常用此词来泛指做了傻事的人，即冤大头、倒霉鬼等。常见的搭配有“大冤种”“纯纯大冤种”“职场大冤种”等。最初是一些东北的博主用此口头语进行自嘲，带起了流行；后来网友们用“冤种”来形容自己或者身边亲友，包含一种亲切憨厚的感觉，来化解生活中“哑巴吃黄连，有苦说不出”的不快经历，还可表达又好笑又心疼的复杂情感。"
slang_dict["小镇做题家"]="这一词条最早见于豆瓣小组“985废物引进计划”。根据豆瓣用户“水果糖”的总结，“小镇做题家”指的是那些“出身小城，埋头苦读，擅长应试，但缺乏一定视野和资源的青年学子”。这一概念一经提出即引发热议，也引发了众多985、211高校已毕业、未毕业学生的共鸣——有反思，有调侃，也有自嘲。"
slang_dict["团长"]="　“团长”原指军队中一个团级单位的最高指挥官，在新冠肺炎疫情期间被赋予了新的内涵。疫情防控期间，线下商超关闭，线上购物平台难以下单，有这么一群人，他们不畏风险，各显神通，无偿组织团购和分发生活物资，被居民们亲切地称为“团长”。“团长”是“平民英雄”，该群体背后是千千万万来自各行各业热心的平凡人。"
slang_dict["退！退！退！"]="某段网络视频记录了一位车主和摆摊大妈因车位发生争吵的过程。视频中，大妈面对别人的质问，并不正面回应，只是一边跺脚一边用手做击剑动作，同时大喊“退！退！退！”。这种类似传统民俗中作法驱逐恶灵的奇特姿势，充满了喜剧效果，引发网友们的模仿；相关表情包也在网络中广泛流传。"
slang_dict["嘴替"]="“嘴替”即“嘴巴的替代”，指能够代替广大网友表达心声的人。网友们对某些事情虽有看法和态度，但因为口才不行或者顾虑太多，往往词不达意。而有些人善于捕捉并总结某一群体、某类人共同的想法，且能言简意赅地表述出来，引发大家的共鸣。于是网友们用“嘴替”表达对这些精彩言论的肯定和对敢于发声者的褒扬。"
slang_dict["一种很新的xx"]="“一种很新的××”出自短视频平台的音乐评论区，最初用来表达对作品中融合过多音乐元素的无法理解，现广泛用于调侃某些不可思议的事物、超出常规的行为。“一种很新的××”可以表达一种不理解、不欣赏的态度，含有一种委婉的批评意味；但有时也仅仅强调事物、情况的新变化、新发展，作为各种领域的新闻讲解开头语，吸引大家的注意。"
slang_dict["服了你个老六"]="“老六”是出自射击游戏的一个梗，带有贬义色彩。游戏对战时通常是“五对五”，但有些人不打配合，在其队友正面拼杀的时候，“老六”则躲在暗处，以阴险狡诈的方式取胜。“服了你个老六”是游戏玩家常用的一句吐槽。除了在游戏圈，这句话在日常交际中多用来嘲讽那些以出其不意的方式获胜或玩阴险手段的人。"
slang_dict["xx刺客"]="“刺客”原指“用武器进行暗杀的人”。“××刺客”的产生与认知隐喻有关：一些外表普通、未明码标价的高价商品，就像刺客一样具有隐藏性，在结账时以远超预期的价格突然“刺”消费者一剑，使其钱包和心理都受到了伤害。如“雪糕刺客”“水果刺客”等。“××刺客”突出了事物带给人的刺激与不适感，也反映了大众消费心态的转变——对“××刺客”要敢于说“不”，进行抵御。"
query=input("请输入您想要查询的流行语：")
if query in slang_dict:
    print("您查询的"+query+"含义如下:")
    print(slang_dict[query])
else:
    print("您查询的流行语暂未收录")
    print("当前本字典收录的词条为："+str(len(slang_dict))+"条。")
