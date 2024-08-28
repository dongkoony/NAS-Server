// ./theme/static_src/tailwind.config.js

const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '!../../node_modules/**/*',
        '!../../**/node_modules/**/*',
    ],
    darkMode: 'media',
    theme: {
        extend: {
            fontFamily: {
                sans: ['Inter var', ...defaultTheme.fontFamily.sans],
                body: ['Inter var', ...defaultTheme.fontFamily.sans],
                heading: ['Inter var', ...defaultTheme.fontFamily.sans],
            },
            colors: {
                gray: defaultTheme.colors.gray,
                blue: defaultTheme.colors.blue,
                red: defaultTheme.colors.red,
                yellow: defaultTheme.colors.yellow,
                green: defaultTheme.colors.green,
            },
            borderRadius: {
                'xl': `calc(var(--radius) + 4px)`,
                'lg': `var(--radius)`,
                'md': `calc(var(--radius) - 2px)`,
                'sm': `calc(var(--radius) - 4px)`,
            },
            keyframes: {
                "accordion-down": {
                    from: { height: 0 },
                    to: { height: "var(--radix-accordion-content-height)" },
                },
                "accordion-up": {
                    from: { height: "var(--radix-accordion-content-height)" },
                    to: { height: 0 },
                },
            },
            animation: {
                "accordion-down": "accordion-down 0.2s ease-out",
                "accordion-up": "accordion-up 0.2s ease-out",
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
        require('@tailwindcss/line-clamp'),
        require("tailwindcss-animate"),
    ],
};