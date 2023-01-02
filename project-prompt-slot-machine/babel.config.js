module.exports = function (api) {
    api.cache(true)

    return {
        presets: [
            '@babel/react',
            '@babel/preset-typescript',
            '@babel/env',
            "@emotion/babel-preset-css-prop"
        ],
    }
}