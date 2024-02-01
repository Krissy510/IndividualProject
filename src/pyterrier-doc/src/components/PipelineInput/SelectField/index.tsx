import { Box, MenuItem, TextField } from "@mui/material";
import { IColumns } from "../model";

interface SelectField {
  data: IColumns;
  onChange: any;
}

export function SelectField({ data, onChange }) {
  return (
    <Box>
      <TextField
        onChange={(e) => onChange(data.id, e.target.value)}
        defaultValue={data.default}
        label={data.name}
        select
        fullWidth
        disabled={data.read_only}
      >
        {data.choices.map((choice, index) => (
          <MenuItem key={index} value={choice}>
            {choice}
          </MenuItem>
        ))}
      </TextField>
    </Box>
  );
}
