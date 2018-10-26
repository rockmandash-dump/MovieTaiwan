const { resolve } = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');

module.exports = env => {
  return {
    entry: [
      'react-hot-loader/patch',
      //activate HMR for React

      'webpack-dev-server/client?http://localhost:8080',
      //bundle the client for webpack dev server
      //and connect to the provided endpoint

      'webpack/hot/only-dev-server',
      //bundle the client for hot reloading
      //only- means to only hot reload for successful updates

      resolve(__dirname, 'src/js/index.jsx')
      //the entry point of our app
    ],
    output: {
      filename: 'bundle.js',
      //the output bundle

      path: resolve(__dirname, 'dist')
    },
    context: resolve(__dirname, 'src'),
    devServer: {
      hot: true,
      //activate hot reloading

      contentBase: resolve(__dirname, 'dist')
    },
    module: {
      rules: [
        { test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel-loader' },
        {
          test: /\.scss$/,
          use: [
            { loader: 'style-loader' },
            { loader: 'css-loader' },
            { loader: 'sass-loader' }
          ]
        },
        {
          test: /\.(png|svg|jpg|gif)$/,
          use: ['file-loader']
        }
      ]
    },
    plugins: [
      new CleanWebpackPlugin(['dist']),
      new HtmlWebpackPlugin({
        title: '臺灣電影資料庫',
        filename: 'index.html',
        template: 'index.ejs'
      }),
      new webpack.HotModuleReplacementPlugin(),
      //activates HMR

      new webpack.NamedModulesPlugin(),
      //prints more readable module names in the browser console on HMR updates
      new UglifyJSPlugin()
    ]
  };
};
