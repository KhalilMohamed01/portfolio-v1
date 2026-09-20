<script setup lang="ts">
interface Education {
  degree: string
  field: string
  institution: string
  startDate: string
  endDate: string
  location: string
}

const education: Education[] = [
  {
    degree: 'Engineering Degree',
    field: 'Computer Science',
    institution: 'École d’Ingénieurs du Littoral-Côte-d’Opale',
    startDate: 'Sep. 2022',
    endDate: 'Dec. 2025',
    location: 'Calais, France',
  },
  {
    degree: 'Professional Bachelor’s Degree',
    field: 'Computer Science',
    institution: 'École Supérieure de Technologie',
    startDate: 'Sep. 2021',
    endDate: 'Jun. 2022',
    location: 'Casablanca, Morocco',
  },
  {
    degree: 'University Diploma of Technology',
    field: 'Computer Science',
    institution: 'École Supérieure de Technologie',
    startDate: 'Sep. 2019',
    endDate: 'Jun. 2021',
    location: 'Casablanca, Morocco',
  },
]
</script>

<template>
  <section class="education">
    <div class="terminal">
      <p class="command">
        <span class="prompt">&gt;</span>
        education
      </p>

      <div class="education-list">
        <article
          v-for="(item, index) in education"
          :key="`${item.degree}-${item.startDate}`"
          class="education-item"
        >
          <div class="education-index">
            [{{ String(index + 1).padStart(2, '0') }}]
          </div>

          <div class="education-content">
            <div class="education-header">
              <div class="education-title">
                <h2>{{ item.degree }}</h2>

                <p class="field">
                  {{ item.field }}
                </p>
              </div>

              <div class="dates">
                {{ item.startDate }} — {{ item.endDate }}
              </div>
            </div>

            <p class="institution">
              {{ item.institution }}
            </p>

            <p class="location">
              {{ item.location }}
            </p>
          </div>
        </article>
      </div>

      <p class="summary">
        <span>&gt;</span>
        {{ education.length }} degrees · Computer Science
      </p>

      <span class="cursor">_</span>
    </div>
  </section>
</template>

<style scoped>
.education {
  width: 100%;
  height: 100%;
  min-height: 0;
  display: flex;
  box-sizing: border-box;
  overflow: hidden;
}

.terminal {
  width: min(1000px, 80%);
  margin: auto;
  font-size: 1.3rem;
}

.command {
  margin: 0 0 1.5rem;
}

.prompt {
  font-weight: bold;
}

.education-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.education-item {
  display: grid;
  grid-template-columns: 45px minmax(0, 1fr);

  gap: 0.75rem;

  border-left: 2px dashed currentColor;

  padding: 0.6rem 0 0.6rem 1rem;

  box-sizing: border-box;
}

.education-index {
  padding-top: 0.15rem;
  opacity: 0.5;
}

.education-content {
  min-width: 0;
}

.education-header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;

  gap: 1.5rem;
}

.education-title {
  min-width: 0;
}

h2 {
  margin: 0;

  font-size: 1.7rem;
  font-weight: normal;

  line-height: 1.2;
}

.field {
  margin: 0.1rem 0 0;

  opacity: 0.6;
}

.dates {
  flex-shrink: 0;

  font-size: 1rem;
  white-space: nowrap;

  opacity: 0.7;
}

.institution {
  margin: 0.5rem 0 0.1rem;

  line-height: 1.3;
}

.location {
  margin: 0;

  font-size: 1rem;

  opacity: 0.6;
}

.summary {
  margin: 1.25rem 0 0;

  opacity: 0.65;
}

.summary span {
  margin-right: 0.3rem;
}

.cursor {
  display: inline-block;

  margin-top: 1rem;

  animation: blink 1s steps(1) infinite;
}

@keyframes blink {
  50% {
    opacity: 0;
  }
}


/* =========================
   Tablet
   ========================= */

@media (max-width: 768px) {
  .education {
    align-items: center;
  }

  .terminal {
    width: 90%;
    font-size: 1.1rem;
  }

  .education-list {
    gap: 0.75rem;
  }

  .education-item {
    grid-template-columns: 35px minmax(0, 1fr);

    gap: 0.5rem;

    padding: 0.5rem 0 0.5rem 0.75rem;
  }

  .education-header {
    flex-direction: column;
    align-items: flex-start;

    gap: 0.2rem;
  }

  h2 {
    font-size: 1.4rem;
  }

  .dates {
    font-size: 0.9rem;
  }

  .institution {
    margin-top: 0.35rem;
  }

  .location {
    font-size: 0.9rem;
  }

  .summary {
    margin-top: 1rem;
  }
}


/* =========================
   Small Mobile
   ========================= */

@media (max-width: 480px) {
  .education {
    align-items: flex-start;

    padding-top: 1.25rem;
  }

  .terminal {
    width: calc(100% - 2rem);
    font-size: 0.95rem;
  }

  .command {
    margin-bottom: 1rem;
  }

  .education-list {
    gap: 0.5rem;
  }

  .education-item {
    grid-template-columns: 30px minmax(0, 1fr);

    gap: 0.4rem;

    padding: 0.35rem 0 0.35rem 0.5rem;
  }

  .education-index {
    padding-top: 0.1rem;
  }

  h2 {
    font-size: 1.15rem;
    line-height: 1.2;
  }

  .field {
    margin-top: 0.1rem;
    font-size: 0.85rem;
  }

  .dates {
    font-size: 0.78rem;
  }

  .institution {
    margin-top: 0.25rem;

    font-size: 0.9rem;
    line-height: 1.25;
  }

  .location {
    font-size: 0.78rem;
  }

  .summary {
    margin-top: 0.75rem;
    font-size: 0.85rem;
  }

  .cursor {
    margin-top: 0.5rem;
  }
}
</style>

