from flask import Flask, request, jsonify, Response
import requests
import json

app = Flask(__name__)

def SendGradioRequest(speaker,text,speed):
    url = "https://v2.genshinvoice.top/run/predict"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5",
        "Content-Type": "application/json",
        "Cookie": "_ga_R1FN4KJKJH=GS1.1.1709167755.1.0.1709167755.0.0.0; _ga=GA1.2.351420634.1709167755; _gid=GA1.2.2091734624.1709167755",
        "Origin": "https://v2.genshinvoice.top",
        "Referer": "https://v2.genshinvoice.top/?",
        "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    }
    data = {
        "data": [
            text,
            speaker,
            0.5,
            0.6,
            0.9,
            speed,
            "ZH",
            None,
            "Happy",
            "Text prompt",
            "",
            0.7
        ],
        "event_data": None,
        "fn_index": 0,
        "session_hash": "7nc3pp547su"
    }
    response = requests.post(url, json=data, headers=headers)

    # 检查响应状态码
    if response.status_code == 200:
        print("请求成功！")
        print(response.text)
        data = json.loads(response.text)
        return data["data"][1]["name"]
        
    else:
        print(f"请求失败，状态码：{response.status_code}")
        print(response)
    return response.status_code
def GetGradioAudio(path):
    url = "https://v2.genshinvoice.top/file="+path
    headers = {
    "Content-Type": "application/json",
    # 添加其他需要的头部信息
    }
    response = requests.get(url) 
    if response.status_code == 200:
        print("请求成功！")
        return response.content
    else:
        print(f"请求失败，状态码：{response.status_code}")
        return response.content

@app.route('/TTSapi', methods=['GET'])
def TTSapi():
    speaker = request.args.get('speaker',"派蒙_ZH")
    text = request.args.get('text',"你的请求中没有文本参数")
    speed = request.args.get('speed',1)
    volume =request.args.get("volume",1)

    path = SendGradioRequest(speaker,text,speed)
    audioData=GetGradioAudio(path)
    return Response(audioData,content_type='audio/x-wav')



if __name__ == '__main__':
    app.run(host="160.251.179.81",port = "8090")       




# 派蒙_ZH, 纳西妲_ZH, 凯亚_ZH, 温迪_ZH, 荒泷一斗_ZH, 娜维娅_ZH, 阿贝多_ZH, 钟离_ZH,
# 枫原万叶_ZH, 那维莱特_ZH, 艾尔海森_ZH, 八重神子_ZH, 宵宫_ZH, 芙宁娜_ZH, 迪希雅_ZH,
# 提纳里_ZH, 莱依拉_ZH, 卡维_ZH, 诺艾尔_ZH, 赛诺_ZH, 林尼_ZH, 莫娜_ZH, 托马_ZH,
# 神里绫华_ZH, 凝光_ZH, 北斗_ZH, 可莉_ZH, 柯莱_ZH, 迪奥娜_ZH, 莱欧斯利_ZH, 芭芭拉_ZH,
# 雷电将军_ZH, 珊瑚宫心海_ZH, 魈_ZH, 五郎_ZH, 胡桃_ZH, 鹿野院平藏_ZH, 安柏_ZH, 琴_ZH,
# 重云_ZH, 达达利亚_ZH, 班尼特_ZH, 夜兰_ZH, 丽莎_ZH, 香菱_ZH, 妮露_ZH, 刻晴_ZH, 珐露珊_ZH,
# 烟绯_ZH, 辛焱_ZH, 早柚_ZH, 迪卢克_ZH, 砂糖_ZH, 云堇_ZH, 久岐忍_ZH, 神里绫人_ZH, 优菈_ZH,
# 甘雨_ZH, 夏洛蒂_ZH, 流浪者_ZH, 行秋_ZH, 夏沃蕾_ZH, 戴因斯雷布_ZH, 闲云_ZH, 白术_ZH, 菲谢尔_ZH,
# 申鹤_ZH, 九条裟罗_ZH, 雷泽_ZH, 荧_ZH, 空_ZH, 嘉明_ZH, 菲米尼_ZH, 多莉_ZH, 迪娜泽黛_ZH,
# 琳妮特_ZH, 凯瑟琳_ZH, 米卡_ZH, 坎蒂丝_ZH, 萍姥姥_ZH, 罗莎莉亚_ZH, 埃德_ZH, 爱贝尔_ZH, 
# 伊迪娅_ZH, 留云借风真君_ZH, 瑶瑶_ZH, 绮良良_ZH, 七七_ZH, 式大将_ZH, 奥兹_ZH, 泽维尔_ZH
# 哲平_ZH, 大肉丸_ZH, 托克_ZH, 蒂玛乌斯_ZH, 昆钧_ZH, 欧菲妮_ZH, 仆人_ZH, 塞琉斯_ZH, 言笑_ZH,
# 迈勒斯_ZH, 希格雯_ZH, 拉赫曼_ZH, 阿守_ZH, 杜拉夫_ZH, 阿晃_ZH, 旁白_ZH, 克洛琳德_ZH,
# 伊利亚斯_ZH, 爱德琳_ZH, 埃洛伊_ZH, 远黛_ZH, 德沃沙克_ZH, 玛乔丽_ZH, 劳维克_ZH, 塞塔蕾_ZH,
# 海芭夏_ZH, 九条镰治_ZH, 柊千里_ZH, 阿娜耶_ZH, 千织_ZH, 笼钓瓶一心_ZH, 回声海螺_ZH, 叶德_ZH,
# 卡莉露_ZH, 元太_ZH, 漱玉_ZH, 阿扎尔_ZH, 查尔斯_ZH, 阿洛瓦_ZH, 纳比尔_ZH, 莎拉_ZH, 迪尔菲_ZH,
# 康纳_ZH, 博来_ZH, 博士_ZH, 玛塞勒_ZH, 阿祇_ZH, 玛格丽特_ZH, 埃勒曼_ZH, 羽生田千鹤_ZH, 宛烟_ZH,
# 海妮耶_ZH, 科尔特_ZH, 霍夫曼_ZH, 一心传名刀_ZH, 弗洛朗_ZH, 佐西摩斯_ZH, 鹿野奈奈_ZH, 舒伯特_ZH,
# 天叔_ZH, 艾莉丝_ZH, 龙二_ZH, 芙卡洛斯_ZH, 莺儿_ZH, 嘉良_ZH, 珊瑚_ZH, 费迪南德_ZH,
# 祖莉亚·德斯特雷_ZH, 久利须_ZH, 嘉玛_ZH, 艾文_ZH, 女士_ZH, 丹吉尔_ZH, 天目十五_ZH,
# 白老先生_ZH, 老孟_ZH, 巴达维_ZH, 长生_ZH, 拉齐_ZH, 吴船长_ZH, 波洛_ZH, 艾伯特_ZH