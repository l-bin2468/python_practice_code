const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  // ���� EsLint �Ķ൥����������
  lintOnSave: false,
  // devServer: {
  //   port: 8000, // �˿�
  //   proxy: {
  //     '/api': {  //   �������ǰ׺�������'/api'��������Ͳ����ߴ��������
  //       target: 'http://192.168.3.13:8000',  //����д·��
  //       // pathRewrite: { '^/api': '' }, //�����к�/api·���ģ�ȥ��/apiת����������
  //       // ws: true,  //����֧��websocket
  //       changeOrigin: true   //���ڿ�������ͷ�е�hostֵ
  //     },
  //   }
  // }
})
