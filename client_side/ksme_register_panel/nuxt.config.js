var fs = require('fs');
var path = require('path');

let ENV_DEV = true;

//Development Environment
let port = 3000;
let host = 'localhost';
let https = false;

//Production Environment
if(ENV_DEV==false)
{
  port = 45782; // make sure this port is open on your server you can do that via WHM or talk to you hosting company
  host = 'ksme.ir';
  https =  {
    key: fs.readFileSync(path.resolve(__dirname,
        './../../navidmnz/ssl/keys/dd156_67297_b3693d761c82fac1ce86b1823455242b.key')),
    cert: fs.readFileSync(path.resolve(__dirname,
        './../../navidmnz/ssl/certs/navidmnzh_ir_dd156_67297_1633038472_da5744c3dbb73989ba8e979544b8b49a.crt'))
  };
}

export default {
  env:{
    level1_url: 'https://ksme.ir/api/level1',
    level2_url: 'https://ksme.ir/api/level2',
    level3_url: 'https://ksme.ir/api/level3',
  },
  server: {
    port: port, 
    host: host, 
    timing: false,
    https: https
  },
  router:{
    //base: '/navid/'
  },
  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  ssr: false,

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'ksme_register_panel',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
    ],
    script: [
        {
          type: 'text/javascript',
          src: 'https://kit.fontawesome.com/7b0dcc43a4.js',
          body: true
        }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '~/assets/css/main.css',
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [

  ],

  fontawesome: {
    icons: [
      
    ]
  },

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    '@nuxtjs/style-resources',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {},

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en'
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  },

  styleResources: {
      scss: [
          '~/assets/css/constants/_fonts.scss',
          '~/assets/css/constants/_flex.scss',
          '~/assets/css/constants/_colors.scss',
          '~/assets/css/constants/_input.scss',
      ]
  }
}
