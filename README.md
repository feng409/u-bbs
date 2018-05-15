## u-bbs

## 开发

- 创建数据库 `python reset.py`
- 创建迁徙脚本仓库并提交第一次版本
    `flask db init`
    `flask db migrate -m "init commit"`
    `flask db upgrade`

## 需要手动上传的
- `u14exyz` 证书
- `config.py` 配置
- `mysql_pass` 安装mysql时，需要输入的密码

## 第一次部署
- 创建数据库 `python3.6 reset.py`
- 执行迁徙脚本 `flask db upgrade`

## 后面部署
- 执行迁徙脚本 `flask db upgrade`