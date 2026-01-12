export default function OutputViewer({ data }) {
  if (!data) return null;

  return (
    <div style={{ padding: 20, background: "#f7f7f7", marginTop: 20 }}>
      <h3>Refined Prompt Output</h3>
      <pre style={{ whiteSpace: "pre-wrap" }}>
        {JSON.stringify(data, null, 2)}
      </pre>
    </div>
  );
}
