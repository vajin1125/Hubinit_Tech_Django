tailwind.config = {
  darkMode: 'class', /* class/media, here we use class to enable manually dark mode */
  theme: {
    extend: {
      colors: {
        // lignt
        'accent-color': '#ff680a',
        'secondary-light-orange': '#ffa770',
        'secondary-dark-orange': '#e05600',
        'primary-color': '#283353',
        'primary-secondary': '#f7f5ff',
        'eerieblack': '#101623',
        // dark
        'dark-bg': '#18181B',
        'dark-second-bg': '#1E1E1E',
        'dark-card-on-second': '#A3A3A3',
        'dark-orange': '#FF893E',
        'dark-light-grey': '#F5F5F5',
        'dark-card': '#3A3A3A',
      },
      screens: {
        'desktop': '1728px',

        'tablet': '828px',

        'mobile': '393px',

        'sm': '640px',
        // => @media (min-width: 640px) { ... }

        'md': '768px',
        // => @media (min-width: 768px) { ... }

        'lg': '1024px',
        // => @media (min-width: 1024px) { ... }

        'xl': '1280px',
        // => @media (min-width: 1280px) { ... }

        '2xl': '1536px',
        // => @media (min-width: 1536px) { ... }
      },
    },
  },
}