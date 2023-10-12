import React from "react";
import clsx from "clsx";
import styles from "./styles.module.css";
import { BiLabel } from "react-icons/bi";
import { TbCodePlus } from "react-icons/tb";
import { BsGithub } from "react-icons/bs";

type FeatureItem = {
  title: string;
  Svg: JSX.Element;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: "Open Source",
    Svg: <BsGithub size={100} />,
    description: (
      <>
        PyTerrier is free and{" "}
        <a href="https://github.com/terrier-org/pyterrier" target="_blank">
          open source
        </a>{" "}
        , enabling transparency and reproducibility.
      </>
    ),
  },
  {
    title: "Interoperable Components",
    Svg: <BiLabel size={100} />,
    description: (
      <>
        Provides a rich library of components, which work together through a
        common data model.
      </>
      // Add link later
    ),
  },
  {
    title: "Extendable",
    Svg: <TbCodePlus size={100} />,
    description: (
      <>Easily extendable, allowing you to experiment with new components.</>
    ),
  },
];

function Feature({ title, Svg, description }: FeatureItem) {
  return (
    <div className={clsx("col col--4")}>
      <div className="text--center">{Svg}</div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
