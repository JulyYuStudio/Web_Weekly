<template>
  <div class="home">
    <div class="home-layout">
      <!-- 左侧年份导航 -->
      <div class="year-navigation">
        <h3 class="nav-title">时间历史</h3>
        <ul class="year-list">
          <li v-for="year in years" :key="year" 
              :class="{'active': activeYear === year}"
              @click="setActiveYear(year)">
            {{ year }}年
          </li>
        </ul>
      </div>
      
      <!-- 右侧文章列表 -->
      <div class="home-weekly-list">
        <div v-for="year in years" :key="year" class="year-section">
          <h2 :id="`year-${year}`" class="year-heading">{{ year }}</h2>
          <div v-for="weekly in weekliesByYear[year]" :key="weekly.id" class="weekly-item">
            <router-link :to="{ name: 'weekly', params: { id: weekly.id } }" class="weekly-link">
              <!-- 图片容器 -->
              <div v-if="weekly.img && weekly.img !== ''" class="weekly-image-container">
                <img :src="getImagePath(weekly)" :alt="weekly.title" class="weekly-image" @error="handleImageError($event)" />
              </div>
              <!-- 内容区域 -->
              <div class="weekly-header">
                <div class="weekly-title">{{ weekly.title }}</div>
                <div class="weekly-date">{{ formatDate(weekly.createTime) }}</div>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      weeklies: [],
      years: [],       // 存储所有年份
      activeYear: null, // 当前选中的年份
      weeklyData: []
    }
  },
  computed: {
    // 所有文章，按照年份分组
    weekliesByYear() {
      const groupedWeeklies = {};
      this.weeklies.forEach(weekly => {
        const date = new Date(weekly.createTime);
        const year = date.getFullYear();
        if (!groupedWeeklies[year]) {
          groupedWeeklies[year] = [];
        }
        groupedWeeklies[year].push(weekly);
      });
      return groupedWeeklies;
    },
    // 所有文章，不再根据年份过滤
    filteredWeeklies() {
      return this.weeklies;
    }
  },
  mounted() {
    this.initWeeklies();
  },
  methods: {
    formatDate(timestamp) {
      const date = new Date(timestamp);
      return date.toLocaleDateString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit'
      }).replace(/\//g, '-');
    },
    getImagePath(weekly) {
      if (weekly.img && weekly.img !== '') {
        // 使用完整的相对路径构建URL，添加No前缀与文件夹结构保持一致
        return `public/Weekly/No${weekly.id}/${weekly.img}`;
      }
      return '';
    },
    handleImageError(event) {
      // 图片加载失败时，添加错误类名以显示备用样式
      event.target.classList.add('image-error');
    },
    initWeeklies() {
      try {
        // 获取base URL，确保在不同部署环境下都能正确加载
        const baseUrl = import.meta.env.BASE_URL || '/';
        // 构建完整的URL路径，考虑baseUrl配置
        const weeklyDataUrl = `${baseUrl}public/weekly-list.json`;
        console.log('尝试加载JSON文件:', weeklyDataUrl);
        
        // 使用XMLHttpRequest对象替代fetch，在某些静态部署环境中可能更可靠
        const xhr = new XMLHttpRequest();
        xhr.open('GET', weeklyDataUrl, true);
        
        // 设置响应类型为json
        xhr.responseType = 'json';
        
        // 处理加载完成事件
        xhr.onload = () => {
          console.log('XHR状态:', xhr.status, '响应类型:', typeof xhr.response);
          
          if (xhr.status >= 200 && xhr.status < 300) {
            // 获取JSON数据
            this.weeklyData = xhr.response;
            // 检查response是否为null
            if (this.weeklyData) {
              console.log('成功加载周刊数据，条目数:', this.weeklyData.length);
              // 按ID降序排序
              this.weeklies = this.weeklyData.sort((a, b) => b.id - a.id);
              
              // 初始化年份数据
              this.initYearsFromWeeklies();
            } else {
              console.error('加载周刊数据失败: 返回数据为null');
              // 尝试使用备用路径
              this.loadFallbackData();
            }
          } else {
            console.error(`HTTP错误! 状态码: ${xhr.status}`);
            // 尝试使用备用路径
            this.loadFallbackData();
          }
        };
        
        // 处理错误事件
        xhr.onerror = (error) => {
          console.error('加载周刊数据出错:', error);
          // 尝试使用备用路径
          this.loadFallbackData();
        };
        
        // 处理超时事件
        xhr.ontimeout = () => {
          console.error('加载周刊数据超时');
          // 尝试使用备用路径
          this.loadFallbackData();
        };
        
        // 发送请求
        xhr.send();
      } catch (error) {
        console.error('初始化Weekly列表失败:', error);
        // 尝试使用备用路径
        this.loadFallbackData();
      }
    },
    
    // 设置当前选中的年份并滚动到对应位置
    setActiveYear(year) {
      this.activeYear = year;
      
      // 使用setTimeout确保DOM已更新
      setTimeout(() => {
        const yearElement = document.getElementById(`year-${year}`);
        if (yearElement) {
          yearElement.scrollIntoView({ behavior: 'smooth' });
        }
      }, 100);
    },
    
    // 从周刊数据中提取年份信息
    initYearsFromWeeklies() {
      // 提取所有年份并去重
      const yearsSet = new Set();
      this.weeklies.forEach(weekly => {
        const date = new Date(weekly.createTime);
        yearsSet.add(date.getFullYear());
      });
      
      // 将年份数组排序（从新到旧）
      this.years = Array.from(yearsSet).sort((a, b) => b - a);
      
      // 默认选中最新的年份
      if (this.years.length > 0) {
        this.activeYear = this.years[0];
      }
    }
  }
}
</script>

