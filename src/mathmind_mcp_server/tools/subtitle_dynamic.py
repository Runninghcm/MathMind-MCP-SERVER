import os 
import sys 
from mathmind_mcp_server.config import BASE_URL,SUFFIX,TEST_API_KEY
import requests
from mathmind_mcp_server.util import remove_about_url

class SubTitleDynamic:
    def __init__(self):
        self.url = f"{BASE_URL}/minimalist/api/audio/subtitle-dynamic"
    
    
    def __call__(self, *args, **kwds):
        
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
        
        x_api_key  = kwds.get("x_api_key")
        videoUrl = kwds.get("videoUrl")
        fontSize = kwds.get("fontSize")
        primaryColor = kwds.get("primaryColor")
        marginV = kwds.get("marginV")
        text = kwds.get("text")
        isFontAuto = kwds.get("isFontAuto")
        textStrokeColor = kwds.get("textStrokeColor")
        textStrokeWidth = kwds.get("textStrokeWidth")
        selectFont = kwds.get("selectFont")
        textBgColor = kwds.get("textBgColor")
        
        
        
        headers = {
        "x-api-key": x_api_key
        }
        body = dict(
            videoUrl = videoUrl,
            fontSize = fontSize,
            primaryColor = primaryColor,
            marginV = marginV,
            text = text,
            isFontAuto = isFontAuto,
            textStrokeColor = textStrokeColor,
            textStrokeWidth = textStrokeWidth,
            selectFont =selectFont,
            textBgColor=textBgColor
            )
        
        # print(body)
        response = requests.post(self.url, json=body, headers=headers)
        if response.status_code != 200:
            return {"code":403,"msg":"接口调用不成功!","error":response.content}
    
        return remove_about_url(response.json())
        
        
        
if __name__ == "__main__":
    
    videoUrl=  "https://cdn-hsy-ai-center.chanjing.cc/chanjing/prod/dhaio/output/2025-06-15/1934258430147559424-1749998139-output.mp4"
    res = SubTitleDynamic()(
        x_api_key = TEST_API_KEY,
        videoUrl = videoUrl
    )
    
    print(res)
        
        
        
        
        