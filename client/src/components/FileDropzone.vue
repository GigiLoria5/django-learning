<script setup lang="ts">
import { ref } from 'vue'

defineProps<{
  modelFile: File | null
}>()

const emit = defineEmits<{
  'file-change': [file: File | null]
}>()

const isDragging = ref(false)

function onFileChange(event: Event) {
  const input = event.target as HTMLInputElement
  emit('file-change', input.files?.[0] ?? null)
}

function onDrop(event: DragEvent) {
  isDragging.value = false
  const file = event.dataTransfer?.files?.[0] ?? null
  if (file && file.type.startsWith('image/')) {
    emit('file-change', file)
  }
}

function onDragOver(event: DragEvent) {
  event.preventDefault()
  isDragging.value = true
}

function onDragLeave() {
  isDragging.value = false
}
</script>

<template>
  <label
    class="flex flex-col items-center justify-center border-2 border-dashed rounded-xl p-8 cursor-pointer transition-all duration-200 select-none"
    :class="{
      'border-indigo-500 bg-indigo-50 text-indigo-600 scale-[1.01]': isDragging,
      'border-indigo-400 bg-indigo-50 text-indigo-600': modelFile && !isDragging,
      'border-gray-200 text-gray-400 hover:border-indigo-400 hover:bg-indigo-50':
        !modelFile && !isDragging,
    }"
    @dragover="onDragOver"
    @dragleave="onDragLeave"
    @drop.prevent="onDrop"
  >
    <input type="file" accept="image/*" class="hidden" @change="onFileChange" />

    <!-- Icon -->
    <div
      class="mb-3 p-3 rounded-full transition-colors"
      :class="modelFile || isDragging ? 'bg-indigo-100' : 'bg-gray-100'"
    >
      <svg
        class="w-6 h-6 transition-colors"
        :class="modelFile || isDragging ? 'text-indigo-500' : 'text-gray-400'"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
      >
        <!-- Switches icon depending on state -->
        <path
          v-if="!modelFile"
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5"
        />
        <path
          v-else
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
        />
      </svg>
    </div>

    <!-- Text -->
    <p v-if="!modelFile" class="text-sm font-medium">
      {{ isDragging ? 'Drop it!' : 'Click or drag an image here' }}
    </p>
    <template v-else>
      <p class="text-sm font-semibold break-all text-center max-w-50 truncate">
        {{ modelFile.name }}
      </p>
      <p class="text-xs mt-1 text-indigo-400">
        {{ (modelFile.size / 1024).toFixed(1) }} KB · Click to change
      </p>
    </template>
  </label>
</template>
