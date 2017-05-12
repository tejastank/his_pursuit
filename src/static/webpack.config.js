var path = require("path")

module.exports = {
    entry: {
        main: './app/components/Main.js',
        //sales: '../sales/static/app/components/tic.js',
    },
    output: {
        path: __dirname + '/public',
        filename: 'bundle.js',
    },
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                exclude: /(node_modules|bower_components)/,
                loader: 'babel',
                query: {
                    presets: ['react']
                }
            }
        ]
    },
    resolveLoader: {
        moduleExtensions: ['-loader'],
    },
}