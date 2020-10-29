<template>
  <div class="card bg-card">
    <div class="card-content">
      <p class="is-size-5">
        {{ state.node }}
      </p>
      <small class="is-size-6 has-text-weight-bold">
        Node
      </small>
      <span class="tag bg-tag is-medium mt-4">Fastify API</span>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, onMounted } from "vue";
import axios from "axios";

export default defineComponent({
  setup() {
    const state = reactive({
      node: null
    });
    async function Fetch() {
      await axios.get("http://localhost/node-api").then(res => {
        state.node = res.data;
      });
    }
    onMounted(Fetch);
    return {
      state,
      Fetch
    };
  }
});
</script>
