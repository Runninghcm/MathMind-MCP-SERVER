import os 
import sys 
import requests
from mathmind_mcp_server.config import BASE_URL,SUFFIX,TEST_API_KEY
from mathmind_mcp_server.util import remove_about_url

class VideoCutRandom:
    def __init__(self):
        self.url = f"{BASE_URL}/minimalist/api/video/cut"
    
    
    def __call__(self, *args, **kwds):
        """
            - **videoUrl**: 视频URL
            - **startPlace**: 开始位置(0-100)
            - **endPlace**: 结束位置(0-100)
        """
        
        
        # api_key = kwds.get("api_key",None)
        videoUrl = kwds.get("videoUrl")
        startPlace = kwds.get("startPlace")
        endPlace = kwds.get("endPlace")
        x_api_key = kwds.get("x_api_key")
        
        
        if not x_api_key:
            return f"未获取到有效的API密钥，请在请求头或请求参数中添加 x-api-key\n\n{SUFFIX}"

        url = self.url
        body = dict(
            videoUrl=videoUrl,
            startPlace=startPlace,
            endPlace=endPlace
        )
        headers = {
            "x-api-key": x_api_key
        }
        response = requests.post(url, json=body, headers=headers)
        if response.status_code != 200:
            return {"code":403,"msg":"接口调用不成功!"}
    
        return remove_about_url(response.json())

if __name__ == "__main__":
    
    videoUrl = "https://mathmind-files.oss-cn-beijing.aliyuncs.com/videos/CaptionedVideo-1753884180324.mp4"
    x_api_key = TEST_API_KEY
    startPlace = 20
    endPlace = 80
    res = VideoCutRandom()(videoUrl=videoUrl,
                           startPlace = startPlace,
                           endPlace = endPlace,
                           x_api_key=x_api_key)
    print(res)
    

