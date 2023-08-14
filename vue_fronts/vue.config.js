const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  // 禁用 EsLint 的多单词命名规则
  lintOnSave: false,
  // devServer: {
  //   port: 8000, // 端口
  //   proxy: {
  //     '/api': {  //   若请求的前缀不是这个'/api'，那请求就不会走代理服务器
  //       target: 'http://192.168.3.13:8000',  //这里写路径
  //       // pathRewrite: { '^/api': '' }, //将所有含/api路径的，去掉/api转发给服务器
  //       // ws: true,  //用于支持websocket
  //       changeOrigin: true   //用于控制请求头中的host值
  //     },
  //   }
  // }
})
