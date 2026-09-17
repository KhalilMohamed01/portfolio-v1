<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref } from 'vue'

interface Experience {
  company: string
  role: string
  type: string
  startDate: string
  endDate: string
  location: string
  responsibilities: string[]
  technologies: string[]
}

const experiences: Experience[] = [
  {
    company: 'SAD Marketing',
    role: 'Web Developer',
    type: 'Fixed-term contract',
    startDate: 'Dec. 2025',
    endDate: 'Jan. 2026',
    location: 'Villeneuve-d’Ascq',
    responsibilities: [
      'Automated the import and processing of customer data using Python with data consistency checks.',
      'Implemented automated notifications and workflows for data import and verification.',
    ],
    technologies: ['Python'],
  },
  {
    company: 'SAD Marketing',
    role: 'Web Developer',
    type: 'Final-year internship',
    startDate: 'May 2025',
    endDate: 'Nov. 2025',
    location: 'Villeneuve-d’Ascq',
    responsibilities: [
      'Designed and developed a time-management application with Vue.js on the frontend and Flask on the backend.',
      'Developed REST APIs with Flask for CRUD operations and business logic.',
      'Designed the PostgreSQL database and migrated data from the previous schema.',
      'Performed functional testing, fixed issues, and prepared the application for production.',
    ],
    technologies: ['Vue.js', 'Flask', 'Python', 'PostgreSQL', 'REST API'],
  },
  {
    company: 'Walden Digital',
    role: 'Frontend Developer',
    type: 'Internship',
    startDate: 'Jun. 2024',
    endDate: 'Sep. 2024',
    location: 'Cournon-d’Auvergne',
    responsibilities: [
      'Redesigned the frontend using Angular and TypeScript based on Figma designs.',
      'Integrated the frontend with Flask APIs using HTTP requests and handled client-side errors.',
      'Applied modularity and reusability best practices across the frontend.',
    ],
    technologies: ['Angular', 'TypeScript', 'Flask', 'REST API'],
  },
  {
    company: 'RABBAH SOFT',
    role: 'Full-Stack Developer',
    type: 'Internship',
    startDate: 'Apr. 2022',
    endDate: 'Jun. 2022',
    location: 'Casablanca',
    responsibilities: [
      'Designed and developed a full-stack ticket management application using Angular and Spring Boot.',
      'Implemented REST APIs with Spring Boot following a Controller / Service / Repository architecture.',
      'Designed the PostgreSQL database and implemented CRUD operations and persistence with JPA.',
      'Wrote and executed functional API and UI tests and fixed identified issues.',
    ],
    technologies: [
      'Java',
      'Spring Boot',
      'Angular',
      'PostgreSQL',
      'JPA',
    ],
  },
]

const currentPage = ref(0)

const totalPages = computed(() => experiences.length)

const currentExperience = computed(() => experiences[currentPage.value])

const hasPrevious = computed(() => currentPage.value > 0)

const hasNext = computed(() => currentPage.value < totalPages.value - 1)

const remainingPages = computed(() => totalPages.value - currentPage.value - 1)

function goToPrevious() {
  if (hasPrevious.value) {
    currentPage.value--
  }
}

function goToNext() {
  if (hasNext.value) {
    currentPage.value++
  }
}

function handleKeyboard(event: KeyboardEvent) {
  if (event.key === 'ArrowLeft') {
    goToPrevious()
  }

  if (event.key === 'ArrowRight') {
    goToNext()
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleKeyboard)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeyboard)
})
</script>

