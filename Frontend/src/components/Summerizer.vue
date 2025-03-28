<template>
    <div class="max-w-xl mx-auto p-6 bg-green-50 rounded-lg shadow-lg">
      <h1 class="text-3xl font-bold text-green-700 text-center mb-6">Summarize Your File</h1>
      
      <form @submit.prevent="uploadFile" class="flex flex-col gap-4">
        <input type="file" ref="fileInput" class="p-3 border-2 border-green-500 rounded-lg bg-green-100 focus:outline-none focus:ring-2 focus:ring-green-300" />
        
        <button type="submit" class="py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 transition duration-200">
          Upload and Summarize
        </button>
      </form>
      
      <div v-if="summary" class="mt-6 p-4 bg-green-100 border-2 border-green-500 rounded-lg">
        <h2 class="text-xl font-semibold text-green-700">Summary:</h2>
        <p>{{ summary }}</p>
      </div>
      
      <div v-if="error" class="mt-6 p-4 bg-red-100 border-2 border-red-500 text-red-700 rounded-lg">
        <p>{{ error }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  
  // Reactive state variables
  const fileInput = ref(null)
  const summary = ref(null)
  const error = ref(null)
  
  // Function to handle the file upload and get the summary
  const uploadFile = async () => {
    const file = fileInput.value.files[0]
  
    if (!file) {
      error.value = 'No file selected.'
      return
    }
  
    // Clear any previous error or summary
    error.value = null
    summary.value = null
  
    const formData = new FormData()
    formData.append('file', file)
  
    try {
      const response = await axios.post('http://localhost:8000/summarize/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      summary.value = response.data.summary
    } catch (err) {
      error.value = err.response?.data?.error || 'An error occurred.'
    }
  }
  </script>
  
  