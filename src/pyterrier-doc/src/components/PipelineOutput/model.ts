import { GridColDef, GridRowsProp, GridValidRowModel } from "@mui/x-data-grid";

export interface PipelineOutputProps {
  defineOutputColumns: GridColDef<GridValidRowModel>[];
  outputRows: GridRowsProp;
  displayMode: string;
  isPostApiProcessing: boolean;
}
