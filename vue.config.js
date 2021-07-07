// const IS_PRODUCTION = process.env.NODE_ENV === 'production'
const webpack = require('webpack');

module.exports = {
    outputDir: 'dist',
    assetsDir: 'static',
    // baseUrl: IS_PRODUCTION
    // ? 'http://cdn123.com'
    // : '/',
    // For Production, replace set baseUrl to CDN
    // And set the CDN origin to `yourdomain.com/static`
    // Whitenoise will serve once to CDN which will then cache
    // and distribute
    devServer: {
      proxy: {
        '/api*': {
          // Forward frontend dev server request for /api to django dev server
          target: 'http://localhost:8000/',
        }
      }
    },
    configureWebpack: {
      // Set up all the aliases we use in our app.
      plugins: [
        new webpack.optimize.LimitChunkCountPlugin({
          maxChunks: 6
        })
      ]
    },
    pwa: {
      name: 'Vue Argon Design',
      themeColor: '#172b4d',
      msTileColor: '#172b4d',
      appleMobileWebAppCapable: 'yes',
      appleMobileWebAppStatusBarStyle: '#172b4d'
    },
    css: {
      // Enable CSS source maps.
      sourceMap: process.env.NODE_ENV !== 'production'
    }
  }
