// module.exports = {
//   publicPath: process.env.NODE_ENV === 'production'
//     ? 'https://rubensmz.github.io/vue-d3-tree'
//     : '/'
// }


module.exports = {
	runtimeCompiler: true,

	chainWebpack: config => {
		config
			.plugin('html')
			.tap(args => {
				args[0].title = 'Tân Thành Đạt'
				return args
			})
	}
}