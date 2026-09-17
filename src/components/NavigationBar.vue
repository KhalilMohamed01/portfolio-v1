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

const scrollToSection = (target: string) => {
  document.getElementById(target)?.scrollIntoView({
    behavior: 'smooth',
  })
}
</script>

<template>
  <nav class="navigation-bar">
    <div class="navigation-inner">
      <button
        v-for="item in navigationItems"
        :key="item.target"
        type="button"
        class="navigation-item"
        @click="scrollToSection(item.target)"
      >
        <span class="caret">&gt;</span>
        <span class="label">{{ item.label }}</span>
      </button>
    </div>
  </nav>
</template>

<style scoped>
.navigation-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;

  display: flex;
  justify-content: center;
  align-items: center;

  padding: 28px 16px;

  background: transparent;

  z-index: 100;
}

.navigation-inner {
  display: flex;
  gap: clamp(18px, 3vw, 46px);

  flex-wrap: wrap;
  justify-content: center;
}

.navigation-item {
  background: none;
  border: none;

  padding: 4px 2px;

  display: inline-flex;
  align-items: baseline;
  gap: 6px;

  font-family: inherit;
  font-size: 22px;
  letter-spacing: 0.5px;

  color: inherit;

  cursor: pointer;

  transition: transform 0.15s ease;
}

.caret {
  opacity: 1;
}

.label {
  border-bottom: 1px solid transparent;

  transition: border-color 0.15s ease;
}

.navigation-item:hover,
.navigation-item:focus-visible {
  transform: translateY(-4px);
  outline: none;
}

.navigation-item:hover .label,
.navigation-item:focus-visible .label {
  border-color: currentColor;
}
</style>
