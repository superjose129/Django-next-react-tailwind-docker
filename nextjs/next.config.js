/** @type {import('next').NextConfig} */

const webpack = require("webpack");
const images = require("next-images");
const offline = require("next-offline");
const withPlugins = require("next-compose-plugins");
const { parsed: localEnv } = require("dotenv").config();
const rewrites = {
  async rewrites() {
    return [
      {
        source: "/:path*",
        destination: "http://django:8000/:path*",
      },
    ];
  },
};

const config = {
  webpack(config) {
    // we depend on nextjs switching to webpack 4 by default. Probably they will
    // change this behavior at some future major version.

    return config;
  },
};

module.exports = withPlugins([config, images, offline, rewrites]);
