/**
 * 自动更新Home.vue中的weeklyData数组
 * 该脚本会在项目启动时运行，从Weekly目录中读取最新的周刊数据
 */

const fs = require('fs');
const path = require('path');

// 获取Weekly目录路径
const weeklyDir = path.resolve(__dirname, '../../Weekly');
// Home.vue文件路径
const homeVuePath = path.resolve(__dirname, '../src/views/Home.vue');

/**
 * 从Weekly目录中读取周刊数据
 * @returns {Array} 周刊数据数组
 */
function getWeeklyData() {
  // 读取Weekly目录下的所有文件夹
  const folders = fs.readdirSync(weeklyDir);
  
  // 用于存储周刊数据的数组
  const weeklyList = [];

  // 遍历每个Weekly文件夹
  folders.forEach(folder => {
    // 只处理No开头的文件夹
    if (folder.startsWith('No')) {
      const folderPath = path.join(weeklyDir, folder);
      const stat = fs.statSync(folderPath);
      
      // 确保是目录
      if (stat.isDirectory()) {
        // 检查markdown文件是否存在
        const mdFile = path.join(folderPath, `${folder}.md`);
        if (fs.existsSync(mdFile)) {
          // 获取markdown文件的创建时间
          const createTime = fs.statSync(mdFile).birthtime.getTime();
          
          // 查找首张图片
          let imgFile = "";
          const imgsDir = path.join(folderPath, 'imgs');
          if (fs.existsSync(imgsDir) && fs.statSync(imgsDir).isDirectory()) {
            const imgFiles = fs.readdirSync(imgsDir);
            if (imgFiles.length > 0) {
              // 保存完整的相对路径
              imgFile = `imgs/${imgFiles[0]}`;
            }
          }
          
          // 添加到周刊列表
          const id = parseInt(folder.replace('No', ''));
          weeklyList.push({
            id,
            title: `第${id}期`,
            createTime: createTime,
            img: imgFile
          });
        }
      }
    }
  });
  
  // 按ID排序
  weeklyList.sort((a, b) => a.id - b.id);
  
  return weeklyList;
}

/**
 * 更新Home.vue文件中的weeklyData数组
 * @param {Array} weeklyData 周刊数据数组
 */
function updateHomeVue(weeklyData) {
  // 读取Home.vue文件内容
  let homeVueContent = fs.readFileSync(homeVuePath, 'utf-8');
  
  // 将weeklyData数组转换为格式化的字符串
  const weeklyDataStr = JSON.stringify(weeklyData, null, 8)
    .replace(/^\[/g, '[')
    .replace(/\]$/g, '\n      ]')
    .replace(/\{/g, '\n        {')
    .replace(/\}/g, '\n        }')
    .replace(/"([^"]+)":/g, '"$1":');
  console.log("----------- " + weeklyDataStr);
  // 使用正则表达式替换weeklyData数组
  // 修改正则表达式，使用更精确的匹配模式，避免生成嵌套的方括号
  const regex = /(weeklyData:\s*\[)[\s\S]*?(\s*\](?=\s*}\s*data\(\)|\s*}\s*,))/;
  const newContent = homeVueContent.replace(regex, `$1${weeklyDataStr}$2`);
  
  // 写入更新后的内容
  fs.writeFileSync(homeVuePath, newContent, 'utf-8');
  
  console.log('Home.vue中的weeklyData数组已更新');
}

// 执行更新
try {
  const weeklyData = getWeeklyData();
  updateHomeVue(weeklyData);
} catch (error) {
  console.error('更新weeklyData数组失败:', error);
}