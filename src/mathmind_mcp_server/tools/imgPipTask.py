import os 
import sys 
import requests
from mathmind_mcp_server.config import BASE_URL,SUFFIX,TEST_API_KEY
from mathmind_mcp_server.util import remove_about_url

class ImgPipTask:
    def __init__(self):
        self.url = f"{BASE_URL}/minimalist/api/volcengine/video/task/detail"
    
    
    def __call__(self, *args, **kwds):
        """
            视频中添加画中画，通过上传的图片插入到视频中进行合成的任务结果进行查询
            
            - **req_id**: 任务id
            - **x_api_key**: API密钥 (可选)
            
            Returns:
                VideoGenerateResponse: 生成的视频信息
        """
        
        
        # api_key = kwds.get("api_key",None)
        req_id = kwds.get("req_id")

        print("req_id:",req_id)
        x_api_key = kwds.get("x_api_key")
        
        
        if not x_api_key:
            return f"未获取到有效的API密钥，请在请求头或请求参数中添加 x-api-key\n\n{SUFFIX}"

        url = self.url
        body = {
            "req_id":req_id,
        }
        headers = {
            "x-api-key": x_api_key
        }
        response = requests.post(url, params=body, headers=headers)
        # response = requests.get(url,headers=headers)
        if response.status_code != 200:
            return {"code":403,"msg":"接口调用不成功!"}
    
        return remove_about_url(response.json())

if __name__ == "__main__":
    # videoUrl = "https://mathmind-files.oss-cn-beijing.aliyuncs.com/videos/CaptionedVideo-1753884180324.mp4"
    # mUrl = "https://static-cse.canva.cn/blob/350295/1.png"
    
    req_id = "e0102cd5802645d7a7f327f194678e19"
    x_api_key = TEST_API_KEY
    res = ImgPipTask()(
        req_id = req_id,
        x_api_key=x_api_key
    )
    print(res)
    
    
    #{'code': 0, 'errorMessage': '', 
    # 'data': {'ReqId': 'e0102cd5802645d7a7f327f194678e19', 'Duration': 23}, 
    # 'aboutUrl': 'https://mathmind.feishu.cn/docx/Q6eodjvPLoq7yDxZaHOcfnFrntg'}

