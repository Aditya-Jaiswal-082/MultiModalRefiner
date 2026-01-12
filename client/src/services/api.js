import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const refinePrompt = async (payload) => {
  const response = await API.post("/refine", payload);
  return response.data;
};
