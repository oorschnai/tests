import React from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import Checks from "./pages/Checks.jsx";
import Projects from "./pages/Projects.jsx";

createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Projects />} />
      <Route path="/checks" element={<Checks />} />
    </Routes>
  </BrowserRouter>,
);
