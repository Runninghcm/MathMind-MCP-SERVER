
from typing import Annotated

from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_request
from pydantic import Field
from typing import List,Dict
from starlette.requests import Request
from starlette.responses import PlainTextResponse

from .config import SUFFIX
from .tools.imgs2video import Imgs2Video
from .tools.video2video import Video2Video
from .tools.video2text import Video2Text
from .tools.subtitle_dynamic import SubTitleDynamic
from .tools.fetch_task_by_traceId import FetchTask
from .tools.video_cut_random import VideoCutRandom
from .tools.image_gen_video import ImageGenVideo
from .tools.imgPip import ImgPip
from .tools.imgPipTask import ImgPipTask

mcp = FastMCP("mathmind-mcp-server")


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")

# @mcp.tool(name="imageGenVideo")
# def image2video(image_url: Annotated[str, Field(description="图片链接")],
#                 prompt: Annotated[str, Field(description="生成视频的文本提示词")]) -> str:
#     """传入图片链接，生成可以将图片动起来的视频"""
#     request: Request = get_http_request()
#     key = request.query_params.get("x-api-key") or request.headers.get("x-api-key")
#     return image_2_video.image2video(image_url, prompt, key)


# @mcp.tool()
# def get_weather(location: Annotated[str, Field(description="城市名称")]) -> str:
#     """获取指定城市24小时天气预报"""
#     request: Request = get_http_request()
#     key = request.query_params.get("x-api-key") or request.headers.get("x-api-key")
#     try:
#         return weather.get_24h_weather_by_location(location, key)
#     except Exception as e:
#         return f"获取天气信息失败: {str(e)}\n\n{SUFFIX}"


@mcp.tool(name="imgs2video")
def imgs2video( 
                imageUrls:Annotated[List[str],Field(description="图片URL列表")],
                voiceUrl:Annotated[str,Field(description="配音URL (可选,非必填)",default=None)],
                bgmUrl:Annotated[str,Field(description="背景音乐URL (可选，非必填)",default=None)],
                bgmVolume:Annotated[float,Field(description="背景音乐音量(0~100),(可选，非必填)",default=100)],
                # durationPerImage:Annotated[float,Field(description="每张图片显示时长(秒) (可选，非必填)",default=3.0)],
                coverImageUrl:Annotated[str,Field(description="封面图片链接 (可选,非必填) ",default=None)],
                coverImageDuration:Annotated[float,Field(description=" 封面图片展示时长(秒)",default=0.1)],
               ):
    """
    将一张或多张图片合成一个静态的视频，支持添加背景音乐、配音；
    视频时长以配音时长为准，当配音时长小于背景音乐时长时，
    会对背景音乐进行裁剪；当配音时长大于背景音乐时，会将背景音乐复制
    返回的内容是一个JSON结构，其中 traceId 代表任务查询id，videoUrl 代表生成视频地址，downloadUrl代表下载链接
    """
    request: Request = get_http_request()
    x_api_key = request.query_params.get("x-api-key") or request.headers.get("x-api-key")
    # return image_2_video.image2video(image_url, prompt, key)
    print("测试输入参数：",request.query_params)
    results = Imgs2Video()(
        imageUrls=imageUrls,
        voiceUrl=voiceUrl,
        bgmUrl= bgmUrl,
        bgmVolume = bgmVolume,
        # durationPerImage = durationPerImage,
        coverImageUrl = coverImageUrl,
        coverImageDuration = coverImageDuration,
        x_api_key=x_api_key
        )
    return results


