import {
  Box,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from "@mui/material";
import { useEffect, useState } from "react";
import { DataGrid, GridColDef, GridRowsProp } from "@mui/x-data-grid";
import { randomId } from "@mui/x-data-grid-generator";

export default function PipelineOutput({ outputRows, displayMode }) {
  const [columns, setColumns] = useState([]);

  useEffect(() => {
    setColumns(outputRows.length > 0 ? Object.keys(outputRows[0]) : []);
  }, [outputRows]);

  const defineColumns: GridColDef[] = [
    ...columns.map((column): GridColDef => {
      return {
        field: column,
        headerName: column,
        editable: false,
      };
    }),
  ];

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
      <DataGrid
        rows={displayRows}
        columns={defineColumns}
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
    </Box>
  );
}
