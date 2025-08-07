import os 
import sys 
import requests
from mathmind_mcp_server.config import BASE_URL,SUFFIX,TEST_API_KEY
from mathmind_mcp_server.util import remove_about_url

class ImgPip:
    def __init__(self):
        self.url = f"{BASE_URL}/minimalist/api/volcengine/video/merge/img"
    
    
    def __call__(self, *args, **kwds):
        """
            视频中添加画中画，通过上传的图片插入到视频中进行合成。
            
            - **voiceUrl**: 视频素材地址
            - **mUrl**: 图片素材地址
            
            videoUrl: str = Field(..., description="视频地址")
            mUrl: str = Field(..., description="素材视频地址")
            mStartTime: int = Field(None, description="素材出现时间")
            mDuration: float = Field(None, description="素材持续时间")
            mXY: list[int]= Field(None, description="素材坐标")
            Width: int = Field(None, description="资源在输出视频画布上的宽度，单位为 pixel。")
            Height: int = Field(None, description="资源在输出视频画布上的高度，单位为 pixel。")
            mEntrAnimo:str = Field(None, description="入场动画id")
            mEntrAniDuration:float = Field(1, description="入场动画持续时间")
            mExitAnimo: str = Field(None, description="出场id")
            mExitAniDuration:float = Field(1, description="出场动画持续时间")
            - **x_api_key**: API密钥 (可选)
            Returns:
                VideoGenerateResponse: 生成的视频信息
        """
        
        
        # api_key = kwds.get("api_key",None)
        videoUrl = kwds.get("videoUrl")
        mUrl = kwds.get("mUrl")
        mStartTime = int(kwds.get("mStartTime",0))
        mDuration = float(kwds.get("mDuration"),4)
        mXY = kwds.get("mXY")
        Width = kwds.get("Width")
        Height = kwds.get("Height")
        mEntrAnimo = kwds.get("mEntrAnimo")
        mEntrAniDuration = kwds.get("mEntrAniDuration")
        mExitAnimo = kwds.get("mExitAnimo")
        mExitAniDuration = kwds.get("mExitAniDuration")
        
        x_api_key = kwds.get("x_api_key")
        
        
        if not x_api_key:
            return f"未获取到有效的API密钥，请在请求头或请求参数中添加 x-api-key\n\n{SUFFIX}"

        url = self.url
        body = {
            "videoUrl":videoUrl,
            "mUrl":mUrl,
            "mStartTime":mStartTime,
            "mDuration":mDuration,
            "mXY":mXY,
            "Width":Width,
            "Height":Height,
            "mEntrAnimo":mEntrAnimo,
            "mEntrAniDuration":mEntrAniDuration,
            "mExitAnimo":mExitAnimo,
            "mExitAniDuration":mExitAniDuration
        }
        headers = {
            "x-api-key": x_api_key
        }
        response = requests.post(url, json=body, headers=headers)
        if response.status_code != 200:
            return {"code":403,"msg":"接口调用不成功!"}
    
        return remove_about_url(response.json())

if __name__ == "__main__":
    videoUrl = "https://mathmind-files.oss-cn-beijing.aliyuncs.com/videos/CaptionedVideo-1753884180324.mp4"
    mUrl = "https://static-cse.canva.cn/blob/350295/1.png"
    
    x_api_key = TEST_API_KEY
    res = ImgPip()(
        videoUrl=videoUrl,
        mUrl = mUrl,
        x_api_key=x_api_key
    )
    print(res)
    
    
    #{'code': 0, 'errorMessage': '', 
    # 'data': {'ReqId': 'e0102cd5802645d7a7f327f194678e19', 'Duration': 23}, 
    # 'aboutUrl': 'https://mathmind.feishu.cn/docx/Q6eodjvPLoq7yDxZaHOcfnFrntg'}

