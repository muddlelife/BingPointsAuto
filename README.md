# BingPointsAuto
利用edge浏览器自动获取bing搜索引擎积分

# 步骤

## 方案一(exe执行)

前提：需要在edge浏览器中登陆bing的账号

### 1. 先找到本地环境Edge浏览器版本号对应的 msedgedriver
msedgedriver [下载地址](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads)

### 2. 将解压后的 msedgedriver 放入main.exe 目录中，双击点击运行即可

### 如图

![截图](image.png)

## 方案二(源码执行)

前提：需要在edge浏览器中登陆bing的账号，推荐python版本 >=3.9

### 1. 先找到本地环境Edge浏览器版本号对应的 msedgedriver
msedgedriver [下载地址](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads)

### 2. 安装依赖库
``````bash
pip3 install -r requirements.txt
``````
### 3. 运行main.py
``````bash
python3 main.py
``````
# 免责声明
可能存在账号被封的情况，谨慎使用，出现任何问题，与本人无关