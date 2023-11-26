import { IColumns, IParameters } from "../PipelineInput/model";

export interface InteractiveFeatureProps {
    example: Array<Object>;
    defaultDisplayMode?: string;
    columns: Array<IColumns>;
    parameters: Array<IParameters>;
    apiUrl: string;
}