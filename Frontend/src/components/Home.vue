<template>
  <div class="flex justify-center items-center bg-cream min-h-screen py-12">
    <div class="container mx-auto px-6">
      
      <!-- Row 1: File Sharing Section -->
      <div class="flex justify-center mb-12 animate-on-scroll">
        <div class="card bg-white shadow-md rounded-lg overflow-hidden transform hover:scale-105 transition-transform duration-300 w-1/2 md:w-1/2">
          <div class="flex">
            <div class="relative w-1/2">
              <img src="C:\Users\win10\Desktop\File_Sharing_Application\Frontend\src\assets\file sharing image.png" alt="File Sharing" class="w-full h-80 object-cover"/>
            </div>
            <div class="p-4 w-1/2">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">File Sharing</h2>
              <p class="text-gray-600 mb-4">Easily share your files with others across platforms.</p>
              <RouterLink to="/share" class="text-green-600 hover:underline">Learn More</RouterLink>
            </div>
          </div>
        </div>
      </div>

      <!-- Row 2: Summarization Section -->
      <div class="flex justify-center mb-12 animate-on-scroll">
        <div class="card bg-white shadow-md rounded-lg overflow-hidden transform hover:scale-105 transition-transform duration-300 w-1/2 md:w-1/2">
          <div class="flex">
            <div class="relative w-1/2">
              <img src="C:\Users\win10\Desktop\File_Sharing_Application\Frontend\src\assets\text summerization image.png" alt="Summarization" class="w-full h-80 object-cover"/>
            </div>
            <div class="p-4 w-1/2">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">Summarization</h2>
              <p class="text-gray-600 mb-4">Quickly summarize your documents in seconds.</p>
              <RouterLink to="/summarize" class="text-blue-600 hover:underline">Learn More</RouterLink>
            </div>
          </div>
        </div>
      </div>

      <!-- Row 3: File Conversion Section -->
      <div class="flex justify-center mb-12 animate-on-scroll">
        <div class="card bg-white shadow-md rounded-lg overflow-hidden transform hover:scale-105 transition-transform duration-300 w-1/2 md:w-1/2">
          <div class="flex">
            <div class="relative w-1/2">
              <img src="C:\Users\win10\Desktop\File_Sharing_Application\Frontend\src\assets\word to pdf file convertor and pdf to word.png" alt="File Conversion" class="w-full h-80 object-cover"/>
            </div>
            <div class="p-4 w-1/2">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">File Conversion</h2>
              <p class="text-gray-600 mb-4">Convert your files into various formats with ease.</p>
              <RouterLink to="/convert" class="text-purple-600 hover:underline">Learn More</RouterLink>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
  /* Base Card Style */
  .card {
    width: 100%;
    height: 100%;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .card h2 {
    font-size: 1.5rem;
  }

  /* Hover Effect for Entire Card */
  .card:hover {
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    transform: scale(1.05);
  }

  .card img {
    object-fit: cover;
    transition: none; /* No transformation or hover effect on the image */
  }

  /* Text Link Styles */
  .text-green-600 {
    color: #48bb78;
  }

  .text-blue-600 {
    color: #3182ce;
  }

  .text-purple-600 {
    color: #805ad5;
  }

  .text-green-600:hover,
  .text-blue-600:hover,
  .text-purple-600:hover {
    text-decoration: underline;
  }

  /* Scroll Animation Styles */
  .animate-on-scroll {
    opacity: 0;
    transform: translateY(50px);
    transition: opacity 0.6s ease, transform 0.6s ease;
  }

  .animate-on-scroll.visible {
    opacity: 1;
    transform: translateY(0);
  }

  /* Flex Layout Adjustments for Image and Text */
  .card .flex {
    display: flex;
    align-items: center;
  }

  .card .p-4 {
    padding-left: 1rem;
    padding-right: 1rem;
    padding-top: 1.5rem;
  }

  /* Background Color Change to Cream */
  .bg-cream {
    background-color: #f7f5eb;
  }
</style>

<script>
  export default {
    mounted() {
      // Intersection Observer to detect when elements come into view
      const elements = document.querySelectorAll('.animate-on-scroll');
      const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
          } else {
            entry.target.classList.remove('visible');
          }
        });
      }, { threshold: 0.2 });

      elements.forEach(element => {
        observer.observe(element);
      });
    }
  };
</script>
