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
  inputRows: GridRowsProp;
  setInputRows: (newRows: GridRowsProp) => void;
  columns: Array<IColumns>;
  parameters: Array<IParameters>;
  apiUrl: string;
  paramData: Object;
  setOutputRows: (newRows: Array<Object>) => void;
  isPostApiProcessing: boolean;
  setIsApiProcessing: (isPostApiProcessing: boolean) => void;
  setParamData: (paramData: Object) => void;
  displayMode: string;
  setGeneratedCode: (code: string) => void;
  setOutputError: (outputError: string) => void;
}
