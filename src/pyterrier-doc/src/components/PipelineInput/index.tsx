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
import axios from "axios";
import { useEffect, useState } from "react";
import { NumberField } from "./NumberField";
import { SelectField } from "./SelectField";
import { PipelineInputProps } from "./model";

export default function PipelineInput({
  inputRows,
  setInputRows,
  columns,
  parameters,
  apiUrl,
  setOutputRows,
  isPostApiProcessing,
  setIsApiProcessing,
  displayMode,
  setGeneratedCode,
}: PipelineInputProps) {
  useEffect(() => {
    setParamData(
      parameters.reduce((obj, item) => {
        obj[item.id] = item.default;
        return obj;
      }, {})
    );

    setParamValidity(
      parameters.reduce((acc, param) => {
        if (param.type === "number") {
          acc[param.id] = Number(param.default) > 0;
        }
        return acc;
      }, {})
    );
  }, [parameters]);

  const [rowModesModel, setRowModesModel] = useState<GridRowModesModel>({});
  const [paramData, setParamData] = useState({});
  const [paramValidity, setParamValidity] = useState({});

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
    const input = inputRows.map(({ id, ...rest }) => rest);
    const request = {
      input,
      ...paramData,
    };

    setIsApiProcessing(true);

    axios
      .post(apiUrl, request, {
        headers: {
          "X-PYTERRIERAPI-KEY": process.env.API_KEY,
        },
      })
      .then((responese) => {
        if (responese.status === 200) {
          setOutputRows(responese.data.result);
          setGeneratedCode(responese.data.code);
        }
      })
      .catch((error) => {})
      .finally(() => {
        setIsApiProcessing(false);
      });
  };

  const isAnyRowInEditMode = (): boolean => {
    return Object.values(rowModesModel).some(
      (modeInfo) => modeInfo.mode === GridRowModes.Edit
    );
  };

  const isAnyRowInvalid = (): boolean => {
    return inputRows.some((row) => {
      return Object.values(row).some((value) => value === "");
    });
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
      setInputRows((oldRows) => {
        const newRow = { id, isNew: true };
        columns.map((col) => (newRow[col.name] = ""));
        return [newRow, ...oldRows];
      });
      setRowModesModel((oldModel) => ({
        ...oldModel,
        [id]: { mode: GridRowModes.Edit },
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
    <Box
      sx={{
        border: "1px solid #7E7E7E",
        borderRadius: 5,
        display: "flex",
        flexDirection: "column",
        gap: 3,
        width: displayMode === "row" ? "50%" : "100%",
      }}
    >
      <Box
        sx={{
          padding: 3,
          paddingBottom: 4,
          height: "40vh",
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
          getRowHeight={() => "auto"}
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
          isAnyRowInvalid() ||
          isPostApiProcessing
        }
      >
        Transform
      </Button>
    </Box>
  );
}
