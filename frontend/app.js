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
  selectedSeason: null,
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
  payload: emptyPayload,
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

function getAvailableSeasons(payload) {
  const seasonOrder = ['Spring', 'Summer', 'Fall', 'Winter'];
  const byKey = new Map();

  const pushSeason = (year, season) => {
    const normalizedYear = Number(year);
    const normalizedSeason = String(season || '').trim();
    if (!normalizedYear || !normalizedSeason) return;
    const key = `${normalizedYear}|${normalizedSeason}`;
    if (!byKey.has(key)) {
      byKey.set(key, { year: normalizedYear, season: normalizedSeason });
    }
  };

  (payload?.availableSeasons ?? []).forEach((entry) => {
    if (entry && entry.year != null && entry.season) {
      pushSeason(entry.year, entry.season);
    }
  });

  getCountryEntries(payload).forEach(([, data]) => {
    (data?.history ?? []).forEach((entry) => {
      pushSeason(entry?.year, entry?.season);
    });
  });

  if (payload?.selectedSeason) {
    pushSeason(payload.selectedSeason.year, payload.selectedSeason.season);
  }

  return Array.from(byKey.values()).sort((a, b) => {
    if (a.year !== b.year) return a.year - b.year;
    return seasonOrder.indexOf(a.season) - seasonOrder.indexOf(b.season);
  });
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

  const validSelection = state.selectedCountry && payload?.countries?.[state.selectedCountry]
    ? state.selectedCountry
    : countries[0][0];
  state.selectedCountry = validSelection;

  select.innerHTML = countries.map(([country]) => `<option value="${country}">${country}</option>`).join('');
  select.value = validSelection;
}

function buildSeasonOptions(payload) {
  const select = document.getElementById('season-select');
  const seasons = getAvailableSeasons(payload);

  if (!seasons.length) {
    select.innerHTML = '<option value="">Load orders to choose a season</option>';
    state.selectedSeason = null;
    select.value = '';
    return;
  }

  const currentSelection = payload?.selectedSeason
    ? `${payload.selectedSeason.year}|${payload.selectedSeason.season}`
    : `${seasons[0].year}|${seasons[0].season}`;

  state.selectedSeason = currentSelection;
  select.innerHTML = seasons.map(({ year, season }) => `<option value="${year}|${season}">${formatSeason(year, season)}</option>`).join('');
  select.value = seasons.some(({ year, season }) => `${year}|${season}` === currentSelection)
    ? currentSelection
    : `${seasons[0].year}|${seasons[0].season}`;
  state.selectedSeason = select.value || currentSelection;
}

