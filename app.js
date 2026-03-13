// ======================================
// GLOBAL STATE
// ======================================
let lastResult = null;
const API_URL = "http://127.0.0.1:8000";

// ======================================
// REGISTER
// ======================================
async function register() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch(`${API_URL}/register`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    const data = await res.json();
    console.log("REGISTER RESPONSE:", data);

    if (!res.ok) {
      alert(data.detail || "Registration failed");
      return;
    }

    alert("Registration successful! Please login.");
    window.location.href = "login.html";

  } catch (err) {
    console.error(err);
    alert("Backend not reachable");
  }
}

// ======================================
// LOGIN
// ======================================
async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch(`${API_URL}/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    const data = await res.json();
    console.log("LOGIN RESPONSE:", data);

    if (!res.ok) {
      alert(data.detail || "Login failed");
      return;
    }

    // Save token
    localStorage.setItem("token", data.access_token);

    // Redirect to dashboard
    window.location.href = "dashboard.html";

  } catch (err) {
    console.error(err);
    alert("Backend not reachable");
  }
}

// ======================================
// CHECK AUTH (DASHBOARD PROTECTION)
// ======================================
function checkAuth() {
  const token = localStorage.getItem("token");
  if (!token) {
    window.location.href = "login.html";
  }
}

// ======================================
// LOGOUT
// ======================================
function logout() {
  localStorage.removeItem("token");
  window.location.href = "login.html";
}

// ======================================
// UPLOAD PDF & ANALYZE
// ======================================
async function uploadPDF() {
  const fileInput = document.getElementById("pdfFile");
  const status = document.getElementById("status");
  const resultsDiv = document.getElementById("results");
  const downloadBtn = document.getElementById("downloadBtn");

  resultsDiv.innerHTML = "";
  status.innerText = "";

  if (!fileInput.files.length) {
    alert("Please upload a PDF file");
    return;
  }

  const token = localStorage.getItem("token");
  if (!token) {
    alert("Not authenticated");
    window.location.href = "login.html";
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  status.innerText = "Analyzing document...";

  try {
    const res = await fetch("http://127.0.0.1:8000/analyze/", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${token}`
      },
      body: formData
    });

    const data = await res.json();
    console.log("ANALYZE RESPONSE:", data);

    if (!res.ok) {
      alert(data.detail || "Unauthorized");
      return;
    }

    lastResult = data;

    status.innerText = `Total clauses found: ${data.total_clauses_found}`;

    if (!data.clauses || data.clauses.length === 0) {
      resultsDiv.innerHTML = "<p>No clauses detected.</p>";
      return;
    }

    // ENABLE DOWNLOAD BUTTON
    downloadBtn.disabled = false;

    // Render cards (same logic as old index)
    data.clauses.forEach((item, index) => {
      const card = document.createElement("div");
      card.className = "card";

      card.innerHTML = `
        <h3>${index + 1}. ${item.clause}</h3>
        <p class="confidence">
          Confidence: ${(item.confidence * 100).toFixed(2)}%
        </p>
        <p class="sentence">${item.sentence}</p>
      `;

      resultsDiv.appendChild(card);
    });

  } catch (err) {
    console.error(err);
    status.innerText = "Error connecting to backend";
  }
}

// ======================================
// DOWNLOAD REPORT
// ======================================
function downloadPDF() {
  if (!lastResult || !lastResult.clauses) {
    alert("Analyze a document first");
    return;
  }

  let content = "LEGAL CLAUSE IDENTIFICATION REPORT\n\n";

  lastResult.clauses.forEach((c, i) => {
    content +=
      `${i + 1}. ${c.clause}\n` +
      `Confidence: ${(c.confidence * 100).toFixed(2)}%\n` +
      `${c.sentence}\n\n` +
      "-----------------------------------\n\n";
  });

  const blob = new Blob([content], { type: "application/pdf" });
  const url = URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = "legal_clause_report.pdf";
  a.click();

  URL.revokeObjectURL(url);
}

// ======================================
// SIDEBAR TOGGLE
// ======================================
function toggleSidebar() {
  document.querySelector(".sidebar").classList.toggle("hidden");
}

