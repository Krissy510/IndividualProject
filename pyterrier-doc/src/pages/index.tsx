import React from "react";
import PyTerrierLogo from "@site/static/img/black_logo.svg";
import { FiCompass } from "react-icons/fi";
import { BsGithub } from "react-icons/bs";
import { IoLibraryOutline } from "react-icons/io5";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";
import HomepageFeatures from "@site/src/components/HomepageFeatures";

import styles from "./index.module.css";

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={styles.heroBanner}>
      <div>
        <h1 className="hero__title">
          <PyTerrierLogo height={70} width={100} className={styles.logo} />
          {siteConfig.title}
        </h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>

        <div className="flex center gap--10">
          <Link className="button button--primary button--lg" to="/docs/intro">
            <div className="flex center gap--5">
              <FiCompass />
              Get Started
            </div>
          </Link>
          <a
            className="button button--secondary button--lg"
            href=""
            target="_blank"
          >
            <div className="flex center gap--5">
              <BsGithub />
              Source Code
            </div>
          </a>

          <Link
            className="button button--secondary button--lg"
            to="/docs/intro"
          >
            <div className="flex center gap--5">
              <IoLibraryOutline />
              Documentation
            </div>
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): JSX.Element {
  // const { siteConfig } = useDocusaurusContext();
  return (
    <Layout>
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
