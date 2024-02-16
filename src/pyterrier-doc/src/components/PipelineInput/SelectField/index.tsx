import { useColorMode } from "@docusaurus/theme-common";
import {
  Box,
  MenuItem,
  Select,
  ThemeProvider,
  createTheme,
} from "@mui/material";
import { IColumns } from "../model";

interface SelectField {
  data: IColumns;
  onChange: any;
}

const darkTheme = createTheme({
  palette: {
    mode: "dark",
    text: {
      primary: "#ffffff",
    },
    primary: {
      main: "#ffffff",
    },
  },
});

export function SelectField({ data, onChange }) {
  const { colorMode, setColorMode } = useColorMode();
  const theme = colorMode === "dark" ? darkTheme : createTheme();
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
