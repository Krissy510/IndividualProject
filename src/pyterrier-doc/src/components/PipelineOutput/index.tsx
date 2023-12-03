import { Box, CircularProgress } from "@mui/material";
import { DataGrid, GridRowsProp } from "@mui/x-data-grid";
import { randomId } from "@mui/x-data-grid-generator";

export default function PipelineOutput({
  defineOutputColumns,
  outputRows,
  displayMode,
  isPostApiProcessing,
}) {
  const displayRows: GridRowsProp = outputRows.map((row) => {
    return { id: randomId(), ...row };
  });

  return (
    <Box
      sx={{
        border: "1px solid #7E7E7E",
        borderRadius: 3,
        display: "flex",
        flexDirection: "column",
        padding: 3,
        width: displayMode === "row" ? "50%" : "100%",
        minHeight: "60vh",
        maxHeight: "100vh",
      }}
    >
      <h4>Pipeline Output</h4>
      {isPostApiProcessing ? (
        <Box
          sx={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            minHeight: "60vh",
            maxHeight: "100vh",
          }}
        >
          <CircularProgress />
        </Box>
      ) : (
        <DataGrid
          rows={displayRows}
          columns={defineOutputColumns}
          rowSelection={false}
          initialState={{
            pagination: {
              paginationModel: { pageSize: 25, page: 0 },
            },
          }}
          sx={{
            height: "100%",
          }}
        />
      )}
    </Box>
  );
}
