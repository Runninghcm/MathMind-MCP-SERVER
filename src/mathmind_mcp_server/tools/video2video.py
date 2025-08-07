import os 
import sys 
from mathmind_mcp_server.config import BASE_URL,SUFFIX,TEST_API_KEY
import requests
from mathmind_mcp_server.util import remove_about_url

class Video2Video:
    def __init__(self):
        self.url = f"{BASE_URL}/minimalist/api/video/concat"
    
    
    def __call__(self, *args, **kwds):
        
        # - **videoFiles**: 视频URL列表
        # - **voiceUrl**: (可选)配音URL
        # - **bgmUrl**: (可选)背景音乐URL
        # - **voiceVolume**: (可选)配音音量
        # - **bgmVolume**: (可选)背景音乐音量
        # - **headerVideoUrl**: (可选)片头视频URL
        # - **footerVideoUrl**: (可选)片尾视频URL
        # - **coverImageUrl**: (可选)封面图片URL
        # - **coverImageDuration**: (可选)封面图片时长
        
        x_api_key  = kwds.get("x_api_key")
        videoFiles = kwds.get("videoFiles",[])
        voiceUrl = kwds.get("voiceUrl")
        bgmUrl = kwds.get("bgmUrl")
        voiceVolume = kwds.get("voiceVolume",100)
        bgmVolume = kwds.get("bgmVolume",100)
        headerVideoUrl = kwds.get("headerVideoUrl")
        footerVideoUrl = kwds.get("footerVideoUrl")
        coverImageUrl = kwds.get("coverImageUrl")
        coverImageDuration = kwds.get("coverImageDuration",0.1)
        
        
        headers = {
        "x-api-key": x_api_key
        }
        body = dict(
            videoFiles=videoFiles,
            voiceUrl = voiceUrl,
            bgmUrl = bgmUrl,
            voiceVolume = voiceVolume,
            bgmVolume = bgmVolume,
            headerVideoUrl = headerVideoUrl,
            footerVideoUrl = footerVideoUrl,
            coverImageUrl = coverImageUrl,
            coverImageDuration = coverImageDuration)
        
        # print(body)
        response = requests.post(self.url, json=body, headers=headers)
        if response.status_code != 200:
            return {"code":403,"msg":"接口调用不成功!","error":response.content}
    
        return remove_about_url(response.json())
        
        
        
if __name__ == "__main__":
    
    videoFiles= ["https://www.w3schools.com/html/movie.mp4","http://www.w3school.com.cn/example/html5/mov_bbb.mp4"]
    voiceUrl =  None #"http://downsc.chinaz.net/Files/DownLoad/sound1/201906/11582.mp3"
    bgmUrl = None
    voiceVolume = 100
    bgmVolume = 100
    headerVideoUrl = None
    footerVideoUrl = None
    coverImageUrl = None
    coverImageDuration = 0.1
    res = Video2Video()(
        x_api_key = TEST_API_KEY,
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
    
    print(res)
        
        
        
        
        
        