<template>
  <section class="experience">
    <div class="terminal">
      <!-- Command -->
      <p class="command">
        <span class="prompt">&gt;</span> experience
      </p>

      <!-- Experience -->
      <article class="experience-card">
        <div class="experience-header">
          <div>
            <h2>{{ currentExperience.role }}</h2>

            <p class="company">
              {{ currentExperience.company }}
              ·
              {{ currentExperience.type }}
            </p>
          </div>

          <div class="metadata">
            <span>
              {{ currentExperience.startDate }}
              —
              {{ currentExperience.endDate }}
            </span>

            <span>
              {{ currentExperience.location }}
            </span>
          </div>
        </div>

        <ul class="responsibilities">
          <li
            v-for="responsibility in currentExperience.responsibilities"
            :key="responsibility"
          >
            {{ responsibility }}
          </li>
        </ul>

        <p class="technologies">
          [
          <span
            v-for="(technology, index) in currentExperience.technologies"
            :key="technology"
          >
            {{ technology }}
            <span v-if="index < currentExperience.technologies.length - 1">
              ·
            </span>
          </span>
          ]
        </p>
      </article>

      <!-- Pagination -->
      <div class="pagination">
        <button
          type="button"
          class="pagination-button"
          :class="{ disabled: !hasPrevious }"
          :disabled="!hasPrevious"
          @click="goToPrevious"
        >
          ← previous
        </button>

        <div class="page-indicator">
          <span>[</span>

          <strong>
            {{ currentPage + 1 }}
          </strong>

          <span>/</span>

          <span>
            {{ totalPages }}
          </span>

          <span>]</span>
        </div>

        <button
          type="button"
          class="pagination-button"
          :class="{ disabled: !hasNext }"
          :disabled="!hasNext"
          @click="goToNext"
        >
          next →
        </button>
      </div>

      <!-- More content indicator -->
      <p v-if="remainingPages > 0" class="more-indicator">
        <span class="arrow">↓</span>
        {{ remainingPages }}
        {{ remainingPages === 1 ? 'more experience' : 'more experiences' }}
      </p>

      <p v-else class="more-indicator">
        <span class="arrow">✓</span>
        end of experience
      </p>

      <!-- Keyboard hint -->
      <p class="keyboard-hint">
        use
        <span>←</span>
        <span>→</span>
        to navigate
      </p>

      <span class="cursor">_</span>
    </div>
  </section>
</template>

<style scoped>
.experience {
  width: 100%;
  height: 90vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  overflow: hidden;
}

.terminal {
  width: min(1100px, 85%);
  font-size: 1.2rem;
}

.command {
  margin: 0 0 2rem;
}

.prompt {
  font-weight: bold;
}

/* Experience */

.experience-card {
  min-height: 340px;
  border-left: 2px dashed currentColor;
  padding: 1.5rem 2rem;
  box-sizing: border-box;
}

.experience-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 2rem;
}

h2 {
  margin: 0;
  font-size: 2rem;
  font-weight: normal;
}

.company {
  margin: 0.4rem 0 0;
}

.metadata {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.25rem;
  font-size: 1rem;
  white-space: nowrap;
}

.responsibilities {
  max-width: 850px;
  margin: 2rem 0 1.5rem;
  padding-left: 1.5rem;
  line-height: 1.4;
}

.responsibilities li {
  margin-bottom: 0.75rem;
}

.technologies {
  margin: 0;
  font-size: 1rem;
}

/* Pagination */

.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  margin-top: 2rem;
}

.pagination-button {
  border: none;
  padding: 0;
  background: transparent;
  color: inherit;
  font: inherit;
  font-size: 1.1rem;
  cursor: pointer;
}

.pagination-button:hover:not(:disabled),
.pagination-button:focus-visible:not(:disabled) {
  text-decoration: underline;
}

.pagination-button:focus-visible {
  outline: none;
}

.pagination-button.disabled,
.pagination-button:disabled {
  opacity: 0.3;
  cursor: default;
}

.page-indicator {
  min-width: 70px;
  display: flex;
  justify-content: center;
  gap: 0.25rem;
}

.page-indicator strong {
  font-weight: normal;
}

/* More indicator */

.more-indicator {
  margin: 1.5rem 0 0;
  text-align: center;
  font-size: 1rem;
  opacity: 0.7;
}

.arrow {
  display: inline-block;
  margin-right: 0.4rem;
}

/* Keyboard hint */

.keyboard-hint {
  margin: 0.75rem 0 0;
  text-align: center;
  font-size: 0.9rem;
  opacity: 0.45;
}

.keyboard-hint span {
  margin: 0 0.15rem;
}

/* Cursor */

.cursor {
  display: block;
  margin-top: 1.5rem;
  animation: blink 1s steps(1) infinite;
}

@keyframes blink {
  50% {
    opacity: 0;
  }
}

/* Smaller screens */

@media (max-width: 768px) {
  .terminal {
    width: 90%;
    font-size: 1rem;
  }

  .experience-card {
    padding: 1rem;
  }

  .experience-header {
    flex-direction: column;
    gap: 1rem;
  }

  .metadata {
    align-items: flex-start;
  }

  h2 {
    font-size: 1.6rem;
  }

  .responsibilities {
    margin-top: 1.5rem;
  }

  .pagination {
    gap: 1rem;
  }
}
</style>
