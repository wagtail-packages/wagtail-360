const { create } = require('browser-sync');
const fs = require('fs');
const sass = require('sass');

// common folder names
const admin_path = "/admin/"; // admin path
const public_path = "/public/"; // public path

// source paths
const sass_admin_path = "./client/sass/admin/"; // path to admin sass files
const sass_public_path = "./client/sass/public/"; // path to public sass files
const js_admin_path = "./client/js/admin/"; // path to admin js files
const js_public_path = "./client/js/public/"; // path to public js files

// build paths
const static = "./client/static/"; // path to static files
const css_admin_path = static + "css" + admin_path; // path to admin css files
const css_public_path = static + "css" + public_path; // path to public css files
const js_admin_build_path = static + "js" + admin_path; // path to admin js build files
const js_public_build_path = static + "js" + public_path; // path to public js build files

if (!fs.existsSync(css_admin_path)) {
    fs.mkdirSync(css_admin_path, { recursive: true });
}

if (!fs.existsSync(css_public_path)) {
    fs.mkdirSync(css_public_path, { recursive: true });
}

if (!fs.existsSync(js_admin_build_path)) {
    fs.mkdirSync(js_admin_build_path, { recursive: true });
}

if (!fs.existsSync(js_public_build_path)) {
    fs.mkdirSync(js_public_build_path, { recursive: true });
}


const panorama_panel = sass.compile(sass_admin_path + "panorama_panel.scss", {
    style: "compressed",
});
console.log(panorama_panel.css);

fs.writeFileSync(css_admin_path + "panorama_panel.css", panorama_panel.css);



