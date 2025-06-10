// import { useStore } from "@/store/useStore";
import { AllCommunityModule, ModuleRegistry, ColDef } from 'ag-grid-community'; 
import { AgGridReact } from "ag-grid-react";
import { useState } from "react";

// Register all Community features
ModuleRegistry.registerModules([AllCommunityModule]);

type CarData = {
  make: string;
  model: string;
  price: number;
  electric: boolean;
}

export default function Sample() {
    // Row Data: The data to be displayed.
    const [rowData, setRowData] = useState<CarData[]>([
      { make: "Tesla", model: "Model Y", price: 64950, electric: true },
      { make: "Ford", model: "F-Series", price: 33850, electric: false },
      { make: "Toyota", model: "Corolla", price: 29600, electric: false },
  ]);

  // Column Definitions: Defines the columns to be displayed.
  const [colDefs, setColDefs] = useState<ColDef<CarData>[]>([
      { field: "make" },
      { field: "model" },
      { field: "price" },
      { field: "electric" }
  ]);
  return (
    // Data Grid will fill the size of the parent container
    <div style={{ height: 500 }} className="ag-theme-alpine">
      <AgGridReact
        rowData={rowData}
        columnDefs={colDefs}
      />
    </div>
)
}

// ✅ 1. React Spreadsheet Grid
// ✅ 2. React-DataSheet-Grid
// ✅ 3. Glide Data Grid
// ✅ 4. TanStack Table + Editable Cells
// ✅ 5. AG Grid (Community Edition)