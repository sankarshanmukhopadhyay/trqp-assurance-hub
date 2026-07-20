import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";

const darkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;
mermaid.initialize({
  startOnLoad: false,
  securityLevel: "strict",
  theme: darkMode ? "dark" : "default",
  flowchart: { useMaxWidth: true, htmlLabels: true },
  sequence: { useMaxWidth: true, wrap: true },
});

function renderMermaid() {
  const blocks = document.querySelectorAll("pre > code.language-mermaid");
  blocks.forEach((code, index) => {
    const container = document.createElement("div");
    container.className = "mermaid";
    container.id = `mermaid-${index}`;
    container.textContent = code.textContent;
    code.parentElement.replaceWith(container);
  });
  if (blocks.length > 0) mermaid.run({ querySelector: ".mermaid" });
}

document.addEventListener("DOMContentLoaded", renderMermaid);
