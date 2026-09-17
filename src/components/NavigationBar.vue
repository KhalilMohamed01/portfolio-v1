<script setup lang="ts">
interface NavigationItem {
  label: string
  target: string
}

const navigationItems: NavigationItem[] = [
  {
    label: 'Who am I',
    target: 'who',
  },
  {
    label: 'My Experiences',
    target: 'experience',
  },
  {
    label: 'My Projects',
    target: 'projects',
  },
  {
    label: 'My Education',
    target: 'education',
  },
  {
    label: 'Ask me anything',
    target: 'ask',
  },
]

defineProps<{
  darkMode: boolean
}>()

const emit = defineEmits<{
  navigate: [target: string]
  toggleTheme: []
}>()
</script>

<template>
  <nav class="navigation">
    <div class="navigation-links">
      <button
        v-for="item in navigationItems"
        :key="item.target"
        type="button"
        class="navigation-item"
        @click="emit('navigate', item.target)"
      >
        <span>&gt;</span>
        {{ item.label }}
      </button>
    </div>

    <button
      type="button"
      class="theme-toggle"
      @click="emit('toggleTheme')"
    >
      [ {{ darkMode ? 'dark' : 'light' }} ]
    </button>
  </nav>
</template>

<style scoped>
.navigation {
  height: 10vh;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  position: relative;
}

.navigation-links {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
}

.navigation-item,
.theme-toggle {
  border: none;
  padding: 0;
  background: transparent;
  color: inherit;
  font: inherit;
  font-size: 1.4rem;
  cursor: pointer;
}

.navigation-item span {
  margin-right: 0.25rem;
}

.navigation-item:hover,
.navigation-item:focus-visible,
.theme-toggle:hover,
.theme-toggle:focus-visible {
  text-decoration: underline;
}

.navigation-item:focus-visible,
.theme-toggle:focus-visible {
  outline: none;
}

.theme-toggle {
  position: absolute;
  right: 2rem;
  font-size: 1.1rem;
  opacity: 0.7;
}

@media (max-width: 900px) {
  .navigation {
    height: auto;
    min-height: 10vh;
    padding: 1rem;
    box-sizing: border-box;
  }

  .navigation-links {
    gap: 1rem;
    flex-wrap: wrap;
  }

  .theme-toggle {
    position: static;
  }

  .navigation-item {
    font-size: 1.1rem;
  }
}
</style>
