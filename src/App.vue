<script setup lang="ts">
import { ref } from 'vue'

import NavigationBar from './components/NavigationBar.vue'
import WhoAmISection from './components/WhoAmISection.vue'
import ExperienceSection from './components/ExperienceSection.vue'
import ProjectSection from './components/ProjectSection.vue'
import EducationSection from './components/EducationSection.vue'
import AskMeAnythingSection from './components/AskMeAnythingSection.vue'

import {
  faLinkedin,
  faGithub,
  faXTwitter,
} from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

type Section = 'who' | 'experience' | 'projects' | 'education' | 'ask'

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
  <div
    class="app"
    :class="{ 'dark-mode': darkMode }"
  >
    <NavigationBar
      :dark-mode="darkMode"
      @navigate="navigateToSection"
      @toggle-theme="toggleTheme"
    />

    <main class="content">
      <WhoAmISection v-if="activeSection === 'who'" />

      <ExperienceSection
        v-else-if="activeSection === 'experience'"
      />

      <ProjectSection
        v-else-if="activeSection === 'projects'"
      />

      <EducationSection
        v-else-if="activeSection === 'education'"
      />

      <AskMeAnythingSection
        v-else-if="activeSection === 'ask'"
      />
    </main>

    <div class="social-links">
      <a
        href="https://www.linkedin.com/in/mohamed-khalil-gi/"
        target="_blank"
        rel="noopener noreferrer"
        aria-label="LinkedIn"
        title="Linkedin"
      >
        <FontAwesomeIcon :icon="faLinkedin" />
      </a>

      <a
        href="https://github.com/KhalilMohamed01"
        target="_blank"
        rel="noopener noreferrer"
        aria-label="GitHub"
        title="GitHub"
      >
        <FontAwesomeIcon :icon="faGithub" />
      </a>

      <a
        href="#"
        target="_blank"
        rel="noopener noreferrer"
        aria-label="X"
        title="X"
      >
        <FontAwesomeIcon :icon="faXTwitter" />
      </a>
    </div>
  </div>
</template>

<style scoped>
.app {
  width: 100%;
  height: 100dvh;
  min-height: 0;

  display: flex;
  flex-direction: column;

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
  flex: 1;
  min-height: 0;
  overflow-y: auto;
}
/* =========================
   Social links
   ========================= */

.social-links {
  position: fixed;

  left: 2rem;
  bottom: 2rem;

  display: flex;
  flex-direction: column;
  gap: 1rem;

  z-index: 50;
}

.social-links a {
  color: inherit;

  font-size: 1.5rem;
  opacity: 0.7;

  transition:
    opacity 0.2s ease,
    transform 0.2s ease;
}

.social-links a:hover {
  opacity: 1;
  transform: translateX(3px);
}


/* =========================
   Mobile
   ========================= */

@media (max-width: 600px) {
  .app {
    height: 100dvh;
    min-height: 100dvh;

    /*
     * The page itself can become taller than the viewport
     * when the navigation menu is open.
     */
    overflow-y: auto;
    overflow-x: hidden;
  }

  .content {
    flex: 0 0 auto;

    /*
     * Let the section determine its own height on mobile.
     */
    min-height: calc(100dvh - 60px);

    overflow: visible;
  }

  .social-links {
    left: 50%;
    bottom: 1rem;

    flex-direction: row;
    gap: 1.25rem;

    transform: translateX(-50%);
  }

  .social-links a:hover {
    transform: none;
  }
}
</style>
