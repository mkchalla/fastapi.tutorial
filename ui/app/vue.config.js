
// https://stackoverflow.com/a/49846977
// vue.config.js

module.exports = {
    devServer: {
        proxy: {
            "/api/*": {
                target: "http://fastapi",
                secure: false
            }
        }
    }
}
