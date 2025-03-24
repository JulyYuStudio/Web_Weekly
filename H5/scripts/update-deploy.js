/**
 * 更新deploy.sh脚本，在部署前先运行updateWeeklyData.js脚本
 * 确保部署的是最新的周刊数据
 */

const fs = require('fs');
const path = require('path');

// deploy.sh文件路径
const deployShPath = path.resolve(__dirname, '../deploy.sh');

// 读取deploy.sh文件内容
let deployShContent = fs.readFileSync(deployShPath, 'utf-8');

// 检查是否已经添加了更新周刊数据的命令
if (!deployShContent.includes('node ./scripts/updateWeeklyData.js')) {
  // 在构建命令前添加更新周刊数据的命令
  deployShContent = deployShContent.replace(
    'npm run build',
    'node ./scripts/updateWeeklyData.js && npm run build'
  );
  
  // 写入更新后的内容
  fs.writeFileSync(deployShPath, deployShContent, 'utf-8');
  
  console.log('deploy.sh脚本已更新，将在部署前先运行updateWeeklyData.js脚本');
} else {
  console.log('deploy.sh脚本已包含更新周刊数据的命令，无需修改');
}