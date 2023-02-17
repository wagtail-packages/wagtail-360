import { terser } from 'rollup-terser';

// `npm run build` -> `production` is true
// `npm run dev` -> `production` is false
const production = !process.env.ROLLUP_WATCH;

export default [
	{
		input: 'client/testapp/js/panorama.js',
		output: {
			file: 'test/testapp/static/testapp/js/panorama.min.js',
			format: 'iife', // immediately-invoked function expression — suitable for <script> tags
			// sourcemap: true
		},
		plugins: [
			production && terser() // minify, but only in production
		]
	},
	{
        input: 'client/wagtail/js/parse_url.js',
        output: {
            file: 'wagtail_360/static/wagtail_360/admin/js/parse_url.min.js',
            format: 'iife',
            // sourcemap: true,
			plugins: [
				production && terser() // minify, but only in production
			]
        },
    },
    {
        input: 'client/wagtail/js/street_view.js',
        output: {
            file: 'wagtail_360/static/wagtail_360/admin/js/street_view.min.js',
            format: 'iife',
            // sourcemap: true,
			plugins: [
				production && terser() // minify, but only in production
			]
        },
    }
];

// export default [
//     {
//         input: 'client/testapp/js/panorama.js',
//         output: {
//             file: 'test/testapp/static/testapp/js/panorama.min.js',
//             format: 'cjs',
//             minifyInternalExports: true,
//         },
//     },
//     {
//         input: 'client/wagtail/js/parse_url.js',
//         output: {
//             file: 'wagtail_360/static/wagtail_360/admin/js/parse_url.min.js',
//             format: 'cjs',
//             minifyInternalExports: true,
//         },
//     },
//     {
//         input: 'client/wagtail/js/street_view.js',
//         output: {
//             file: 'wagtail_360/static/wagtail_360/admin/js/street_view.min.js',
//             format: 'esm',
//             minifyInternalExports: true,
//         },
//     }
// ];
