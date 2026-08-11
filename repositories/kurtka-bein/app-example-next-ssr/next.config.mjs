/** @type {import('next').NextConfig} */
const nextConfig = {
    // SSR включен по умолчанию
    // Убрали 'output: export' чтобы разрешить серверный рендеринг

    // Опциональные настройки для SSR:
    // compress: true, // Сжатие gzip (включено по умолчанию)
    // poweredByHeader: false, // Убрать заголовок X-Powered-By
};

export default nextConfig;
