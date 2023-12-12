import ExpandLessIcon from "@mui/icons-material/ExpandLess";
import SplitscreenIcon from "@mui/icons-material/Splitscreen";
import VerticalSplitIcon from "@mui/icons-material/VerticalSplit";
import { Button, CircularProgress, IconButton } from "@mui/material";
import Box from "@mui/material/Box";
import { GridColDef, GridRowsProp } from "@mui/x-data-grid";
import { randomId } from "@mui/x-data-grid-generator";
import PipelineInput from "@site/src/components/PipelineInput";
import axios from "axios";
import { useEffect, useState } from "react";
import PipelineOutput from "../PipelineOutput";
import { InteractiveFeatureProps } from "./model";

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
  const [displayMode, setDisplayMode] = useState("column");
  const [outputRows, setOutputRows] = useState([]);
  const [displayInteractive, setDisplayInteractive] = useState(false);
  const [generatedCode, setGeneratedCode] = useState<string>("");

  useEffect(() => {
    if (displayInteractive && inputColumns.length === 0) {
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
    }
  }, [displayInteractive]);

  const handleTryButton = () => {
    setDisplayInteractive(!displayInteractive);
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
              justifyContent: "space-between",
              marginBottom: 1,
            }}
          >
            <IconButton
              onClick={handleTryButton}
              aria-label="collapse-interactive"
            >
              <ExpandLessIcon />
            </IconButton>
            <Box>
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
          </Box>
          <Box
            sx={{
              display: "flex",
              flexDirection: displayMode,
              gap: 3,
              marginRight: displayMode === "row" ? 3 : 0,
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
              displayMode={displayMode}
              setGeneratedCode={setGeneratedCode}
            />
            <PipelineOutput
              outputRows={outputRows}
              defineOutputColumns={defineOutputColumns}
              displayMode={displayMode}
              isPostApiProcessing={isPostApiProcessing}
              code={generatedCode}
            />
          </Box>
        </Box>
      )}
    </Box>
  ) : (
    <Button
      onClick={handleTryButton}
      variant="contained"
      sx={{
        marginBottom: 2,
      }}
    >
      Try!
    </Button>
  );
}
