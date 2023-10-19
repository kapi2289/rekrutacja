import defaultTheme from 'tailwindcss/defaultTheme';

/** @type {import('tailwindcss').Config} */
export default {
    content: ['./index.html', './src/**/*.vue'],
    theme: {
        extend: {
            colors: {
                primary: '#FAA21B',
                background: '#191f2d',
            },
            fontFamily: {
                sans: ['Roboto', ...defaultTheme.fontFamily.sans],
            }
        },
    },
    plugins: [],
}
