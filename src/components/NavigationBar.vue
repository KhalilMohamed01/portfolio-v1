<script setup lang="ts">
import { ref } from 'vue'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faBars, faXmark } from '@fortawesome/free-solid-svg-icons'

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

const isMenuOpen = ref(false)

function toggleMenu() {
  isMenuOpen.value = !isMenuOpen.value
}

function handleNavigation(target: string) {
  emit('navigate', target)
  isMenuOpen.value = false
}

function toggleTheme() {
  emit('toggleTheme')
  isMenuOpen.value = false
}
</script>

<template>
  <nav class="navigation">
    <!-- Top bar -->
    <div class="navigation-header">
      <button
        type="button"
        class="menu-toggle"
        :aria-expanded="isMenuOpen"
        aria-label="Toggle navigation menu"
        @click="toggleMenu"
      >
        <FontAwesomeIcon
          :icon="isMenuOpen ? faXmark : faBars"
        />
      </button>

      <div class="desktop-navigation-links">
        <button
          v-for="item in navigationItems"
          :key="item.target"
          type="button"
          class="navigation-item"
          @click="handleNavigation(item.target)"
        >
          <span>&gt;</span>
          {{ item.label }}
        </button>
      </div>

      <button
        type="button"
        class="theme-toggle"
        @click="toggleTheme"
      >
        [ {{ darkMode ? 'dark' : 'light' }} ]
      </button>
    </div>

    <!-- Mobile menu -->
    <div
      v-if="isMenuOpen"
      class="mobile-navigation-links"
    >
      <button
        v-for="item in navigationItems"
        :key="item.target"
        type="button"
        class="navigation-item"
        @click="handleNavigation(item.target)"
      >
        <span>&gt;</span>
        {{ item.label }}
      </button>
    </div>
  </nav>
</template>

<style scoped>
.navigation {
  width: 100%;
  min-height: 10vh;

  display: flex;
  flex-direction: column;

  box-sizing: border-box;

  position: relative;
}

.navigation-header {
  width: 100%;
  min-height: 10vh;

  display: flex;
  align-items: center;
  justify-content: center;

  position: relative;

  box-sizing: border-box;
}

.desktop-navigation-links {
  display: flex;
  align-items: center;
  justify-content: center;

  gap: 2rem;
}

.mobile-navigation-links {
  display: none;
}

.navigation-item,
.theme-toggle,
.menu-toggle {
  border: none;
  padding: 0;

  background: transparent;
  color: inherit;

  font: inherit;
  cursor: pointer;
}

.navigation-item {
  font-size: 1.4rem;
}

.navigation-item span {
  margin-right: 0.25rem;
}

.navigation-item:hover,
.navigation-item:focus-visible,
.theme-toggle:hover,
.theme-toggle:focus-visible,
.menu-toggle:hover,
.menu-toggle:focus-visible {
  text-decoration: underline;
}

.navigation-item:focus-visible,
.theme-toggle:focus-visible,
.menu-toggle:focus-visible {
  outline: none;
}

.theme-toggle {
  position: absolute;
  right: 2rem;

  font-size: 1.1rem;
  opacity: 0.7;
}

.menu-toggle {
  display: none;
}


/* =========================
   Tablet
   ========================= */

@media (max-width: 900px) {
  .navigation-header {
    min-height: 60px;
    padding: 1rem;
  }

  .desktop-navigation-links {
    gap: 1rem;
    flex-wrap: wrap;
  }

  .navigation-item {
    font-size: 1.1rem;
  }
}


/* =========================
   Mobile
   ========================= */

@media (max-width: 600px) {
.navigation {
  width: 100%;
  min-height: 10vh;

  display: flex;
  flex-direction: column;

  box-sizing: border-box;
  position: relative;

  flex-shrink: 0; 
}

  .navigation-header {
    width: 100%;
    height: 60px;
    min-height: 60px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    padding: 1rem;

    box-sizing: border-box;
  }

  .desktop-navigation-links {
    display: none;
  }

  .menu-toggle {
    display: block;

    font-size: 1.4rem;
  }

  .theme-toggle {
    position: static;

    font-size: 0.95rem;
  }

  /*
   * This is the important part.
   *
   * The menu is NOT absolute.
   * It is NOT fixed.
   * It occupies real space in the navbar.
   */
  .mobile-navigation-links {
    width: 100%;

    display: flex;
    flex-direction: column;

    gap: 0.25rem;

    padding: 0.5rem 1rem 1rem;

    box-sizing: border-box;
  }

  .mobile-navigation-links .navigation-item {
    width: 100%;

    padding: 0.65rem 0;

    text-align: left;

    font-size: 1rem;
  }
}
</style>
