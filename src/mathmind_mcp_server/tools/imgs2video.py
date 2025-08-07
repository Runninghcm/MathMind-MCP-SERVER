import os 
import sys 
import requests
from mathmind_mcp_server.config import BASE_URL,SUFFIX,TEST_API_KEY
from mathmind_mcp_server.util import remove_about_url

class Imgs2Video:
    def __init__(self):
        self.url = f"{BASE_URL}/minimalist/api/video/generate"
    
    
    def __call__(self, *args, **kwds):
        """
            将多张图片转换为视频（简单版本）
            
            - **imageUrls**: 图片URL列表
            - **voiceUrl**: 配音URL (可选)
            - **bgmUrl**: 背景音乐URL (可选)
            - **bgmVolume**: 背景音乐音量(0~100)
            - **durationPerImage**: 每张图片显示时长(秒)
            - **coverImageUrl**: 封面图片链接 (可选)
            - **coverImageDuration**: 封面图片展示时长(秒)
            - **x_api_key**: API密钥 (可选)
            
            Returns:
                VideoGenerateResponse: 生成的视频信息
        """
        
        
        # api_key = kwds.get("api_key",None)
        imageUrls = kwds.get("imageUrls")
        voiceUrl = kwds.get("voiceUrl")
        bgmUrl = kwds.get("bgmUrl")
        bgmVolume = kwds.get("bgmVolume",100.0)
        # durationPerImage = kwds.get("durationPerImage",3.0)
        coverImageUrl = kwds.get("coverImageUrl")
        coverImageDuration = kwds.get("coverImageDuration",0.1)
        x_api_key = kwds.get("x_api_key")
        
        
        if not x_api_key:
            return f"未获取到有效的API密钥，请在请求头或请求参数中添加 x-api-key\n\n{SUFFIX}"

        url = self.url
        body = {
            "imageUrls": imageUrls,
            "voiceUrl": voiceUrl,
            "bgmUrl":bgmUrl,
            "bgmVolume":bgmVolume,
            # "durationPerImage":durationPerImage,
            "coverImageUrl":coverImageUrl,
            "coverImageDuration":coverImageDuration
        }
        headers = {
            "x-api-key": x_api_key
        }
        response = requests.post(url, json=body, headers=headers)
        if response.status_code != 200:
            return {"code":403,"msg":"接口调用不成功!"}
    
        return remove_about_url(response.json())

if __name__ == "__main__":
    imageUrls = ["https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg","https://pics0.baidu.com/feed/cc11728b4710b912b98c0b8a85f0b50d92452214.jpeg"]
    
    x_api_key = TEST_API_KEY
    res = Imgs2Video()(imageUrls=imageUrls,x_api_key=x_api_key)
    print(res)
    

