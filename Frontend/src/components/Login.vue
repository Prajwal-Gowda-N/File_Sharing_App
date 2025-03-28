<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-200 to-green-500">
    <div class="p-8 bg-white rounded-xl shadow-lg w-full max-w-md">
      <h2 class="text-3xl font-semibold text-center text-gray-800 mb-6">Sign In</h2>

      <form @submit.prevent="submitSignIn" class="space-y-6">
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
          Sign In
        </button>
      </form>

      <p class="mt-4 text-center text-gray-600">
        Don't have an account?
        <router-link to="/signup" class="text-green-600 hover:underline">Sign Up</router-link>
      </p>

      <!-- Logout Button -->
      <button
        v-if="isLoggedIn"
        @click="logout"
        class="mt-4 w-full py-3 bg-red-600 text-white font-semibold rounded-lg hover:bg-red-700 transition duration-300"
      >
        Logout
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      isLoggedIn: false, // Start as false, and update based on token presence
    };
  },
  created() {
    // Check if the user is already logged in by verifying the access token
    this.isLoggedIn = !!localStorage.getItem('access_token');
  },
  methods: {
    // Handle Sign In
    async submitSignIn() {
      try {
        const response = await axios.post('http://localhost:8000/api/signin/', {
          username: this.username,
          password: this.password,
        });
        const { access, refresh } = response.data;
        localStorage.setItem('access_token', access);
        localStorage.setItem('refresh_token', refresh);
        this.isLoggedIn = true; // Update the login state
        this.$router.push('/'); // Redirect to Dashboard after successful login
      } catch (error) {
        console.error(error.response);
        alert('Error during sign in');
      }
    },

    // Handle Logout
    logout() {
      // Optionally, invalidate the refresh token on the backend
      axios
        .post('http://localhost:8000/api/logout/', {
          refresh_token: localStorage.getItem('refresh_token'),
        })
        .catch((error) => {
          console.error('Logout failed:', error);
        });

      // Clear tokens from localStorage
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');

      // Manually update the reactive variable
      this.isLoggedIn = false;

      // Redirect to login page
      this.$router.push('/signin');
    },
  },
};
</script>

<style scoped>
/* Custom Tailwind CSS styling (if needed) */
</style>
