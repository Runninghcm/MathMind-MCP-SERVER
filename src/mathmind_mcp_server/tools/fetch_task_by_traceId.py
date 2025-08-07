import os 
import sys 
from mathmind_mcp_server.config import BASE_URL,SUFFIX,TEST_API_KEY
import requests
from mathmind_mcp_server.util import remove_about_url

class FetchTask:
    def __init__(self):
        self.url = f"{BASE_URL}//minimalist/api/task/"
    
    
    def __call__(self, *args, **kwds):
        
        #     通过videoUrl输入视频链接，可识别并提取文案
    
        # - **videoUrl**: 视频URL，支持本地文件路径或远程链接（如抖音链接）
        
        x_api_key  = kwds.get("x_api_key")
        traceId = kwds.get("traceId")
        
        headers = {
        "x-api-key": x_api_key
        }

        
        # print(body)
        url = self.url + traceId
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return {"code":403,"msg":"接口调用不成功!","error":response.content}
    
        return remove_about_url(response.json())
        
        
        
if __name__ == "__main__":
    
    # traceId = "4750d221-a58a-441c-9345-a215f1126b8e"
    traceId = "412ea335-477b-483f-a057-e731f882f4d3"
    
    res = FetchTask()(traceId=traceId,x_api_key=TEST_API_KEY)
    print(res)
        
        
        
        
        