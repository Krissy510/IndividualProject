import { GridRowsProp } from "@mui/x-data-grid/models";

export interface IColumns {
  name: string;
  width?: number;
}

export interface IParameters {
  name: string;
  id: string;
  type: string;
  choices?: Array<string>;
  default: string | number;
}

export interface PipelineInputProps {
  exampleInputRows: GridRowsProp;
  columns: Array<IColumns>;
  parameters: Array<IParameters>;
  apiUrl: string;
}
