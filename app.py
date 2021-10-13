from flask import Flask, render_template, request
import json

app = Flask(__name__)

#主界面跳转服务
@app.route('/')
def index():
    return render_template('index.html')

#登录后台服务
@app.route('/login')
def login():
    return render_template('login.html')

# 获得已登录用户信息服务（暂时写死，后期改成读取数据库用户信息表）
@app.route('/getUserInfo', methods=["POST"])
def getUserInfo():
    userInfo = {}
    userInfo['user'] = 'test user'
    userInfo['phoneNumber'] = '12345678910'
    userInfo['mail'] = 'example@shu.com'
    userInfo['unit'] = '上海大学'
    userInfo['isSuccess'] = 1
    newData = json.dumps(userInfo)  # json.dumps封装
    return newData

# 使用说明，内嵌子页面跳转服务
@app.route('/introduce')
def introduce():
    '''
    TODO
    :return:
    '''
    test = "使用说明界面"
    # 把需要的数据给对应的页面
    return render_template('introduce.html', test=test)

# 关于我们，内嵌子页面跳转服务
@app.route('/aboutUs')
def aboutUs():
    '''
    TODO
    :return:
    '''
    return render_template('aboutUs.html')

# 介绍影响力最大化模型，跳转服务
@app.route('/introduceMaximumInfluenceModel')
def introduceMaximumInfluenceModel():
    '''
    TODO
    :return:
    '''
    return render_template('introduceMaximumInfluenceModel.html')

# 影响力最大化模型展示，后端服务
@app.route('/DemonstrationOfMaximumInfluenceModel')
def DemonstrationOfMaximumInfluenceModel():
    '''
    TODO
    :return:
    '''
    return render_template('DemonstrationOfMaximumInfluenceModel.html')

# 介绍社区划分模型，跳转服务
@app.route('/introduceCommunityDivisionModel')
def introduceCommunityDivisionModel():
    '''
    TODO
    :return:
    '''
    return render_template('introduceCommunityDivisionModel.html')

# 社区划分模型展示，后端服务
@app.route('/DemonstrationOfCommunityDivisionModel')
def DemonstrationOfCommunityDivisionModel():
    '''
    TODO
    :return:
    '''
    return render_template('DemonstrationOfCommunityDivisionModel.html')

if __name__ == '__main__':
    app.run()
