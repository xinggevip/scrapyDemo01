## Scrapy学习笔记

## 相关链接

[Scrapy官网](https://docs.scrapy.org/en/latest/)

[Scrapy中文官网](https://www.osgeo.cn/scrapy/topics/request-response.html)

[Scrapy中文文档](http://www.scrapyd.cn/doc/137.html)

[床长人工智能网校](https://www.cbedai.net/)

## 架构图

- Scrapy Engine(引擎)：负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯、信号、数据传递等
- Scheduler(调度器)：它负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队，当引擎需要时，交还给引擎
- Downloader(下载器)：负责下载Scrapy Engine(引擎)发送过来的Request请求，并将其获取到的Response交还给Scrapy Engine(引擎)，由引擎交给Spider处理
- Spider(爬虫)：它负责处理所有的Response，从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Schedule(调度器)
- Item Pipeline(管道)：它负责处理Spider中获取的Item，并进行后期处理(详细分析、过滤、存储等)的地方
- Downloader Middlewares(下载中间件)：可以理解为可以自定义的操作引擎和Spider中间通信的功能组件(比如进入Spider的Response和Spider出去的Request)

## 创建项目和爬虫

1. 创建项目

   ```bash
   scrapy startproject 项目名字
   ```

2. 创建爬虫

   ```bash
   cd 爬虫项目目录
   scrapy genspider 爬虫名字
   ```

## 项目目录结构

1. `items.py`:用来存放爬虫爬取下来数据的模型
2. `middlewares.py`：用来存放各种中间件的文件。
3. `pipelines.py`:用来将`items`的模型存储到本地磁盘中。
4. `settings.py`：爬虫的一些配置信息（如请求头，多久发送一次请求，ip代理池等）
5. `scrapy.cfg`：项目的配置文件。
6. `spiders`包：以后所有的爬虫，都是存放到这里。

## 快速入门

1. response是一个`scrapy.http.response.html.HtmlResonse`对象，可以执行`xpath`和`css`语法来提取数据。

2. 提取出来的数据是一个`Selector`或`SelectorList`对象。获取其中字符串应该执行`getall`或`get`方法。

3. `getall`方法：获取`Selector`中的所有文本，返回一个列表。

4. `get`方法：获取的是`Selector`中的第一个文本，返回一个`str`类型。

5. 如果数据解析回来，要传给`pipeline`处理，可以使用`yield`来返回。或者收集所有的`item`,最后统一使用return返回。

6. `item`：建议在`items.py`中定义好模型，以后就不用使用字典的方式。

7. `pipeline`:这个是专门用来保存数据的，其中有三个方法会经常使用：

   - `open_spider(self, spider)`：当爬虫被打开的时候执行
   - `process_item(self, item, spider)`:当爬虫有`item`传过来的时候会被调用。
   - `closs_spider(self, spider)`: 当爬虫关闭的时候回被调用

   要激活`pipeline`，应该在`settings.py`中，设置`ITEM_PIPELINES`。

8. 保存`json`数据的时候可以使用`JsonItemExporter`和`JsonLinesItemExporter`

   - `JsonItemExporter`:每次把数据添加到内存中，最后统一写入到磁盘中。好处是存储的数据是一个满足`json`规则的数据。坏处是如果数据量比较大，那么比较耗内存。

     ```
     from scrapy.exporters import JsonItemExporter
     
     class QsbkPipeline(object):
         def __init__(self):
             self.fp = open('duanzi.json', 'wb')
             self.exporter = JsonItemExporter(self.fp, ensure_ascii=False,
                                              encoding='utf-8')
             self.exporter.start_exporting()
     
         def open_spider(self, spider):
             pass
     
         def process_item(self, item, spider):
             self.exporter.export_item(item)
     
             return item
     
         def close_spider(self, spider):
             self.exporter.finish_exporting()
             self.fp.close()
     ```

   - `JsonLinesItemExporter`：每次调用`exorter_item`的时候就把`item`存储到磁盘中。坏处是每一个字典是一行，整个文件不是一个满足`json`格式的文件。好处是每次处理数据的时候就直接存储到磁盘中，不会耗内存，数据也比较安全。

     ```
     from scrapy.exporters import JsonLinesItemExporter
     
     class QsbkPipeline(object):
         def __init__(self):
             self.fp = open('duanzi.json', 'wb')
             self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False,
                                              encoding='utf-8')
     
         def open_spider(self, spider):
             pass
     
         def process_item(self, item, spider):
             self.exporter.export_item(item)
     
             return item
     
         def close_spider(self, spider):
             self.fp.close()
     ```

## CrawlSpider

**在创建爬虫的命令修改为`scrapy genspider -t crawl 爬虫名字 爬虫域名`**

需要使用`LinkExtractor`和`Rule`，这两个东西决定爬虫的具体走向。

1. `allow`设置规则的方法，要能够限制在我们想要的`url`上，不要跟其他的`url`产生相同的正则表达式即可。
2. 什么情况下使用`follow`:如果在爬取页面的 时候，需要将满足当前条件的`url`再进行跟进，那么就设置为True,否则设置为False.
3. 什么情况下指定`callback`：如果这个`url`对应的页面，只是为了获取更多的`url`， 并不需要里面的数据，那么可以不指定`callback`；如果想要获取`url`对应页面的数据，那么就需要指定一个`callback`。

## Scrapy Shell

1. 可以方便我们做一些数据提取的测试代码
2. 如果想要执行`scrapy`命令，毫无疑问是要先进入到`scrapy`所在的环境中
3. 如果先要读取某个项目的配置信息，那么应该先进入到这个项目中，再执行`scrapy shell`命令