<template>
    <div class="min-h-screen bg-gray-100 py-8">
      <div class="max-w-4xl mx-auto px-4">
        <h1 class="text-3xl font-bold text-gray-800 mb-8">Document Converter</h1>
        
        <div class="grid md:grid-cols-2 gap-6">
          <!-- Word to PDF Converter -->
          <div class="bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-xl font-semibold mb-4">Word to PDF</h2>
            <input 
              type="file" 
              @change="handleFileUpload($event, 'word_to_pdf')"
              accept=".docx,.doc"
              class="mb-4 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
            />
            <button 
              @click="convertFile('word_to_pdf')"
              :disabled="!files.word_to_pdf"
              class="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Convert to PDF
            </button>
          </div>
  
          <!-- PDF to Word Converter -->
          <div class="bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-xl font-semibold mb-4">PDF to Word</h2>
            <input 
              type="file" 
              @change="handleFileUpload($event, 'pdf_to_word')"
              accept=".pdf"
              class="mb-4 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-green-50 file:text-green-700 hover:file:bg-green-100"
            />
            <button 
              @click="convertFile('pdf_to_word')"
              :disabled="!files.pdf_to_word"
              class="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Convert to Word
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  
  const files = ref({
    word_to_pdf: null,
    pdf_to_word: null
  });
  
  // Handle file upload and save the file in the state based on the type
  const handleFileUpload = (event, type) => {
    files.value[type] = event.target.files[0];
  };
  
  // Function to handle file conversion
  const convertFile = async (type) => {
    const formData = new FormData();
    formData.append('file', files.value[type]);
    formData.append('type', type);
  
    try {
      // Make the request to the backend for file conversion
      const response = await axios.post('http://localhost:8000/api/convert/', formData, {
        responseType: 'blob'
      });
  
      // Handle file download once conversion is successful
      const downloadUrl = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = downloadUrl;
      link.setAttribute('download', `converted.${type.split('_to_')[1]}`);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (error) {
      console.error('Conversion error:', error);
    }
  };
  </script>
  
  <style scoped>
  /* Scoped styles for the document converter */
  </style>
  