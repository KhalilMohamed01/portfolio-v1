<script setup lang="ts">
import { ref } from 'vue'
import TypingText from './TypingText.vue'

interface Profile {
  name: string
  role: string
  graduationYear: number
  specialization: string
  introduction: string
}



interface Skill {
  name: string
  category: 'language' | 'framework' | 'database'
}

interface LearningTopic {
  name: string
  focus?: string
}

const profile: Profile = {
  name: 'Mohamed Khalil',
  role: 'Software Engineer',
  graduationYear: 2026,
  specialization: 'Artificial Intelligence',
  introduction:
    'I am a software engineer passionate about building reliable and useful software. During my studies, I gained hands-on experience through three internships and a fixed-term contract, primarily working on full-stack applications.',
}


const skills: Skill[] = [
  { name: 'Java', category: 'language' },
  { name: 'TypeScript', category: 'language' },
  { name: 'Python', category: 'language' },
  { name: 'Spring Boot', category: 'framework' },
  { name: 'Angular', category: 'framework' },
  { name: 'Flask', category: 'framework' },
  { name: 'Vue.js', category: 'framework' },
  { name: 'PostgreSQL', category: 'database' },
]

const currentlyLearning: LearningTopic[] = [
  {
    name: 'AI Engineering',
  },
  {
    name: 'Natural Language Processing',
    focus: 'NLP',
  },
  {
    name: 'Large Language Models',
    focus: 'LLMs',
  },
]

const hobbies: string[] = ['Chess', 'Football', 'Video games']

const showRole = ref(false)
</script>

<template>
  <section class="who-am-i">
    <div class="terminal">
      <p class="command"><span class="prompt">&gt;</span> whoami</p>

    <div class="profile">
      <h1>
        <TypingText
          :text="profile.name"
          :speed="50"
          @finished="showRole = true"
        />
      </h1>

      <p class="role">
        <TypingText
          v-if="showRole"
          :text="`${profile.role} · Class of ${profile.graduationYear}`"
          :speed="40"
        />
      </p>

      <p class="introduction">
        {{ profile.introduction }}
      </p>
    </div>

      <p class="command"><span class="prompt">&gt;</span> skills</p>

      <div class="skills">
        <span v-for="skill in skills" :key="skill.name" class="skill">
          {{ skill.name }}
        </span>
      </div>

      <p class="command"><span class="prompt">&gt;</span> currently-learning</p>

      <div class="learning">
        <span v-for="topic in currentlyLearning" :key="topic.name" class="learning-item">
          {{ topic.name }}
          <span v-if="topic.focus">({{ topic.focus }})</span>
        </span>
      </div>

      <p class="command"><span class="prompt">&gt;</span> hobbies</p>

      <div class="hobbies">
        <span v-for="hobby in hobbies" :key="hobby" class="hobby">
          {{ hobby }}
        </span>
      </div>

      <span class="cursor">_</span>
    </div>
  </section>
</template>

<style scoped>
.who-am-i {
  height: 90vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}

.terminal {
  width: min(1000px, 80%);
  font-size: 1.4rem;
}

.command {
  margin: 0 0 1.25rem;
}

.prompt {
  font-weight: bold;
}

.profile {
  margin-bottom: 2rem;
}

h1 {
  margin: 0;
  font-size: 4rem;
  font-weight: normal;
}

.role {
  margin: 0.5rem 0 1.5rem;
  font-size: 1.6rem;
}

.introduction {
  max-width: 850px;
  line-height: 1.5;
  margin: 0 0 1rem;
}

.experience-summary {
  margin: 0;
}

.skills,
.learning,
.hobbies {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1.5rem;
  margin-bottom: 2rem;
}

.skill::before,
.learning-item::before,
.hobby::before {
  content: '- ';
}

.learning-item span {
  opacity: 0.7;
}

.cursor {
  display: inline-block;
  animation: blink 1s steps(1) infinite;
}

@keyframes blink {
  50% {
    opacity: 0;
  }
}
</style>
