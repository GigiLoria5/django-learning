import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useProductImageStore = defineStore('productImage', () => {
  const isUploading = ref(false)
  const uploadStatus = ref<'idle' | 'success' | 'error'>('idle')
  const errorMessage = ref('')

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
      })
      if (!response.ok) {
        uploadStatus.value = 'error'
        const responseData = await response.json()
        errorMessage.value = responseData.image[0] || 'Failed to upload image'
        return
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

  return { isUploading, uploadStatus, errorMessage, uploadImage, reset }
})
