import {ref} from 'vue'
import {defineStore} from 'pinia'

// defineStore('id', setupFn) — the setup syntax mirrors Vue's Composition API
// which makes it feel natural coming from React hooks
export const useProductImageStore = defineStore('productImage', () => {
  // STATE — equivalent to useState in React
  const isUploading = ref(false)
  const uploadStatus = ref<'idle' | 'success' | 'error'>('idle')
  const errorMessage = ref('')

  // ACTION — a plain async function; Pinia makes it reactive automatically
  async function uploadImage(productId: number, file: File) {
    const formData = new FormData()
    formData.append('image', file)

    isUploading.value = true
    uploadStatus.value = 'idle'
    errorMessage.value = ''

    try {
      const response = await fetch(`/api/store/products/${productId}/images/`, {
        method: 'POST',
        body: formData,
        // Never set Content-Type manually with FormData —
        // the browser must set it so it includes the multipart boundary
      })

      if (!response.ok) {
        throw new Error(`Upload failed — server returned ${response.status}`)
      }

      uploadStatus.value = 'success'
    } catch (err) {
      uploadStatus.value = 'error'
      errorMessage.value = err instanceof Error ? err.message : 'Unknown error'
    } finally {
      isUploading.value = false
    }
  }

  function reset() {
    uploadStatus.value = 'idle'
    errorMessage.value = ''
  }

  // Everything you return here is accessible in any component via the store
  return {isUploading, uploadStatus, errorMessage, uploadImage, reset}
})
