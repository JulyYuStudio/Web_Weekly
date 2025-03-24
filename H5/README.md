# Weekly Blog

这是一个用于展示Weekly markdown文件的博客页面。

## 开发

```bash
npm install
npm run dev
```

## 构建

```bash
npm run build
```

## 部署

### 手动部署

使用deploy.sh脚本将构建后的文件部署到GitHub Pages：

```bash
# 确保脚本有执行权限
chmod +x deploy.sh
# 执行部署脚本
./deploy.sh
```

### 自动部署

项目已配置GitHub Actions，当推送到main分支时会自动部署到GitHub Pages。

配置文件位于：`.github/workflows/deploy.yml`

## 项目结构

- `src/`: 源代码目录
  - `views/`: 页面组件
  - `router/`: 路由配置
  - `assets/`: 静态资源
- `public/`: 公共资源目录
  - `Weekly/`: 构建时自动生成的Weekly内容