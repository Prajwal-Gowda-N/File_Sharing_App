<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-200 to-green-500">
    <div class="p-8 bg-white rounded-xl shadow-2xl w-full max-w-lg transform transition-all hover:scale-105 hover:shadow-xl duration-300">
      <h2 class="text-2xl font-semibold text-center text-gray-800 mb-6">Upload Your File</h2>
      
      <form @submit.prevent="submitFile" class="space-y-4">
        <div>
          <input
            v-model="fileName"
            type="text"
            placeholder="Enter file name"
            class="w-full p-3 border-2 border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:outline-none text-gray-700"
            required
          />
        </div>
        
        <div>
          <input
            type="file"
            @change="handleFileUpload"
            class="w-full p-3 border-2 border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:outline-none"
            required
          />
        </div>
        
        <div>
          <button
            type="submit"
            class="w-full py-3 bg-green-600 text-white font-semibold rounded-lg hover:bg-green-700 transition duration-300"
          >
            Upload File
          </button>
        </div>
      </form>
  
      <!-- Display the file URL after upload -->
      <div v-if="fileUrl" class="mt-6 p-6 bg-gray-50 rounded-lg border-2 border-gray-200 text-center">
        <p class="text-green-600 font-bold">File Uploaded Successfully!</p>
        <p class="mt-2 text-blue-600 break-all">{{ fileUrl }}</p>
        
        <!-- Email input for sending URL -->
        <div v-if="fileUrl && !emailSent" class="mt-4">
          <input
            v-model="email"
            type="email"
            placeholder="Enter your email"
            class="w-full p-3 border-2 border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:outline-none"
            required
          />
          <button
            @click="sendUrlToEmail"
            class="mt-4 py-2 px-4 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 transition duration-300"
          >
            Send URL to Email
          </button>
        </div>
        
        <!-- Confirmation message -->
        <div v-if="emailSent" class="mt-4 text-green-600 font-semibold">
          <p>Email sent successfully!</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  setup() {
    const fileName = ref('');
    const file = ref(null);
    const fileUrl = ref('');
    const email = ref('');
    const emailSent = ref(false);

    const handleFileUpload = (event) => {
      file.value = event.target.files[0];
    };

    const submitFile = async () => {
      if (!file.value) return;
      const formData = new FormData();
      formData.append('file_name', fileName.value);
      formData.append('file', file.value);

      try {
        const response = await axios.post('http://localhost:8000/api/upload/', formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        });

        fileUrl.value = response.data.file_url; // Store the actual file URL
        console.log('File uploaded:', response.data);
      } catch (error) {
        console.error('Upload failed:', error);
      }
    };

    const sendUrlToEmail = async () => {
      if (!email.value) return;

      try {
        const response = await axios.post('http://localhost:8000/api/send-email/', {
          email: email.value,
          file_url: fileUrl.value
        });

        if (response.status === 200) {
          emailSent.value = true;
        }
      } catch (error) {
        console.error('Error sending email:', error);
        alert("Enter a valid email Id")
      }
    };

    return {
      fileName,
      file,
      fileUrl,
      email,
      emailSent,
      handleFileUpload,
      submitFile,
      sendUrlToEmail
    };
  }
};
</script>
