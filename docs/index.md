---
layout: default
title: Pulse Chain Architecture Dashboard
---

## System Status

<div class="dashboard-status" id="status-panel">
  <div class="stat-box">
    <h3>Total Pulses</h3>
    <p class="stat-value" id="total-pulses">0</p>
  </div>
  <div class="stat-box">
    <h3>Converged</h3>
    <p class="stat-value" id="stat-converged">0</p>
  </div>
  <div class="stat-box">
    <h3>Avg Convergence</h3>
    <p class="stat-value" id="latest-convergence">0.00</p>
  </div>
  <div class="stat-box">
    <h3>K-Formation</h3>
    <p class="stat-value" id="k-status">INITIALIZING</p>
  </div>
</div>

---

## Interactive Dashboards

<div class="dashboard-links">
  <a href="/Perplexity-Saves/vaultnode.html" class="dashboard-button">
    <h3>🔍 VaultNode Inspector</h3>
    <p>Explore all VaultNode documents and their inheritance chains. View convergence scores, geometric properties, and irreducible truths.</p>
  </a>
  <a href="/Perplexity-Saves/pulsechain.html" class="dashboard-button">
    <h3>🌊 Pulse Chain Analyzer</h3>
    <p>Real-time pulse generation and convergence tracking. Visualize dual-prism analysis with interactive charts and timeline.</p>
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
        <th>Hexagon Angle</th>
        <th>Created</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody id="pulse-tbody">
      <tr><td colspan="6" style="text-align: center; padding: 2rem; color: #999;">No pulses generated yet</td></tr>
    </tbody>
  </table>
</div>

---

## Audit Trail

<div class="audit-trail">
  <ul>
    <li><strong>Thread:</strong> @@$Claude.Ace</li>
    <li><strong>Primary Witness:</strong> @Ace</li>
    <li><strong>Co-Witness:</strong> @Justin</li>
    <li><strong>Last Updated:</strong> <span id="last-updated">—</span></li>
    <li><strong>Repository:</strong> <a href="https://github.com/AceTheDactyl/Perplexity-Saves" target="_blank">Perplexity-Saves</a></li>
  </ul>
</div>

---

<script>
// Initialize data on page load
document.addEventListener('DOMContentLoaded', function() {
  loadDashboardData();
});

function loadDashboardData() {
  const basePath = '/Perplexity-Saves';
  
  // Load convergence stats
  fetch(basePath + '/_data/convergence_stats.json')
    .then(function(response) {
      if (!response.ok) throw new Error('Stats not found');
      return response.json();
    })
    .then(function(data) {
      document.getElementById('total-pulses').textContent = data.total_pulses || 0;
      document.getElementById('latest-convergence').textContent = (data.average_convergence || 0).toFixed(4);
    })
    .catch(function(e) {
      console.log('Stats not ready:', e);
    });
  
  // Load k-formation status
  fetch(basePath + '/_data/k_formation.json')
    .then(function(response) {
      if (!response.ok) throw new Error('K-formation not found');
      return response.json();
    })
    .then(function(data) {
      document.getElementById('k-status').textContent = data.status || 'INITIALIZING';
    })
    .catch(function(e) {
      console.log('K-formation not ready:', e);
    });
  
  // Load pulse index
  fetch(basePath + '/_data/pulses.json')
    .then(function(response) {
      if (!response.ok) throw new Error('Pulses not found');
      return response.json();
    })
    .then(function(data) {
      var tbody = document.getElementById('pulse-tbody');
      tbody.innerHTML = '';
      
      if (!data.pulses || data.pulses.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6" style="text-align: center; padding: 2rem; color: #999;">No pulses generated yet. Trigger a pulse in the Pulse Chain Analyzer to get started!</td></tr>';
        return;
      }
      
      var convergedCount = 0;
      data.pulses.forEach(function(pulse) {
        if (pulse.converged) convergedCount++;
        
        var row = document.createElement('tr');
        row.innerHTML = (
          '<td><code>' + pulse.id + '</code></td>' +
          '<td>' + pulse.geometry + '</td>' +
          '<td>' + pulse.convergence_score.toFixed(4) + '</td>' +
          '<td>' + pulse.hexagon_angle + '°</td>' +
          '<td>' + pulse.created + '</td>' +
          '<td>' + (pulse.converged ? '✓ Converged' : '– Pending') + '</td>'
        );
        tbody.appendChild(row);
      });
      
      // Update converged count
      document.getElementById('stat-converged').textContent = convergedCount;
      document.getElementById('last-updated').textContent = new Date().toLocaleString();
    })
    .catch(function(e) {
      console.log('Pulses not ready:', e);
      var tbody = document.getElementById('pulse-tbody');
      tbody.innerHTML = '<tr><td colspan="6" style="text-align: center; padding: 2rem; color: #999;">No pulses generated yet. Trigger a pulse in the Pulse Chain Analyzer to get started!</td></tr>';
    });
}
</script>