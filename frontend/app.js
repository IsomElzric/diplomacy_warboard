const defaultCountryBaseline = {
  England: {
    current: {
      country: 'England',
      year: 1901,
      season: 'Spring',
      sc: 3,
      units: 3,
      builds: 0,
      sc_gains: 0,
      unit_growth: 0,
      build_effeciency: 0,
      momentum: 0,
      ema_momentum: 0,
      growth_rate: 0,
      cgi: 0,
      holds: 0,
      supports: 0,
      active_fronts: 0,
      hold_rate: 0,
      support_rate: 0,
      isolation: 0,
      encirclement: 0,
    },
    history: [
      { year: 1901, season: 'Spring', country: 'England', sc: 3, units: 3, builds: 0, momentum: 0, ema_momentum: 0, cgi: 0 },
    ],
  },
  France: {
    current: {
      country: 'France',
      year: 1901,
      season: 'Spring',
      sc: 3,
      units: 3,
      builds: 0,
      sc_gains: 0,
      unit_growth: 0,
      build_effeciency: 0,
      momentum: 0,
      ema_momentum: 0,
      growth_rate: 0,
      cgi: 0,
      holds: 0,
      supports: 0,
      active_fronts: 0,
      hold_rate: 0,
      support_rate: 0,
      isolation: 0,
      encirclement: 0,
    },
    history: [
      { year: 1901, season: 'Spring', country: 'France', sc: 3, units: 3, builds: 0, momentum: 0, ema_momentum: 0, cgi: 0 },
    ],
  },
  Germany: {
    current: {
      country: 'Germany',
      year: 1901,
      season: 'Spring',
      sc: 3,
      units: 3,
      builds: 0,
      sc_gains: 0,
      unit_growth: 0,
      build_effeciency: 0,
      momentum: 0,
      ema_momentum: 0,
      growth_rate: 0,
      cgi: 0,
      holds: 0,
      supports: 0,
      active_fronts: 0,
      hold_rate: 0,
      support_rate: 0,
      isolation: 0,
      encirclement: 0,
    },
    history: [
      { year: 1901, season: 'Spring', country: 'Germany', sc: 3, units: 3, builds: 0, momentum: 0, ema_momentum: 0, cgi: 0 },
    ],
  },
  Italy: {
    current: {
      country: 'Italy',
      year: 1901,
      season: 'Spring',
      sc: 3,
      units: 3,
      builds: 0,
      sc_gains: 0,
      unit_growth: 0,
      build_effeciency: 0,
      momentum: 0,
      ema_momentum: 0,
      growth_rate: 0,
      cgi: 0,
      holds: 0,
      supports: 0,
      active_fronts: 0,
      hold_rate: 0,
      support_rate: 0,
      isolation: 0,
      encirclement: 0,
    },
    history: [
      { year: 1901, season: 'Spring', country: 'Italy', sc: 3, units: 3, builds: 0, momentum: 0, ema_momentum: 0, cgi: 0 },
    ],
  },
  Austria: {
    current: {
      country: 'Austria',
      year: 1901,
      season: 'Spring',
      sc: 3,
      units: 3,
      builds: 0,
      sc_gains: 0,
      unit_growth: 0,
      build_effeciency: 0,
      momentum: 0,
      ema_momentum: 0,
      growth_rate: 0,
      cgi: 0,
      holds: 0,
      supports: 0,
      active_fronts: 0,
      hold_rate: 0,
      support_rate: 0,
      isolation: 0,
      encirclement: 0,
    },
    history: [
      { year: 1901, season: 'Spring', country: 'Austria', sc: 3, units: 3, builds: 0, momentum: 0, ema_momentum: 0, cgi: 0 },
    ],
  },
  Turkey: {
    current: {
      country: 'Turkey',
      year: 1901,
      season: 'Spring',
      sc: 3,
      units: 3,
      builds: 0,
      sc_gains: 0,
      unit_growth: 0,
      build_effeciency: 0,
      momentum: 0,
      ema_momentum: 0,
      growth_rate: 0,
      cgi: 0,
      holds: 0,
      supports: 0,
      active_fronts: 0,
      hold_rate: 0,
      support_rate: 0,
      isolation: 0,
      encirclement: 0,
    },
    history: [
      { year: 1901, season: 'Spring', country: 'Turkey', sc: 3, units: 3, builds: 0, momentum: 0, ema_momentum: 0, cgi: 0 },
    ],
  },
  Russia: {
    current: {
      country: 'Russia',
      year: 1901,
      season: 'Spring',
      sc: 3,
      units: 3,
      builds: 0,
      sc_gains: 0,
      unit_growth: 0,
      build_effeciency: 0,
      momentum: 0,
      ema_momentum: 0,
      growth_rate: 0,
      cgi: 0,
      holds: 0,
      supports: 0,
      active_fronts: 0,
      hold_rate: 0,
      support_rate: 0,
      isolation: 0,
      encirclement: 0,
    },
    history: [
      { year: 1901, season: 'Spring', country: 'Russia', sc: 3, units: 3, builds: 0, momentum: 0, ema_momentum: 0, cgi: 0 },
    ],
  },
};

