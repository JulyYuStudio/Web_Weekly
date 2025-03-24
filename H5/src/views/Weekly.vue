<template>
  <div class="weekly-container">
    <div class="back-button">
      <router-link to="/" class="back-link">
        <span class="back-icon">←</span> 返回首页
      </router-link>
    </div>
    <div v-if="loading" class="loading">
      <p>加载中...</p>
    </div>
    <div v-else-if="error" class="error">
      <p>{{ error }}</p>
    </div>
    <div v-else class="weekly-content-wrapper">
      <div class="weekly-main-content">
        <h1 class="weekly-title">第{{ id }}期</h1>
        <iframe v-if="iframeUrl" :src="iframeUrl" class="weekly-iframe" frameborder="0" ref="weeklyIframe" @load="handleIframeLoad"></iframe>
        <div v-else class="markdown-content" ref="markdownContent" v-html="htmlContent"></div>
      </div>
    </div>
    <button 
      v-show="showBackToTop" 
      @click="scrollToTop" 
      class="back-to-top" 
      title="回到顶部"
    >
      <span class="back-to-top-icon">🚀</span>
    </button>
  </div>
</template>

<script>
// 不再需要marked和highlight.js，因为HTML已经预先生成

export default {
  name: 'Weekly',
  props: {
    id: {
      type: [String, Number],
      required: true
    }
  },
  data() {
    return {
      loading: true,
      error: null,
      markdownContent: '',
      htmlContent: '',
      showBackToTop: false,
      iframeUrl: ''
    }
  },
  watch: {
    id: {
      immediate: true,
      handler() {
        this.fetchMarkdownContent();
      }
    }
  },
  mounted() {
    // 添加滚动事件监听器
    window.addEventListener('scroll', this.handleScroll);
    
    // 添加主题变化的监听器
    this.setupThemeChangeListener();
  },
  
  beforeUnmount() {
    // 移除滚动事件监听器，避免内存泄漏
    window.removeEventListener('scroll', this.handleScroll);
    
    // 移除主题变化的监听器
    this.removeThemeChangeListener();
  },
  methods: {
    async fetchMarkdownContent() {
      this.loading = true;
      this.error = null;
      
      try {
        // 获取base URL，确保在不同部署环境下都能正确跳转
        const baseUrl = import.meta.env.BASE_URL || '/';
        // 构建完整的URL路径，考虑baseUrl配置
        const weeklyUrl = `${baseUrl}Weekly/No${this.id}/No${this.id}.html`;
        // 设置iframe的URL，而不是重定向
        this.iframeUrl = weeklyUrl;
        this.loading = false;
      } catch (error) {
        console.error('加载周刊内容出错:', error);
        this.error = `加载周刊内容失败: ${error.message}`;
        this.loading = false;
      }
    },
    
    // 处理iframe加载完成事件
    handleIframeLoad() {
      if (this.$refs.weeklyIframe) {
        try {
          // 尝试调整iframe高度以适应内容
          this.adjustIframeHeight();
          
          // 尝试将iframe内部的样式应用主题
          this.applyThemeToIframe();
        } catch (error) {
          console.error('处理iframe加载事件出错:', error);
        }
      }
    },
    
    // 调整iframe高度以适应内容
    adjustIframeHeight() {
      const iframe = this.$refs.weeklyIframe;
      if (!iframe) return;
      
      try {
        // 尝试获取iframe内容的高度
        const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
        if (iframeDoc) {
          const height = iframeDoc.body.scrollHeight;
          // 设置最小高度为80vh，如果内容更长则使用内容高度
          iframe.style.height = Math.max(height, window.innerHeight * 0.8) + 'px';
        }
      } catch (e) {
        console.warn('无法调整iframe高度:', e);
      }
    },
    
    // 将当前主题应用到iframe内部
    applyThemeToIframe() {
      const iframe = this.$refs.weeklyIframe;
      if (!iframe) return;
      
      try {
        const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
        if (iframeDoc) {
          // 获取当前主题
          const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
          // 将主题应用到iframe的html元素上
          iframeDoc.documentElement.setAttribute('data-theme', currentTheme);
        }
      } catch (e) {
        console.warn('无法应用主题到iframe:', e);
      }
    },
    
    // 处理滚动事件，控制回到顶部按钮的显示和隐藏
    handleScroll() {
      // 当页面滚动超过300px时显示按钮
      this.showBackToTop = window.scrollY > 300;
    },
    
    // 滚动回顶部
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth' // 平滑滚动
      });
    },
    
    // 设置主题变化的监听器
    setupThemeChangeListener() {
      // 使用MutationObserver监听html元素的data-theme属性变化
      this.themeObserver = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
          if (mutation.type === 'attributes' && mutation.attributeName === 'data-theme') {
            // 当主题变化时，重新应用主题到iframe
            this.applyThemeToIframe();
          }
        });
      });
      
      // 开始观察document.documentElement的属性变化
      this.themeObserver.observe(document.documentElement, {
        attributes: true,
        attributeFilter: ['data-theme']
      });
    },
    
    // 移除主题变化的监听器
    removeThemeChangeListener() {
      if (this.themeObserver) {
        this.themeObserver.disconnect();
        this.themeObserver = null;
      }
    }
  }
}
</script>

