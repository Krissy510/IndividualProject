import {
  Box,
  MenuItem,
  Select,
  ThemeProvider,
  createTheme,
} from "@mui/material";
import { IColumns } from "../model";
import { useColorMode } from "@docusaurus/theme-common";

interface SelectField {
  data: IColumns;
  onChange: any;
}

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

export function SelectField({ data, onChange }) {
  const { colorMode, setColorMode } = useColorMode();
  const theme = colorMode === "dark" ? darkTheme : createTheme(); // Use dark theme if prefers dark mode, otherwise use default theme
  return (
    <ThemeProvider theme={theme}>
      <Box>
        <span>{data.name}</span>
        <Select
          onChange={(e) => onChange(data.id, e.target.value)}
          defaultValue={data.default}
          fullWidth
          disabled={data.read_only}
        >
          {data.choices.map((choice, index) => (
            <MenuItem key={index} value={choice}>
              {choice}
            </MenuItem>
          ))}
        </Select>
      </Box>
    </ThemeProvider>
  );
}