const emptyPayload = {
  selectedSeason: null,
  countries: defaultCountryBaseline,
};

const fallbackPayload = {
  selectedSeason: { year: 1901, season: 'Spring' },
  countries: {
    England: {
      current: {
        country: 'England',
        year: 1901,
        season: 'Spring',
        sc: 3,
        units: 3,
        builds: 0,
        sc_gains: 0,
        unit_growth: 0,
        build_effeciency: 0,
        momentum: 0,
        ema_momentum: 0,
        growth_rate: 0,
        cgi: 0,
        holds: 0,
        supports: 0,
        active_fronts: 0,
        hold_rate: 0,
        support_rate: 0,
        isolation: 0,
        encirclement: 0,
      },
      history: [
        { year: 1901, season: 'Spring', country: 'England', sc: 3, units: 3, builds: 0, momentum: 0, ema_momentum: 0, cgi: 0 },
      ],
    },
    France: {
      current: {
        country: 'France',
        year: 1901,
        season: 'Spring',
        sc: 3,
        units: 3,
        builds: 0,
        sc_gains: 0,
        unit_growth: 0,
        build_effeciency: 0,
        momentum: 0,
        ema_momentum: 0,
        growth_rate: 0,
        cgi: 0,
        holds: 0,
        supports: 0,
        active_fronts: 0,
        hold_rate: 0,
        support_rate: 0,
        isolation: 0,
        encirclement: 0,
      },
      history: [
        { year: 1901, season: 'Spring', country: 'France', sc: 3, units: 3, builds: 0, momentum: 0, ema_momentum: 0, cgi: 0 },
      ],
    },
    Germany: {
      current: {
        country: 'Germany',
        year: 1901,
        season: 'Spring',
        sc: 3,
        units: 3,
        builds: 0,
        sc_gains: 0,
        unit_growth: 0,
        build_effeciency: 0,
        momentum: 0,
        ema_momentum: 0,
        growth_rate: 0,
        cgi: 0,
        holds: 0,
        supports: 0,
        active_fronts: 0,
        hold_rate: 0,
        support_rate: 0,
        isolation: 0,
        encirclement: 0,
      },
      history: [
        { year: 1901, season: 'Spring', country: 'Germany', sc: 3, units: 3, builds: 0, momentum: 0, ema_momentum: 0, cgi: 0 },
      ],
    },
    Italy: {
      current: {
        country: 'Italy',
        year: 1901,
        season: 'Spring',
        sc: 3,
        units: 3,
        builds: 0,
        sc_gains: 0,
        unit_growth: 0,
        build_effeciency: 0,
        momentum: 0,
        ema_momentum: 0,
        growth_rate: 0,
        cgi: 0,
        holds: 0,
        supports: 0,
        active_fronts: 0,
        hold_rate: 0,
        support_rate: 0,
        isolation: 0,
        encirclement: 0,
      },
      history: [
        { year: 1901, season: 'Spring', country: 'Italy', sc: 3, units: 3, builds: 0, momentum: 0, ema_momentum: 0, cgi: 0 },
      ],
    },
    Austria: {
      current: {
        country: 'Austria',
        year: 1901,
        season: 'Spring',
        sc: 3,
        units: 3,
        builds: 0,
        sc_gains: 0,
        unit_growth: 0,
        build_effeciency: 0,
        momentum: 0,
        ema_momentum: 0,
        growth_rate: 0,
        cgi: 0,
        holds: 0,
        supports: 0,
        active_fronts: 0,
        hold_rate: 0,
        support_rate: 0,
        isolation: 0,
        encirclement: 0,
      },
      history: [
        { year: 1901, season: 'Spring', country: 'Austria', sc: 3, units: 3, builds: 0, momentum: 0, ema_momentum: 0, cgi: 0 },
      ],
    },
    Turkey: {
      current: {
        country: 'Turkey',
        year: 1901,
        season: 'Spring',
        sc: 3,
        units: 3,
        builds: 0,
        sc_gains: 0,
        unit_growth: 0,
        build_effeciency: 0,
        momentum: 0,
        ema_momentum: 0,
        growth_rate: 0,
        cgi: 0,
        holds: 0,
        supports: 0,
        active_fronts: 0,
        hold_rate: 0,
        support_rate: 0,
        isolation: 0,
        encirclement: 0,
      },
      history: [
        { year: 1901, season: 'Spring', country: 'Turkey', sc: 3, units: 3, builds: 0, momentum: 0, ema_momentum: 0, cgi: 0 },
      ],
    },
    Russia: {
      current: {
        country: 'Russia',
        year: 1901,
        season: 'Spring',
        sc: 3,
        units: 3,
        builds: 0,
        sc_gains: 0,
        unit_growth: 0,
        build_effeciency: 0,
        momentum: 0,
        ema_momentum: 0,
        growth_rate: 0,
        cgi: 0,
        holds: 0,
        supports: 0,
        active_fronts: 0,
        hold_rate: 0,
        support_rate: 0,
        isolation: 0,
        encirclement: 0,
      },
      history: [
        { year: 1901, season: 'Spring', country: 'Russia', sc: 3, units: 3, builds: 0, momentum: 0, ema_momentum: 0, cgi: 0 },
      ],
    },
  },
};

