# 一、简介：

MathMind MCP Server提供了一个基于MCP协议的一系列音视频创作与合成的工具服务。用户再任意支持MCP服务的工具中添加MathMind-MCP服务，即可实现通过自然语言描述场景和需求，工具即可自主调度MathMind的一系列工具，从而实现音视频多媒体内容的智能化生成。

# 二、核心工具

1、多张图片合成视频

imgs2video：将一张或多张图片合成一个视频，支持添加背景音乐、配音；视频时长以配音时长为准，当配音时长小于背景音乐时长时，会对背景音乐进行裁剪；当配音时长大于背景音乐时，会将背景音乐复制

2、多个视频合成视频

video2video：将一个或多段视频素材合成一个视频，支持上传背景音乐（非必填）、配音（非必填）合成新的视频。支持单独上传首、尾视频，固定视频首尾。支持设置封面图、支持配音音量控制、支持背景音乐自定义音量。

3、单张图片合成视频

imgToVideo：将一张图通过自定义时长合成视频，最大支持60s

4、视频字幕识别

subtitleDynamic：上传视频，即可识别字幕并输出最终的视频。字幕支持特效设定与无特效。

5、视频字幕识别任务查询

taskFetch2：输入工具subtitleDynamic输出的traceId即可获得添加了字幕以后的视频地址

6、为视频添加音频

videoAddAudio：为视频添加音频，当音视频时长不一致时，支持以视频时长为准，音频通过裁剪或调整速度与视频对齐，或以音频时长为准，视频通过裁剪或调整速度与音频对其

7、图生视频

imageGenVideo：上传图片，输入提示词，即可生成视频，模型为VIDU

8、图生视频任务结果查询

videoTaskFetch：当图生视频工具imageGenVideo的任务是异步的时，就需要调用该工具查询生成的视频结果

# 三、快速开始

- 在MathMind开放平台注册并获取apikey，立即前往

- SSE 远程调用

## SSE 调用方式

### Windsurf

前往 Windsurf > Settings > Cascade > Add Server > Add custom server 添加配置：


`
{
  "mcpServers": {
    "mcp-server-mathmind": {
      "url": "https://mcp.mathmind.cn/sse?x-api-key=<YOUR_API_KEY>"
    }
  }
}
`


### Cursor

前往 Cursor -> Preferences -> Cursor Settings -> MCP -> Add new global MCP Server 添加配置:

`
{
  "mcpServers": {
    "mcp-server-mathmind": {
      "url": "https://mcp.mathmind.cn/sse?x-api-key=<YOUR_API_KEY>"
    }
  }
}
`

### 通义灵码

前往 通义灵码 -> MCP工具 -> MCP服务 -> 通过配置文件添加新增MCP服务 -> lingma_mcp.json添加以下配置:

`
{
  "mcpServers": {
    "mcp-server-mathmind": {
      "url": "https://mcp.mathmind.cn/sse?x-api-key=<YOUR_API_KEY>"
    }
  }
}
`


# 技术支持

下方添加kk企微，获得技术支持~

<img width="494" height="496" alt="image" src="https://github.com/user-attachments/assets/f53ed106-d378-4347-aa48-91c6968b0bfe" />


--- 
# 快捷入口
- 官网入口：https://mathmind.cn/
- 开放平台：https://admin.mathmind.cn/#/
- 插件市场：https://www.coze.cn/user/829510688450616
- 免费教程：https://mathmind.feishu.cn/wiki/OtIZwYuxbi1ErQkyovmc07HmnOh
- 付费空间：https://mathmind.feishu.cn/wiki/GvW8wyv2VithdnkNsVmcqhVNnYb
- B站视频讲解：https://space.bilibili.com/87911991/channel/seriesdetail?sid=4634704
- 帮助中心：https://mathmind.feishu.cn/docx/Q6eodjvPLoq7yDxZaHOcfnFrntg
- Coze折扣：https://mathmind.feishu.cn/wiki/D9qSwIoaEixfqmkDupuceF62nFg
