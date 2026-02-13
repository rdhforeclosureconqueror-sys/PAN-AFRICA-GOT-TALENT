import { useState } from "react";
import Layout from "../../components/Layout";

const checklist = [
  "3 Shares",
  "Receipt included",
  "Location included",
  "Menu included",
  "Community impact",
  "HD video/audio",
];

export default function SubmitEntryPage() {
  const [file, setFile] = useState<File | null>(null);
  const [message, setMessage] = useState("");

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a video first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/contest/upload`,
        {
          method: "POST",
          body: formData,
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        }
      );

      const data = await res.json();

      if (res.ok) {
        setMessage("Upload successful!");
      } else {
        setMessage(data.detail || "Upload failed.");
      }
    } catch (err) {
      setMessage("Server error.");
    }
  };

  return (
    <Layout>
      <div className="card">
        <h2>Submit Talent Entry</h2>

        <ul>
          {checklist.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>

        <br />

        <input
          type="file"
          accept="video/*"
          onChange={(e) => {
            if (e.target.files) {
              setFile(e.target.files[0]);
            }
          }}
        />

        <br />
        <br />

        <button onClick={handleUpload}>Upload Video</button>

        {message && <p>{message}</p>}
      </div>
    </Layout>
  );
}