const boardLayout = [
  ['England', 'England', 'England', 'Neutral', 'Neutral', 'Neutral', 'Neutral', 'Neutral', 'Neutral', 'Neutral', 'Neutral', 'Neutral'],
  ['England', 'England', 'France', 'France', 'France', 'Neutral', 'Neutral', 'Neutral', 'Neutral', 'Neutral', 'Russia', 'Russia'],
  ['Neutral', 'France', 'France', 'Germany', 'Germany', 'Germany', 'Neutral', 'Neutral', 'Russia', 'Russia', 'Russia', 'Russia'],
  ['Neutral', 'Neutral', 'Germany', 'Germany', 'Germany', 'Italy', 'Italy', 'Austria', 'Austria', 'Russia', 'Russia', 'Russia'],
  ['Neutral', 'Neutral', 'Neutral', 'Italy', 'Italy', 'Italy', 'Austria', 'Austria', 'Austria', 'Turkey', 'Turkey', 'Turkey'],
  ['Neutral', 'Neutral', 'Neutral', 'Neutral', 'Neutral', 'Austria', 'Austria', 'Turkey', 'Turkey', 'Turkey', 'Turkey', 'Neutral'],
];

const countryPalette = {
  England: 'english',
  France: 'french',
  Germany: 'german',
  Italy: 'italian',
  Austria: 'austrian',
  Turkey: 'turkish',
  Russia: 'russian',
  Neutral: 'neutral',
};

const state = {
  payload: fallbackPayload,
  selectedCountry: null,
  selectedSeason: null,
};

function round(value, digits = 2) {
  const n = Number(value ?? 0);
  return Number.isFinite(n) ? Number(n.toFixed(digits)) : 0;
}

function formatNumber(value, digits = 2) {
  return typeof value === 'number' ? value.toFixed(digits) : value ?? '0';
}

function formatSeason(year, season) {
  return `${season} ${year}`;
}

function getCountryEntries(payload) {
  return Object.entries(payload?.countries ?? {});
}

function getCountryHistory(country, payload) {
  const entry = payload?.countries?.[country];
  return entry?.history ?? [];
}

function getTick(current, previous) {
  if (current === previous || current == null || previous == null) return 'flat';
  return current > previous ? 'up' : 'down';
}

function getTickSymbol(direction) {
  if (direction === 'up') return '▲';
  if (direction === 'down') return '▼';
  return '•';
}

function buildCountryOptions(payload) {
  const select = document.getElementById('country-select');
  const countries = getCountryEntries(payload);

  if (!countries.length) {
    select.innerHTML = '<option value="">No countries loaded</option>';
    state.selectedCountry = null;
    select.value = '';
    return;
  }

  select.innerHTML = countries.map(([country]) => `<option value="${country}">${country}</option>`).join('');

  const firstCountry = countries[0]?.[0];
  state.selectedCountry = state.selectedCountry || firstCountry;
  select.value = state.selectedCountry || firstCountry;
}

