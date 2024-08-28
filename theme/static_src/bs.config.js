// ./theme/static_src/bs.config.js

const tailwindConfig = require('./tailwind.config.js');

module.exports = {
    files: [
        '../../**/*.html',
        '../../**/static/**/*.(s)?css',
        '../../**/static/**/*.js',
        '../static/css/dist/styles.css',
    ],
    ignore: [...(tailwindConfig.content || [])],
    watch: true,
    server: {
        baseDir: "../../",  // 프로젝트 루트 디렉토리를 기준으로 설정
        directory: true
    },
    port: 3000,  // 명시적으로 포트 지정
    proxy: false,
    open: false,  // 브라우저 자동 실행 방지
    browser: "default",
    notify: false,
    injectChanges: true,
};