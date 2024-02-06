import CloseIcon from "@mui/icons-material/Close";
import CodeIcon from "@mui/icons-material/Code";
import ContentCopyIcon from "@mui/icons-material/ContentCopy";
import { Box, Button, CircularProgress, IconButton } from "@mui/material";
import { DataGrid, GridRowsProp } from "@mui/x-data-grid";
import { randomId } from "@mui/x-data-grid-generator";
import { useEffect, useState } from "react";
import { PipelineOutputProps } from "./model";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import {
  a11yDark,
  oneLight,
} from "react-syntax-highlighter/dist/esm/styles/prism";
import { useColorMode } from "@docusaurus/theme-common";

export default function PipelineOutput({
  defineOutputColumns,
  outputRows,
  displayMode,
  isPostApiProcessing,
  code,
}: PipelineOutputProps) {
  const displayRows: GridRowsProp = outputRows.map((row) => {
    return { id: randomId(), ...row };
  });
  const [codeExpand, setCodeExpand] = useState(false);
  const [copyText, setCopyText] = useState("Copy");
  const { colorMode, setColorMode } = useColorMode();

  const copyToClipboard = () => {
    navigator.clipboard
      .writeText(code)
      .then(() => {
        // Handle successful copy
        setCopyText("Copied!");
        setTimeout(() => {
          setCopyText("Copy");
        }, 3000);
      })
      .catch((err) => {
        // Handle error
        console.error("Error copying text: ", err);
      });
  };

  return (
    <Box
      sx={{
        border: "1px solid #7E7E7E",
        borderRadius: 3,
        display: "flex",
        flexDirection: "column",
        padding: 3,
        width: displayMode === "row" ? "50%" : "100%",
        minHeight: "60vh",
        maxHeight: "100vh",
      }}
    >
      <Box
        sx={{
          display: "flex",
          width: "100%",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <h4 style={{ margin: 0 }}>Pipeline Output</h4>

        <IconButton
          color="primary"
          disabled={code === ""}
          onClick={() => {
            setCodeExpand(!codeExpand);
          }}
        >
          {codeExpand ? <CloseIcon /> : <CodeIcon />}
        </IconButton>
      </Box>
      {isPostApiProcessing ? (
        <Box
          sx={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            minHeight: "60vh",
            maxHeight: "100vh",
          }}
        >
          <CircularProgress />
        </Box>
      ) : (
        <>
          {codeExpand ? (
            <Box>
              <SyntaxHighlighter
                language="python"
                style={colorMode === "dark" ? a11yDark : oneLight}
              >
                {code}
              </SyntaxHighlighter>

              <Button
                onClick={copyToClipboard}
                variant="contained"
                size="small"
                startIcon={<ContentCopyIcon />}
                sx={{
                  marginTop: 1,
                }}
              >
                {copyText}
              </Button>
            </Box>
          ) : (
            <DataGrid
              rows={displayRows}
              columns={defineOutputColumns}
              rowSelection={false}
              initialState={{
                pagination: {
                  paginationModel: { pageSize: 25, page: 0 },
                },
              }}
              getRowHeight={() => "auto"}
              sx={{
                height: "100%",
              }}
            />
          )}
        </>
      )}
    </Box>
  );
}