function buildSeasonOptions(payload) {
  const select = document.getElementById('season-select');
  const selectedSeason = payload?.selectedSeason ?? null;

  if (!selectedSeason) {
    select.innerHTML = '<option value="">Load orders to choose a season</option>';
    state.selectedSeason = null;
    select.value = '';
    return;
  }

  const seasons = [
    { year: selectedSeason.year, season: selectedSeason.season },
    { year: selectedSeason.year, season: selectedSeason.season === 'Spring' ? 'Fall' : selectedSeason.season === 'Fall' ? 'Winter' : 'Spring' },
  ];

  select.innerHTML = seasons.map(({ year, season }) => `<option value="${year}|${season}">${formatSeason(year, season)}</option>`).join('');
  state.selectedSeason = `${selectedSeason.year}|${selectedSeason.season}`;
  select.value = state.selectedSeason;
}

function renderWarboard(country) {
  const board = document.getElementById('warboard-grid');
  board.innerHTML = '';

  for (let rowIndex = 0; rowIndex < boardLayout.length; rowIndex += 1) {
    for (let colIndex = 0; colIndex < boardLayout[rowIndex].length; colIndex += 1) {
      const owner = boardLayout[rowIndex][colIndex];
      const tile = document.createElement('div');
      const tileName = owner === 'Neutral' ? 'Neutral' : owner;
      tile.className = `province-tile ${countryPalette[owner] ?? 'neutral'}`;
      if (country && owner === country) {
        tile.classList.add('selected');
      }
      tile.innerHTML = `<span>${tileName}</span><i class="center-dot"></i>`;
      board.appendChild(tile);
    }
  }
}

function renderSummaryTable(payload) {
  const body = document.getElementById('country-table-body');
  const rows = getCountryEntries(payload).map(([country, data]) => {
    const current = data.current ?? {};
    const history = data.history ?? [];
    const previous = history.length > 1 ? history[history.length - 2] : null;
    const emaDirection = getTick(current.ema_momentum ?? 0, previous?.ema_momentum ?? 0);
    const cgiDirection = getTick(current.cgi ?? 0, previous?.cgi ?? 0);
    const scDirection = getTick(current.sc ?? 0, previous?.sc ?? 0);
    const tick = scDirection === 'flat' && emaDirection === 'flat' && cgiDirection === 'flat'
      ? 'flat'
      : (scDirection === 'up' || emaDirection === 'up' || cgiDirection === 'up' ? 'up' : 'down');

    return `
      <tr>
        <td class="country-name">${country}</td>
        <td>${current.sc ?? 0}</td>
        <td>${current.units ?? 0}</td>
        <td>${formatNumber(current.ema_momentum ?? 0)}</td>
        <td>${formatNumber(current.cgi ?? 0)}</td>
        <td><span class="tick ${tick}">${getTickSymbol(tick)}</span></td>
      </tr>
    `;
  });

  body.innerHTML = rows.join('');
}

function renderMomentumChart(payload) {
  const chart = document.getElementById('momentum-chart');
  const countries = getCountryEntries(payload);
  const max = Math.max(1, ...countries.map(([, data]) => Number(data?.current?.momentum ?? 0)));

  chart.innerHTML = countries.map(([country, data]) => {
    const current = data.current ?? {};
    const momentum = Number(current.momentum ?? 0);
    const percent = (momentum / max) * 100;
    return `
      <div class="bar-row">
        <div class="bar-label">${country}</div>
        <div class="bar-track"><div class="bar-fill" style="width:${percent}%"></div></div>
        <div>${formatNumber(momentum)}</div>
      </div>
    `;
  }).join('');
}

function renderCountryTrendChart(country, payload) {
  const chart = document.getElementById('country-trend-chart');
  const history = getCountryHistory(country, payload);

  if (!history.length) {
    chart.innerHTML = '<div class="empty-state">No trend history available.</div>';
    return;
  }

  const maxValue = Math.max(1, ...history.map((entry) => Number(entry.momentum ?? entry.sc ?? 0)));

  chart.innerHTML = `
    <div class="trend-line">
      ${history.map((entry) => {
        const value = Number(entry.momentum ?? 0);
        const height = Math.max(12, (value / maxValue) * 100);
        return `
          <div class="trend-point" title="${entry.season} ${entry.year}: ${value}">
            <span style="height:${height}%"></span>
            <small>${entry.season.slice(0, 3)}</small>
          </div>
        `;
      }).join('')}
    </div>
  `;
}

