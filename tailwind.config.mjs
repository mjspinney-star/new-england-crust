import typography from '@tailwindcss/typography';

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        // Rich reds — like a pizza sauce simmering down on the stovetop.
        ember: {
          50: '#fdf3f1',
          100: '#fbe3df',
          200: '#f6c1b8',
          300: '#ee9384',
          400: '#e26551',
          500: '#c63d28',
          600: '#a82e1d',
          700: '#86241a',
          800: '#6b1f18',
          900: '#581b16',
          950: '#300d0a',
        },
        // Warm wood — pine boards on a worn-in deck.
        timber: {
          50: '#f8f3eb',
          100: '#ede0cb',
          200: '#dcc197',
          300: '#c79d63',
          400: '#b27f43',
          500: '#946635',
          600: '#76502b',
          700: '#5c3f25',
          800: '#46301f',
          900: '#33231a',
        },
        // Fire glow — yellows and oranges from the oven mouth.
        glow: {
          50: '#fff8ec',
          100: '#ffeac7',
          200: '#ffd185',
          300: '#ffb247',
          400: '#ff921a',
          500: '#f37207',
          600: '#d85604',
          700: '#a93f08',
          800: '#88330e',
          900: '#702b0f',
        },
        // Harbor — coastal New England navy, the kind on shutters and clapboard.
        harbor: {
          50: '#eef3fa',
          100: '#d8e3f1',
          200: '#b1c5e1',
          300: '#7e9ec8',
          400: '#4f78a9',
          500: '#305a8c',
          600: '#234670',
          700: '#1b3658',
          800: '#142845',
          900: '#0d1c30',
          950: '#07111e',
        },
        // Twilight — that deep New England backyard sky.
        twilight: {
          50: '#f5f5f4',
          100: '#dcdad6',
          200: '#9d978e',
          300: '#5b554b',
          400: '#3a3530',
          500: '#26221d',
          600: '#1c1916',
          700: '#141210',
          800: '#0d0c0a',
          900: '#070605',
        },
      },
      fontFamily: {
        display: ['"Fraunces"', 'Georgia', 'serif'],
        sans: ['"Inter"', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
      backgroundImage: {
        'fire-glow':
          'radial-gradient(ellipse at center, rgba(255,178,71,0.45) 0%, rgba(243,114,7,0.25) 35%, rgba(13,12,10,0) 75%)',
        'wood-grain':
          'linear-gradient(135deg, #5c3f25 0%, #46301f 50%, #33231a 100%)',
      },
      boxShadow: {
        ember: '0 0 40px -10px rgba(243,114,7,0.55)',
        deck: '0 20px 40px -20px rgba(0,0,0,0.6)',
      },
      maxWidth: {
        prose: '70ch',
      },
    },
  },
  plugins: [typography],
};
