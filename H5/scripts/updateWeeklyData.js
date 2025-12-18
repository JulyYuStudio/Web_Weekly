/**
 * 自动生成周刊数据JSON文件
 * 该脚本会在项目启动时运行，从Weekly目录中读取最新的周刊数据，并生成JSON文件
 */

const fs = require('fs');
const path = require('path');

// 获取Weekly目录路径
const weeklyDir = path.resolve(__dirname, '../../docs/Weekly');
const weeklyDocsDir = path.resolve(__dirname, '../../docs');
// 周刊数据JSON文件路径
const weeklyDataJsonPath = path.resolve(weeklyDocsDir, 'weekly-list.json');

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
          // console.log(id + " " + createTime + " " + imgFile);
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
 * 将周刊数据保存为JSON文件
 * @param {Array} weeklyData 周刊数据数组
 */
function saveWeeklyDataJson(weeklyData) {
  // 将weeklyData数组转换为格式化的JSON字符串
  const weeklyDataStr = JSON.stringify(weeklyData, null, 4);
  
  // 写入JSON文件
  fs.writeFileSync(weeklyDataJsonPath, weeklyDataStr, 'utf-8');
  
  console.log('周刊数据已保存到JSON文件:', weeklyDataJsonPath);
}

// 执行更新
try {
  const weeklyData = getWeeklyData();
  saveWeeklyDataJson(weeklyData);
} catch (error) {
  console.error('生成周刊数据JSON文件失败:', error);
}