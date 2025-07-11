// Configuration for your app
// https://v2.quasar.dev/quasar-cli-vite/quasar-config-js

import { configure } from 'quasar/wrappers'

export default configure(function (/* ctx */) {
  return {
    eslint: {
      warnings: true,
      errors: true
    },

    // app boot file (/src/boot)
    boot: [
      'axios',
      'main.js'
    ],

    // https://v2.quasar.dev/quasar-cli-vite/quasar-config-js#css
    css: [
      'app.scss'
    ],

    // https://github.com/quasarframework/quasar/tree/dev/extras
    extras: [
      'fontawesome-v6',
      'material-icons',
    ],

    // Full list of options: https://v2.quasar.dev/quasar-cli-vite/quasar-config-js#build
    build: {
      target: {
        browser: ['es2019', 'edge88', 'firefox78', 'chrome87', 'safari13.1'],
        node: 'node16'
      },
      vueRouterMode: 'hash',
      // Custom build output directory for Dataiku plugin
      distDir: 'resource/dist',
      // Ensure assets are referenced correctly
      publicPath: '/plugins/dss-plugin-scoping-assistant/resource/dist/'
    },

    // Full list of options: https://v2.quasar.dev/quasar-cli-vite/quasar-config-js#devServer
    devServer: {
      server: {
        type: 'http'
      },
      port: 8080,
      open: true
    },

    // https://v2.quasar.dev/quasar-cli-vite/quasar-config-js#framework
    framework: {
      config: {},
      plugins: []
    },

    animations: [],

    ssr: {
      pwa: false,
      prodPort: 3000,
      middlewares: [
        'render'
      ]
    },

    pwa: {
      workboxMode: 'generateSW',
      injectPwaMetaTags: true,
      swFilename: 'sw.js',
      manifestFilename: 'manifest.json',
      useCredentialsHack: false,
    },

    cordova: {
    },

    capacitor: {
      hideSplashscreen: false
    },

    electron: {
      inspectPort: 5858,
      entry: 'electron-main',
      builder: {
        appId: 'scoping-assistant'
      }
    },

    bex: {
      contentScripts: [
        'my-content-script'
      ],
    }
  }
})
