## 报告提纲

### 1.选题背景

<u>说明本课题应解决的主要问题及应达到的技术要求，简述本设计的指导思想。</u>

直接照抄要求即可。

### 2.方案论证

<u>说明设计原理（理念）并进行方案选择，阐明为什么要选择这个设计方案以及所采用方案的特点。重点说明要实现的功能及其要求、系统的安全性、数据的完整性、应用的运行环境及其性能等要求。</u>

按软工课说的那样，先写我们有什么需求（比如分词需要有效率，需要分词准确度高，需要便于用户操作，数据完整性、系统安全性balabala），而我们选用的算法/模块有什么优势（比如jieba分词效率高，准确度高，封装性好，便于操作）

- 语料库选择


With the development of Web 2.0 technology and mobile networks, more and more people are interacting on the Web, generating a large amount of unstructured Web text. It is because people express themselves very casual in social media, so a large number of non-standard expressions like abbreviations, emoticons, etc. are generated in today's network, which is not conducive to our Chinese word separation for normative texts. Additionally, there is a lot of noise, which increases the difficulty of understanding and word separation, causing the later high-level applications such as natural language processing cannot analyze and interpret directly on this word separation result. Some studies indicate a 10% difference between the same word separation system applied to a social platform corpus and a normative corpus. Therefore, we try to avoid crawling social media user posts when selecting the corpus. Instead, we choose news website articles to crawl. News is a standardized style with good ability for separation. However, in order not to lose coverage of the new vocabulary, we additionally chose web novels to add to the corpus, meaning that we ensure both the richness and normativity of the sample pool in the corpus.

**Our corpus,**

**Sina News, 2022, 924MB**

**Xinwenlianbo scripts of CCTV, 63MB**

**Biquge Web Novels, 877MB**


#### scheme design和parameter

- [ ] 修改workflow图
- [ ] 画一个数据流图
- [ ] 表格重要的参数与说明

#### 粒度控制

论证每次迭代读取的语料库大小，从迭代用时、新词发现数量、分出的词的总量等指标来看，做一个对比表格

#### 字典数据库的存储与更新

用txt?用mysql?关于如何维护，谈谈为什么要建立数据库。

#### 初始词库的考虑

清华的词库给我们提供分类

搜狗的词库给我们提供词性

虽然结巴分词也自带词性，但是（摆出具体词性数量的对比，举一些例子）没有搜狗词库的效果好

给出训练的准确度（也可能放到结果分析那里）

#### 爬取语料库的理念

效率问题，选取语料库的考虑

#### 分词的工具：结巴分词

扯一下结巴分词的算法优越在哪里

As the massive words dictionary construction tool is required to obtain separated words from tens of millions of words in the corpus, there is no doubt that the Chinese text segmentation is a module of vital significance in the software. Among those famous text segmentation tools, we chose Jieba Chinese text segmentation, considering both the performance and the function.

Specifically speaking, our requirements for the text segmentation module include these aspects. First of all, the word segmentation should be accurate enough so that the subsequent word sorting and dictionary construction can be accurate. Secondly, the word segmentation should support user defined dictionary so that the word segmentation can evolve as the dictionary updated iteratively. Last but not least, the efficiency of both the loading of dictionary and segmentation should be ensured, so that the massive dictionary construction can be efficient enough to meet the users' demand.

With 28.8k stars on GitHub and used by 13.2k GitHub developers, Jieba Chinese text segmentation has been one of the most popular Chinese Natural Language Processing tools since its birth on last decade. Jieba Chinese text segmentation is built to be the best Python Chinese word segmentation module, with an MIT license. The details of the word segmentation tool is available at https://github.com/fxsjy/jieba.

From the aspects of functions, jieba Chinese word segmentation support 3 types of segmentation mode including Accurate Mode, Full Mode and Search Engine Mode. In addition, it supports traditional Chinese as well as customized dictionaries. The segmentation tool realize these functions with these fundamental designs:

- Based on a prefix dictionary structure to achieve efficient word graph scanning. Build a directed acyclic graph (DAG) for all possible word combinations.
- Use dynamic programming to find the most probable combination based on the word frequency.
- For unknown words, a HMM-based model is used with the Viterbi algorithm.

From the aspect of performance, the segmentation speed is fast enough to meet our needs of efficient massive dictionary construction:

- 1.5 MB / Second in Full Mode
- 400 KB / Second in Default Mode
- Test Env: Intel(R) Core(TM) i7-2600 CPU @ 3.4GHz；《围城》.txt

#### 分类的工具：gensim

Gensim（generate similarity）是一个简单高效的自然语言处理Python库，用于抽取文档的语义主题（semantic topics）。Gensim的输入是原始的、无结构的数字文本（纯文本），内置的算法包括Word2Vec，FastText，潜在语义分析（Latent Semantic Analysis，LSA），潜在狄利克雷分布（Latent Dirichlet Allocation，LDA）等，通过计算训练语料中的统计共现模式自动发现文档的语义结构。这些算法都是非监督的，这意味着不需要人工输入——仅仅需要一组纯文本语料。一旦发现这些统计模式后，任何纯文本（句子、短语、单词）就能采用语义表示简洁地表达。

