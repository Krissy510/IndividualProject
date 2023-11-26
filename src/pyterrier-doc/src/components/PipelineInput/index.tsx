import AddIcon from "@mui/icons-material/Add";
import CancelIcon from "@mui/icons-material/Close";
import DeleteIcon from "@mui/icons-material/DeleteOutlined";
import EditIcon from "@mui/icons-material/Edit";
import SaveIcon from "@mui/icons-material/Save";
import { Box, Button } from "@mui/material";
import {
  DataGrid,
  GridActionsCellItem,
  GridColDef,
  GridEventListener,
  GridRowEditStopReasons,
  GridRowId,
  GridRowModel,
  GridRowModes,
  GridRowModesModel,
  GridRowsProp,
  GridToolbarContainer,
} from "@mui/x-data-grid";
import { randomId } from "@mui/x-data-grid-generator";
import { useState } from "react";
import { NumberField } from "./NumberField";
import { SelectField } from "./SelectField";
import { PipelineInputProps } from "./model";
import axios from "axios";

export default function PipelineInput({
  exampleInputRows,
  columns,
  parameters,
  apiUrl,
}: PipelineInputProps) {
  const defaultValuesObject = parameters.reduce((obj, item) => {
    obj[item.id] = item.default;
    return obj;
  }, {});

  const initialValidity = parameters.reduce((acc, param) => {
    if (param.type === "number") {
      acc[param.id] = Number(param.default) > 0;
    }
    return acc;
  }, {});

  const [inputRows, setInputRows] = useState(exampleInputRows);
  const [rowModesModel, setRowModesModel] = useState<GridRowModesModel>({});
  const [paramData, setParamData] = useState(defaultValuesObject);
  const [paramValidity, setParamValidity] = useState(initialValidity);

  const isAnyParamInvalid = () => {
    return Object.values(paramValidity).some((value) => value === false);
  };

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
    setInputRows(inputRows.filter((row) => row.id !== id));
  };

  const handleCancelClick = (id: GridRowId) => () => {
    setRowModesModel({
      ...rowModesModel,
      [id]: { mode: GridRowModes.View, ignoreModifications: true },
    });

    const editedRow = inputRows.find((row) => row.id === id);
    if (editedRow!.isNew) {
      setInputRows(inputRows.filter((row) => row.id !== id));
    }
  };

  const processRowUpdate = (newRow: GridRowModel) => {
    const updatedRow = { ...newRow, isNew: false };
    setInputRows(
      inputRows.map((row) => (row.id === newRow.id ? updatedRow : row))
    );
    return updatedRow;
  };

  const handleRowModesModelChange = (newRowModesModel: GridRowModesModel) => {
    setRowModesModel(newRowModesModel);
  };

  const handleParamChange = (name, value) => {
    setParamData((prev) => ({ ...prev, [name]: value }));
  };

  const handelTransform = () => {
    const queries = inputRows.map(({ id, ...rest }) => rest);
    const request = {
      queries,
      ...paramData,
    };

    axios
      .post(apiUrl, request)
      .then((responese) => {
        if (responese.status === 200) {
          console.log(responese.data);
        }
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const isAnyRowInEditMode = (): boolean => {
    return Object.values(rowModesModel).some(
      (modeInfo) => modeInfo.mode === GridRowModes.Edit
    );
  };

  const isAnyRoleInvalid = (): boolean => {
    return inputRows.some(
      (row) => row.qid === "" || isNaN(Number(row.qid)) || row.query === ""
    );
  };

  const defineColumns: GridColDef[] = [
    ...columns.map((column): GridColDef => {
      return {
        field: column.name,
        headerName: column.name,
        editable: true,
        ...(column.width && { width: column.width }),
      };
    }),
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
    setInputRows: (newRows: (oldRows: GridRowsProp) => GridRowsProp) => void;
    setRowModesModel: (
      newModel: (oldModel: GridRowModesModel) => GridRowModesModel
    ) => void;
  }

  function EditToolbar(props: EditToolbarProps) {
    const { setInputRows, setRowModesModel } = props;

    const handleClick = () => {
      const id = randomId();
      setInputRows((oldRows) => [
        { id, qid: "", query: "", isNew: true },
        ...oldRows,
      ]);
      setRowModesModel((oldModel) => ({
        ...oldModel,
        [id]: { mode: GridRowModes.Edit, fieldToFocus: "query" },
      }));
    };

    return (
      <GridToolbarContainer>
        <Button
          color="primary"
          startIcon={<AddIcon />}
          onClick={handleClick}
          disabled={inputRows.length > 100}
        >
          Add Query
        </Button>
      </GridToolbarContainer>
    );
  }

  return (
    <div
      style={{
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
          padding: 3,
          paddingBottom: 1,
        }}
      >
        <h4>Pipeline Input</h4>
        <DataGrid
          rows={inputRows}
          columns={defineColumns}
          editMode="row"
          rowModesModel={rowModesModel}
          onRowModesModelChange={handleRowModesModelChange}
          onRowEditStop={handleRowEditStop}
          processRowUpdate={processRowUpdate}
          rowSelection={false}
          slots={{
            toolbar: EditToolbar,
          }}
          slotProps={{
            toolbar: { setInputRows, setRowModesModel },
          }}
          hideFooter={true}
          initialState={{
            pagination: {
              paginationModel: { pageSize: 100, page: 0 },
            },
          }}
          sx={{ height: "40vh" }}
        />
      </Box>
      <Box
        sx={{
          marginX: 3,
          display: "flex",
          flexDirection: "column",
          gap: 2,
        }}
      >
        {parameters.map((param, index) => {
          switch (param.type) {
            case "number":
              return (
                <NumberField
                  key={index}
                  data={param}
                  onChange={handleParamChange}
                  setParamValidity={setParamValidity}
                />
              );
            case "select":
              return (
                <SelectField
                  key={index}
                  data={param}
                  onChange={handleParamChange}
                />
              );
            default:
              return null;
          }
        })}
      </Box>

      <Button
        variant="contained"
        onClick={handelTransform}
        sx={{
          marginX: 3,
          marginBottom: 2,
        }}
        disabled={
          isAnyParamInvalid() ||
          inputRows.length < 1 ||
          isAnyRowInEditMode() ||
          isAnyRoleInvalid()
        }
      >
        Transform
      </Button>
    </div>
  );
}
