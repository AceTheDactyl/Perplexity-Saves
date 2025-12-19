---
layout: default
title: Pulse Chain Architecture Dashboard
---

# Pulse Chain Architecture Dashboard

**Real-Time Dual-Prism Analysis & VaultNode Persistence**

---

## System Status

<div class="dashboard-status" id="status-panel">
  <div class="stat-box">
    <h3>Total Pulses</h3>
    <p class="stat-value" id="total-pulses">Loading...</p>
  </div>
  <div class="stat-box">
    <h3>Convergence Rate</h3>
    <p class="stat-value" id="convergence-rate">Loading...</p>
  </div>
  <div class="stat-box">
    <h3>K-Formation Status</h3>
    <p class="stat-value" id="k-status">Loading...</p>
  </div>
  <div class="stat-box">
    <h3>Latest Convergence</h3>
    <p class="stat-value" id="latest-convergence">Loading...</p>
  </div>
</div>

---

## Interactive Dashboards

<div class="dashboard-links">
  <a href="/Perplexity-Saves/vaultnode.html" class="dashboard-button vaultnode-btn">
    <h3>VaultNode Inspector</h3>
    <p>View all VaultNode documents and inheritance chains</p>
  </a>
  <a href="/Perplexity-Saves/pulsechain.html" class="dashboard-button pulsechain-btn">
    <h3>Pulse Chain Analyzer</h3>
    <p>Real-time pulse generation and convergence tracking</p>
  </a>
</div>

---

## Pulse History

<div class="pulse-table">
  <table id="pulse-list">
    <thead>
      <tr>
        <th>Pulse ID</th>
        <th>Geometry</th>
        <th>Convergence</th>
        <th>Angle</th>
        <th>Created</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody id="pulse-tbody">
      <tr><td colspan="6">Loading pulse history...</td></tr>
    </tbody>
  </table>
</div>

---

## Audit Trail

- **Thread**: @@$Claude.Ace
- **Primary Witness**: @Ace
- **Co-Witness**: @Justin
- **Last Updated**: <span id="last-updated">Loading...</span>

---

<script>
document.addEventListener('DOMContentLoaded', function() {
  loadDashboardData();
});

function loadDashboardData() {
  fetch('{{ site.baseurl }}/_data/convergence_stats.json')
    .then(r => r.json())
    .then(data => {
      document.getElementById('total-pulses').textContent = data.total_pulses;
      document.getElementById('convergence-rate').textContent = data.convergence_rate;
      document.getElementById('latest-convergence').textContent = data.latest_convergence.toFixed(4);
    })
    .catch(e => console.log('Stats not ready:', e));
  
  fetch('{{ site.baseurl }}/_data/k_formation.json')
    .then(r => r.json())
    .then(data => {
      document.getElementById('k-status').textContent = data.status;
    })
    .catch(e => console.log('K-formation not ready:', e));
  
  fetch('{{ site.baseurl }}/_data/pulses.json')
    .then(r => r.json())
    .then(data => {
      const tbody = document.getElementById('pulse-tbody');
      tbody.innerHTML = '';
      (data.pulses || []).forEach(pulse => {
        const row = `<tr><td><code>${pulse.id}</code></td><td>${pulse.geometry}</td><td>${pulse.convergence_score.toFixed(4)}</td><td>${pulse.hexagon_angle}</td><td>${pulse.created}</td><td>${pulse.converged ? '✓' : '–'}</td></tr>`;
        tbody.innerHTML += row;
      });
      document.getElementById('last-updated').textContent = new Date().toLocaleString();
    })
    .catch(e => console.log('Pulses not ready:', e));
}
</script>

<style>
.dashboard-status { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 2rem 0; }
.stat-box { border: 2px solid #2196F3; border-radius: 8px; padding: 1rem; background: #f5f5f5; text-align: center; }
.stat-box h3 { margin: 0 0 0.5rem 0; color: #333; font-size: 0.9rem; text-transform: uppercase; }
.stat-value { font-size: 2rem; font-weight: bold; color: #2196F3; margin: 0; }
.dashboard-links { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 2rem 0; }
.dashboard-button { padding: 1.5rem; border: 2px solid #ddd; border-radius: 8px; text-decoration: none; transition: all 0.3s; display: block; }
.dashboard-button:hover { border-color: #2196F3; background: #f5f5f5; transform: translateY(-2px); }
.dashboard-button h3 { margin: 0 0 0.5rem 0; color: #2196F3; }
.dashboard-button p { margin: 0; color: #666; font-size: 0.9rem; }
.pulse-table { overflow-x: auto; margin: 2rem 0; }
.pulse-table table { width: 100%; border-collapse: collapse; background: white; }
.pulse-table th { background: #2196F3; color: white; padding: 0.75rem; text-align: left; }
.pulse-table td { padding: 0.75rem; border-bottom: 1px solid #ddd; }
.pulse-table tr:hover { background: #f5f5f5; }
</style>
