import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import fs from 'fs'
import { marked } from 'marked'
import hljs from 'highlight.js'
import updateWeeklyDataPlugin from './scripts/updateWeeklyPlugin'

// 自定义插件：复制Weekly目录下的markdown文件到public目录并预生成HTML文件
function copyWeeklyFiles() {
  return {
    name: 'copy-weekly-files',
    buildStart() {
      // 确保public/Weekly目录存在
      const publicWeeklyDir = path.resolve(__dirname, 'Weekly')
      if (!fs.existsSync(path.resolve(__dirname, 'Weekly'))) {
        fs.mkdirSync(path.resolve(__dirname, 'Weekly'))
      }
      if (!fs.existsSync(publicWeeklyDir)) {
        fs.mkdirSync(publicWeeklyDir)
      }
      
      // 获取Weekly目录路径
      const weeklyDir = path.resolve(__dirname, '../Weekly')
      
      // 读取Weekly目录下的所有文件夹
      const folders = fs.readdirSync(weeklyDir)
      
      // 用于生成weekly-list.json的数组
      const weeklyList = []

      // 遍历每个Weekly文件夹
      folders.forEach(folder => {
        // 只处理No开头的文件夹
        if (folder.startsWith('No')) {
          const folderPath = path.join(weeklyDir, folder)
          const stat = fs.statSync(folderPath)
          
          // 确保是目录
          if (stat.isDirectory()) {
            // 创建对应的public目录
            const targetDir = path.join(publicWeeklyDir, folder)
            if (!fs.existsSync(targetDir)) {
              fs.mkdirSync(targetDir)
            }
            
            // 复制markdown文件
            const mdFile = path.join(folderPath, `${folder}.md`)
            if (fs.existsSync(mdFile)) {

              // 读取markdown内容并转换为HTML
              const mdContent = fs.readFileSync(mdFile, 'utf-8')
              
              // 配置marked以使用highlight.js进行代码高亮
              marked.setOptions({
                highlight: function(code, lang) {
                  if (lang && hljs.getLanguage(lang)) {
                    return hljs.highlight(code, { language: lang }).value;
                  }
                  return hljs.highlightAuto(code).value;
                },
                breaks: true
              })
              
              // 处理图片路径，将相对路径转换为绝对路径
              const processedContent = mdContent.replace(
                /!\[(.*?)\]\((imgs\/.*?)\)/g,
                `![$1](./Weekly/${folder}/$2)`
              )
              
              // 转换为HTML并保存
              const htmlContent = marked(processedContent)
              fs.writeFileSync(path.join(targetDir, `${folder}.html`), htmlContent)
              // 获取到markdown文件的创建时间
              const createTime = fs.statSync(mdFile).birthtime.getTime()
              
            // 首张图片地址
            var imgFile = ""
            // 复制imgs目录
            const imgsDir = path.join(folderPath, 'imgs')
            if (fs.existsSync(imgsDir) && fs.statSync(imgsDir).isDirectory()) {
              const targetImgsDir = path.join(targetDir, 'imgs')
              if (!fs.existsSync(targetImgsDir)) {
                fs.mkdirSync(targetImgsDir)
              }
              
              // 复制所有图片文件
              const imgFiles = fs.readdirSync(imgsDir)
              imgFiles.forEach(imgFile => {
                const imgPath = path.join(imgsDir, imgFile)
                if (fs.statSync(imgPath).isFile()) {
                  fs.copyFileSync(imgPath, path.join(targetImgsDir, imgFile))
                }
              })
              const dirFiles = fs.readdirSync(targetImgsDir)
              if(dirFiles.length > 0){
                // 保存完整的相对路径，而不仅仅是文件名
                imgFile = `imgs/${dirFiles[0]}`;
              }
            }

              // 添加到weekly列表
              const id = parseInt(folder.replace('No', ''))
              weeklyList.push({
                id,
                title: `第${id}期`,
                createTime: createTime,
                img: imgFile
              })
            }
          
          }
        }
      })
      
      // 按ID排序
      weeklyList.sort((a, b) => a.id - b.id)
      
      // 生成weekly-list.json文件
      fs.writeFileSync(
        path.join(publicWeeklyDir, 'weekly-list.json'),
        JSON.stringify(weeklyList, null, 2)
      )
      
      console.log('Weekly files copied and weekly-list.json generated')
    }
  }
}

export default defineConfig({
  plugins: [vue(), copyWeeklyFiles(), updateWeeklyDataPlugin()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  },
  server: {
    port: 3000
  },
  build: {
    outDir: 'static/docs'
  },
  base: '/Web_Weekly/'
})