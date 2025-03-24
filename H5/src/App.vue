<template>
  <div class="app-container" :data-theme="theme">
    <button class="theme-toggle" @click="toggleTheme" :title="theme === 'dark' ? '切换到亮色模式' : '切换到暗黑模式'">
      <span v-if="theme === 'dark'">🌞</span>
      <span v-else>🌙</span>
    </button>
    <header class="header">
      <h1>余小余周刊</h1>
      <nav class="main-nav">
        <router-link to="/" class="nav-link">首页</router-link>
        <router-link to="/about" class="nav-link">关于</router-link>
      </nav>
    </header>
    <div class="main-content">
      <main class="content">
        <router-view />
      </main>
    </div>
    <footer class="footer">
      <p>&copy; {{ new Date().getFullYear() }} 余小余周刊 - 力量来自Trae</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      theme: localStorage.getItem('theme') || 'light'
    }
  },
  provide() {
    return {
      theme: () => this.theme,
      toggleTheme: this.toggleTheme
    }
  },
  mounted() {
    // 初始化时应用保存的主题
    document.documentElement.setAttribute('data-theme', this.theme);
  },
  methods: {
    toggleTheme() {
      this.theme = this.theme === 'light' ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', this.theme);
      localStorage.setItem('theme', this.theme);
    }
  }
}
</script>

<style>
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.header {
  background-color: var(--accent-color);
  color: white;
  padding: 1rem;
  text-align: center;
}

.main-content {
  display: flex;
  flex: 1;
}

.content {
  flex: 1;
  padding: 1rem;
  max-width: 1200px;
  margin: 0 auto;
}

.footer {
  background-color: var(--bg-secondary);
  padding: 1rem;
  text-align: center;
  border-top: 1px solid var(--border-color);
}

.main-nav {
  display: flex;
  justify-content: center;
  margin-top: 0.5rem;
}

.nav-link {
  color: white;
  text-decoration: none;
  margin: 0 1rem;
  padding: 0.3rem 0.8rem;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.nav-link:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

.nav-link.router-link-active {
  font-weight: bold;
  background-color: rgba(255, 255, 255, 0.15);
}
</style>