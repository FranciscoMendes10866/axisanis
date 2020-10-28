<template>
  <div class="hero is-fullheight has-text-centered bg-main">
    <div class="hero-body">
      <div class="container">
        <div class="cloumns">
          <div class="column">
            <Node />
          </div>
          <div class="column">
            <Go />
          </div>
          <div class="column">
            <Python />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Node from "./components/Node.vue";
import Go from "./components/Go.vue";
import Python from "./components/Python.vue";

export default defineComponent({
  components: {
    Node,
    Go,
    Python
  }
});
</script>
