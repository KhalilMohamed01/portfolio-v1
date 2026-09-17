
<script setup lang="ts">
import NavigationBar from './components/NavigationBar.vue';
</script>

<template>
  <NavigationBar />

  <main>
    <section id="who">
      <div class="tag">// section 01</div>

      <h1>
        Your Name<span class="blink">_</span>
      </h1>

      <p>
        A short line about who you are and what you do.
      </p>
    </section>

    <section id="experience">
      <div class="tag">// section 02</div>

      <h1>Experience</h1>

      <p>
        Your experience goes here.
      </p>
    </section>

    <section id="projects">
      <div class="tag">// section 03</div>

      <h1>Projects</h1>

      <p>
        Your projects go here.
      </p>
    </section>

    <section id="education">
      <div class="tag">// section 04</div>

      <h1>Education</h1>

      <p>
        Your education goes here.
      </p>
    </section>

    <section id="ask">
      <div class="tag">// section 05</div>

      <h1>Ask me anything</h1>

      <p>
        Contact information goes here.
      </p>
    </section>
  </main>
</template>

