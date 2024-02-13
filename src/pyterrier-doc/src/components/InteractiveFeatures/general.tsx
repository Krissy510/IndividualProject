import { ReactElement } from "react";

export const generateErrorMessage = (
  errCode: string,
  textAlign
): ReactElement => {
  const commonStyle = { textAlign: textAlign };

  let errorMessage;

  switch (errCode) {
    case "ERR_NETWORK":
      errorMessage = (
        <p style={commonStyle}>
          Invalid URL provided.
          <br />
          Please check the URL's accessibility and ensure it is whitelisted for
          CORS.
          <br />
          If correct, the server might be blocking requests from your domain.
        </p>
      );
      break;
    case "INVALID_RESPONSE_PROPS":
      errorMessage = (
        <p style={commonStyle}>
          Invalid response data received.
          <br />
          Ensure that the API response adheres to the ResponseProps interface.
        </p>
      );
      break;
    case "400":
      errorMessage = (
        <p style={commonStyle}>
          Invalid input. Please try different inputs.
          <br />
          Inputs resembling code or containing double quotes may cause issues.
        </p>
      );
      break;
    case "422":
      errorMessage = (
        <p style={commonStyle}>Invalid input. Incorrect input type.</p>
      );
      break;
    default:
      errorMessage = (
        <p style={commonStyle}>
          Apologies, but the current error is not documented.
          <br />
          Please consider posting this issue on the project's GitHub repository.
          <br />
          Thank you for your cooperation!
        </p>
      );
      break;
  }

  return errorMessage;
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
