import React from "react";
import Layout from "@theme/Layout";

const TestPage = () => {
  return (
    <Layout
      title="Contributors"
      description="Cool people who made this cool library"
    >
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "50vh",
          fontSize: "20px",
        }}
      ></div>
    </Layout>
  );
};

export default TestPage;