@mcp.tool(name="video2video")
def video2video(
    videoFiles:Annotated[List[str],Field(description="视频URL列表")],
    voiceUrl:Annotated[str,Field(description="配音URL(可选,非必填)")]=None,
    bgmUrl:Annotated[str,Field(description="背景音乐URL(可选,非必填)")]=None,
    voiceVolume:Annotated[float,Field(description="配音音量(可选,非必填)")]=None,
    bgmVolume:Annotated[float,Field(description="背景音乐音量(可选,非必填)")]=None,
    headerVideoUrl:Annotated[str,Field(description="片头视频URL(可选,非必填)")]=None,
    footerVideoUrl:Annotated[str,Field(description="片尾视频URL(可选,非必填)")]=None,
    coverImageUrl :Annotated[str,Field(description="封面图片URL(可选,非必填)")]=None,
    coverImageDuration:Annotated[float,Field(description="封面图片时长(可选,非必填)")]=None
    ):
    """
    通过视频素材合成新的视频,将一个或多段视频素材合成一个视频，支持上传背景音乐（非必填）、配音（非必填）合成新的视频。
    支持单独上传首、尾视频，固定视频首尾。支持设置封面图、支持配音音量控制、支持背景音乐自定义音量。
    """
    # - **videoFiles**: 视频URL列表
    # - **voiceUrl**: (可选)配音URL
    # - **bgmUrl**: (可选)背景音乐URL
    # - **voiceVolume**: (可选)配音音量
    # - **bgmVolume**: (可选)背景音乐音量
    # - **headerVideoUrl**: (可选)片头视频URL
    # - **footerVideoUrl**: (可选)片尾视频URL
    # - **coverImageUrl**: (可选)封面图片URL
    # - **coverImageDuration**: (可选)封面图片时长
    request: Request = get_http_request()
    x_api_key = request.query_params.get("x-api-key") or request.headers.get("x-api-key")
    # return image_2_video.image2video(image_url, prompt, key)
    # print("测试输入参数：",request.query_params)
    results = Video2Video()(
        x_api_key = x_api_key,
        videoFiles=videoFiles,
        voiceUrl = voiceUrl,
        bgmUrl = bgmUrl,
        voiceVolume = voiceVolume,
        bgmVolume = bgmVolume,
        headerVideoUrl = headerVideoUrl,
        footerVideoUrl = footerVideoUrl,
        coverImageUrl = coverImageUrl,
        coverImageDuration = coverImageDuration
        )

    # print(results)
    return results
    
    
    
@mcp.tool(name="video2txt")
def video2txt(
    videoUrl:Annotated[str,Field(default="视频链接地址")]
):
    """
    提取用户提供的视频链接地址对应视频中的文案，用户输入视频链接即可。建议上传5分钟以下的视频.
    """
    request: Request = get_http_request()
    print(request.query_params.items())
    x_api_key = request.query_params.get("x-api-key") or request.headers.get("x-api-key")
    results = Video2Text()(x_api_key=x_api_key,videoUrl=videoUrl)
    return results


