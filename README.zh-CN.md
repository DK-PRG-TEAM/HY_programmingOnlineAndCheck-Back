[English](README.md) · **简体中文**

> 英文版是规范版本。本页与 [README.md](README.md) 不一致时，以英文版为准。

<!-- translation-of: README.md sha256:edb514a64033a413 -->

<!-- Source: Best-README-Template BLANK_README (Unlicense) — https://github.com/othneildrew/Best-README-Template -->
<a id="readme-top"></a>

# HY_programmingOnlineAndCheck-Back

一个 Flask + SQLAlchemy 后端，服务于 HY 在线编程平台；目前只实现了基于邮箱的用户注册、登录和令牌校验，并连接到一个 MySQL 数据库。

[![CI](https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back/actions/workflows/ci.yml/badge.svg)](https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back)](LICENSE)

[报告问题](https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back/issues/new?template=bug_report.yml) · [提出需求](https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back/issues/new?template=feature_request.yml)

<details>
  <summary>目录</summary>
  <ol>
    <li><a href="#about-the-project">关于本项目</a></li>
    <li><a href="#getting-started">开始使用</a></li>
    <li><a href="#usage">用法</a></li>
    <li><a href="#contributing">参与贡献</a></li>
    <li><a href="#license">许可证</a></li>
    <li><a href="#contact">联系方式</a></li>
  </ol>
</details>

## 关于本项目

HY_programmingOnlineAndCheck-Back 是 HY 在线编程项目的 Flask API，目前只实现了账号管理：`src/views/user.py` 暴露了 `POST /regist/email`、`POST /login/email`，以及一个需要令牌验证的 `GET /request_test`，背后是 `src/modules/user.py` 中的 `User` 模型和 `src/__init__.py` 里配置的 MySQL 数据库。登录与路由保护使用的是在 `src/uniti/common/token.py` 中签发和校验的、带有效期的签名令牌。尽管项目名称如此，本仓库目前尚不包含任何提交、运行或批改程序的代码。

计划中的功能与已知问题，见 [open issues](https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back/issues)。

## 开始使用

### 环境要求

- Python 3.11 —— 更新的解释器会破坏下面固定的 Flask/Werkzeug 版本组合（Werkzeug 的路由模块用到了 `ast.Str`，而 Python 3.12 已将其移除）
- 一台可在 3306 端口访问的 MySQL 服务器，对应 `src/__init__.py` 中写死的 `SQLALCHEMY_DATABASE_URI`
- 本仓库没有 `requirements.txt` 或 `pyproject.toml`。安装当前版本的 Flask 会附带一个已经移除 `TimedJSONWebSignatureSerializer` 的 `itsdangerous`，而这正是 `src/uniti/common/token.py` 所导入的类，因此必须使用以下固定版本：Flask 1.1.4、Flask-SQLAlchemy 2.5.1、itsdangerous 1.1.0、Werkzeug 1.0.1、Jinja2 2.11.3、MarkupSafe 1.1.1、Click 7.1.2、SQLAlchemy < 2，以及 `mysql-connector-python`

### 安装

```sh
git clone https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back.git
cd HY_programmingOnlineAndCheck-Back
pip install "flask==1.1.4" "itsdangerous==1.1.0" "werkzeug==1.0.1" "jinja2==2.11.3" \
  "markupsafe==1.1.1" "click==7.1.2" "flask-sqlalchemy==2.5.1" "sqlalchemy<2" \
  mysql-connector-python
```

创建一个名为 `anying_dev` 的 MySQL 数据库；如果你的账号密码与 `src/__init__.py` 中写死的不同，请同步修改那里的连接字符串。

## 用法

启动开发服务器：

```sh
python src/main.py
```

然后调用两个账号接口以及需要令牌的接口：

```sh
curl -X POST http://127.0.0.1:5000/regist/email \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "Password1"}'

curl -X POST http://127.0.0.1:5000/login/email \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "Password1"}'

curl http://127.0.0.1:5000/request_test -H "token: <登录响应中的令牌>"
```

## 参与贡献

欢迎参与。[CONTRIBUTING.md](CONTRIBUTING.md) 说明如何提交 issue 或 pull request，[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) 说明对所有参与者的行为要求。

请不要在公开的 issue 或 pull request 中报告安全问题。[SECURITY.md](SECURITY.md) 说明了私下报告的方式。

## 许可证

以 MIT 许可证分发。详见 [LICENSE](LICENSE)。

## 联系方式

项目地址：[https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back](https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
