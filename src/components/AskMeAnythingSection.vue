<script setup lang="ts">
import { ref } from 'vue'

const question = ref('')
</script>

<template>
  <section class="ask">
    <div class="terminal">
      <p class="command">
        <span class="prompt">&gt;</span> ask-me-anything
      </p>

      <p class="description">
        Have a question? Type it below.
      </p>

      <form class="input-line" @submit.prevent>
        <span class="prompt">&gt;</span>

        <input
          v-model="question"
          type="text"
          placeholder="Type your question..."
          autocomplete="off"
        />

        <button type="submit">[enter]</button>
      </form>

      <span class="cursor">_</span>
    </div>
  </section>
</template>

<style scoped>
.ask {
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
  margin: 0 0 2rem;
}

.prompt {
  font-weight: bold;
}

.description {
  margin: 0 0 2rem;
  line-height: 1.4;
}

.input-line {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

input {
  flex: 1;
  min-width: 0;
  border: none;
  outline: none;
  background: transparent;
  color: inherit;
  font: inherit;
  caret-color: currentColor;
}

input::placeholder {
  color: inherit;
  opacity: 0.5;
}

button {
  border: none;
  background: transparent;
  color: inherit;
  font: inherit;
  cursor: pointer;
}

button:hover,
button:focus {
  text-decoration: underline;
}

.cursor {
  display: inline-block;
  margin-top: 2rem;
  animation: blink 1s steps(1) infinite;
}

@keyframes blink {
  50% {
    opacity: 0;
  }
}
</style>