<style>
.weekly-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 1rem;
}

/* 文章内容容器 */
.weekly-content-wrapper {
  display: block;
}

/* 文章内容区域 */
.weekly-main-content {
  width: 100%;
}

/* iframe样式 */
.weekly-iframe {
  width: 100%;
  min-height: 80vh; /* 设置最小高度为视口高度的80% */
  border: none;
  overflow: auto;
  background-color: var(--bg-primary);
  border-radius: 8px;
  box-shadow: 0 2px 8px var(--shadow-color);
  transition: height 0.3s ease;
}

.back-button {
  margin-bottom: 1rem;
}

.back-link {
  display: inline-flex;
  align-items: center;
  color: var(--accent-color);
  text-decoration: none;
  padding: 0.5rem 0.8rem;
  background-color: var(--bg-secondary);
  border-radius: 4px;
  transition: all 0.2s ease;
}

.back-link:hover {
  background-color: var(--bg-tertiary);
}

.back-icon {
  margin-right: 0.5rem;
  font-size: 1.2em;
}

.weekly-title {
  color: var(--accent-color);
  margin-bottom: 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--border-color);
}

.loading, .error {
  padding: 2rem;
  text-align: center;
  color: var(--text-secondary);
}

.error {
  color: var(--error-color);
  background-color: var(--error-bg);
  border-radius: 4px;
  padding: 1rem;
}

/* Markdown 内容样式 */
.markdown-content {
  line-height: 1.6;
  color: var(--text-primary);
}

.markdown-content h2 {
  margin-top: 1.5rem;
  margin-bottom: 1rem;
  padding-bottom: 0.3rem;
  border-bottom: 1px solid var(--border-color);
  color: var(--text-primary);
}

.markdown-content h3, 
.markdown-content h4, 
.markdown-content h5, 
.markdown-content h6 {
  margin-top: 1.2rem;
  margin-bottom: 0.8rem;
  color: var(--text-primary);
}

.markdown-content p {
  margin-bottom: 1rem;
}

.markdown-content ul, 
.markdown-content ol {
  padding-left: 2rem;
  margin-bottom: 1rem;
}

.markdown-content li {
  margin-bottom: 0.5rem;
}

.markdown-content img {
  max-width: 100%;
  height: auto;
  margin: 1rem 0;
  border-radius: 4px;
  box-shadow: 0 2px 4px var(--shadow-color);
}

.markdown-content a {
  color: var(--accent-color);
  text-decoration: none;
}

.markdown-content a:hover {
  text-decoration: underline;
}

.markdown-content blockquote {
  border-left: 4px solid var(--accent-color);
  padding-left: 1rem;
  margin-left: 0;
  margin-right: 0;
  color: var(--text-secondary);
  font-style: italic;
}

.markdown-content code {
  font-family: monospace;
  background-color: var(--code-bg);
  padding: 0.2rem 0.4rem;
  border-radius: 3px;
  font-size: 0.9em;
}

.markdown-content pre {
  background-color: var(--code-bg);
  padding: 1rem;
  border-radius: 4px;
  overflow-x: auto;
  margin-bottom: 1rem;
}

.markdown-content pre code {
  background-color: transparent;
  padding: 0;
  border-radius: 0;
}

.markdown-content table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1rem;
}

.markdown-content table th,
.markdown-content table td {
  border: 1px solid var(--border-color);
  padding: 0.5rem;
}

.markdown-content table th {
  background-color: var(--bg-secondary);
  font-weight: 600;
}

/* 回到顶部按钮样式 */
.back-to-top {
  position: fixed;
  bottom: 30px;
  right: 30px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: var(--accent-color);
  color: white;
  border: none;
  box-shadow: 0 2px 10px var(--shadow-color);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  z-index: 100;
  opacity: 0.8;
}

.back-to-top:hover {
  opacity: 1;
  transform: translateY(-5px);
}

.back-to-top-icon {
  font-size: 1.5rem;
}

/* 响应式调整 */
@media (max-width: 768px) {
  .back-to-top {
    width: 40px;
    height: 40px;
    bottom: 20px;
    right: 20px;
  }
  
  .back-to-top-icon {
    font-size: 1.2rem;
  }
}
</style>