import os 
import sys 
from mathmind_mcp_server.config import BASE_URL,SUFFIX,TEST_API_KEY
import requests
from mathmind_mcp_server.util import remove_about_url

class ImageGenVideo:
    def __init__(self):
        self.url = f"{BASE_URL}/minimalist/api/image-to-video/vira/createImage2Video"
    
    def __call__(self, *args, **kwds):
        
        """
            通过单张图片生成视频 (兼容旧版路径)
            
            - **model**: 模型名称
            - **imageUrl**: 图片URL
            - **duration**: 视频时长(秒)，只能是4或8
            - **resolution**: 分辨率，如720p
            - **movementAmplitude**: 动画幅度，auto/small/medium/large
            - **prompt**: 提示词
            - **async**: 是否异步执行
            - **fileName**: 文件名
            """
        x_api_key  = kwds.get("x_api_key")
        imageUrl = kwds.get("imageUrl")
        prompt = kwds.get("prompt")
        # async_flag = kwds.get("async")
        duration = kwds.get("duration",4)
        resolution = kwds.get("resolution","720p")
        movementAmplitude = kwds.get("movementAmplitude","auto")
        fileName = kwds.get("fileName")
        
        body = {
            "imageUrl" :imageUrl,
            "prompt" : prompt,
            "async":True,
            "duration":duration,
            "movementAmplitude":movementAmplitude,
            "fileName":fileName,
            "resolution":resolution
        }
        
        headers = {
        "x-api-key": x_api_key
        }
     
        # print(body)
        response = requests.post(self.url, json=body, headers=headers)
        if response.status_code != 200:
            return {"code":403,"msg":"接口调用不成功!","error":response.content}
    
        return  str(remove_about_url(response.json()))
        
        
if __name__ == "__main__":
    
    imageUrl = "https://cdn.pixabay.com/photo/2025/04/30/13/05/cat-9569386_1280.jpg"
    prompt = "图片中的小猫正在和他的朋友们在麦当劳里一起喝咖啡。"
    
    res = ImageGenVideo()(imageUrl=imageUrl,
                          prompt = prompt,
                          x_api_key=TEST_API_KEY)
    print(res)
        
        
        
        
        
        