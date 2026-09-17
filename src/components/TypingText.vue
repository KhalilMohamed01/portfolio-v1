<script setup lang="ts">
import { onMounted,ref } from 'vue'

interface Props {
  text: string
  speed?: number
}
const displayedText = ref('')
const props = withDefaults(defineProps<Props>(), {
  speed: 30,
})

function typeText() {
  if (displayedText.value.length >= props.text.length) {
    return
  }

  displayedText.value = props.text.slice(
    0,
    displayedText.value.length + 1,
  )

  setTimeout(typeText, props.speed)
}

onMounted(() => {
  typeText()
})
</script>

<template>
  <span>{{ displayedText }}</span>
</template>
