#!/usr/bin/env bash

# 错误时退出脚本
set -e

# 显示执行的命令
set -x

# 构建网站
npm run build

# 进入构建输出目录
cd static

# 初始化git仓库
git init
# git remote add origin git@github.com:lifelikejuly/Web_Weekly.git

# 创建main分支
# git checkout -b main
git add .
git commit -m 'deploy: update site content'

# 如果你要部署到自定义域名
# echo 'www.example.com' > CNAME

# 如果你要部署到 https://<USERNAME>.github.io
# git push -f git@github.com:<USERNAME>/<USERNAME>.github.io.git main

# 如果你要部署到 https://<USERNAME>.github.io/<REPO>
# 请替换为你的GitHub用户名和仓库名
# git push -f git@github.com:lifelikejuly/Web_Weekly.git 
git push origin main --force

cd -