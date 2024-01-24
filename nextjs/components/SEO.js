// Original author: JoseRFelix (https://github.com/JoseRFelix/nextjs-starter-blog/blob/master/components/Seo.js)

import Head from "next/head";
import SiteConfig from "../package.json";

export default function SEO({ title, description = "" }) {
  return (
    <Head>
      <title>
        {title} | {SiteConfig.title}
      </title>
      <meta name="description" content={description} />
      <meta property="og:type" content="website" />
      <meta name="og:title" property="og:title" content={title} />
      <meta
        name="og:description"
        property="og:description"
        content={description}
      />
      <meta name="twitter:card" content="summary" />
      <meta name="twitter:title" content={title} />
      <meta name="twitter:description" content={description} />
      <link rel="icon" type="image/png" href="/images/favicon.ico" />
      <link rel="apple-touch-icon" href="/images/favicon.ico" />
    </Head>
  );
}
