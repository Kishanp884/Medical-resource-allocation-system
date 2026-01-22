async function runAllocation() {
  const out = document.getElementById('output');
  out.innerHTML = '<div class="card"><div class="spinner"></div> Running allocation...</div>';

  try {
    const res = await fetch('/api/allocate', { method: 'POST' });
    const data = await res.json();

    lastResults = data.results || [];
    renderAllocation(data.results);
    showToast('Allocation complete');

  } catch (err) {
    out.innerHTML = `<div class="card">Error: ${err.message}</div>`;
  }
}

async function showStatus() {
  const out = document.getElementById('output');
  out.innerHTML = '<div class="card"><div class="spinner small"></div> Loading status...</div>';
  try {
    const res = await fetch('/api/status');
    const data = await res.json();

    lastStatus = data;
    renderStatus(data);
    showToast('Status loaded');

  } catch (err) {
    out.innerHTML = `<div class="card">Error: ${err.message}</div>`;
  }
}

async function showAlerts() {
  const out = document.getElementById('output');
  out.innerHTML = '<div class="card"><div class="spinner small"></div> Checking alerts...</div>';
  try {
    const res = await fetch('/api/alerts');
    const data = await res.json();

    renderAlerts(data);
    showToast('Alerts loaded');

  } catch (err) {
    out.innerHTML = `<div class="card">Error: ${err.message}</div>`;
  }
}

async function updateSimulation() {
  try {
    await fetch('/api/update_simulation', { method: 'POST' });
    showToast('Simulation updated');
  } catch (err) {
    showToast('Error updating simulation');
  }
}
let lastResults = null;
let lastStatus = null;

function renderAllocation(results) {
  const out = document.getElementById('output');
  if (!results || !results.length) {
    out.innerHTML = `<div class="card">No results</div>`;
    return;
  }

  const rows = results.map(r => {
    const amb = r.ambulance ? r.ambulance : '-';
    const hos = r.hospital ? r.hospital : 'No resources';
    const ambClass = r.ambulance ? '' : 'muted';
    const hosClass = r.hospital ? '' : 'muted';
    return `<tr>
      <td data-label="Patient">${r.patient}</td>
      <td data-label="Ambulance" class="${ambClass}">${amb}</td>
      <td data-label="Hospital" class="${hosClass}">${hos}</td>
    </tr>`;
  }).join('');

  out.innerHTML = `
    <div class="card">
      <h3>Allocation Results</h3>
      <div class="muted">${results.length} rows</div>
      <table>
        <thead><tr><th>Patient</th><th>Ambulance</th><th>Hospital</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>
    </div>`;
}

function renderStatus(data) {
  const out = document.getElementById('output');
  const ambRows = data.ambulances.map(a => `<tr><td data-label="ID">${a.id}</td><td data-label="Location">${a.location}</td><td data-label="Available">${a.available}</td><td data-label="IV Supplies">${a.iv_supplies}</td></tr>`).join('');
  const hosRows = data.hospitals.map(h => `<tr><td data-label="ID">${h.id}</td><td data-label="Location">${h.location}</td><td data-label="Capacity">${h.capacity}</td><td data-label="ICU">${h.icu}</td><td data-label="Organs">${h.organs ? h.organs.join(', ') : ''}</td></tr>`).join('');
  const patRows = data.patients.map(p => `<tr><td data-label="ID">${p.id}</td><td data-label="Severity">${p.severity}</td><td data-label="IV Required">${p.iv_required}</td><td data-label="Needs Organ">${p.needs_organ || ''}</td><td data-label="IV Status">${p.iv_status || ''}</td></tr>`).join('');
  const orgRows = data.organs.map(o => `<tr><td data-label="ID">${o.id}</td><td data-label="Type">${o.type}</td><td data-label="Temperature">${o.temperature}°C</td><td data-label="Transport Time">${o.transport_time} min</td><td data-label="Viable">${o.viable}</td></tr>`).join('');

  out.innerHTML = `
    <div class="card">
      <h3>Ambulances</h3>
      <table><thead><tr><th>ID</th><th>Location</th><th>Available</th><th>IV Supplies</th></tr></thead><tbody>${ambRows}</tbody></table>
    </div>
    <div class="spacer"></div>
    <div class="card">
      <h3>Hospitals</h3>
      <table><thead><tr><th>ID</th><th>Location</th><th>Capacity</th><th>ICU</th><th>Organs</th></tr></thead><tbody>${hosRows}</tbody></table>
    </div>
    <div class="spacer"></div>
    <div class="card">
      <h3>Patients</h3>
      <table><thead><tr><th>ID</th><th>Severity</th><th>IV Required</th><th>Needs Organ</th><th>IV Status</th></tr></thead><tbody>${patRows}</tbody></table>
    </div>
    <div class="spacer"></div>
    <div class="card">
      <h3>Organs</h3>
      <table><thead><tr><th>ID</th><th>Type</th><th>Temperature</th><th>Transport Time</th><th>Viable</th></tr></thead><tbody>${orgRows}</tbody></table>
    </div>`;
}

