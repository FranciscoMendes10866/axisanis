<template>
  <div class="card bg-card">
    <div class="card-content">
      <p class="is-size-5">
        {{ state.python }}
      </p>
      <small class="is-size-6 has-text-weight-bold">
        Python
      </small>
      <span class="tag bg-tag is-medium mt-4">Bottle API</span>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, onMounted } from "vue";
import axios from "axios";

export default defineComponent({
  setup() {
    const state = reactive({
      python: null
    });
    async function Fetch() {
      await axios.get("http://localhost/python-api").then(res => {
        state.python = res.data;
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
