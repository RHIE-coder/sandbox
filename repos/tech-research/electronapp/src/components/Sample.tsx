import { HotTable } from "@handsontable/react-wrapper";
import { registerAllModules } from "handsontable/registry";
import "handsontable/styles/handsontable.css";
import "handsontable/styles/ht-theme-main.css";
import { useStore } from "@/store/useStore";

// register Handsontable's modules
registerAllModules();

export default function Sample() {
  const data = useStore((state) => state.data);
  const headers = data[0].map(String);
  const tableData = data.slice(1);
  console.log(tableData);

  return (
    <HotTable
      data={tableData}
      rowHeaders={false}
      colHeaders={headers}
      height="auto"
      autoWrapRow={true}
      autoWrapCol={true}
      licenseKey="non-commercial-and-evaluation" // for non-commercial use only
    />
  );
}
