<script setup lang="ts">
import { nextTick, ref } from 'vue'

import { askQuestion } from '../services/api'
import TypingText from './TypingText.vue'

interface Message {
  question: string
  answer: string
}

const question = ref('')
const messages = ref<Message[]>([])
const isLoading = ref(false)
const error = ref('')

const terminalContent = ref<HTMLElement | null>(null)

const scrollToBottom = async () => {
  await nextTick()

  if (terminalContent.value) {
    terminalContent.value.scrollTop = terminalContent.value.scrollHeight
  }
}

const handleAsk = async () => {
  const currentQuestion = question.value.trim()

  if (!currentQuestion || isLoading.value) {
    return
  }

  question.value = ''
  error.value = ''
  isLoading.value = true

  try {
    const data = await askQuestion(currentQuestion)

    messages.value.push({
      question: currentQuestion,
      answer: data.answer,
    })

    await scrollToBottom()
  } catch {
    error.value = 'Something went wrong. Please try again. (╥﹏╥)'
    await scrollToBottom()
  } finally {
    isLoading.value = false
  }
}

const handleTypingFinished = async () => {
  await scrollToBottom()
}
</script>

<template>
  <section class="ask">
    <div class="terminal">
      <div ref="terminalContent" class="terminal-content">
        <div class="terminal-header">
          <p class="command">
            <span class="prompt">&gt;</span> ask-me-anything
          </p>

          <p class="description">
            Have a question? Type it below.
          </p>
        </div>

        <div
          v-for="(message, index) in messages"
          :key="`${message.question}-${index}`"
          class="message"
        >
          <p class="question">
            <span class="prompt">&gt;</span> {{ message.question }}
          </p>

          <p class="answer">
            <TypingText
              v-if="index === messages.length - 1"
              :text="message.answer"
              :speed="25"
              @finished="handleTypingFinished"
            />

            <span v-else>{{ message.answer }}</span>
          </p>
        </div>

        <p v-if="isLoading" class="thinking">
          <span class="prompt">&gt;</span> thinking...
        </p>

        <p v-if="error" class="error">
          {{ error }}
        </p>
      </div>

      <form class="input-line" @submit.prevent="handleAsk">
        <span class="prompt">&gt;</span>

        <input
          v-model="question"
          type="text"
          placeholder="Type your question..."
          autocomplete="off"
          :disabled="isLoading"
        />

        <button type="submit" :disabled="isLoading || !question.trim()">
          {{ isLoading ? '[thinking...]' : '[enter]' }}
        </button>
      </form>
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
  height: 70vh;
  display: flex;
  flex-direction: column;
  font-size: 1.4rem;
}

.terminal-content {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
  padding-right: 1rem;
  scrollbar-width: thin;
}

.terminal-header {
  padding-bottom: 2rem;
}

.command {
  margin: 0 0 2rem;
}

.prompt {
  font-weight: bold;
}

.description {
  margin: 0;
  line-height: 1.4;
}

.message {
  margin-bottom: 2rem;
}

.question {
  margin: 0 0 1rem;
  line-height: 1.4;
}

.answer {
  margin: 0 0 0 1.5rem;
  line-height: 1.5;
  white-space: pre-wrap;
}

.thinking {
  margin: 0 0 2rem;
  opacity: 0.6;
}

.error {
  margin: 0 0 2rem;
  opacity: 0.7;
}

.input-line {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding-top: 1rem;
  flex-shrink: 0;
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

input:disabled {
  opacity: 0.5;
}

button {
  border: none;
  background: transparent;
  color: inherit;
  font: inherit;
  cursor: pointer;
}

button:hover:not(:disabled),
button:focus-visible:not(:disabled) {
  text-decoration: underline;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.cursor {
  display: inline-block;
  margin-top: 0.5rem;
  flex-shrink: 0;
  animation: blink 1s steps(1) infinite;
}

@keyframes blink {
  50% {
    opacity: 0;
  }
}

@media (max-width: 700px) {
  .terminal {
    width: 90%;
    height: 75vh;
    font-size: 1.2rem;
  }

  .answer {
    margin-left: 0.5rem;
  }

  .input-line {
    gap: 0.5rem;
  }

  button {
    font-size: 1.1rem;
  }
}
</style>
