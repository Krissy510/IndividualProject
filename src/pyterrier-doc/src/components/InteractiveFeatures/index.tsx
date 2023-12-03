import SplitscreenIcon from "@mui/icons-material/Splitscreen";
import VerticalSplitIcon from "@mui/icons-material/VerticalSplit";
import { IconButton } from "@mui/material";
import Box from "@mui/material/Box";
import { GridRowsProp } from "@mui/x-data-grid";
import { randomId } from "@mui/x-data-grid-generator";
import PipelineInput from "@site/src/components/PipelineInput";
import { useEffect, useState } from "react";
import { InteractiveFeatureProps } from "./model";
import PipelineOutput from "../PipelineOutput";
import axios from "axios";

export default function InteractiveFeature({
  apiUrl,
}: InteractiveFeatureProps) {
  const [inputRows, setInputRows] = useState<GridRowsProp>([]);
  const [columns, setColumns] = useState([]);
  const [parameters, setParameters] = useState([]);
  const [isApiProcessing, setIsApiProcessing] = useState(false);

  useEffect(() => {
    setIsApiProcessing(true);

    axios
      .get(apiUrl)
      .then((response) => {
        setInputRows(
          response.data["example"].map((row) => {
            return { id: randomId(), ...row };
          })
        );
        setColumns(response.data["columns"]);
        setParameters(response.data["parameters"]);
      })
      .catch((error) => {})
      .finally(() => {
        setIsApiProcessing(false);
      });
  }, []);

  const [displayMode, setDisplayMode] = useState("column");

  const [outputRows, setOutputRows] = useState([]);

  return (
    <Box sx={{ marginBottom: 3 }}>
      <Box
        sx={{
          width: "100%",
          display: "flex",
          justifyContent: "flex-end",
        }}
      >
        <IconButton
          color="primary"
          disabled={displayMode === "row"}
          onClick={() => setDisplayMode("row")}
        >
          <VerticalSplitIcon />
        </IconButton>

        <IconButton
          color="primary"
          disabled={displayMode === "column"}
          onClick={() => setDisplayMode("column")}
        >
          <SplitscreenIcon />
        </IconButton>
      </Box>
      <Box
        sx={{
          display: "flex",
          flexDirection: displayMode,
          gap: 3,
        }}
      >
        <PipelineInput
          inputRows={inputRows}
          setInputRows={setInputRows}
          columns={columns}
          parameters={parameters}
          apiUrl={apiUrl}
          setOutputRows={setOutputRows}
          isApiProcessing={isApiProcessing}
          setIsApiProcessing={setIsApiProcessing}
        />
        <PipelineOutput outputRows={outputRows} displayMode={displayMode} />
      </Box>
    </Box>
  );
}