function renderAlerts(data) {
  const out = document.getElementById('output');
  const ivAlerts = data.iv_alerts.map(a => `<li>${a}</li>`).join('');
  const organAlerts = data.organ_alerts.map(a => `<li>${a}</li>`).join('');

  out.innerHTML = `
    <div class="card">
      <h3>IV Drip Alerts</h3>
      <ul>${ivAlerts || '<li>No alerts</li>'}</ul>
    </div>
    <div class="spacer"></div>
    <div class="card">
      <h3>Organ Alerts</h3>
      <ul>${organAlerts || '<li>No alerts</li>'}</ul>
    </div>`;
}

function downloadResults() {
  if (!lastResults) return showToast('No results to download');
  const blob = new Blob([JSON.stringify(lastResults, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = 'emras-results.json';
  document.body.appendChild(a); a.click(); a.remove();
  URL.revokeObjectURL(url);
  showToast('Downloaded results');
}

async function copyResults() {
  if (!lastResults) return showToast('No results to copy');
  try {
    await navigator.clipboard.writeText(JSON.stringify(lastResults, null, 2));
    showToast('Results copied to clipboard');
  } catch (e) {
    showToast('Clipboard not available');
  }
}

function clearOutput() {
  document.getElementById('output').innerHTML = '';
  lastResults = null; lastStatus = null;
}

function showToast(msg, timeout = 2500) {
  let t = document.getElementById('toast');
  if (!t) {
    t = document.createElement('div');
    t.id = 'toast'; document.body.appendChild(t);
  }
  t.textContent = msg; t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), timeout);
}

function applyFilter() {
  const q = document.getElementById('filter').value.toLowerCase().trim();
  const onlyUn = document.getElementById('onlyUnassigned').checked;
  if (!lastResults) return;
  const f = lastResults.filter(r => {
    const hay = `${r.patient} ${r.ambulance||''} ${r.hospital||''}`.toLowerCase();
    if (onlyUn && (r.ambulance || r.hospital)) return false;
    if (!q) return true;
    return hay.includes(q);
  });
  renderAllocation(f);
}

document.getElementById('run').addEventListener('click', runAllocation);
document.getElementById('status').addEventListener('click', showStatus);
document.getElementById('alerts').addEventListener('click', showAlerts);
document.getElementById('updateSim').addEventListener('click', updateSimulation);
document.getElementById('download').addEventListener('click', downloadResults);
document.getElementById('copy').addEventListener('click', copyResults);
document.getElementById('clear').addEventListener('click', clearOutput);
document.getElementById('filter').addEventListener('input', applyFilter);
document.getElementById('onlyUnassigned').addEventListener('change', applyFilter);
