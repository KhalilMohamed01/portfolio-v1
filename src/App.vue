<script setup lang="ts">
import { ref } from 'vue'

import NavigationBar from './components/NavigationBar.vue'
import WhoAmISection from './components/WhoAmISection.vue'
import ExperienceSection from './components/ExperienceSection.vue'
import ProjectSection from './components/ProjectSection.vue'
import EducationSection from './components/EducationSection.vue'
import AskMeAnythingSection from './components/AskMeAnythingSection.vue'

type Section =
  | 'who'
  | 'experience'
  | 'projects'
  | 'education'
  | 'ask'

const activeSection = ref<Section>('who')
const darkMode = ref(true)

function navigateToSection(section: string) {
  activeSection.value = section as Section
}

function toggleTheme() {
  darkMode.value = !darkMode.value
}
</script>

<template>

  <div class="app" :class="{ 'dark-mode': darkMode }">
    <NavigationBar
      :dark-mode="darkMode"
      @navigate="navigateToSection"
      @toggle-theme="toggleTheme"
    />

    <main class="content">
      <WhoAmISection v-if="activeSection === 'who'" />

      <ExperienceSection v-else-if="activeSection === 'experience'" />

      <ProjectSection v-else-if="activeSection === 'projects'" />

      <EducationSection v-else-if="activeSection === 'education'" />

      <AskMeAnythingSection v-else-if="activeSection === 'ask'" />
    </main>
  </div>
</template>

<style scoped>
.app {
  width: 100%;
  height: 100vh;
  overflow: hidden;

  background: #f5f5f5;
  color: #111;
  transition:
    background-color 0.2s ease,
    color 0.2s ease;
}

.app.dark-mode {
  background: #111;
  color: #f5f5f5;
}

.content {
  width: 100%;
  height: 90vh;
  overflow: hidden;
}
</style>
