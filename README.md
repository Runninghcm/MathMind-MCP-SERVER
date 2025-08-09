# 一、简介：

MathMind MCP Server提供了一个基于MCP协议的一系列音视频创作与合成的工具服务。用户在任意支持MCP服务的工具中添加MathMind-MCP服务，即可通过自然语言描述场景和需求，工具即可自主调度MathMind的一系列工具，从而实现音视频多媒体内容的智能化生成。

# 二、核心工具
| 序号 | 工具中文名称 | 工具英文名称 | 工具介绍（中文） |
|----|--------------|--------------|------------------|
| 1  | 多张图片合成视频 | imgs2video | 将一张或多张图片合成一个视频，支持添加背景音乐、配音。 |
| 2  | 多个视频合成视频 | video2video | 将一个或多段视频素材合成一个视频，支持上传背景音乐（非必填）、配音（非必填）合成新的视频。支持单独上传首、尾视频，固定视频首尾。支持设置封面图、支持配音音量控制、支持背景音乐自定义音量。 |
| 3  | 视频文案提取 | video2txt | 实时提取视频中的文案，用户输入视频链接即可。建议上传5分钟以下的视频 |
| 4  | 视频字幕识别 | subtitleDynamic | 上传视频，即可识别字幕并输出最终带字幕的视频。字幕支持设置字体与位置等。支持传入text文本。 |
| 5  | 视频字幕识别任务查询 | taskFetch2 | 输入工具subtitleDynamic输出的traceId即可获得添加了字幕以后的视频地址 |
| 6  | 视频片段获取 | videoCutRandom | 输入视频链接，输入截取的起始和结束位置，即可截取视频片段 |
| 7  | 图生视频 | imageGenVideo | 上传图片，输入提示词，即可生成视频，模型为VIDU。<br>支持实时生成和异步生成。当异步生成，则需要调用查询工具：videoTaskFetch<br>实时直接生成URL；<br>异步先只给traceId，用户需要调用videoTaskFetch |
| 8  | 图片画中画 | imgPip | 输入视频，为视频添加图片，如logo、视频提及内容等图片素材。<br>支持自定义素材的宽高、入场和出场的时间、动画以及显示的位置，非必填，取默认值。 |
| 9 | 画中画任务查询 | cutTaskFetch | 上述imgPip只会返回ReqId，此时需要使用任务查询工具主动查询结果 |


# 三、快速开始
## 获取apikey
在MathMind开放平台注册并获取apikey，[立即前往](https://admin.mathmind.cn/login?referralCode=REF22431068)

## SSE 调用方式

### Windsurf

前往 Windsurf > Settings > Cascade > Add Server > Add custom server 添加配置：


```
{
  "mcpServers": {
    "mcp-server-mathmind": {
      "url": "https://mcp.mathmind.cn/sse?x-api-key=<YOUR_API_KEY>"
    }
  }
}
```


### Cursor

前往 Cursor -> Preferences -> Cursor Settings -> MCP -> Add new global MCP Server 添加配置:

```
{
  "mcpServers": {
    "mcp-server-mathmind": {
      "url": "https://mcp.mathmind.cn/sse?x-api-key=<YOUR_API_KEY>"
    }
  }
}
```

### 通义灵码

前往 通义灵码 -> MCP工具 -> MCP服务 -> 通过配置文件添加新增MCP服务 -> lingma_mcp.json添加以下配置:

```
{
  "mcpServers": {
    "mcp-server-mathmind": {
      "url": "https://mcp.mathmind.cn/sse?x-api-key=<YOUR_API_KEY>"
    }
  }
}
```


# 其他

## 技术支持

邮件联系：ai@mathmind.cn

技术支持：

<img width="150" height="150" alt="image" src="https://github.com/user-attachments/assets/f53ed106-d378-4347-aa48-91c6968b0bfe" />


--- 
## 快捷入口
- 官网入口：https://mathmind.cn/
- 开放平台：https://admin.mathmind.cn/#/
- 插件市场：https://www.coze.cn/user/829510688450616
- 免费教程：https://mathmind.feishu.cn/wiki/OtIZwYuxbi1ErQkyovmc07HmnOh
- 付费空间：https://mathmind.feishu.cn/wiki/GvW8wyv2VithdnkNsVmcqhVNnYb
- B站视频讲解：https://space.bilibili.com/87911991/channel/seriesdetail?sid=4634704
- 帮助中心：https://mathmind.feishu.cn/docx/Q6eodjvPLoq7yDxZaHOcfnFrntg
- Coze折扣：https://mathmind.feishu.cn/wiki/D9qSwIoaEixfqmkDupuceF62nFg
