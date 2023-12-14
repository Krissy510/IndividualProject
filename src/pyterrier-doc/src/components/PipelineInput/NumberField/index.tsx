import { TextField } from "@mui/material";
import { useState } from "react";

export function NumberField({ data, onChange, setParamValidity }) {
  const [value, setValue] = useState(data.default);
  const isError = !(value > 0);

  return (
    <TextField
      type="number"
      required
      label={data.name}
      onChange={(e) => {
        const newValue = Number(e.target.value);
        onChange(data.id, newValue);
        setValue(newValue);
        setParamValidity((prev) => ({ ...prev, [data.id]: newValue > 0 }));
      }}
      defaultValue={data.default}
      error={isError}
      helperText={isError ? "Value must be greater than 0" : ""}
    />
  );
}
