<template>
  <div class="about-container">
    <div class="back-button">
      <router-link to="/" class="back-link">
        <span class="back-icon">←</span> 返回首页
      </router-link>
    </div>
    
    <div class="about-content-wrapper">
      <div class="about-main-content">
        <h1 class="about-title">关于余小余周刊</h1>
        
        <div class="about-section">
          <h2>项目简介</h2>
          <p>余小余周刊是一个通过Trae AI助力创建的技术分享平台，旨在收集和分享有价值的技术文章、工具和资源。每期周刊都包含精选的内容，帮助开发者了解行业动态和技术趋势。</p>
        </div>
        
        <div class="about-section">
          <h2>技术栈</h2>
          <p>本项目采用现代前端技术栈构建：</p>
          <ul>
            <li>Vue 3 - 渐进式JavaScript框架</li>
            <li>Vue Router - 官方路由管理器</li>
            <li>Vite - 下一代前端构建工具</li>
            <li>Marked - Markdown解析器</li>
            <li>Highlight.js - 代码高亮库</li>
          </ul>
        </div>
        
        <div class="about-section">
          <h2>Trae的贡献</h2>
          <p>Trae是一个强大的AI助手，在本项目中发挥了关键作用：</p>
          <ul>
            <li>自动化代码生成 - 快速构建项目框架和组件</li>
            <li>智能化问题解决 - 协助解决开发过程中的技术难题</li>
            <li>创意与设计支持 - 提供UI/UX设计建议和创意思路</li>
            <li>代码优化与重构 - 改进代码质量和性能</li>
          </ul>
          <p>通过Trae的协助，我们能够更高效地开发和维护这个项目，专注于内容创作和用户体验的提升。</p>
        </div>
        
        <div class="about-section">
          <h2>项目特点</h2>
          <ul>
            <li>响应式设计 - 适配各种设备屏幕</li>
            <li>暗黑模式支持 - 提供舒适的阅读体验</li>
            <li>Markdown渲染 - 优雅展示文章内容</li>
            <li>代码高亮 - 增强技术内容的可读性</li>
            <li>自动化构建 - 简化内容更新和部署流程</li>
          </ul>
        </div>
        
        <!-- <div class="about-section">
          <h2>联系我们</h2>
          <p>如果您有任何问题、建议或合作意向，欢迎通过以下方式联系我们：</p>
          <p>邮箱：<a href="mailto:contact@yuxiaoyu.com">contact@yuxiaoyu.com</a></p>
          <p>GitHub：<a href="https://github.com/yuxiaoyu" target="_blank">github.com/yuxiaoyu</a></p>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'About',
  data() {
    return {}
  },
  mounted() {
    // 页面加载时滚动到顶部
    window.scrollTo(0, 0);
  }
}
</script>

<style scoped>
.about-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 1rem;
}

.back-button {
  margin-bottom: 2rem;
}

.back-link {
  display: inline-flex;
  align-items: center;
  color: var(--accent-color);
  font-weight: 500;
  transition: color 0.2s;
}

.back-link:hover {
  color: var(--accent-hover);
  text-decoration: none;
}

.back-icon {
  margin-right: 0.5rem;
  font-size: 1.2rem;
}

.about-title {
  font-size: 2rem;
  margin-bottom: 2rem;
  color: var(--accent-color);
  border-bottom: 2px solid var(--border-color);
  padding-bottom: 0.5rem;
}

.about-section {
  margin-bottom: 2.5rem;
}

.about-section h2 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: var(--text-primary);
}

.about-section p {
  margin-bottom: 1rem;
  line-height: 1.6;
  color: var(--text-primary);
}

.about-section ul {
  list-style-type: disc;
  padding-left: 1.5rem;
  margin-bottom: 1rem;
}

.about-section li {
  margin-bottom: 0.5rem;
  line-height: 1.6;
  color: var(--text-primary);
}

.about-section a {
  color: var(--accent-color);
  text-decoration: none;
  transition: color 0.2s;
}

.about-section a:hover {
  color: var(--accent-hover);
  text-decoration: underline;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .about-container {
    padding: 1rem 0.5rem;
  }
  
  .about-title {
    font-size: 1.75rem;
  }
  
  .about-section h2 {
    font-size: 1.25rem;
  }
}
</style>