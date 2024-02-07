import { Box, TextField, createTheme, ThemeProvider } from "@mui/material";
import { useState } from "react";
import { useColorMode } from "@docusaurus/theme-common";

// Custom theme for dark mode
const darkTheme = createTheme({
  palette: {
    mode: "dark",
    text: {
      primary: "#ffffff", // White text color
    },
    primary: {
      main: "#ffffff", // White border color
    },
  },
});

export function NumberField({ data, onChange, setParamValidity }) {
  const [value, setValue] = useState(data.default);
  const isError = !(value > 0);
  const { colorMode, setColorMode } = useColorMode();
  const theme = colorMode === "dark" ? darkTheme : createTheme(); // Use dark theme if prefers dark mode, otherwise use default theme

  return (
    <ThemeProvider theme={theme}>
      <Box>
        <span>{data.name}</span>
        <TextField
          type="number"
          required
          onChange={(e) => {
            const newValue = Number(e.target.value);
            onChange(data.id, newValue);
            setValue(newValue);
            setParamValidity((prev) => ({ ...prev, [data.id]: newValue > 0 }));
          }}
          defaultValue={data.default}
          error={isError}
          helperText={isError ? "Value must be greater than 0" : ""}
          fullWidth
        />
      </Box>
    </ThemeProvider>
  );
}