##### 特点
-Memory independence： 不需要一次性将整个训练语料读入内存，Gensim充分利用了Python内置的生成器（generator）和迭代器（iterator）用于流式数据处理，内存效率是Gensim设计目标之一。
-Memory sharing： 训练好的模型可以持久化到硬盘，和重载到内存。多个进程之间可以共享相同的数据，减少了内存消耗。
-多种向量空间算法的高效实现： 包括Word2Vec，Doc2Vec，FastText，TF-IDF，LSA，LDA，随机映射等。
-支持多种数据结构。
-基于语义表示的文档相似度查询。

#### 监控系统

（抄PPT里的模板）

### 3.过程论述

<u>重点说明设计是如何实现的，包括：对设计工作的详细表述。要求层次分明、表达确切。要求：每个图都必须有文字说明，图前说明为什么使用该图、图的主要作用；图后说明图中各成分的作用，和成分之间的交互或图所表达的流程。</u>

把**各个模块**，**各个函数**的**input**和**output**都写一下，把代码里的逻辑说明一下即可。围绕着workflow图和数据流图写即可。

用语言难以描述的可以搞几个示意图。

#### 爬取语料库

We use Scrapy framwork to corpus.

1. Set scraping date.

2. We start from main page, generating every news page waiting for scraping according to the user input of date.

3. Get the html code using Requests module in Python for every news page, parse the news id, title, content, and release time respectively according to the structure of the webpage.

    - Sina News:

        ```python
        item = SinaNewsItem()
        item['news_id'] = re.search(r'\d+', response.url.split('/')[-1]).group()
        item['news_title'] = response.xpath('//h1[@class="main-title"]/text()').extract_first()
        article_p_list = response.xpath('//div[@class="article"]//p//text()').extract()
        article = '/'.join(article_list)
        item['news_content'] = article
        item['news_date'] = response.xpath('//span[@class="date"]/text()').extract_first()
        ```

    - Xinwenlianbo:

        ```python
        def tag_filter_headline(tag):
            flag_1 = (tag.name == 'li') and not tag.has_attr('class')
        def tag_filter_content(tag):
            flag_1 = (tag.name == 'p') and not tag.has_attr('class')
        soup = BeautifulSoup(r.text, features="lxml")
        outlines_raw = soup.find_all(tag_filter_headline)
        full_texts_raw = soup.find_all(tag_filter_content)
        ```

    - Biquge Novel:

        ```python
        def get_toc(url):
            toc_url_block = re.findall('<dl(.*?)</dl>', toc_html.text, re.S)[0]
            toc_url = re.findall('href="(.*?)"', toc_url_block, re.S)
            time_block = re.findall('<head(.*?)</head>', toc_html.text, re.S)[0]
            time = re.findall('<meta property="og:novel:update_time" content="(.*?)"', time_block, re.S)[0]
        def get_article(url, update_year):
            chapter_name = re.findall('<h1>(.*?)</h1>', chapter_html.text, re.S)
            info = selector.xpath('//*[@id="content"]/text()')
        ```

        

4. Insert records into the MySQL server for news storage, and put an record to Redis server to mark down the id of each news to prevent duplicate crawling during subsequent parsing.


#### 分词

#### 新词发现

#### 分类

##### 获取训练数据
1. SougouLabDic: 提供共157202个词语的文本，词频以及词性信息
2. THUOCL（清华大学开源词库）：提供11个分类下词语的文本及词频信息。11个分类分别为：animal,caijing,car,chenyu,diming,food,it,law,lishimingren,medical,poem

##### 训练数据处理
- 词语分类：将THUOCL中词语提取出来，将词频的对数作为个数插入进列表，并赋予文件夹名作为标签。同时将SougouDic中的词语依照同样方式插入列表，区别在于标签设为"other"
- 词性分类：只讲将SougouDic插入进列表，同时将第三列的词性转化为列表，列表长度为17，与SougouDic中提供的17种词性对应，存在的词性设为1，其余设为0。

##### word2vec
导入腾讯ailab提供的预训练好的word2vec模型。直接导入时间过久，便将模型转换为二进制文件保存便于后续读取。导入后的文件可被视作字典。若文本存在于键中，则直接导出一个100维的列表，否则随机生成一个100维的列表。

##### 训练模型
<code>    X_train, X_test, y_train, y_test = train_test_split(vector_list, label, test_size=0.33, random_state=1)</code>

通过gensim自主将所有训练文本划分为训练集和测试集。

- 词类训练：运用svm<code>clf = LinearSVC() svm = CalibratedClassifierCV(clf)</code> 测试准确率为80.9%
- 词性训练：运用moc<code>classifier = MultiOutputClassifier(XGBClassifier()) clf = Pipeline([('classify', classifier)])</code> 测试准确率为94.5%

##### 输出分类结果
均获得与输入相同长度的标签序列
- 词类训练：获得词类的文字标签
- 词性训练：获得与词性对应的0/1标签序列

#### 构建新词典

#### 对数据库的初始化与数据库的访问

### 4.结果分析

<u>对研究过程中所获得的主要的数据、现象进行定性或定量分析，得出结论和推论。</u>

