
const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  entry: './static/src/styles/main.scss',
  output: {
    path: path.resolve(__dirname, 'static/dist'),
    filename: 'bundle.js', // Puedes dejarlo aunque sea solo SASS
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader, // Extrae el CSS a un archivo aparte
          'css-loader',
          'sass-loader',
        ],
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'main.css', // este será tu archivo CSS final
    }),
  ],
  mode: 'development',
};
