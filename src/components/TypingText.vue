<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'

interface Props {
  text: string
  speed?: number
}

const props = withDefaults(defineProps<Props>(), {
  speed: 50,
})

const emit = defineEmits<{
  finished: []
}>()

const displayedText = ref('')

let timer: ReturnType<typeof setTimeout> | null = null

function typeText() {
  if (displayedText.value.length >= props.text.length) {
    emit('finished')
    return
  }

  displayedText.value = props.text.slice(
    0,
    displayedText.value.length + 1,
  )

  timer = setTimeout(typeText, props.speed)
}

onMounted(() => {
  typeText()
})

onUnmounted(() => {
  if (timer) {
    clearTimeout(timer)
  }
})
</script>

<template>
  <span>{{ displayedText }}</span>
</template>
