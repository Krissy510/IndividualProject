import * as React from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import AddIcon from "@mui/icons-material/Add";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/DeleteOutlined";
import SaveIcon from "@mui/icons-material/Save";
import CancelIcon from "@mui/icons-material/Close";
import {
  GridRowsProp,
  GridRowModesModel,
  GridRowModes,
  DataGrid,
  GridColDef,
  GridToolbarContainer,
  GridActionsCellItem,
  GridEventListener,
  GridRowId,
  GridRowModel,
  GridRowEditStopReasons,
} from "@mui/x-data-grid";
import { randomId } from "@mui/x-data-grid-generator";
import {
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  SelectChangeEvent,
  TextField,
} from "@mui/material";

export default function InteractiveFeature() {
  const [rows, setRows] = React.useState([]);
  const [dataset, setDataset] = React.useState("msmarco_passage");
  const [wmodel, setWmodel] = React.useState("BM25");
  const [numResult, setNumResult] = React.useState(5);

  const handleDatasetChange = (event: SelectChangeEvent) => {
    setDataset(event.target.value);
  };

  const handleWmodelChange = (event: SelectChangeEvent) => {
    setWmodel(event.target.value);
  };

  const handleNumResultChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setNumResult(Number(event.target.value));
  };

  const [rowModesModel, setRowModesModel] = React.useState<GridRowModesModel>(
    {}
  );

  const handleRowEditStop: GridEventListener<"rowEditStop"> = (
    params,
    event
  ) => {
    if (params.reason === GridRowEditStopReasons.rowFocusOut) {
      event.defaultMuiPrevented = true;
    }
  };

  const handleEditClick = (id: GridRowId) => () => {
    setRowModesModel({ ...rowModesModel, [id]: { mode: GridRowModes.Edit } });
  };

  const handleSaveClick = (id: GridRowId) => () => {
    setRowModesModel({ ...rowModesModel, [id]: { mode: GridRowModes.View } });
  };

  const handleDeleteClick = (id: GridRowId) => () => {
    setRows(rows.filter((row) => row.id !== id));
  };

  const handleCancelClick = (id: GridRowId) => () => {
    setRowModesModel({
      ...rowModesModel,
      [id]: { mode: GridRowModes.View, ignoreModifications: true },
    });

    const editedRow = rows.find((row) => row.id === id);
    if (editedRow!.isNew) {
      setRows(rows.filter((row) => row.id !== id));
    }
  };

  const processRowUpdate = (newRow: GridRowModel) => {
    const updatedRow = { ...newRow, isNew: false };
    setRows(rows.map((row) => (row.id === newRow.id ? updatedRow : row)));
    return updatedRow;
  };

  const handleRowModesModelChange = (newRowModesModel: GridRowModesModel) => {
    setRowModesModel(newRowModesModel);
  };

  const query: GridColDef[] = [
    { field: "qid", headerName: "qid", width: 50 },
    {
      field: "query",
      headerName: "query",
      width: 180,
      editable: true,
    },
    {
      field: "actions",
      type: "actions",
      headerName: "Actions",
      width: 100,
      cellClassName: "actions",
      getActions: ({ id }) => {
        const isInEditMode = rowModesModel[id]?.mode === GridRowModes.Edit;

        if (isInEditMode) {
          return [
            <GridActionsCellItem
              icon={<SaveIcon />}
              label="Save"
              sx={{
                color: "primary.main",
              }}
              onClick={handleSaveClick(id)}
            />,
            <GridActionsCellItem
              icon={<CancelIcon />}
              label="Cancel"
              className="textPrimary"
              onClick={handleCancelClick(id)}
              color="inherit"
            />,
          ];
        }

        return [
          <GridActionsCellItem
            icon={<EditIcon />}
            label="Edit"
            className="textPrimary"
            onClick={handleEditClick(id)}
            color="inherit"
          />,
          <GridActionsCellItem
            icon={<DeleteIcon />}
            label="Delete"
            onClick={handleDeleteClick(id)}
            color="inherit"
          />,
        ];
      },
    },
  ];

  interface EditToolbarProps {
    setRows: (newRows: (oldRows: GridRowsProp) => GridRowsProp) => void;
    setRowModesModel: (
      newModel: (oldModel: GridRowModesModel) => GridRowModesModel
    ) => void;
  }

  function EditToolbar(props: EditToolbarProps) {
    const { setRows, setRowModesModel } = props;

    const handleClick = () => {
      const id = randomId();
      const qid = rows.length;
      setRows((oldRows) => [{ id, qid, query: "" }, ...oldRows]);
      setRowModesModel((oldModel) => ({
        ...oldModel,
        [id]: { mode: GridRowModes.Edit, fieldToFocus: "query" },
      }));
    };

    return (
      <GridToolbarContainer>
        <Button color="primary" startIcon={<AddIcon />} onClick={handleClick}>
          Add Query
        </Button>
      </GridToolbarContainer>
    );
  }

  return (
    <div
      style={{
        width: "50%",
        border: "1px solid #7E7E7E",
        borderRadius: 10,
        display: "flex",
        flexDirection: "column",
        gap: 10,
        marginBottom: 10,
      }}
    >
      <Box
        sx={{
          height: 350,
          padding: 3,
        }}
      >
        <h4>Pipeline Input</h4>
        <DataGrid
          rows={rows}
          columns={query}
          editMode="row"
          rowModesModel={rowModesModel}
          autoPageSize
          onRowModesModelChange={handleRowModesModelChange}
          onRowEditStop={handleRowEditStop}
          processRowUpdate={processRowUpdate}
          rowSelection={false}
          pagination={false}
          slots={{
            toolbar: EditToolbar,
          }}
          slotProps={{
            toolbar: { setRows, setRowModesModel },
          }}
        />
      </Box>
      <Box
        sx={{
          margin: 3,
          display: "flex",
          flexDirection: "column",
          gap: 2,
        }}
      >
        <FormControl fullWidth variant="filled">
          <InputLabel id="dataset-select-label">Sample Dataset</InputLabel>
          <Select
            labelId="dataset-select-label"
            id="dataset-select"
            value={dataset}
            label="Dataset"
            onChange={handleDatasetChange}
          >
            <MenuItem value={"msmarco_passage"}>msmarco_passage</MenuItem>
            <MenuItem value={"trec-deep-learning-passages"}>
              trec-deep-learning-passages
            </MenuItem>
          </Select>
        </FormControl>

        <Box sx={{ display: "flex", justifyContent: "space-between", gap: 2 }}>
          <FormControl sx={{ width: "50%" }} variant="filled">
            <InputLabel id="wmodel-select-label">Weight model</InputLabel>
            <Select
              labelId="wmodel-select-label"
              id="wmodel-select"
              value={wmodel}
              label="Wmodel"
              onChange={handleWmodelChange}
            >
              <MenuItem value={"BM25"}>BM25</MenuItem>
              <MenuItem value={"DFIC"}>DFIC</MenuItem>
              <MenuItem value={"DFRWeightingModel"}>DFRWeightingModel</MenuItem>
            </Select>
          </FormControl>

          <TextField
            label="Number result"
            id="number-result"
            type="number"
            sx={{ width: "40%" }}
            value={numResult}
            onChange={handleNumResultChange}
          />
        </Box>
        <Button variant="contained" disabled={rows.length === 0}>
          Transform
        </Button>
      </Box>
    </div>
  );
}
