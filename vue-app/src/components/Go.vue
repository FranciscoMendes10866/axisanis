<template>
  <div class="card bg-card">
    <div class="card-content">
      <p class="is-size-5">
        {{ state.go }}
      </p>
      <small class="is-size-6 has-text-weight-bold">
        Go
      </small>
      <span class="tag bg-tag is-medium mt-4">Fiber API</span>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, onMounted } from "vue";
import axios from "axios";

export default defineComponent({
  setup() {
    const state = reactive({
      go: null
    });
    async function Fetch() {
      await axios.get("http://localhost/go-api").then(res => {
        state.go = res.data;
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

