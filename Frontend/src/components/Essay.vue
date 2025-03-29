<template>
    <div class="editor-container">
      <h1 class="title">Essay Editor</h1>
      <div class="form-container">
        <input
          v-model="document.title"
          class="input-field"
          placeholder="Enter essay title"
        />
        <textarea
          v-model="document.content"
          class="input-field"
          rows="10"
          placeholder="Enter essay content"
        ></textarea>
        <button @click="generateWordDocument" class="generate-btn">
          Generate Essay Word Document
        </button>
      </div>
      <div v-if="isGenerating" class="loading">
        <span>Generating Essay...</span>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        document: {
          title: "",  // Default title as "Essay"
          content: ""
        },
        isGenerating: false // To show a loading state when generating the document
      };
    },
    methods: {
      async generateWordDocument() {
        if (!this.document.content || !this.document.title) {
          alert("Please provide both title and content.");
          return;
        }
  
        this.isGenerating = true;
  
        try {
          const response = await axios.post(
            "http://localhost:8000/api/generate-word/",
            this.document,
            {
              responseType: "blob" // Set responseType to blob to handle file download
            }
          );
  
          // Create a link to trigger the download
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement("a");
          link.href = url;
          link.setAttribute("download", `${this.document.title}.docx`);
          document.body.appendChild(link);
          link.click();
  
          // Clean up the URL object after downloading
          window.URL.revokeObjectURL(url);
        } catch (error) {
          console.error("Error generating Word document:", error);
        } finally {
          this.isGenerating = false;
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* General Styles */
  .editor-container {
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: #f3f8f4; /* Light green background */
    height: 100vh;
    padding: 20px;
  }
  
  .title {
    color: #4caf50; /* Green color */
    font-size: 36px;
    margin-bottom: 20px;
  }
  
  .form-container {
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 600px;
    padding: 20px;
    background-color: #ffffff; /* White background for form */
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  /* Input fields */
  .input-field {
    margin-bottom: 15px;
    padding: 12px;
    border: 1px solid #4caf50;
    border-radius: 6px;
    font-size: 16px;
    outline: none;
    transition: border-color 0.3s ease;
  }
  
  .input-field:focus {
    border-color: #2e7d32; /* Darker green when focused */
  }
  
  /* Button Styles */
  .generate-btn {
    padding: 12px;
    background-color: #4caf50; /* Green button */
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .generate-btn:hover {
    background-color: #388e3c; /* Darker green on hover */
  }
  
  .generate-btn:focus {
    outline: none;
  }
  
  /* Loading Spinner */
  .loading {
    margin-top: 20px;
    font-size: 18px;
    color: #4caf50;
    font-weight: bold;
    animation: fadeIn 1s ease-in-out;
  }
  
  /* Animations */
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
  </style>
  