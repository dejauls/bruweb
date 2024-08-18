/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/index.html', './templates/acian.html', './templates/acianbeton.html'
    , './templates/perata.html', './templates/plester.html', './templates/render.html', './templates/thinbed.html', './templates/tile.html'
  ],
  theme: {
    extend: {
      colors: {
        'brucolor': '#FA622B',
      },
    },
  },
  plugins: [],
}
