<script setup lang="ts">
import { ref } from 'vue'
import { useProductImageStore } from '@/stores/productImage'
import BaseButton from '@/components/BaseButton.vue'
import FileDropzone from '@/components/FileDropzone.vue'

const store = useProductImageStore()
const selectedFile = ref<File | null>(null)
const PRODUCT_ID = 1

function onFileChange(file: File | null) {
  selectedFile.value = file
  store.reset()
}

async function handleUpload() {
  if (!selectedFile.value) return
  await store.uploadImage(PRODUCT_ID, selectedFile.value)
  if (store.uploadStatus === 'success') selectedFile.value = null
}
</script>

<template>
  <main class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-md p-10 w-full max-w-md">
      <h1 class="text-2xl font-bold text-gray-900 mb-1">Product Image Upload</h1>
      <p class="text-sm text-gray-400 mb-6">Product #{{ PRODUCT_ID }}</p>

      <FileDropzone :modelFile="selectedFile" class="mb-4" @file-change="onFileChange" />

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

      <BaseButton :loading="store.isUploading" :disabled="!selectedFile" @click="handleUpload">
        Upload Image
      </BaseButton>
    </div>
  </main>
</template>