<style scoped>
.home {
  max-width: 1000px;
  margin: 0 auto;
  padding: 1rem;
}

.home-layout {
  display: flex;
  gap: 2rem;
}

.home-title {
  color: var(--accent-color);
  margin-bottom: 1.5rem;
  text-align: center;
  font-size: 1.8rem;
  border-bottom: 2px solid var(--border-color);
  padding-bottom: 0.8rem;
}

/* 年份导航样式 */
.year-navigation {
  width: 120px;
  flex-shrink: 0;
  background-color: var(--bg-secondary);
  border-radius: 8px;
  padding: 1rem;
  position: sticky;
  top: 1rem;
  max-height: calc(100vh - 2rem);
  align-self: flex-start;
}

.nav-title {
  color: var(--accent-color);
  margin-bottom: 1rem;
  font-size: 1.2rem;
  text-align: center;
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 0.5rem;
}

.year-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.year-list li {
  padding: 0.5rem;
  margin-bottom: 0.5rem;
  border-radius: 4px;
  cursor: pointer;
  text-align: center;
  transition: all 0.2s ease;
}

.year-list li:hover {
  background-color: var(--bg-tertiary);
  color: var(--accent-color);
}

.year-list li.active {
  background-color: var(--accent-color);
  color: white;
}

/* 文章列表样式 */
.home-weekly-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  flex-grow: 1;
}

/* 年份区域样式 */
.year-section {
  margin-bottom: 2rem;
}

.year-heading {
  color: var(--accent-color);
  padding-bottom: 0.5rem;
  margin-bottom: 1rem;
  border-bottom: 2px solid var(--border-color);
  scroll-margin-top: 2rem; /* 确保滚动定位时有足够的上边距 */
}

.weekly-item {
  transition: transform 0.2s ease, box-shadow 0.3s ease;
  margin-bottom: 1.2rem;
}

.weekly-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

.weekly-link {
  display: flex;
  flex-direction: column;
  color: var(--text-primary);
  text-decoration: none;
  border-radius: 10px;
  transition: all 0.3s ease;
  background-color: var(--bg-secondary);
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.08);
  width: 100%;
  overflow: hidden;
}

.weekly-image-container {
  width: 100%;
  position: relative;
  padding-top: 56.25%; /* 16:9 比例 */
  overflow: hidden;
}

.weekly-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.weekly-image.image-error {
  object-fit: contain;
  background-color: var(--bg-tertiary);
}

.weekly-link:hover .weekly-image {
  transform: scale(1.05);
}

.weekly-link:hover {
  background-color: var(--bg-tertiary);
  color: var(--accent-color);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.weekly-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  position: relative;
  z-index: 1;
  padding: 1rem 1.2rem;
}

.weekly-title {
  font-size: 1.2rem;
  font-weight: 600;
  text-align: left;
  margin: 0;
  line-height: 1.4;
  flex: 1;
  padding-right: 1rem;
}

.weekly-date {
  font-size: 0.9rem;
  color: var(--text-secondary);
  text-align: right;
  white-space: nowrap;
}

/* 响应式调整 */
@media (max-width: 768px) {
  .home-layout {
    flex-direction: column;
  }
  
  .year-navigation {
    width: 100%;
    position: static;
    margin-bottom: 1.5rem;
  }
  
  .year-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    justify-content: center;
  }
  
  .year-list li {
    margin-bottom: 0;
    padding: 0.4rem 0.8rem;
  }
  
  .weekly-header {
    padding: 0.8rem 1rem;
  }
  
  .weekly-title {
    font-size: 1.1rem;
  }
  
  .weekly-date {
    font-size: 0.8rem;
  }
}
</style>


// 加载备用数据的方法
loadFallbackData() {
  console.log('尝试加载备用数据路径');
  // 尝试不同的路径格式
  const fallbackUrls = [
    './Weekly/weeklyData.json',
    '../Weekly/weeklyData.json',
    '/Weekly/weeklyData.json'
  ];
  
  // 尝试加载第一个备用URL
  this.tryLoadFallbackUrl(fallbackUrls, 0);
},

// 递归尝试加载备用URL
tryLoadFallbackUrl(urls, index) {
  if (index >= urls.length) {
    console.error('所有备用路径均加载失败');
    // 如果本地有缓存数据则使用
    if (this.weeklyData && Array.isArray(this.weeklyData) && this.weeklyData.length > 0) {
      console.log('使用本地缓存数据');
      this.weeklies = this.weeklyData.sort((a, b) => b.id - a.id);
      this.initYearsFromWeeklies();
    } else {
      console.error('无可用数据，显示空列表');
      this.weeklies = [];
    }
    return;
  }
  
  const url = urls[index];
  console.log(`尝试加载备用路径 (${index + 1}/${urls.length}):`, url);
  
  const xhr = new XMLHttpRequest();
  xhr.open('GET', url, true);
  xhr.responseType = 'json';
  
  xhr.onload = () => {
    if (xhr.status >= 200 && xhr.status < 300 && xhr.response) {
      console.log(`备用路径 ${url} 加载成功`);
      this.weeklyData = xhr.response;
      this.weeklies = this.weeklyData.sort((a, b) => b.id - a.id);
      this.initYearsFromWeeklies();
    } else {
      console.log(`备用路径 ${url} 加载失败，尝试下一个`);
      this.tryLoadFallbackUrl(urls, index + 1);
    }
  };
  
  xhr.onerror = () => {
    console.log(`备用路径 ${url} 加载出错，尝试下一个`);
    this.tryLoadFallbackUrl(urls, index + 1);
  };
  
  xhr.send();
},