function computeProjectedWinChance(country, payload) {
  const entries = getCountryEntries(payload);
  const scores = entries.map(([, data]) => Number(data?.current?.forecast_score ?? data?.current?.momentum ?? 0));
  const total = scores.reduce((sum, value) => sum + value, 0) || 1;
  const current = payload?.countries?.[country]?.current ?? {};
  const score = Number(current.forecast_score ?? current.momentum ?? 0);
  return round((score / total) * 100, 1);
}

function renderCountryFocus(country, payload) {
  const current = payload?.countries?.[country]?.current ?? {};
  const history = payload?.countries?.[country]?.history ?? [];
  const winChance = computeProjectedWinChance(country, payload);
  const confidence = Math.min(95, Math.max(25, winChance + (Number(current.ema_momentum ?? 0) * 12)));

  document.getElementById('focus-country').textContent = country;
  document.getElementById('focus-sc').textContent = current.sc ?? 0;
  document.getElementById('focus-units').textContent = current.units ?? 0;
  document.getElementById('focus-ema').textContent = formatNumber(current.ema_momentum ?? 0);
  document.getElementById('focus-cgi').textContent = formatNumber(current.cgi ?? 0);
  document.getElementById('focus-win').textContent = `${winChance}%`;
  document.getElementById('focus-confidence').textContent = `${round(confidence, 0)}%`;
  document.getElementById('confidence-bar').style.width = `${Math.min(100, confidence)}%`;

  const momentumText = Number(current.momentum ?? 0) >= 1 ? 'is sustaining constructive momentum' : 'is struggling to convert pressure into gains';
  const summary = current.sc >= 9 ? 'is shaping a dominant center presence' : current.sc >= 5 ? 'is building a credible foothold' : 'is still contesting space and tempo';
  const brief = `${country} ${summary} and ${momentumText}. Its EMA momentum is ${formatNumber(current.ema_momentum ?? 0)}, CGI is ${formatNumber(current.cgi ?? 0)}, and the model gives it a ${winChance}% win outlook this cycle. With ${current.active_fronts ?? 0} active fronts and ${current.isolation ?? 0} isolation exposure, the strategic picture remains ${Number(current.momentum ?? 0) >= 1 ? 'promising but volatile' : 'fragile and contested'}.`;
  document.getElementById('country-brief').textContent = brief;

  const historyList = document.getElementById('history-list');
  historyList.innerHTML = history.slice(-4).reverse().map((entry) => {
    const previous = history.length > 1 ? history[history.length - 2] : null;
    const delta = previous ? Number(entry.sc ?? 0) - Number(previous.sc ?? 0) : 0;
    const tick = delta > 0 ? 'up' : delta < 0 ? 'down' : 'flat';
    return `
      <div class="history-item">
        <div><strong>${entry.season}</strong> ${entry.year}</div>
        <div>SC ${entry.sc ?? 0} <span class="tick ${tick}">${getTickSymbol(tick)}</span></div>
      </div>
    `;
  }).join('');

  const rank = countryEntriesRank(country, payload);
  document.getElementById('focus-rank').textContent = `Rank ${rank}`;
  document.getElementById('season-header').textContent = payload?.selectedSeason
    ? formatSeason(payload.selectedSeason.year, payload.selectedSeason.season)
    : 'No Season Loaded';
}

function countryEntriesRank(country, payload) {
  const scored = getCountryEntries(payload).map(([name, data]) => ({ country: name, score: Number(data?.current?.forecast_score ?? data?.current?.momentum ?? 0) }));
  scored.sort((a, b) => b.score - a.score);
  const index = scored.findIndex((entry) => entry.country === country);
  return index >= 0 ? index + 1 : 'N/A';
}