function renderWarboard(country) {
  const board = document.getElementById('warboard-grid');
  board.innerHTML = '';

  const selectedCountry = country || state.selectedCountry;
  const selectedUnits = Number(state.payload?.countries?.[selectedCountry]?.current?.units ?? 0);

  const isEnemyAdjacent = (rowIndex, colIndex, owner) => {
    if (!selectedCountry || owner === selectedCountry || owner === 'Neutral') return false;

    const deltas = [-1, 0, 1];
    return deltas.some((rowDelta) => deltas.some((colDelta) => {
      if (rowDelta === 0 && colDelta === 0) return false;
      const nextRow = rowIndex + rowDelta;
      const nextCol = colIndex + colDelta;
      if (nextRow < 0 || nextRow >= boardLayout.length || nextCol < 0 || nextCol >= boardLayout[nextRow].length) {
        return false;
      }
      return boardLayout[nextRow][nextCol] === selectedCountry;
    }));
  };

  for (let rowIndex = 0; rowIndex < boardLayout.length; rowIndex += 1) {
    for (let colIndex = 0; colIndex < boardLayout[rowIndex].length; colIndex += 1) {
      const owner = boardLayout[rowIndex][colIndex];
      const tile = document.createElement('div');
      const tileName = owner === 'Neutral' ? 'Neutral' : owner;
      const isFriendly = !!selectedCountry && owner === selectedCountry;
      const isFront = !!selectedCountry && isFriendly && (
        rowIndex > 0 && boardLayout[rowIndex - 1][colIndex] && boardLayout[rowIndex - 1][colIndex] !== selectedCountry && boardLayout[rowIndex - 1][colIndex] !== 'Neutral'
        || rowIndex < boardLayout.length - 1 && boardLayout[rowIndex + 1][colIndex] && boardLayout[rowIndex + 1][colIndex] !== selectedCountry && boardLayout[rowIndex + 1][colIndex] !== 'Neutral'
        || colIndex > 0 && boardLayout[rowIndex][colIndex - 1] && boardLayout[rowIndex][colIndex - 1] !== selectedCountry && boardLayout[rowIndex][colIndex - 1] !== 'Neutral'
        || colIndex < boardLayout[rowIndex].length - 1 && boardLayout[rowIndex][colIndex + 1] && boardLayout[rowIndex][colIndex + 1] !== selectedCountry && boardLayout[rowIndex][colIndex + 1] !== 'Neutral'
      );
      const isConflict = !!selectedCountry && isEnemyAdjacent(rowIndex, colIndex, owner);

      tile.className = `province-tile ${countryPalette[owner] ?? 'neutral'}`;
      if (isFriendly) {
        tile.classList.add('selected');
      }
      if (isFront) {
        tile.classList.add('front-zone');
      }
      if (isConflict) {
        tile.classList.add('conflict-zone');
      }

      const unitBadge = isFriendly && selectedUnits > 0
        ? `<span class="unit-badge">${Math.min(9, Math.max(1, Math.round(selectedUnits / 2)))}</span>`
        : '';
      const frontBadge = isConflict ? '<span class="front-badge">!</span>' : '';
      tile.innerHTML = `<span>${tileName}</span>${unitBadge}${frontBadge}<i class="center-dot"></i>`;
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
  const values = countries.map(([, data]) => Number(data?.current?.momentum ?? 0));
  const maxAbs = Math.max(1, ...values.map((value) => Math.abs(value)));

  chart.innerHTML = countries.map(([country, data]) => {
    const current = data.current ?? {};
    const momentum = Number(current.momentum ?? 0);
    const width = (Math.abs(momentum) / maxAbs) * 50;
    const fillStyle = momentum >= 0
      ? `left:50%; width:${width}%;`
      : `right:50%; width:${width}%;`;

    return `
      <div class="bar-row">
        <div class="bar-label">${country}</div>
        <div class="bar-track">
          <div class="bar-zero"></div>
          <div class="bar-fill ${momentum >= 0 ? 'positive' : 'negative'}" style="${fillStyle}"></div>
        </div>
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
  if (!payload) return 0;

  const mcChance = Number(payload?.forecast?.[country] ?? payload?.countries?.[country]?.current?.win_probability ?? 0);
  if (mcChance > 0) {
    return round(mcChance * 100, 1);
  }

  const entries = getCountryEntries(payload);
  const scores = entries.map(([, data]) => Number(data?.current?.forecast_score ?? data?.current?.momentum ?? 0));
  const total = scores.reduce((sum, value) => sum + value, 0) || 1;
  const current = payload?.countries?.[country]?.current ?? {};
  const score = Number(current.forecast_score ?? current.momentum ?? 0);
  return round((score / total) * 100, 1);
}

function getProjectedWinChance(country, payload) {
  return computeProjectedWinChance(country, payload);
}

function getProjectedLeader(payload) {
  const countries = getCountryEntries(payload);
  if (!countries.length) return null;

  return countries
    .map(([country, data]) => {
      const current = data.current ?? {};
      const mcWin = Number(payload?.forecast?.[country] ?? current?.win_probability ?? 0);
      const strategicScore = (
        (mcWin * 100) +
        (Number(current.cgi ?? 0) * 2.5) +
        (Number(current.ema_momentum ?? 0) * 1.8) +
        (Number(current.sc ?? 0) * 1.7) +
        (Number(current.momentum ?? 0) * 1.4) +
        (Number(current.holds ?? 0) * 0.8) +
        (Number(current.supports ?? 0) * 0.9) +
        (Number(current.active_fronts ?? 0) * 0.6) -
        (Number(current.isolation ?? 0) * 1.5) -
        (Number(current.encirclement ?? 0) * 1.7)
      );

      return {
        country,
        score: strategicScore,
        sc: Number(current.sc ?? 0),
        units: Number(current.units ?? 0),
        ema: Number(current.ema_momentum ?? 0),
        cgi: Number(current.cgi ?? 0),
        momentum: Number(current.momentum ?? 0),
        activeFronts: Number(current.active_fronts ?? 0),
        isolation: Number(current.isolation ?? 0),
        encirclement: Number(current.encirclement ?? 0),
        holds: Number(current.holds ?? 0),
        supports: Number(current.supports ?? 0),
      };
    })
    .sort((a, b) => b.score - a.score)[0];
}

function renderGlobalOverview(payload) {
  const countries = getCountryEntries(payload);
  const overviewFronts = document.getElementById('overview-fronts');
  const overviewIsolation = document.getElementById('overview-isolation');
  const overviewEncirclement = document.getElementById('overview-encirclement');
  const overviewHolds = document.getElementById('overview-holds');
  const overviewSupports = document.getElementById('overview-supports');
  const overviewMomentum = document.getElementById('overview-momentum');
  const overviewFactors = document.getElementById('overview-factors');

  if (!countries.length) {
    overviewFronts.textContent = '0';
    overviewIsolation.textContent = '0.00';
    overviewEncirclement.textContent = '0.00';
    overviewHolds.textContent = '0';
    overviewSupports.textContent = '0';
    overviewMomentum.textContent = '0.00';
    overviewFactors.innerHTML = '';
    return;
  }

  const totals = countries.reduce((acc, [, data]) => {
    const current = data.current ?? {};
    acc.fronts += Number(current.active_fronts ?? 0);
    acc.isolation += Number(current.isolation ?? 0);
    acc.encirclement += Number(current.encirclement ?? 0);
    acc.holds += Number(current.holds ?? 0);
    acc.supports += Number(current.supports ?? 0);
    acc.momentum += Number(current.momentum ?? 0);
    return acc;
  }, { fronts: 0, isolation: 0, encirclement: 0, holds: 0, supports: 0, momentum: 0 });

  const leader = getProjectedLeader(payload);
  const avgFronts = countries.length ? totals.fronts / countries.length : 0;
  const avgIsolation = countries.length ? totals.isolation / countries.length : 0;
  const avgEncirclement = countries.length ? totals.encirclement / countries.length : 0;
  const avgMomentum = countries.length ? totals.momentum / countries.length : 0;

  overviewFronts.textContent = round(avgFronts, 1);
  overviewIsolation.textContent = round(avgIsolation, 2);
  overviewEncirclement.textContent = round(avgEncirclement, 2);
  overviewHolds.textContent = totals.holds;
  overviewSupports.textContent = totals.supports;
  overviewMomentum.textContent = round(avgMomentum, 2);

  const mostIsolated = countries
    .map(([country, data]) => ({ country, value: Number(data.current?.isolation ?? 0) }))
    .sort((a, b) => b.value - a.value)[0];
  const mostPressed = countries
    .map(([country, data]) => ({ country, value: Number(data.current?.active_fronts ?? 0) }))
    .sort((a, b) => b.value - a.value)[0];

  overviewFactors.innerHTML = `
    <div class="overview-factor">
      <strong>Front pressure</strong>
      ${mostPressed ? `${mostPressed.country} is fighting on ${mostPressed.value} fronts, driving the broadest operational footprint.` : 'No active fronts recorded.'}
    </div>
    <div class="overview-factor">
      <strong>Exposure</strong>
      ${mostIsolated ? `${mostIsolated.country} carries the highest isolation index at ${round(mostIsolated.value, 2)}, which raises strategic vulnerability.` : 'No isolation data available.'}
    </div>
    <div class="overview-factor">
      <strong>Leader</strong>
      ${leader ? `${leader.country} remains the model favorite with ${round(getProjectedWinChance(leader.country, payload), 0)}% confidence and ${leader.sc} centers.` : 'No leader available.'}
    </div>
    <div class="overview-factor">
      <strong>Operational tempo</strong>
      ${leader ? `${leader.country} is sustaining ${round(leader.ema, 2)} EMA momentum alongside ${leader.holds} holds and ${leader.supports} supports.` : 'No operational tempo available.'}
    </div>
  `;
}

function renderIntelPanel(payload) {
  const leader = getProjectedLeader(payload);
  const selectedCountry = state.selectedCountry && payload?.countries?.[state.selectedCountry]
    ? state.selectedCountry
    : (payload && Object.keys(payload.countries || {})[0]) || null;

  const intelCountry = document.getElementById('intel-country');
  const intelConfidence = document.getElementById('intel-confidence');
  const intelSummary = document.getElementById('intel-summary');
  const intelFactors = document.getElementById('intel-factors');
  const intelAdvice = document.getElementById('intel-advice');

  if (!leader || !payload || !Object.keys(payload.countries || {}).length) {
    intelCountry.textContent = '—';
    intelConfidence.textContent = '0%';
    intelSummary.textContent = 'No data available yet.';
    intelFactors.innerHTML = '';
    intelAdvice.textContent = 'No country selected.';
    return;
  }

  const confidence = computeProjectedWinChance(leader.country, payload);
  const selectedState = selectedCountry ? (payload.countries[selectedCountry]?.current ?? {}) : {};

  const leadingFactors = [
    `${leader.country} controls ${leader.sc} supply centers and is fielding ${leader.units} units, giving it the strongest raw center base in the current board state.`,
    `EMA momentum is ${formatNumber(leader.ema)}, CGI is ${formatNumber(leader.cgi)}, and momentum sits at ${formatNumber(leader.momentum)}, showing a durable trend rather than a one-off gain.`,
    `They are fighting on ${leader.activeFronts} fronts with ${leader.holds} holds and ${leader.supports} supports, while their isolation and encirclement are comparatively contained at ${formatNumber(leader.isolation)} and ${formatNumber(leader.encirclement)}.`,
  ];

  intelCountry.textContent = leader.country;
  intelConfidence.textContent = `${round(confidence, 0)}%`;
  intelSummary.textContent = `${leader.country} is the model favorite to win with ${round(confidence, 0)}% confidence. The combination of a stronger center count, more durable momentum, higher EMA and CGI, and manageable exposure suggests they are converting strategic advantage into a harder-to-stop position.`;
  intelFactors.innerHTML = leadingFactors.map((factor) => `<li>${factor}</li>`).join('');

  if (!selectedCountry) {
    intelAdvice.textContent = 'No country selected.';
    return;
  }

  const selectedName = selectedCountry;
  const selectedMomentum = Number(selectedState.momentum ?? 0);
  const selectedEma = Number(selectedState.ema_momentum ?? 0);
  const selectedSc = Number(selectedState.sc ?? 0);
  const selectedCgi = Number(selectedState.cgi ?? 0);
  const selectedIsolation = Number(selectedState.isolation ?? 0);
  const selectedEncirclement = Number(selectedState.encirclement ?? 0);
  const selectedHolds = Number(selectedState.holds ?? 0);
  const selectedSupports = Number(selectedState.supports ?? 0);

  if (selectedName === leader.country) {
    intelAdvice.textContent = `${selectedName} is in the strongest position. To stay ahead, keep converting center gains into sustained pressure, preserve high support rates, and avoid letting isolation or encirclement drift upward enough to compromise the position.`;
    return;
  }

  const gapText = selectedSc >= leader.sc ? 'close the center-count gap' : 'keep the center-count gap from widening';
  intelAdvice.textContent = `${selectedName} needs to ${gapText}, reduce isolation from ${formatNumber(selectedIsolation)} and encirclement from ${formatNumber(selectedEncirclement)}, and improve its operational support profile from ${selectedHolds} holds and ${selectedSupports} supports so it can recover momentum and challenge ${leader.country} before the lead hardens.`;
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

  if (state.selectedCountry && !normalizedPayload.countries?.[state.selectedCountry]) {
    state.selectedCountry = null;
  }

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

  const activeCountry = state.selectedCountry && normalizedPayload.countries[state.selectedCountry]
    ? state.selectedCountry
    : Object.keys(normalizedPayload.countries)[0];
  state.selectedCountry = activeCountry;

  renderSummaryTable(normalizedPayload);
  renderMomentumChart(normalizedPayload);
  renderWarboard(activeCountry);
  renderCountryFocus(activeCountry, normalizedPayload);
  renderCountryTrendChart(activeCountry, normalizedPayload);
  renderGlobalOverview(normalizedPayload);
  renderIntelPanel(normalizedPayload);
  document.getElementById('season-header').textContent = season ? formatSeason(season.year, season.season) : 'No Season Loaded';
}

async function loadDashboardData() {
  renderDashboard(emptyPayload);

  document.getElementById('country-select').addEventListener('change', (event) => {
    state.selectedCountry = event.target.value;
    if (state.selectedCountry && state.payload?.countries?.[state.selectedCountry]) {
      renderWarboard(state.selectedCountry);
      renderCountryFocus(state.selectedCountry, state.payload);
      renderCountryTrendChart(state.selectedCountry, state.payload);
      renderIntelPanel(state.payload);
    }
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
    document.getElementById('upload-text').value = '';
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
  const uploadPanel = document.getElementById('upload-panel');
  const uploadToggle = document.getElementById('upload-panel-toggle');

  uploadMode.addEventListener('change', () => {
    const isFullGame = uploadMode.value === 'full';
    uploadYear.disabled = isFullGame;
    uploadSeason.disabled = isFullGame;
  });

  uploadToggle.addEventListener('click', () => {
    uploadPanel.classList.toggle('collapsed');
  });

  document.getElementById('upload-submit').addEventListener('click', submitUploadedOrders);

  uploadPanel.classList.add('collapsed');
}

document.addEventListener('DOMContentLoaded', () => {
  bindUploadControls();
  loadDashboardData();
});
