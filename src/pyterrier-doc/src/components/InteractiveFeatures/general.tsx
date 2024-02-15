import { ReactElement } from "react";

export const generateErrorMessage = (
  errCode: string,
  textAlign
): ReactElement => {
  let errorMessage;

  switch (errCode) {
    case "ERR_NETWORK":
      errorMessage = (
        <>
          Invalid URL provided.
          <br />
          Please check the URL's accessibility and ensure it is whitelisted for
          CORS.
          <br />
          If correct, the server might be blocking requests from your domain.
        </>
      );
      break;
    case "INVALID_RESPONSE_PROPS":
      errorMessage = (
        <>
          Invalid response data received.
          <br />
          Ensure that the API response adheres to the ResponseProps interface.
        </>
      );
      break;
    case "400":
      errorMessage = (
        <>
          Invalid input. Please try different inputs.
          <br />
          Inputs resembling code or containing double quotes may cause issues.
        </>
      );
      break;
    case "422":
      errorMessage = <>Invalid input. Incorrect input type.</>;
      break;
    default:
      errorMessage = (
        <>
          Apologies, but the current error is not documented.
          <br />
          Please consider posting this issue on the project's GitHub repository.
          <br />
          Thank you for your cooperation!
        </>
      );
      break;
  }

  return (
    <p className="error--elements" style={{ textAlign }}>
      {errorMessage}
    </p>
  );
};

export const isPropValid = (data: object): boolean => {
  const basicProps =
    "example" in data &&
    "input" in data &&
    "output" in data &&
    "parameters" in data;
  const multiProps = "options" in data && "parameters" in data;
  return basicProps || multiProps;
};