function renderDashboard(payload) {
  const normalizedPayload = payload && payload.countries ? payload : emptyPayload;
  const season = normalizedPayload?.selectedSeason ?? null;
  state.payload = normalizedPayload;
  buildSeasonOptions(normalizedPayload);
  buildCountryOptions(normalizedPayload);

  if (!Object.keys(normalizedPayload.countries || {}).length) {
    document.getElementById('season-header').textContent = 'No Season Loaded';
    document.getElementById('focus-country').textContent = '—';
    document.getElementById('focus-sc').textContent = '0';
    document.getElementById('focus-units').textContent = '0';
    document.getElementById('focus-ema').textContent = '0.00';
    document.getElementById('focus-cgi').textContent = '0.00';
    document.getElementById('focus-win').textContent = '0%';
    document.getElementById('focus-confidence').textContent = '0%';
    document.getElementById('confidence-bar').style.width = '0%';
    document.getElementById('country-brief').textContent = 'Load orders to select a season and begin tracking the game.';
    document.getElementById('history-list').innerHTML = '<div class="history-item"><div>No history loaded</div></div>';
    document.getElementById('country-table-body').innerHTML = '<tr><td colspan="6" class="empty-table">No countries available yet.</td></tr>';
    document.getElementById('momentum-chart').innerHTML = '<div class="empty-state">No data loaded.</div>';
    document.getElementById('country-trend-chart').innerHTML = '<div class="empty-state">No trend history loaded.</div>';
    renderWarboard(null);
    return;
  }

  renderSummaryTable(normalizedPayload);
  renderMomentumChart(normalizedPayload);
  renderWarboard(state.selectedCountry || Object.keys(normalizedPayload.countries)[0]);
  renderCountryFocus(state.selectedCountry || Object.keys(normalizedPayload.countries)[0], normalizedPayload);
  renderCountryTrendChart(state.selectedCountry || Object.keys(normalizedPayload.countries)[0], normalizedPayload);
  document.getElementById('season-header').textContent = formatSeason(season.year, season.season);
}

async function loadDashboardData() {
  renderDashboard(emptyPayload);

  document.getElementById('country-select').addEventListener('change', (event) => {
    state.selectedCountry = event.target.value;
    renderWarboard(state.selectedCountry);
    renderCountryFocus(state.selectedCountry, state.payload);
    renderCountryTrendChart(state.selectedCountry, state.payload);
  });

  document.getElementById('season-select').addEventListener('change', (event) => {
    const [year, season] = event.target.value.split('|');
    loadDashboardDataForSeason(Number(year), season);
  });
}

async function loadDashboardDataForSeason(year, season) {
  try {
    const response = await fetch(`/api/dashboard?year=${year}&season=${season}`);
    if (!response.ok) throw new Error('Season payload request failed');
    const payload = await response.json();
    renderDashboard(payload);
  } catch (error) {
    console.warn('Using fallback payload for selected season', error);
    renderDashboard(fallbackPayload);
  }
}

async function submitUploadedOrders() {
  const mode = document.getElementById('upload-mode').value;
  const text = document.getElementById('upload-text').value.trim();
  const year = Number(document.getElementById('upload-year').value || 1901);
  const season = document.getElementById('upload-season').value || 'Spring';
  const status = document.getElementById('upload-status');

  if (!text) {
    status.textContent = 'Paste order text before loading.';
    status.classList.add('error');
    return;
  }

  status.textContent = 'Uploading orders...';
  status.classList.remove('error');

  try {
    const response = await fetch('/api/upload', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, year, season, mode })
    });

    const contentType = response.headers.get('content-type') || '';
    if (!contentType.includes('application/json')) {
      const htmlText = await response.text();
      throw new Error(
        htmlText.includes('<!DOCTYPE')
          ? 'The dashboard server is serving the HTML page instead of the API. Refresh the page or restart the backend server and try again.'
          : `Upload failed with status ${response.status}.`
      );
    }

    const payload = await response.json();
    if (!response.ok) {
      throw new Error(payload?.error || 'Upload failed');
    }

    status.classList.remove('error');
    renderDashboard(payload);
    const seasonLabel = payload?.selectedSeason ? `${payload.selectedSeason.season} ${payload.selectedSeason.year}` : `${season} ${year}`;
    status.textContent = `Loaded orders for ${seasonLabel}.`;
  } catch (error) {
    console.warn('Order upload failed', error);
    status.textContent = error.message || 'Upload failed.';
    status.classList.add('error');
  }
}

function bindUploadControls() {
  const uploadMode = document.getElementById('upload-mode');
  const uploadYear = document.getElementById('upload-year');
  const uploadSeason = document.getElementById('upload-season');

  uploadMode.addEventListener('change', () => {
    const isFullGame = uploadMode.value === 'full';
    uploadYear.disabled = isFullGame;
    uploadSeason.disabled = isFullGame;
  });

  document.getElementById('upload-submit').addEventListener('click', submitUploadedOrders);
}

document.addEventListener('DOMContentLoaded', () => {
  bindUploadControls();
  loadDashboardData();
});
