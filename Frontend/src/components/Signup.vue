<template>
    <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-200 to-green-500">
      <div class="p-8 bg-white rounded-xl shadow-lg w-full max-w-md">
        <h2 class="text-3xl font-semibold text-center text-gray-800 mb-6">Sign Up</h2>
  
        <form @submit.prevent="submitSignUp" class="space-y-6">
          <div>
            <input 
              v-model="username" 
              type="text" 
              placeholder="Username" 
              class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:outline-none" 
              required 
            />
          </div>
  
          <div>
            <input 
              v-model="email" 
              type="email" 
              placeholder="Email" 
              class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:outline-none" 
              required 
            />
          </div>
  
          <div>
            <input 
              v-model="password" 
              type="password" 
              placeholder="Password" 
              class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:outline-none" 
              required 
            />
          </div>
  
          <button 
            type="submit" 
            class="w-full py-3 bg-green-600 text-white font-semibold rounded-lg hover:bg-green-700 transition duration-300"
          >
            Sign Up
          </button>
        </form>
  
        <p class="mt-4 text-center text-gray-600">
          Already have an account? 
          <router-link to="/signin" class="text-green-600 hover:underline">Sign In</router-link>
        </p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: ''
      };
    },
    methods: {
      async submitSignUp() {
        try {
          const response = await axios.post('http://localhost:8000/api/signup/', {
            username: this.username,
            email: this.email,
            password: this.password
          });
          alert('User created successfully');
          this.$router.push('/signin'); // Redirect to SignIn after successful signup
        } catch (error) {
          console.error(error.response);
          alert('Error during sign up');
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Custom Tailwind CSS styling (if needed) */
  </style>
  