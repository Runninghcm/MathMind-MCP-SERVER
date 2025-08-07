import os 
import sys 
from mathmind_mcp_server.config import BASE_URL,SUFFIX,TEST_API_KEY
import requests
from mathmind_mcp_server.util import remove_about_url

class Video2Text:
    def __init__(self):
        self.url = f"{BASE_URL}/minimalist/api/video-audio/recognize"
    
    
    def __call__(self, *args, **kwds):
        
        #     通过videoUrl输入视频链接，可识别并提取文案
    
        # - **videoUrl**: 视频URL，支持本地文件路径或远程链接（如抖音链接）
        
        x_api_key  = kwds.get("x_api_key")
        videoUrl = kwds.get("videoUrl")
        
        
        headers = {
        "x-api-key": x_api_key
        }
        body = dict(
            videoUrl=videoUrl)
        
        # print(body)
        response = requests.post(self.url, json=body, headers=headers)
        if response.status_code != 200:
            return {"code":403,"msg":"接口调用不成功!","error":response.content}
    
        return remove_about_url(response.json())
        
        
        
if __name__ == "__main__":
    
    videoUrl = "https://cdn-hsy-ai-center.chanjing.cc/chanjing/prod/dhaio/output/2025-06-15/1934258430147559424-1749998139-output.mp4"
    
    res = Video2Text()(videoUrl=videoUrl,x_api_key=TEST_API_KEY)
    print(res)
        
        
        
        
        
        