@mcp.tool(name="subtitleDynamic")
def subtitleDynamic(
    videoUrl:Annotated[str,Field(description="需要转换为字幕的视频URL")],
    fontSize:Annotated[str,Field(description="字体大小（可选、非必填）")]=None,
    primaryColor:Annotated[str,Field(description="字体颜色（可选、非必填）")]=None,
    marginV :Annotated[str,Field(description="垂直边距（可选、非必填）")]=None,
    text:Annotated[str,Field(description=" 字幕文本（可选、非必填）")]=None,
    isFontAuto:Annotated[int,Field(description="是否自动调整字体大小，1自适应，0不自适应（可选、非必填）")]=None,
    isFontBold:Annotated[int,Field(description="是否加粗，1为加粗，0为不加粗，1自适应，0不自适应（可选、非必填）")]=None,
    textStrokeColor:Annotated[str,Field(description="描边颜色（可选、非必填）")]=None,
    textStrokeWidth:Annotated[str,Field(description="描边宽度（可选、非必填）")]=None,
    selectFont :Annotated[int,Field(description="选择字体编码，从1开始（可选、非必填）")]=None,
    textBgColor:Annotated[str,Field(description="字幕背景颜色（可选、非必填）")]=None,
):
    """
    根据输入的视频地址,给视频添加字幕。如果原视频没有字幕，本接口可以自动识别视频中音频文字内容（无需调用其他接口提取视频中的文字内容），并将输出添加到视频上，形成带字幕的视频。
    如果用户同时输入了字幕文本，以提供的文本作为参考，从而提升字幕文本的准确性，形成带字幕的视频。
    字幕支持设置字体与位置等。支持传入text文本。
    返回的内容是一个JSON结构，其中 taskID 代表任务查询id,traceId 任务跟踪id 
    注意：只需要返回接口内容，无需主动调用任务查询接口
    """
    
    # videoUrl: str = Field(..., description="需要转换为字幕的视频URL")
    # fontSize: Optional[str] = Field(None, description="字体大小")
    # primaryColor: Optional[str] = Field(None, description="字体颜色")
    # marginV: Optional[str] = Field(None, description="垂直边距")
    # text: Optional[str] = Field(None, description="字幕文本")
    # isFontAuto: Optional[int] = Field(None, description="是否自动调整字体大小，1自适应，0不自适应")
    # isFontBold: Optional[int] = Field(None, description="是否加粗，1为加粗，0为不加粗")
    # textStrokeColor: Optional[str] = Field(None, description="描边颜色")
    # textStrokeWidth: Optional[str] = Field(None, description="描边宽度")
    # selectFont: Optional[int] = Field(None, description="选择字体编码，从1开始")
    # textBgColor: Optional[str] = Field(None, description="字幕背景颜色")
    
    # - **videoUrl**: 需要转换为字幕的视频URL
    # - **fontSize**: 字体大小
    # - **primaryColor**: 字体颜色
    # - **marginV**: 垂直边距
    # - **text**: 字幕文本
    # - **isFontAuto**: 是否自动调整字体大小，1自适应，0不自适应
    # - **isFontBold**: 是否加粗，1为加粗，0为不加粗
    # - **textStrokeColor**: 描边颜色
    # - **textStrokeWidth**: 描边宽度
    # - **selectFont**: 选择字体编码，从1开始
    # - **textBgColor**: 字幕背景颜色
    # - **x_api_key**: API密钥，用于验证用户身份和权限
    request: Request = get_http_request()
    # print(request.query_params.items())
    x_api_key = request.query_params.get("x-api-key") or request.headers.get("x-api-key")
    results = SubTitleDynamic()(
        x_api_key=x_api_key,
        videoUrl=videoUrl,
        fontSize=fontSize,
        primaryColor=primaryColor,
        marginV=marginV,
        text=text,
        isFontAuto=isFontAuto,
        isFontBold=isFontBold,
        textStrokeColor=textStrokeColor,
        textStrokeWidth=textStrokeWidth,
        selectFont=selectFont,
        textBgColor=textBgColor
        
    )
    return results


@mcp.tool(name="taskFetchByTraceID")
def taskFetch2(
    traceId=Annotated[str,Field(description="任务跟踪ID")]
):
    """
    根据用户已经提交过的任务 traceId 查询提交的任务结果
    """
    # 4750d221-a58a-441c-9345-a215f1126b8e
    
    request: Request = get_http_request()
    # print(request.query_params.items())
    x_api_key = request.query_params.get("x-api-key") or request.headers.get("x-api-key")
    results = FetchTask()(
        x_api_key=x_api_key,
        traceId=traceId
    )
    return str(results)


@mcp.tool(name="videoCutRandom")
def videoCutRandom(
    videoUrl:Annotated[str,Field(description="视频URL地址")],
    startPlace:Annotated[float,Field(description="裁剪视频的起始位置，时长的百分比",default=0,ge=0,le=100)]=None,
    endPlace:Annotated[float,Field(description="裁剪视频的结束位置，时长的百分比",default=100,ge=0,le=100)]=None,
):
    """
    输入视频链接，输入截取的起始和结束位置，即可截取位置获得对应的视频片段
    """
    # - **videoUrl**: 视频URL
    #         - **startPlace**: 开始位置(0-100)
    #         - **endPlace**: 结束位置(0-100)
    # VideoCutRandom
    request: Request = get_http_request()
    # print(request.query_params.items())
    x_api_key = request.query_params.get("x-api-key") or request.headers.get("x-api-key")
    results = VideoCutRandom()(
        x_api_key=x_api_key,
        videoUrl=videoUrl,
        startPlace=startPlace,
        endPlace=endPlace
    )
    return results



