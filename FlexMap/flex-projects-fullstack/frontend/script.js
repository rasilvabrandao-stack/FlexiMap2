let projects = [];

const API = 'https://flexmap.onrender.com/api/prazos'; // <-- mude depois

async function loadProjects() {
  const res = await fetch(API);
  projects = await res.json();
  // 🔧 Normaliza nomes e datas do backend
projects = projects.map(p => ({
  ...p,
  name: p.name || p.nome || "Sem nome",
  startDate: p.startDate || p.data_inicio,
  endDate: p.endDate || p.data_fim,
  type: p.type || p.tipo || "Outro"
}));

  updateDashboard(); renderTimeline(); renderCalendar(); addProjectMarkers();
}

async function saveProject(p) {
  await fetch(API, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      nome: p.name,
      descricao: p.description,
      tipo: p.type,
      data_inicio: p.startDate,
      data_fim: p.endDate,
      estado: p.location.state,
      endereco: p.address,
      latitude: p.location.lat,
      longitude: p.location.lng
    })
  });
  loadProjects();
}

async function updateProject(id, changes) {
  await fetch(`${API}/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(changes)
  });
  loadProjects();
}

async function deleteProject(id) {
  await fetch(`${API}/${id}`, { method: 'DELETE' });
  loadProjects();
}

// ----- substitua suas funções antigas por estas -----
// no lugar de saveToLocal() → chame saveProject() ou updateProject()
// no lugar de deleteProject() local → chame deleteProject(id)

// ----- inicie tudo -----

loadProjects();
