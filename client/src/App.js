import { useState } from "react";
import InputForm from "./components/InputForm";
import OutputViewer from "./components/OutputViewer";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div style={{ maxWidth: 800, margin: "auto" }}>
      <InputForm onResult={setResult} />
      <OutputViewer data={result} />
    </div>
  );
}

export default App;
