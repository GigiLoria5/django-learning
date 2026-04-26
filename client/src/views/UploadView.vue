<script setup lang="ts">
import { ref } from 'vue'
import { useProductImageStore } from '@/stores/productImage'

const store = useProductImageStore()
const selectedFile = ref<File | null>(null)
const PRODUCT_ID = 1

function onFileChange(event: Event) {
  const input = event.target as HTMLInputElement
  selectedFile.value = input.files?.[0] ?? null
  store.reset()
}

async function handleUpload() {
  if (!selectedFile.value) return
  await store.uploadImage(PRODUCT_ID, selectedFile.value)
  if (store.uploadStatus === 'success') {
    selectedFile.value = null
  }
}
</script>

<template>
  <main class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-md p-10 w-full max-w-md">
      <h1 class="text-2xl font-bold text-gray-900 mb-1">Product Image Upload</h1>
      <p class="text-sm text-gray-400 mb-6">Product #{{ PRODUCT_ID }}</p>

      <!-- File picker -->
      <label
        class="flex flex-col items-center justify-center border-2 border-dashed rounded-xl p-8 cursor-pointer transition-colors mb-4"
        :class="
          selectedFile
            ? 'border-indigo-500 bg-indigo-50 text-indigo-600'
            : 'border-gray-200 text-gray-400 hover:border-indigo-400 hover:bg-indigo-50'
        "
      >
        <input type="file" accept="image/*" class="hidden" @change="onFileChange" />
        <span v-if="!selectedFile" class="text-sm">Click or drag an image here</span>
        <span v-else class="text-sm font-medium break-all text-center">
          📎 {{ selectedFile.name }}
        </span>
      </label>

      <!-- Status messages -->
      <Transition
        enter-active-class="transition-opacity duration-200"
        enter-from-class="opacity-0"
        leave-active-class="transition-opacity duration-200"
        leave-to-class="opacity-0"
      >
        <div
          v-if="store.uploadStatus === 'success'"
          class="text-sm font-medium px-4 py-3 rounded-lg bg-emerald-50 text-emerald-700 mb-4"
        >
          ✓ Image uploaded successfully
        </div>
      </Transition>

      <Transition
        enter-active-class="transition-opacity duration-200"
        enter-from-class="opacity-0"
        leave-active-class="transition-opacity duration-200"
        leave-to-class="opacity-0"
      >
        <div
          v-if="store.uploadStatus === 'error'"
          class="text-sm font-medium px-4 py-3 rounded-lg bg-red-50 text-red-700 mb-4"
        >
          ✗ {{ store.errorMessage }}
        </div>
      </Transition>

      <!-- Upload button -->
      <button
        class="w-full py-3 rounded-xl text-sm font-semibold text-white transition-colors"
        :class="
          !selectedFile || store.isUploading
            ? 'bg-indigo-300 cursor-not-allowed'
            : 'bg-indigo-600 hover:bg-indigo-700'
        "
        :disabled="!selectedFile || store.isUploading"
        @click="handleUpload"
      >
        <span v-if="store.isUploading">Uploading…</span>
        <span v-else>Upload Image</span>
      </button>
    </div>
  </main>
</template>
