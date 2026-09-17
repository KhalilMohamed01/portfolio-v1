<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref } from 'vue'

interface Project {
  title: string
  description: string
  highlights: string[]
  technologies: string[]
  github?: string
  demo?: string
}

const projects: Project[] = [
  {
    title: 'AI-Powered Job Application Tracker',
    description:
      'A full-stack platform for centralizing and automating the job search process, from application tracking to AI-assisted CV generation.',
    highlights: [
      'Built a REST API with Spring Boot 4 and Java 17 using a feature-based architecture.',
      'Implemented stateless JWT authentication with Spring Security and BCrypt.',
      'Designed a PostgreSQL database with Spring Data JPA, Hibernate, and dedicated DTOs.',
      'Built a multi-step generative AI pipeline using the OpenAI API to analyze job offers, score candidate experiences, select relevant content, and generate tailored CV content.',
      'Generated customized LaTeX CVs and compiled them into PDF using FreeMarker and pdflatex.',
      'Integrated Microsoft Graph API with OAuth2 to synchronize Outlook job application emails.',
      'Used Ollama to extract structured application data from email content and implemented message-based deduplication.',
      'Developed a Vue 3 frontend using Composition API, TypeScript, Pinia, Vue Router, and Tailwind CSS.',
      'Containerized the entire application with Docker Compose.',
    ],
    technologies: [
      'Java 17',
      'Spring Boot 4',
      'Spring Security',
      'PostgreSQL',
      'JPA / Hibernate',
      'Vue 3',
      'TypeScript',
      'Pinia',
      'Tailwind CSS',
      'OpenAI API',
      'Ollama',
      'Microsoft Graph API',
      'Docker',
    ],
  },

  {
    title: 'School Clubs Management Platform',
    description:
      'A MERN web application designed to help schools manage student clubs while providing students with a central place to discover clubs and upcoming events.',
    highlights: [
      'Built dedicated interfaces for club communication managers and regular students.',
      'Implemented CRUD operations for club events and information.',
      'Added JWT-based authentication and protected user areas.',
      'Created interfaces for managing club members and events.',
      'Developed a student-facing interface for discovering clubs and upcoming events.',
    ],
    technologies: ['MongoDB', 'Express.js', 'React', 'Node.js', 'JWT'],
  },

  {
    title: 'Automotive Sales Forecasting',
    description:
      'A data-driven forecasting application designed to analyze historical automotive sales and predict future sales trends.',
    highlights: [
      'Developed sales forecasting models using SARIMA and Prophet.',
      'Built an Angular dashboard to visualize historical data, statistics, and predictions.',
      'Developed a Flask API to expose the forecasting models and manage data.',
    ],
    technologies: ['Python', 'SARIMA', 'Prophet', 'Flask', 'Angular', 'TypeScript'],
  },

  {
    title: 'School Payment Management Platform',
    description:
      'A web platform designed to simplify school fee management for private schools, allowing parents to track invoices and make payments online.',
    highlights: [
      'Developed an administrative interface for registering students and tracking paid and unpaid invoices.',
      'Implemented automated emails containing account credentials for newly registered parents.',
      'Built a parent interface for viewing children’s invoices and payment status.',
      'Integrated secure online payments using Stripe.',
    ],
    technologies: ['LARAVEL', 'PHP', 'Email Automation', 'Stripe'],
  },
]

const selectedIndex = ref(0)

const selectedProject = computed<Project>(() => {
  const project = projects[selectedIndex.value]

  if (project) {
    return project
  }

  return projects[0]!
})

function selectProject(index: number) {
  selectedIndex.value = index
}

function selectPrevious() {
  selectedIndex.value = selectedIndex.value === 0 ? projects.length - 1 : selectedIndex.value - 1
}

function selectNext() {
  selectedIndex.value = selectedIndex.value === projects.length - 1 ? 0 : selectedIndex.value + 1
}