设计测试用例，定量说明

#### 功能测试

把各个模块测试的测试用例列一下，把结果图截下来
Parsing Info Logging:

```
['绝世兵王', '不灭战神', '小村那些事', '绝美女神爱上我', '逆天邪神', '小蛮腰', '宋末之乱臣贼子', '混在东瀛成大亨', '刀碎星河', '超级抢红包系统', '美女总裁俏房客', '草根富豪', '夺舍之停不下来', '文娱大时代', '首辅沈栗', '绝品透视眼', '我老婆是冰山女总裁', '纵天神帝', '最佳娱乐时代', '我的极品小姨', '特战医王', '我在女子监狱的日子', '太古丹尊', '美漫之道门修士', '武道系统之草民崛起', '我的邻家空姐', '异次元游戏', '锦医卫', '重生学霸小甜妻', '圣者', '隐婚甜宠：大财阀的小娇妻', '快穿之炮灰逆袭记', '万古第一神', '武侠之巅峰主播', '惜春是个佛修[红楼]', '快穿逆袭：神秘boss，别乱撩', '娱乐帝国系统', '面瘫宝贝，变身吧', '乡村透视小神医', '无敌悍民']
['https://www.bbiquge.net/book/26668/', 'https://www.bbiquge.net/book/43606/', 'https://www.bbiquge.net/book/56540/', 'https://www.bbiquge.net/book/74020/', 'https://www.bbiquge.net/book/72891/', 'https://www.bbiquge.net/book/84637/', 'https://www.bbiquge.net/book/42602/', 'https://www.bbiquge.net/book/12690/', 'https://www.bbiquge.net/book/14570/', 'https://www.bbiquge.net/book/33128/', 'https://www.bbiquge.net/book/85197/', 'https://www.bbiquge.net/book/368/', 'https://www.bbiquge.net/book/79586/', 'https://www.bbiquge.net/book/45127/', 'https://www.bbiquge.net/book/33597/', 'https://www.bbiquge.net/book/53714/', 'https://www.bbiquge.net/book/99767/', 'https://www.bbiquge.net/book/60402/', 'https://www.bbiquge.net/book/124071/', 'https://www.bbiquge.net/book/92056/', 'https://www.bbiquge.net/book/72568/', 'https://www.bbiquge.net/book/92087/', 'https://www.bbiquge.net/book/96578/', 'https://www.bbiquge.net/book/120165/', 'https://www.bbiquge.net/book/29168/', 'https://www.bbiquge.net/book/4612/', 'https://www.bbiquge.net/book/24396/', 'https://www.bbiquge.net/book/971/', 'https://www.bbiquge.net/book/119295/', 'https://www.bbiquge.net/book/19407/', 'https://www.bbiquge.net/book/116853/', 'https://www.bbiquge.net/book/19937/', 'https://www.bbiquge.net/book/131134/', 'https://www.bbiquge.net/book/40796/', 'https://www.bbiquge.net/book/124118/', 'https://www.bbiquge.net/book/105919/', 'https://www.bbiquge.net/book/4877/', 'https://www.bbiquge.net/book/45648/', 'https://www.bbiquge.net/book/121647/', 'https://www.bbiquge.net/book/79894/']
正在抓取  绝世兵王
['第005章 曾经的记忆']
['第010章 百里柔冰']
['第014章 恶人先告状']
['第003章 酒入愁肠']
['第001章 野店美酒']
['第006章 活着的痛苦与希望']
['第009章 应聘']['第002章 机会，靠自己去争取！']
['第007章 唐小薇']
['第008章 天铭集团']
```

File Storage Tree:

```
D:.
├─2022年01月01日
│      2528066.txt
│            #三只松鼠#【“5年防骗、3年补脑” #三只松鼠营销海报又遭质疑#】近日，网红品牌三只松鼠的一张“331补脑节”的商业海报再次引发关注。海报上少先队员戴着红领巾，拿着“5年防骗、3年补脑”的零食大礼包，行少先队礼的内容被网友质疑。据三只松鼠官方显示，该海报上架与2019年3月，为三只松鼠创立的“331补脑节”。与此同时，三只松鼠也面临营收下滑、大股东减持、市值蒸发、多次被曝出食品安全问题，其“贴牌+代工”的生产模式，也频频陷入舆论风波。责任编辑：梁斌
│ 
├─2022年01月02日
│      7926488.txt
│
├─2022年01月03日
│      8072311.txt
│
└─2022年06月15日
        6815960.txt
        6816967.txt
        6855254.txt
        6855909.txt
```

#### 性能测试

测各个模块的时间

#### 压力测试

1.跟方案论证里的粒度的测试很像，看看一次迭代要读取很大的文件时会发生什么事情

2.试一下输入很大的迭代次数（超过最大迭代次数，比如100000与不超过最大迭代次数的，比如100），看看输出的各项指标，跟一个普通的迭代次数（比如10）的各项指标对比

### 5.课程设计总结

<u>课程设计过程的收获、遇到的问题，遇到问题解决问题过程的思考、程序调试能力的思考，课程设计实现过程中的收获和体会等。</u>

