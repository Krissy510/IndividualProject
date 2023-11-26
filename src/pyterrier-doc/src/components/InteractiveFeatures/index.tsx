import SplitscreenIcon from "@mui/icons-material/Splitscreen";
import VerticalSplitIcon from "@mui/icons-material/VerticalSplit";
import { IconButton } from "@mui/material";
import Box from "@mui/material/Box";
import { GridRowsProp } from "@mui/x-data-grid";
import { randomId } from "@mui/x-data-grid-generator";
import PipelineInput from "@site/src/components/PipelineInput";
import { useState } from "react";
import { InteractiveFeatureProps } from "./model";

export default function InteractiveFeature({
  example,
  defaultDisplayMode,
  columns,
  parameters,
  apiUrl,
}: InteractiveFeatureProps) {
  const exampleInputRows: GridRowsProp = example.map((row) => {
    return { id: randomId(), ...row };
  });

  const [displayMode, setDisplayMode] = useState(
    defaultDisplayMode ?? "column"
  );

  return (
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
        }}
      >
        <PipelineInput
          exampleInputRows={exampleInputRows}
          columns={columns}
          parameters={parameters}
          apiUrl={apiUrl}
        />
      </Box>
    </Box>
  );
}
