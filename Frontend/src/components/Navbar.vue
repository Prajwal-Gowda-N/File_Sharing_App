<template>
  <nav class="bg-gradient-to-r from-green-700 via-green-800 to-green-900 p-4 shadow-md hover:bg-gradient-to-r hover:from-green-600 hover:via-green-700 hover:to-green-800 transition-all duration-300">
    <div class="container mx-auto flex justify-between items-center">
      <h1 class="text-white text-2xl font-bold cursor-pointer hover:text-green-200 transition-all duration-300">File Sharing App</h1>
      <ul class="flex space-x-8">
        <li v-for="(item, index) in menuItems" :key="index" class="relative group">
          <RouterLink
            :to="item.link"
            @click.prevent="item.action ? item.action() : null"
            class="text-white hover:text-green-200 text-lg px-4 py-2 transition-all duration-200"
          >
            <span>{{ item.name }}</span>
            <!-- Hover underline animation -->
            <span class="absolute bottom-0 left-0 w-full h-0.5 bg-green-200 transform scale-x-0 group-hover:scale-x-100 transition-transform"></span>
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
      { name: 'EssayWriting', link: '/essay' },
      { name: 'Logout', link: '/#', action: logout }, // Attach logout action here
    ];
  } else {
    menuItems.value = [
      { name: 'Home', link: '/' },
      { name: 'Share', link: '/share' },
      { name: 'Summarize', link: '/summarize' },
      { name: 'Convert', link: '/convert' },
      { name: 'EssayWriting', link: '/essay' },
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
/* Navigation bar background and hover effect */
nav {
  transition: background-color 0.3s ease;
}

/* Link hover effect */
nav ul li a:hover {
  transform: translateY(-3px);
  text-decoration: none;
}

/* Smooth transition on logo hover */
h1:hover {
  transform: scale(1.05);
}
</style>
