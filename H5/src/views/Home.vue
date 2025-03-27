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
      // 内联周刊数据
      weeklyData: [
        
        {
                "id": 1,
                "title": "第1期",
                "createTime": 1715762550000,
                "img": "imgs/20240515164354.png"
        
        },
        
        {
                "id": 2,
                "title": "第2期",
                "createTime": 1716256970000,
                "img": "imgs/20240521100428.png"
        
        },
        
        {
                "id": 3,
                "title": "第3期",
                "createTime": 1716773555000,
                "img": "imgs/20240527165107.png"
        
        },
        
        {
                "id": 4,
                "title": "第4期",
                "createTime": 1717338844000,
                "img": "imgs/20240607140450.png"
        
        },
        
        {
                "id": 5,
                "title": "第5期",
                "createTime": 1718069436000,
                "img": "imgs/20240611180342.png"
        
        },
        
        {
                "id": 6,
                "title": "第6期",
                "createTime": 1718588643000,
                "img": "imgs/20240621153738.png"
        
        },
        
        {
                "id": 7,
                "title": "第7期",
                "createTime": 1719194149000,
                "img": "imgs/20240624114254.png"
        
        },
        
        {
                "id": 8,
                "title": "第8期",
                "createTime": 1719798410000,
                "img": ""
        
        },
        
        {
                "id": 9,
                "title": "第9期",
                "createTime": 1720402517000,
                "img": "imgs/20240714224605.png"
        
        },
        
        {
                "id": 10,
                "title": "第10期",
                "createTime": 1721007980000,
                "img": ""
        
        },
        
        {
                "id": 11,
                "title": "第11期",
                "createTime": 1721614249000,
                "img": "imgs/20240729093052.png"
        
        },
        
        {
                "id": 12,
                "title": "第12期",
                "createTime": 1722217853000,
                "img": "imgs/20240805085854.png"
        
        },
        
        {
                "id": 13,
                "title": "第13期",
                "createTime": 1722869272000,
                "img": ""
        
        },
        
        {
                "id": 14,
                "title": "第14期",
                "createTime": 1723429770000,
                "img": "imgs/20240816105050.png"
        
        },
        
        {
                "id": 15,
                "title": "第15期",
                "createTime": 1724054750000,
                "img": "imgs/20240819160754.png"
        
        },
        
        {
                "id": 16,
                "title": "第16期",
                "createTime": 1724638031000,
                "img": "imgs/20240827095301.png"
        
        },
        
        {
                "id": 17,
                "title": "第17期",
                "createTime": 1725413961000,
                "img": "imgs/20240908222257.png"
        
        },
        
        {
                "id": 18,
                "title": "第18期",
                "createTime": 1725846662000,
                "img": "imgs/20240910094039.png"
        
        },
        
        {
                "id": 19,
                "title": "第19期",
                "createTime": 1726623970000,
                "img": "imgs/20240923165227.png"
        
        },
        
        {
                "id": 20,
                "title": "第20期",
                "createTime": 1728351638000,
                "img": "imgs/20241010095004.png"
        
        },
        
        {
                "id": 21,
                "title": "第21期",
                "createTime": 1736214906220,
                "img": "imgs/20241118131824.png"
        
        },
        
        {
                "id": 22,
                "title": "第22期",
                "createTime": 1733801721564,
                "img": "imgs/20250107160845.png"
        
        },
        
        {
                "id": 23,
                "title": "第23期",
                "createTime": 1736733611899,
                "img": "imgs/20250113113156.png"
        
        },
        
        {
                "id": 24,
                "title": "第24期",
                "createTime": 1737683230558,
                "img": "imgs/20250225153617.png"
        
        },
        
        {
                "id": 25,
                "title": "第25期",
                "createTime": 1740925286899,
                "img": "imgs/20250303140153.png"
        
        },
        
        {
                "id": 26,
                "title": "第26期",
                "createTime": 1741615582094,
                "img": "imgs/20250311100255.png"
        
        },
        
        {
                "id": 27,
                "title": "第27期",
                "createTime": 1742043288813,
                "img": "imgs/20250317214223.png"
        
        },
        
        {
                "id": 28,
                "title": "第28期",
                "createTime": 1742868523343,
                "img": "imgs/20250325101206.png"
        
        }

      ]
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
        return `./Weekly/No${weekly.id}/${weekly.img}`;
      }
      return '';
    },
    handleImageError(event) {
      // 图片加载失败时，添加错误类名以显示备用样式
      event.target.classList.add('image-error');
    },
    initWeeklies() {
      try {
        // 使用内联数据代替fetch请求
        this.weeklies = this.weeklyData.sort((a, b) => b.id - a.id);
        
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
      } catch (error) {
        console.error('初始化Weekly列表失败:', error);
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