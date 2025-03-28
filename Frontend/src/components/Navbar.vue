<template>
  <nav class="bg-green-800 p-4 shadow-md">
    <div class="container mx-auto flex justify-between items-center">
      <h1 class="text-white text-2xl font-bold">File Sharing App</h1>
      <ul class="flex space-x-8">
        <li v-for="(item, index) in menuItems" :key="index">
          <RouterLink
            :to="item.link"
            @click.prevent="item.action ? item.action() : null"
            class="text-white hover:text-green-200 text-lg px-4 py-2"
          >
            {{ item.name }}
          </RouterLink>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref, computed, watchEffect } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

// Vue router instance
const router = useRouter();

// Define reactive state for menu items
const menuItems = ref([]);

// Computed property to check if the user is logged in
const isLoggedIn = computed(() => {
  return localStorage.getItem('access_token') !== null;
});

// Method to update menu items based on login state
const updateMenuItems = () => {
  if (isLoggedIn.value) {
    menuItems.value = [
      { name: 'Home', link: '/' },
      { name: 'Share', link: '/share' },
      { name: 'Summarize', link: '/summarize' },
      { name: 'Convert', link: '/convert' },
      { name: 'Logout', link: '/#', action: logout }, // Attach logout action here
    ];
  } else {
    menuItems.value = [
      { name: 'Home', link: '/' },
      { name: 'Share', link: '/share' },
      { name: 'Summarize', link: '/summarize' },
      { name: 'Convert', link: '/convert' },
      { name: 'Login', link: '/signin' },
    ];
  }
};

// Logout method to clear localStorage and redirect
const logout = async () => {
  try {
    // Optionally, invalidate the refresh token on the backend
    await axios.post('http://localhost:8000/api/logout/', {
      refresh_token: localStorage.getItem('refresh_token'),
    });

    // Clear tokens from localStorage
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');

    // Update login state
    updateMenuItems();

    // Redirect to login page
    router.push('/signin');
  } catch (error) {
    console.error('Logout failed:', error);
  }
};

// Watch for changes in the login state and update the menu items
watchEffect(() => {
  updateMenuItems();
});
</script>

<style scoped>
nav {
  transition: background-color 0.3s ease;
}
</style>
