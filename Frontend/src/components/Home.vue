<template>
    <div class="flex justify-center items-center h-screen">
      <div class="grid grid-cols-3 gap-25">
        <RouterLink to="/share" class="block bg-green-800 text-white p-6 rounded-lg shadow-md hover:bg-green-600 transition text-center">
          <h2 class="text-xl font-semibold">File Sharing</h2>
        </RouterLink>
        <RouterLink to="/summarize" class="block bg-green-800 text-white p-6 rounded-lg shadow-md hover:bg-green-600 transition text-center">
          <h2 class="text-xl font-semibold">Summarization</h2>
        </RouterLink>
        <RouterLink to="/convert" class="block bg-green-800 text-white p-6 rounded-lg shadow-md hover:bg-green-600 transition text-center">
          <h2 class="text-xl font-semibold">File Conversion</h2>
        </RouterLink>
      </div>
    </div>
  </template>