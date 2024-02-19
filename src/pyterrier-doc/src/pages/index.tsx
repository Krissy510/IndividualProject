import React from "react";
import PyTerrierLogo from "@site/static/img/logo.svg";
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
              <FiCompass className="text" />
              <span className="text">Get Started</span>
            </div>
          </Link>
          <a
            className="button button--secondary button--lg text"
            href="https://github.com/terrier-org/pyterrier"
            target="_blank"
          >
            <div className="flex center gap--5">
              <BsGithub className="text" />
              <span className="text">Source Code</span>
            </div>
          </a>

          <Link
            className="button button--secondary button--lg text"
            to="https://github.com/Krissy510/IndividualProject/tree/main/src/pyterrier-doc"
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
  return (
    <Layout>
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
