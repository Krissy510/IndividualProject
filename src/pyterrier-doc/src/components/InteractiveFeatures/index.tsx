import ErrorIcon from "@mui/icons-material/Error";
import { Button, CircularProgress } from "@mui/material";
import Box from "@mui/material/Box";
import { GridColDef, GridRowsProp } from "@mui/x-data-grid";
import { randomId } from "@mui/x-data-grid-generator";
import PipelineInput from "@site/src/components/PipelineInput";
import axios, { AxiosError, AxiosResponse } from "axios";
import { useEffect, useState } from "react";
import PipelineOutput from "../PipelineOutput";
import { generateErrorMessage, isPropValid } from "./general";
import { InteractiveFeatureProps, ResponseProps } from "./model";

export default function InteractiveFeature({
  apiUrl,
}: InteractiveFeatureProps) {
  const [inputRows, setInputRows] = useState<GridRowsProp>([]);
  const [inputColumns, setInput] = useState([]);
  const [defineOutputColumns, setDefineOutputColumns] = useState<
    Array<GridColDef>
  >([]);
  const [parameters, setParameters] = useState([]);
  const [isPostApiProcessing, setIsApiProcessing] = useState(false);
  const [isPageLoading, setIsPageLoading] = useState(false);
  const [outputRows, setOutputRows] = useState([]);
  const [displayInteractive, setDisplayInteractive] = useState(false);
  const [generatedCode, setGeneratedCode] = useState<string>("");
  const [options, setOptions] = useState({});
  const [isMulti, setIsMulti] = useState(false);
  const [paramData, setParamData] = useState({});
  const [inputError, setInputError] = useState("");
  const [outputError, setOutputError] = useState("");

  const updateState = (data: object) => {
    setInputRows(
      data["example"].map((row) => {
        return { id: randomId(), ...row };
      })
    );
    setInput(data["input"]);
    setDefineOutputColumns([
      ...data["output"].map((column): GridColDef => {
        return {
          field: column.name,
          headerName: column.name,
          width: column.width,
          editable: false,
        };
      }),
    ]);
  };

  useEffect(() => {
    if (isMulti) {
      updateState(options[paramData["type"]]);
      setOutputRows([]);
    }
  }, [paramData]);

  const handleTryButton = () => {
    setDisplayInteractive(true);
    if (inputColumns.length === 0) {
      setIsPageLoading(true);
      axios
        .get<ResponseProps>(apiUrl)
        .then((response: AxiosResponse<ResponseProps>) => {
          const data = response.data;
          if (isPropValid(data)) {
            setParameters(data["parameters"]);
            if (data.hasOwnProperty("options")) {
              setOptions(data.options);
              setIsMulti(true);
            } else {
              updateState(data);
            }
            setInputError("");
          } else {
            throw new Error("INVALID_RESPONSE_PROPS");
          }
        })
        .catch((err: Error | AxiosError) => {
          setDisplayInteractive(false);
          if (axios.isAxiosError(err)) {
            setInputError(err.code);
          } else {
            setInputError(err.message);
          }
        })
        .finally(() => {
          setIsPageLoading(false);
        });
    }
  };

  return displayInteractive ? (
    <Box sx={{ marginBottom: 3 }}>
      {isPageLoading ? (
        <Box>
          <CircularProgress />
        </Box>
      ) : (
        <Box>
          <Box
            sx={{
              width: "100%",
              display: "flex",
              flexDirection: "column",
              gap: 3,
              marginRight: 0,
            }}
          >
            <PipelineInput
              inputRows={inputRows}
              setInputRows={setInputRows}
              columns={inputColumns}
              parameters={parameters}
              apiUrl={apiUrl}
              setOutputRows={setOutputRows}
              isPostApiProcessing={isPostApiProcessing}
              setIsApiProcessing={setIsApiProcessing}
              setGeneratedCode={setGeneratedCode}
              paramData={paramData}
              setParamData={setParamData}
              setOutputError={setOutputError}
            />
            <PipelineOutput
              outputRows={outputRows}
              defineOutputColumns={defineOutputColumns}
              isPostApiProcessing={isPostApiProcessing}
              code={generatedCode}
              outputError={outputError}
            />
          </Box>
        </Box>
      )}
    </Box>
  ) : (
    <Box>
      {inputError === "" ? (
        <></>
      ) : (
        <Box
          sx={{
            display: "flex",
            flexDirection: "cols",
            gap: 1,
            border: "1px solid #7E7E7E",
            borderRadius: 5,
            paddingX: 2,
            paddingY: 1,
            marginBottom: 2,
          }}
        >
          <ErrorIcon sx={{ fill: "red" }} />
          {generateErrorMessage(inputError, "left")}
        </Box>
      )}

      <Button
        onClick={handleTryButton}
        variant="contained"
        sx={{
          marginBottom: 2,
        }}
        color={inputError === "" ? "primary" : "error"}
      >
        {inputError === "" ? "Try!" : "Retry!"}
      </Button>
    </Box>
  );
}
