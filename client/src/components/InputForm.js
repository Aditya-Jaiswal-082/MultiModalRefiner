import { useState } from "react";
import { refinePrompt } from "../services/api";

export default function InputForm({ onResult }) {
  const [text, setText] = useState("");
  const [images, setImages] = useState([]);
  const [documents, setDocuments] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);

    const payload = {
      text,
      images: images.map((file) => ({
        filename: file.name,
        caption: "User uploaded image"
      })),
      documents: documents.map((file) => ({
        filename: file.name,
        extracted_text: "Document uploaded by user"
      }))
    };

    try {
      const result = await refinePrompt(payload);
      onResult(result);
    } catch (err) {
      alert("Failed to refine prompt");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Multi-Modal Prompt Refiner</h2>

      <textarea
        placeholder="Enter product or task description..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={6}
        style={{ width: "100%", marginBottom: 10 }}
      />

      <input
        type="file"
        accept="image/*"
        multiple
        onChange={(e) => setImages([...e.target.files])}
      />

      <br /><br />

      <input
        type="file"
        accept=".pdf,.doc,.docx"
        multiple
        onChange={(e) => setDocuments([...e.target.files])}
      />

      <br /><br />

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Refining..." : "Refine Prompt"}
      </button>
    </div>
  );
}
