import SplitscreenIcon from "@mui/icons-material/Splitscreen";
import VerticalSplitIcon from "@mui/icons-material/VerticalSplit";
import { CircularProgress, IconButton } from "@mui/material";
import Box from "@mui/material/Box";
import { GridColDef, GridRowsProp } from "@mui/x-data-grid";
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
  const [input, setInput] = useState([]);
  const [defineOutputColumns, setDefineOutputColumns] = useState<
    Array<GridColDef>
  >([]);
  const [parameters, setParameters] = useState([]);
  const [isPostApiProcessing, setIsApiProcessing] = useState(false);
  const [isPageLoading, setIsPageLoading] = useState(false);
  const [displayMode, setDisplayMode] = useState("column");
  const [outputRows, setOutputRows] = useState([]);

  useEffect(() => {
    setIsPageLoading(true);

    axios
      .get(apiUrl)
      .then((response) => {
        setInputRows(
          response.data["example"].map((row) => {
            return { id: randomId(), ...row };
          })
        );
        setInput(response.data["input"]);
        setParameters(response.data["parameters"]);
        setDefineOutputColumns([
          ...response.data["output"].map((column): GridColDef => {
            return {
              field: column.name,
              headerName: column.name,
              width: column.width,
              editable: false,
            };
          }),
        ]);
      })
      .catch((error) => {
        // Console log for now will add exception handeling later.
        console.log(`GET request to ${apiUrl} failed!`);
      })
      .finally(() => {
        // For testing only
        // setTimeout(() => {
        //   setIsPageLoading(false);
        // }, 5000);

        setIsPageLoading(false);
      });
  }, []);

  return (
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
              columns={input}
              parameters={parameters}
              apiUrl={apiUrl}
              setOutputRows={setOutputRows}
              isPostApiProcessing={isPostApiProcessing}
              setIsApiProcessing={setIsApiProcessing}
            />
            <PipelineOutput
              outputRows={outputRows}
              defineOutputColumns={defineOutputColumns}
              displayMode={displayMode}
              isPostApiProcessing={isPostApiProcessing}
            />
          </Box>
        </Box>
      )}
    </Box>
  );
}