function handleKeyboard(event: KeyboardEvent) {
  if (event.key === 'ArrowUp' || event.key === 'ArrowLeft') {
    selectPrevious()
  }

  if (event.key === 'ArrowDown' || event.key === 'ArrowRight') {
    selectNext()
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
  <section class="projects">
    <div class="terminal">
      <!-- Command -->
      <p class="command"><span class="prompt">&gt;</span> projects</p>

      <div class="explorer">
        <!-- Project list -->
        <aside class="project-list">
          <p class="list-title">projects/</p>

          <button
            v-for="(project, index) in projects"
            :key="project.title"
            type="button"
            class="project-item"
            :class="{ selected: index === selectedIndex }"
            @click="selectProject(index)"
          >
            <span class="project-number">
              {{ String(index + 1).padStart(2, '0') }}
            </span>

            <span class="project-name">
              {{ project.title }}
            </span>

            <span v-if="index === selectedIndex" class="selection-arrow"> &gt; </span>
          </button>

          <p class="navigation-hint">↑ ↓ select</p>
        </aside>

        <!-- Project details -->
        <main class="project-details">
          <div class="details-header">
            <span class="project-index"> [{{ String(selectedIndex + 1).padStart(2, '0') }}] </span>

            <h2>
              {{ selectedProject.title }}
            </h2>
          </div>

          <div class="separator">─────────────────────────────────</div>

          <p class="label">description</p>

          <p class="description">
            {{ selectedProject.description }}
          </p>

          <p class="label">stack</p>

          <div class="technologies">
            <span
              v-for="technology in selectedProject.technologies"
              :key="technology"
              class="technology"
            >
              {{ technology }}
            </span>
          </div>

          <div class="links">
            <a
              v-if="selectedProject.github"
              :href="selectedProject.github"
              target="_blank"
              rel="noopener noreferrer"
            >
              [ github ]
            </a>

            <a
              v-if="selectedProject.demo"
              :href="selectedProject.demo"
              target="_blank"
              rel="noopener noreferrer"
            >
              [ demo ]
            </a>
          </div>
        </main>
      </div>

      <!-- Bottom navigation -->
      <div class="explorer-footer">
        <button type="button" @click="selectPrevious">← previous</button>

        <span> {{ selectedIndex + 1 }} / {{ projects.length }} </span>

        <button type="button" @click="selectNext">next →</button>
      </div>

      <p class="keyboard-hint">use ↑ ↓ or ← → to explore projects</p>

      <span class="cursor">_</span>
    </div>
  </section>
</template>

<style scoped>
.projects {
  width: 100%;
  height: 90vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  overflow: hidden;
}

.terminal {
  width: min(1200px, 88%);
  font-size: 1.2rem;
}

.command {
  margin: 0 0 2rem;
}

.prompt {
  font-weight: bold;
}

/* Explorer */

.explorer {
  min-height: 430px;
  display: grid;
  grid-template-columns: 280px 1fr;
  border: 1px solid currentColor;
}

/* Project list */

.project-list {
  padding: 1.5rem;
  border-right: 1px dashed currentColor;
}

.list-title {
  margin: 0 0 1.5rem;
  opacity: 0.7;
}

.project-item {
  width: 100%;
  display: grid;
  grid-template-columns: 35px 1fr 15px;
  align-items: center;
  gap: 0.5rem;

  border: none;
  padding: 0.7rem 0;
  background: transparent;
  color: inherit;
  font: inherit;
  text-align: left;
  cursor: pointer;
}

.project-item:hover {
  text-decoration: underline;
}

.project-item.selected {
  font-weight: bold;
}

.project-number {
  opacity: 0.5;
}

.project-name {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.selection-arrow {
  font-weight: bold;
}

.navigation-hint {
  margin: 2rem 0 0;
  font-size: 0.95rem;
  opacity: 0.45;
}

/* Project details */

.project-details {
  min-width: 0;
  padding: 2rem;
}

.details-header {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.project-index {
  opacity: 0.5;
}

h2 {
  margin: 0;
  font-size: 2rem;
  font-weight: normal;
}

.separator {
  margin: 1.5rem 0;
  overflow: hidden;
  white-space: nowrap;
  opacity: 0.4;
}

.label {
  margin: 1.5rem 0 0.5rem;
  opacity: 0.6;
}

.label::before {
  content: '> ';
  opacity: 1;
}

.description {
  max-width: 700px;
  margin: 0;
  line-height: 1.5;
}

.technologies {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.technology {
  border: 1px solid currentColor;
  padding: 0.3rem 0.6rem;
  font-size: 1rem;
}

.links {
  display: flex;
  gap: 1.5rem;
  margin-top: 2rem;
}

.links a {
  color: inherit;
  text-decoration: none;
}

.links a:hover,
.links a:focus-visible {
  text-decoration: underline;
}

.links a:focus-visible {
  outline: none;
}

/* Footer */

.explorer-footer {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  margin-top: 1.5rem;
}

.explorer-footer button {
  border: none;
  padding: 0;
  background: transparent;
  color: inherit;
  font: inherit;
  cursor: pointer;
}

.explorer-footer button:hover,
.explorer-footer button:focus-visible {
  text-decoration: underline;
}

.explorer-footer button:focus-visible {
  outline: none;
}

.explorer-footer span {
  min-width: 50px;
  text-align: center;
}

/* Keyboard hint */

.keyboard-hint {
  margin: 0.75rem 0 0;
  text-align: center;
  font-size: 0.9rem;
  opacity: 0.45;
}

/* Cursor */

.cursor {
  display: block;
  margin-top: 1.25rem;
  animation: blink 1s steps(1) infinite;
}

@keyframes blink {
  50% {
    opacity: 0;
  }
}

/* Mobile */

@media (max-width: 768px) {
  .terminal {
    width: 90%;
    font-size: 1rem;
  }

  .explorer {
    grid-template-columns: 1fr;
    min-height: auto;
  }

  .project-list {
    border-right: none;
    border-bottom: 1px dashed currentColor;
    padding: 1rem;
  }

  .project-item {
    padding: 0.5rem 0;
  }

  .navigation-hint {
    display: none;
  }

  .project-details {
    padding: 1.5rem;
  }

  h2 {
    font-size: 1.6rem;
  }

  .separator {
    margin: 1rem 0;
  }
}
</style>
