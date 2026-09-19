<!-- Source: Best-README-Template BLANK_README (Unlicense) — https://github.com/othneildrew/Best-README-Template -->
<a id="readme-top"></a>

# HY_programmingOnlineAndCheck-Back

A Flask and SQLAlchemy backend for the HY online programming platform that currently implements only email-based user registration, login, and token verification against a MySQL database.

**English** · [简体中文](README.zh-CN.md)

[![CI](https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back/actions/workflows/ci.yml/badge.svg)](https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back)](LICENSE)

[Report a bug](https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back/issues/new?template=bug_report.yml) · [Request a feature](https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back/issues/new?template=feature_request.yml)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

HY_programmingOnlineAndCheck-Back is the Flask API behind the HY online programming project, and today it implements only account management: `src/views/user.py` exposes `POST /regist/email`, `POST /login/email` and a token-protected `GET /request_test`, backed by the `User` model in `src/modules/user.py` and a MySQL database configured in `src/__init__.py`. Login and route protection use a signed, time-limited token issued and checked in `src/uniti/common/token.py`. No code for submitting, running, or checking a program exists in this repository yet, despite the project's name.

See the [open issues](https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back/issues) for planned features and known issues.

## Getting Started

### Prerequisites

- Python 3.11 — a newer interpreter breaks the pinned Flask/Werkzeug versions below (Werkzeug's routing module uses `ast.Str`, which Python 3.12 removed)
- A MySQL server reachable on port 3306, matching the `SQLALCHEMY_DATABASE_URI` hardcoded in `src/__init__.py`
- This repository ships no `requirements.txt` or `pyproject.toml`. Installing a current Flask pulls in an `itsdangerous` release that removed `TimedJSONWebSignatureSerializer`, the class `src/uniti/common/token.py` imports, so the exact versions below are required: Flask 1.1.4, Flask-SQLAlchemy 2.5.1, itsdangerous 1.1.0, Werkzeug 1.0.1, Jinja2 2.11.3, MarkupSafe 1.1.1, Click 7.1.2, SQLAlchemy < 2, and `mysql-connector-python`

### Installation

```sh
git clone https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back.git
cd HY_programmingOnlineAndCheck-Back
pip install "flask==1.1.4" "itsdangerous==1.1.0" "werkzeug==1.0.1" "jinja2==2.11.3" \
  "markupsafe==1.1.1" "click==7.1.2" "flask-sqlalchemy==2.5.1" "sqlalchemy<2" \
  mysql-connector-python
```

Create a MySQL database named `anying_dev` and update the connection string in `src/__init__.py` if your credentials differ from the ones hardcoded there.

## Usage

Start the development server:

```sh
python src/main.py
```

Then call the two account endpoints and the token-protected one:

```sh
curl -X POST http://127.0.0.1:5000/regist/email \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "Password1"}'

curl -X POST http://127.0.0.1:5000/login/email \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "Password1"}'

curl http://127.0.0.1:5000/request_test -H "token: <token from the login response>"
```

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) for how to open an issue or a pull request, and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for the standards expected of everyone taking part.

Please do not report security issues in public issues or pull requests. [SECURITY.md](SECURITY.md) explains how to report them privately.

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact

Project link: [https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back](https://github.com/DK-PRG-TEAM/HY_programmingOnlineAndCheck-Back)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
