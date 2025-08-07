import requests

from . import SUFFIX


def image2video(image_url: str, prompt: str, api_key: str) -> str:
    if not api_key:
        return f"未获取到有效的API密钥，请在请求头或请求参数中添加 x-api-key\n\n{SUFFIX}"

    url = "https://agent.mathmind.cn/minimalist/api/imageToVideo/createImage2Video"
    body = {
        "imageUrl": image_url,
        "prompt": prompt,
        "async": True,
    }
    headers = {
        "x-api-key": api_key
    }
    response = requests.post(url, json=body, headers=headers)
    if response.status_code != 200:
        return f'''# 请求失败
- 状态码：{response.status_code}
- 错误信息：{response.text}

{SUFFIX}'''

    data = response.json()
    if data.get("code") != 0:
        return f'''# 请求失败
- 错误信息：{data.get("errorMessage")}

{SUFFIX}'''

    download_url = data.get("downloadUrl")
    return f'''# 视频生成成功
- [视频下载链接]({download_url})

{SUFFIX}'''