@mcp.tool(name="imageGenVideo")
def image2video(imageUrl: Annotated[str, Field(description="图片链接地址")],
                prompt: Annotated[str, Field(description="生成视频的文本提示词（非必填）")]=None) -> str:
    
    """基于传入的单张图片链接，将图片里面的内容通过图生视频的模型生成可以动起来的视频
    将接口返回的JSON内容输出即可,其中 traceId 任务跟踪id
    注意：只需要返回接口 traceId 内容，无需主动调用任务查询接口
    """
    request: Request = get_http_request()
    x_api_key = request.query_params.get("x-api-key") or request.headers.get("x-api-key")
    
    results = ImageGenVideo()(
        imageUrl = imageUrl,
        prompt = prompt,
        x_api_key = x_api_key
        
    )
    return results


@mcp.tool(name="imgPip")
def imgpip(
        videoUrl:Annotated[str,Field(description="视频链接地址")],
        mUrl :Annotated[str,Field(description="图片素材链接地址")],
        mStartTime :Annotated[int,Field(description="素材出现时间（可选、非必填）")]=None,
        mDuration :Annotated[float,Field(description="素材持续时间（可选、非必填）")]=None,
        mXY :Annotated[list[int],Field(description="素材坐标（可选、非必填）")]=None,
        Width :Annotated[int,Field(description="资源在输出视频画布上的宽度，单位为 pixel。（可选、非必填）")]=None,
        Height :Annotated[int,Field(description="资源在输出视频画布上的高度，单位为 pixel。（可选、非必填）")]=None,
        mEntrAnimo :Annotated[str,Field(description="入场动画id（可选、非必填）")]=None,
        mEntrAniDuration :Annotated[float,Field(description="入场动画持续时间（可选、非必填）")]=None,
        mExitAnimo :Annotated[str,Field(description="出场动画id（可选、非必填）")]=None,
        mExitAniDuration:Annotated[float,Field(description="出场动画持续时间（可选、非必填）")]=None,
    
    ) -> str:
    
    """
    视频中添加画中画，通过用户提供的在线图片链接将图片以画中画的方式插入到视频中进行合成。比如添加logo等
    将接口返回的JSON内容输出即可,其中 traceId 表示任务跟踪id。
    注意：只需要返回接口内容，无需主动调用任务查询接口
    """

        # videoUrl: str = Field(..., description="视频地址")
        # mUrl: str = Field(..., description="素材视频地址")
        # mStartTime: int = Field(None, description="素材出现时间")
        # mDuration: float = Field(None, description="素材持续时间")
        # mXY: list[int]= Field(None, description="素材坐标")
        # Width: int = Field(None, description="资源在输出视频画布上的宽度，单位为 pixel。")
        # Height: int = Field(None, description="资源在输出视频画布上的高度，单位为 pixel。")
        # mEntrAnimo:str = Field(None, description="入场动画id")
        # mEntrAniDuration:float = Field(1, description="入场动画持续时间")
        # mExitAnimo: str = Field(None, description="出场id")
        # mExitAniDuration:float = Field(1, description="出场动画持续时间")
    
    
    request: Request = get_http_request()
    x_api_key = request.query_params.get("x-api-key") or request.headers.get("x-api-key")
    
    results = ImgPip()(
        videoUrl=videoUrl,
        mUrl = mUrl,
        mStartTime =mStartTime,
        mDuration = mDuration,
        mXY = mXY,
        Width = Width,
        Height = Height,
        mEntrAnimo = mEntrAnimo,
        mEntrAniDuration = mEntrAniDuration,
        mExitAnimo = mExitAnimo,
        mExitAniDuration = mExitAniDuration,
        x_api_key = x_api_key
        
    )
    return str(results)


@mcp.tool(name="imgPipTaskFetchbyReqID")
def imgPipTaskFetch(req_id: Annotated[str, Field(description="imgPip 视频画中画任务返回的req_id")]) -> str:
    
    """根据用户输入的req_id来查询 视频中添加画中画功能的任务结果。
    将接口返回的JSON内容输出即可
    """
    
            
    request: Request = get_http_request()
    x_api_key = request.query_params.get("x-api-key") or request.headers.get("x-api-key")
    
    results = ImgPipTask()(
        req_id = req_id,
        x_api_key = x_api_key
        
    )
    return str(results)

def main():
    print("start mcp server !")
    mcp.run(transport="sse", host="0.0.0.0", port=8000)
    # mcp.run(transport="stdio")

if __name__ == '__main__':
    main()
    # mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
