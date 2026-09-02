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

const provinceToGrid = {
  "Lon": [0, 0],
  "Edi": [0, 1],
  "Lvp": [0, 2],
  "Yor": [1, 2],
  "Wal": [1, 1],
  "Cly": [0, 1],

  "Par": [1, 3],
  "Bre": [1, 2],
  "Mar": [2, 3],
  "Gas": [2, 2],
  "Bur": [2, 4],

  "Ber": [2, 5],
  "Mun": [3, 5],
  "Kie": [2, 4],
  "Ruh": [3, 4],

  "Rom": [4, 3],
  "Ven": [3, 3],
  "Nap": [4, 4],

  "Vie": [3, 6],
  "Bud": [4, 6],
  "Tri": [4, 5],
  "Gal": [3, 7],

  "War": [2, 8],
  "Mos": [2, 9],
  "Stp": [1, 10],
  "Sev": [3, 9],
  "Ukr": [3, 8],

  "Rum": [4, 7],
  "Bul": [4, 8],
  "Gre": [5, 7],
  "Ser": [4, 6],

  "Nwy": [1, 11],
  "Swe": [2, 11],
  "Den": [2, 10],
  "Hol": [2, 3],
  "Bel": [1, 3],
};

const mapFillColors = {
  England: '#4d7dff', France: '#74d8ff', Germany: '#dfe3e8', Italy: '#59c777',
  Austria: '#d64b4b', Turkey: '#f5d845', Russia: '#d93bcf', Neutral: '#d6d2bd', '': '#d6d2bd',
};

const svgProvinceAliases = {
  MAO: 'mid',
  NAO: 'nat',
  NWG: 'nrg',
};

const splitCoastProvinces = {
  Bul: ['bul/ec', 'bul/sc'],
  Spa: ['spa/nc', 'spa/sc'],
  Stp: ['stp/nc', 'stp/sc'],
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

function buildDynamicBoard(payload) {
  const rows = 6;
  const cols = 12;
  const dynamic = Array.from({ length: rows }, () =>
    Array.from({ length: cols }, () => "Neutral")
  );

  const scOwners = payload.board?.scOwners ?? {};
  const units = payload.board?.units ?? [];

  // Paint SC ownership
  for (const [province, owner] of Object.entries(scOwners)) {
    const pos = provinceToGrid[province];
    if (pos) {
      const [r, c] = pos;
      dynamic[r][c] = owner || "Neutral";
    }
  }

  // Paint unit presence (units override SC ownership)
  for (const unit of units) {
    const pos = provinceToGrid[unit.province];
    if (pos) {
      const [r, c] = pos;
      dynamic[r][c] = unit.country;
    }
  }

  return dynamic;
}

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
  gameText: '',
  gameSession: 0,
  restorePromise: null,
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

function seasonIndex(season) {
  return ['Spring', 'Summer', 'Fall', 'Winter'].indexOf(season);
}

function isOnOrBeforeSelectedSeason(entry, selectedSeason) {
  if (!selectedSeason || !entry) return true;
  if (Number(entry.year) !== Number(selectedSeason.year)) {
    return Number(entry.year) < Number(selectedSeason.year);
  }
  return seasonIndex(entry.season) <= seasonIndex(selectedSeason.season);
}

function selectedHistory(country, payload) {
  return getCountryHistory(country, payload)
    .filter((entry) => isOnOrBeforeSelectedSeason(entry, payload?.selectedSeason));
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

function isConflictTile(r, c, dynamicBoard, selectedCountry) {
  const deltas = [-1, 0, 1];

  return deltas.some((dr) =>
    deltas.some((dc) => {
      if (dr === 0 && dc === 0) return false;
      const nr = r + dr;
      const nc = c + dc;
      if (nr < 0 || nr >= dynamicBoard.length) return false;
      if (nc < 0 || nc >= dynamicBoard[0].length) return false;

      const neighborOwner = dynamicBoard[nr][nc];
      return neighborOwner && neighborOwner !== selectedCountry && neighborOwner !== 'Neutral';
    })
  );
}

function renderWarboard(country) {
  const board = document.getElementById('warboard-grid');
  const scOwners = state.payload?.board?.scOwners ?? {};
  const selectedCountry = country || state.selectedCountry;
  const units = state.payload?.board?.units ?? [];

  board.innerHTML = `
    <object class="diplomacy-map" id="diplomacy-map" data="data/DiplomacyMap.svg" type="image/svg+xml" aria-label="Standard Diplomacy board map"></object>
  `;

  const mapObject = document.getElementById('diplomacy-map');
  mapObject.addEventListener('load', () => applyMapState(mapObject, scOwners, units, selectedCountry), { once: true });
}

function getSvgProvincePaths(svgDocument, province) {
  const normalizedProvince = String(province || '').trim();
  const baseProvince = normalizedProvince.split('/')[0];
  const directId = svgProvinceAliases[normalizedProvince] ?? normalizedProvince.toLowerCase();
  const directPath = svgDocument.getElementById(directId);
  if (directPath) return [directPath];

  const coastIds = splitCoastProvinces[baseProvince];
  if (coastIds) {
    return coastIds
      .map((coastId) => svgDocument.getElementById(coastId))
      .filter(Boolean);
  }

  console.warn(`No SVG province path found for ${normalizedProvince}.`);
  return [];
}

function ensureHatchPattern(svgDocument, patternId, baseColor, stripeColor) {
  if (svgDocument.getElementById(patternId)) return `url(#${patternId})`;

  const namespace = 'http://www.w3.org/2000/svg';
  const defs = svgDocument.querySelector('defs') || svgDocument.documentElement.insertBefore(
    svgDocument.createElementNS(namespace, 'defs'),
    svgDocument.documentElement.firstChild,
  );
  const pattern = svgDocument.createElementNS(namespace, 'pattern');
  pattern.setAttribute('id', patternId);
  pattern.setAttribute('width', '12');
  pattern.setAttribute('height', '12');
  pattern.setAttribute('patternUnits', 'userSpaceOnUse');
  pattern.setAttribute('patternTransform', 'rotate(45)');

  const background = svgDocument.createElementNS(namespace, 'rect');
  background.setAttribute('width', '12');
  background.setAttribute('height', '12');
  background.setAttribute('fill', baseColor);

  const stripe = svgDocument.createElementNS(namespace, 'path');
  stripe.setAttribute('d', 'M 0 0 L 0 12');
  stripe.setAttribute('stroke', stripeColor);
  stripe.setAttribute('stroke-width', '4');

  pattern.append(background, stripe);
  defs.append(pattern);
  return `url(#${patternId})`;
}

function applyProvinceStyle(paths, fill, stroke, strokeWidth, label) {
  paths.forEach((path) => {
    path.style.fill = fill;
    path.style.fillOpacity = '1';
    path.style.stroke = stroke;
    path.style.strokeWidth = strokeWidth;
    path.style.cursor = 'pointer';
    path.setAttribute('aria-label', label);
  });
}

function applyMapState(mapObject, scOwners, units, selectedCountry) {
  const svgDocument = mapObject.contentDocument;
  if (!svgDocument) return;

  const provinceLayer = svgDocument.getElementById('provinces');
  if (provinceLayer) {
    provinceLayer.style.display = 'inline';
    provinceLayer.querySelectorAll(':scope > path, :scope > polygon').forEach((path) => {
      path.style.fill = 'transparent';
      path.style.stroke = 'transparent';
    });
  }

  Object.entries(scOwners).forEach(([province, owner]) => {
    const fill = mapFillColors[owner] ?? mapFillColors.Neutral;
    const selected = owner === selectedCountry;
    applyProvinceStyle(
      getSvgProvincePaths(svgDocument, province),
      fill,
      selected ? '#d7b46d' : '#ffffff',
      selected ? '4' : '1.5',
      `${province}: ${owner || 'Neutral'} supply center`,
    );
  });

  units.forEach((unit) => {
    const owner = scOwners[unit.province];
    const baseColor = owner === undefined
      ? '#d6d2bd'
      : (mapFillColors[owner] ?? mapFillColors.Neutral);
    const fill = ensureHatchPattern(
      svgDocument,
      `unit-hatch-${String(owner || 'neutral').toLowerCase()}-${unit.country.toLowerCase()}`,
      baseColor,
      mapFillColors[unit.country] ?? mapFillColors.Neutral,
    );
    const selected = unit.country === selectedCountry;
    const front = !selected && state.payload?.countries?.[unit.country]?.current?.active_fronts > 0;
    applyProvinceStyle(
      getSvgProvincePaths(svgDocument, unit.province),
      fill,
      selected ? '#d7b46d' : (front ? '#d77b6d' : '#ffffff'),
      selected ? '4' : (front ? '3' : '1.5'),
      `${unit.country} ${unit.unit_type} in ${unit.province}`,
    );
  });
}

function isFrontTile(r, c, dynamicBoard, selectedCountry) {
  const deltas = [-1, 0, 1];

  return deltas.some((dr) =>
    deltas.some((dc) => {
      if (dr === 0 && dc === 0) return false;
      const nr = r + dr;
      const nc = c + dc;
      if (nr < 0 || nr >= dynamicBoard.length) return false;
      if (nc < 0 || nc >= dynamicBoard[0].length) return false;

      const neighborOwner = dynamicBoard[nr][nc];
      return neighborOwner && neighborOwner !== selectedCountry && neighborOwner !== 'Neutral';
    })
  );
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
  const values = countries.map(([country]) => selectedHistory(country, payload)
    .reduce((total, entry) => total + Number(entry.momentum ?? 0), 0));
  const maxAbs = Math.max(1, ...values.map((value) => Math.abs(value)));

  chart.innerHTML = countries.map(([country], index) => {
    const momentum = values[index];
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
  const history = selectedHistory(country, payload);

  if (!history.length) {
    chart.innerHTML = '<div class="empty-state">No trend history available.</div>';
    return;
  }

  const values = history.map((entry) => Number(entry.growth_rate ?? 0));
  const maxAbs = Math.max(0.01, ...values.map((value) => Math.abs(value)));

  chart.innerHTML = `
    <div class="growth-axis-label">SC growth rate by season</div>
    <div class="trend-line growth-trend-line">
      ${history.map((entry, index) => {
        const value = values[index];
        const height = Math.max(4, (Math.abs(value) / maxAbs) * 50);
        const direction = value >= 0 ? 'positive' : 'negative';
        return `
          <div class="trend-point ${direction}" title="${entry.season} ${entry.year}: ${(value * 100).toFixed(1)}% SC growth">
            <span style="height:${height}%"></span>
            <small>${entry.season.slice(0, 3)} ${entry.year}</small>
          </div>
        `;
      }).join('')}
    </div>
  `;
}

function renderScControlChart(payload) {
  const chart = document.getElementById('sc-control-chart');
  const countries = getCountryEntries(payload);
  const totalCenters = 34;
  const controlled = countries.reduce((total, [, data]) => total + Number(data.current?.sc ?? 0), 0);
  let cursor = 0;
  const segments = countries.map(([country, data]) => {
    const share = (Number(data.current?.sc ?? 0) / totalCenters) * 100;
    const color = `var(--${country.toLowerCase()})`;
    const segment = `${color} ${cursor}% ${cursor + share}%`;
    cursor += share;
    return segment;
  });
  if (cursor < 100) segments.push(`rgba(255,255,255,0.12) ${cursor}% 100%`);

  chart.innerHTML = `
    <div class="sc-donut" style="background:conic-gradient(${segments.join(', ')})">
      <div><strong>${controlled}</strong><span>of ${totalCenters} SCs</span></div>
    </div>
    <div class="sc-legend">
      ${countries.map(([country, data]) => `<button class="sc-legend-row" data-country="${country}"><i class="legend-swatch ${countryPalette[country]}"></i><span>${country}</span><strong>${data.current?.sc ?? 0}</strong></button>`).join('')}
    </div>
  `;
  chart.querySelectorAll('[data-country]').forEach((button) => {
    button.addEventListener('click', () => {
      state.selectedCountry = button.dataset.country;
      renderDashboard(payload);
    });
  });
}

function renderPositionScatterChart(payload) {
  const chart = document.getElementById('position-scatter-chart');
  const countries = getCountryEntries(payload);
  const maxSc = Math.max(1, ...countries.map(([, data]) => Number(data.current?.sc ?? 0)));
  const maxPosition = Math.max(0.01, ...countries.map(([, data]) => Number(data.current?.strategic_position ?? 0)));

  chart.innerHTML = `
    <span class="scatter-axis scatter-y">Position</span>
    <span class="scatter-axis scatter-x">Supply centers</span>
    <div class="scatter-grid"></div>
    ${countries.map(([country, data]) => {
      const current = data.current ?? {};
      const left = 8 + (Number(current.sc ?? 0) / maxSc) * 84;
      const bottom = 8 + (Number(current.strategic_position ?? 0) / maxPosition) * 76;
      const size = 1.25 + (computeProjectedWinChance(country, payload) / 100) * 1.2;
      return `<button class="scatter-point ${countryPalette[country]}${country === state.selectedCountry ? ' selected-point' : ''}" data-country="${country}" style="left:${left}%;bottom:${bottom}%;width:${size}rem;height:${size}rem" title="${country}: ${current.sc ?? 0} SCs, position ${formatNumber(current.strategic_position ?? 0)}">${country.slice(0, 2)}</button>`;
    }).join('')}
  `;
  chart.querySelectorAll('[data-country]').forEach((button) => {
    button.addEventListener('click', () => {
      state.selectedCountry = button.dataset.country;
      renderDashboard(payload);
    });
  });
}

function renderPostureMatrix(payload) {
  const matrix = document.getElementById('posture-matrix');
  const countries = getCountryEntries(payload);
  const seasons = getAvailableSeasons(payload)
    .filter((entry) => isOnOrBeforeSelectedSeason(entry, payload.selectedSeason));
  if (!seasons.length) {
    matrix.innerHTML = '<div class="empty-state">No posture history available.</div>';
    return;
  }

  const postureClass = {
    Defensive: 'posture-defensive', 'Mixed-Defense': 'posture-mixed-defense', Balanced: 'posture-balanced',
    'Mixed-Offense': 'posture-mixed-offense', Aggressive: 'posture-aggressive', Inactive: 'posture-inactive',
  };
  matrix.style.setProperty('--season-count', seasons.length);
  matrix.innerHTML = `
    <div class="posture-row posture-header"><span>Country</span>${seasons.map((entry) => `<span>${entry.season.slice(0, 3)} ${String(entry.year).slice(2)}</span>`).join('')}</div>
    ${countries.map(([country]) => {
      const history = selectedHistory(country, payload);
      return `<div class="posture-row"><strong>${country}</strong>${seasons.map((season) => {
        const snapshot = history.find((entry) => Number(entry.year) === Number(season.year) && entry.season === season.season);
        const posture = snapshot?.posture ?? 'Inactive';
        return `<button class="posture-cell ${postureClass[posture]}" title="${country}, ${season.season} ${season.year}: ${posture}">${posture === 'Inactive' ? '-' : posture.replace('Mixed-', '')}</button>`;
      }).join('')}</div>`;
    }).join('')}
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
  const stageReport = document.getElementById('global-stage-report');

  if (!countries.length) {
    overviewFronts.textContent = '0';
    overviewIsolation.textContent = '0.00';
    overviewEncirclement.textContent = '0.00';
    overviewHolds.textContent = '0';
    overviewSupports.textContent = '0';
    overviewMomentum.textContent = '0.00';
    overviewFactors.innerHTML = '';
    stageReport.innerHTML = '<p>No historical game state is loaded.</p>';
    return;
  }

  const leader = getProjectedLeader(payload);
  const forecastEntries = Object.entries(payload.forecastDetails?.countries ?? {});
  const fallbackProjection = { country: leader?.country ?? 'N/A', win_probability: getProjectedWinChance(leader?.country, payload) / 100, solo_probability: 0, expected_scs: leader?.sc ?? 0, elimination_probability: 0 };
  const forecastLeader = forecastEntries.length
    ? forecastEntries.map(([country, details]) => ({ country, ...details })).sort((a, b) => b.win_probability - a.win_probability)[0]
    : fallbackProjection;
  const bestSoloChance = forecastEntries.length
    ? forecastEntries.map(([country, details]) => ({ country, ...details })).sort((a, b) => b.solo_probability - a.solo_probability)[0]
    : fallbackProjection;
  const topExpectedScs = forecastEntries.length
    ? forecastEntries.map(([country, details]) => ({ country, ...details })).sort((a, b) => b.expected_scs - a.expected_scs)[0]
    : fallbackProjection;
  const highestEliminationRisk = forecastEntries.length
    ? forecastEntries.map(([country, details]) => ({ country, ...details })).sort((a, b) => b.elimination_probability - a.elimination_probability)[0]
    : fallbackProjection;
  const drawChance = round(Number(payload.forecastDetails?.draw_probability ?? 0) * 100, 0);

  overviewFronts.textContent = forecastLeader.country;
  overviewIsolation.textContent = `${round(Number(forecastLeader.win_probability ?? 0) * 100, 0)}%`;
  overviewEncirclement.textContent = `${round(Number(bestSoloChance.solo_probability ?? 0) * 100, 0)}%`;
  overviewHolds.textContent = `${drawChance}%`;
  overviewSupports.textContent = `${formatNumber(topExpectedScs.expected_scs ?? 0, 1)} ${topExpectedScs.country}`;
  overviewMomentum.textContent = `${round(Number(highestEliminationRisk.elimination_probability ?? 0) * 100, 0)}% ${highestEliminationRisk.country}`;

  const mostIsolated = countries
    .map(([country, data]) => ({ country, value: Number(data.current?.isolation ?? 0) }))
    .sort((a, b) => b.value - a.value)[0];
  const mostPressed = countries
    .map(([country, data]) => ({ country, value: Number(data.current?.active_fronts ?? 0) }))
    .sort((a, b) => b.value - a.value)[0];
  const mostExposed = countries
    .map(([country, data]) => ({ country, value: Number(data.current?.exposed_centers ?? 0) }))
    .sort((a, b) => b.value - a.value)[0];
  const closestToSolo = countries
    .map(([country, data]) => ({ country, value: Number(data.current?.solo_distance ?? 18) }))
    .sort((a, b) => a.value - b.value)[0];
  const postureGroups = countries.reduce((groups, [country, data]) => {
    const posture = data.current?.posture || 'Inactive';
    groups[posture] = groups[posture] || [];
    groups[posture].push(country);
    return groups;
  }, {});
  const aggregateMomentum = countries.map(([country]) => ({
    country,
    value: selectedHistory(country, payload).reduce(
      (total, entry) => total + Number(entry.momentum ?? 0), 0,
    ),
  })).sort((a, b) => b.value - a.value);
  const strongestTrajectory = aggregateMomentum[0];
  const fragileCountries = countries
    .map(([country, data]) => ({
      country,
      risk: Number(data.current?.isolation ?? 0) + Number(data.current?.encirclement ?? 0),
    }))
    .sort((a, b) => b.risk - a.risk)
    .slice(0, 2);
  const postures = Object.entries(postureGroups)
    .filter(([posture]) => posture !== 'Inactive')
    .map(([posture, names]) => `${names.join(' and ')} ${names.length === 1 ? 'is' : 'are'} ${posture.toLowerCase()}`);
  const selectedLabel = payload.selectedSeason
    ? formatSeason(payload.selectedSeason.year, payload.selectedSeason.season)
    : 'the current board';
  const mostAtRisk = countries
    .map(([country]) => ({
      country,
      value: Number(payload.forecastDetails?.countries?.[country]?.elimination_probability ?? 0),
    }))
    .sort((a, b) => b.value - a.value)[0];
  const survivalRisk = mostAtRisk?.value
    ? `${mostAtRisk.country} faces the highest elimination risk at ${round(mostAtRisk.value * 100, 0)}%.`
    : 'No power is projected to be eliminated within the current horizon.';

  overviewFactors.innerHTML = `
    <div class="overview-factor">
      <strong>Front pressure</strong>
      ${mostPressed ? `${mostPressed.country} is fighting on ${mostPressed.value} fronts, driving the broadest operational footprint.` : 'No active fronts recorded.'}
    </div>
    <div class="overview-factor">
      <strong>Center security</strong>
      ${mostExposed?.value ? `${mostExposed.country} has ${mostExposed.value} exposed supply ${mostExposed.value === 1 ? 'center' : 'centers'} without adjacent unit cover.` : 'Every threatened supply center currently has adjacent friendly coverage.'}
    </div>
    <div class="overview-factor">
      <strong>Leader</strong>
      ${leader ? `${leader.country} remains the model favorite with ${round(getProjectedWinChance(leader.country, payload), 0)}% confidence and ${leader.sc} centers.` : 'No leader available.'}
    </div>
    <div class="overview-factor">
      <strong>Solo race</strong>
      ${closestToSolo ? `${closestToSolo.country} is ${closestToSolo.value} supply ${closestToSolo.value === 1 ? 'center' : 'centers'} from the 18-center solo threshold.` : 'No solo-race data available.'}
    </div>
  `;

  stageReport.innerHTML = `
    <p>${leader.country} holds the present material lead with ${leader.sc} supply centers and ${leader.units} units. ${strongestTrajectory.country} has accumulated ${formatNumber(strongestTrajectory.value)} momentum through ${selectedLabel}, making ${strongestTrajectory.country === leader.country ? 'that lead' : 'its long-term trajectory'} the clearest strategic signal.</p>
    <p>${postures.length ? `${postures.join('; ')}. ` : ''}${mostPressed.country} has the broadest active perimeter across ${mostPressed.value} fronts. ${mostExposed?.value ? `${mostExposed.country} has ${mostExposed.value} supply ${mostExposed.value === 1 ? 'center' : 'centers'} under direct pressure without adjacent cover.` : 'No supply center is currently under direct pressure without friendly cover.'}</p>
    <p>${fragileCountries.map((entry) => `${entry.country} (${formatNumber(entry.risk)})`).join(' and ')} carry the highest combined positional risk. The current projection assigns a ${drawChance}% chance to operational stalemate before the forecast horizon. ${survivalRisk}</p>
  `;
}

function renderOperationalLedger(payload) {
  const ledgerBody = document.getElementById('operational-ledger-body');
  const countries = getCountryEntries(payload)
    .sort(([, left], [, right]) => Number(right.current?.sc ?? 0) - Number(left.current?.sc ?? 0));

  ledgerBody.innerHTML = countries.map(([country, data]) => {
    const current = data.current ?? {};
    const winterAdjustment = Number(current.winter_adjustment ?? 0);
    const winter = winterAdjustment > 0
      ? `+${winterAdjustment} build${winterAdjustment === 1 ? '' : 's'}`
      : winterAdjustment < 0
        ? `${Math.abs(winterAdjustment)} remove${winterAdjustment === -1 ? '' : 's'}`
        : 'Even';
    const orderRate = `${round(Number(current.order_success_rate ?? 0) * 100, 0)}%`;
    const failedMoves = Number(current.failed_moves ?? 0);
    const exposedCenters = Number(current.exposed_centers ?? 0);
    const homeLost = Number(current.home_centers_lost ?? 0);
    const homeCenters = Number(current.home_centers ?? 0);
    const riskClass = exposedCenters || homeLost ? 'ledger-risk' : 'ledger-secure';

    return `
      <tr>
        <td><strong>${country}</strong></td>
        <td>${current.sc ?? 0} / ${current.units ?? 0}</td>
        <td>${current.solo_distance ?? 18} to 18</td>
        <td>${winter}</td>
        <td>${orderRate}${failedMoves ? `, ${failedMoves} failed move${failedMoves === 1 ? '' : 's'}` : ''}</td>
        <td>${current.frontline_units ?? 0} units / ${current.active_fronts ?? 0} fronts</td>
        <td class="${riskClass}">${exposedCenters} exposed / ${current.threatened_centers ?? 0} threatened</td>
        <td class="${homeLost ? 'ledger-risk' : 'ledger-secure'}">${homeCenters - homeLost}/${homeCenters} secure</td>
      </tr>
    `;
  }).join('');
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
  const selectedExposure = Number(selectedState.exposed_centers ?? 0);

  if (selectedName === leader.country) {
    intelAdvice.textContent = `${selectedName} is in the strongest position. To stay ahead, keep converting center gains into sustained pressure, preserve high support rates, and avoid letting isolation or encirclement drift upward enough to compromise the position.`;
    return;
  }

  const gapText = selectedSc >= leader.sc ? 'close the center-count gap' : 'keep the center-count gap from widening';
  intelAdvice.textContent = `${selectedName} needs to ${gapText}, reduce isolation from ${formatNumber(selectedIsolation)} and encirclement from ${formatNumber(selectedEncirclement)}, and improve its operational profile from ${selectedHolds} holds and ${selectedSupports} supports.${selectedExposure ? ` It also has ${selectedExposure} exposed supply ${selectedExposure === 1 ? 'center' : 'centers'} requiring attention.` : ''}`;
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

  const winterAdjustment = Number(current.winter_adjustment ?? 0);
  const winterText = winterAdjustment > 0
    ? `+${winterAdjustment} build${winterAdjustment === 1 ? '' : 's'}`
    : winterAdjustment < 0
      ? `${Math.abs(winterAdjustment)} remove${winterAdjustment === -1 ? '' : 's'}`
      : 'Even';
  document.getElementById('focus-solo-distance').textContent = `${current.solo_distance ?? 18} to 18`;
  document.getElementById('focus-winter-adjustment').textContent = winterText;
  document.getElementById('focus-order-success').textContent = `${round(Number(current.order_success_rate ?? 0) * 100, 0)}%`;
  document.getElementById('focus-center-defense').textContent = `${round(Number(current.center_defense_rate ?? 1) * 100, 0)}%`;
  document.getElementById('focus-frontline-units').textContent = current.frontline_units ?? 0;
  document.getElementById('focus-exposed-centers').textContent = current.exposed_centers ?? 0;

  const momentumText = Number(current.momentum ?? 0) >= 1 ? 'is sustaining constructive momentum' : 'is struggling to convert pressure into gains';
  const summary = current.sc >= 9 ? 'is shaping a dominant center presence' : current.sc >= 5 ? 'is building a credible foothold' : 'is still contesting space and tempo';
  const exposedCenters = Number(current.exposed_centers ?? 0);
  const centerRisk = exposedCenters
    ? `${exposedCenters} supply ${exposedCenters === 1 ? 'center is' : 'centers are'} under direct pressure without adjacent cover`
    : 'every directly threatened supply center has adjacent friendly cover';
  const projection = payload?.forecastDetails?.countries?.[country];
  const forecastText = projection
    ? `Across the current simulation horizon, it averages ${formatNumber(projection.expected_scs, 1)} SCs and ${formatNumber(projection.expected_units, 1)} units, with an expected rank of ${formatNumber(projection.expected_rank, 1)} and a ${round(Number(projection.solo_probability ?? 0) * 100, 0)}% solo chance.${Number(projection.home_center_loss_probability ?? 0) ? ` Home-center loss appears in ${round(Number(projection.home_center_loss_probability) * 100, 0)}% of trials.` : ''}${Number(projection.elimination_probability ?? 0) ? ` Elimination risk is ${round(Number(projection.elimination_probability) * 100, 0)}%.` : ''}`
    : '';
  const brief = `${country} ${summary}, ${current.solo_distance ?? 18} centers from a solo, and ${momentumText}. Orders converted at ${round(Number(current.order_success_rate ?? 0) * 100, 0)}%; ${centerRisk}. ${winterText === 'Even' ? 'Its current force matches its center count for Winter.' : `The current material balance allows ${winterText} in Winter.`} ${forecastText}`;
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
    document.getElementById('sc-control-chart').innerHTML = '<div class="empty-state">No supply-center data loaded.</div>';
    document.getElementById('position-scatter-chart').innerHTML = '<div class="empty-state">No positional data loaded.</div>';
    document.getElementById('posture-matrix').innerHTML = '<div class="empty-state">No posture history loaded.</div>';
    document.getElementById('operational-ledger-body').innerHTML = '<tr><td colspan="8" class="empty-table">No operational data loaded.</td></tr>';
    renderWarboard(null);
    return;
  }

  const activeCountry = state.selectedCountry && normalizedPayload.countries[state.selectedCountry]
    ? state.selectedCountry
    : Object.keys(normalizedPayload.countries)[0];
  state.selectedCountry = activeCountry;

  renderSummaryTable(normalizedPayload);
  renderMomentumChart(normalizedPayload);
  renderScControlChart(normalizedPayload);
  renderPositionScatterChart(normalizedPayload);
  renderPostureMatrix(normalizedPayload);
  renderWarboard(activeCountry);
  renderCountryFocus(activeCountry, normalizedPayload);
  renderCountryTrendChart(activeCountry, normalizedPayload);
  renderGlobalOverview(normalizedPayload);
  renderOperationalLedger(normalizedPayload);
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
    const gameSession = state.gameSession;
    const existingText = state.gameText || '';
    const response = await fetch('/api/upload', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, year, season, mode, existing_text: existingText })
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
    if (gameSession !== state.gameSession) return;

    state.gameText = payload?.savedGameText || existingText || text;
    if (state.gameText) {
      localStorage.setItem('warboard-saved-game-text', state.gameText);
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

async function restoreSavedGameState() {
  const savedText = localStorage.getItem('warboard-saved-game-text') || '';
  if (!savedText.trim()) {
    return;
  }
  const gameSession = state.gameSession;

  try {
    const response = await fetch('/api/upload', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: savedText, mode: 'full' }),
    });

    if (!response.ok) {
      return;
    }

    if (gameSession !== state.gameSession) return;
    const payload = await response.json();
    state.gameText = payload?.savedGameText || savedText;
    renderDashboard(payload);
  } catch (error) {
    console.warn('Unable to restore saved game state', error);
  }
}

async function startNewWarboard() {
  state.gameSession += 1;
  if (state.restorePromise) {
    await state.restorePromise;
  }
  state.gameText = '';
  state.selectedCountry = null;
  state.selectedSeason = null;
  localStorage.removeItem('warboard-saved-game-text');
  document.getElementById('upload-text').value = '';
  document.getElementById('upload-year').value = '1901';
  document.getElementById('upload-season').value = 'Spring';
  renderDashboard({ selectedSeason: null, countries: {} });
  const status = document.getElementById('upload-status');
  status.textContent = 'Starting new Warboard...';
  status.classList.remove('error');
  try {
    const response = await fetch('/api/reset', { method: 'POST' });
    if (!response.ok) throw new Error('The active game could not be cleared on the server.');
    status.textContent = 'New Warboard ready for Spring 1901 orders.';
  } catch (error) {
    status.textContent = error.message || 'The active game could not be cleared.';
    status.classList.add('error');
  }
}

function saveWarboard() {
  const status = document.getElementById('upload-status');
  if (!state.gameText.trim()) {
    status.textContent = 'Load at least one season before saving.';
    status.classList.add('error');
    return;
  }

  const file = new Blob([state.gameText], { type: 'text/plain;charset=utf-8' });
  const url = URL.createObjectURL(file);
  const link = document.createElement('a');
  link.href = url;
  link.download = 'diplomacy-warboard-orders.txt';
  link.click();
  URL.revokeObjectURL(url);
  status.textContent = 'Warboard history saved.';
  status.classList.remove('error');
}

async function loadSavedWarboard(event) {
  const [file] = event.target.files;
  if (!file) return;

  const status = document.getElementById('upload-status');
  try {
    const text = await file.text();
    if (!text.trim()) throw new Error('The selected save file is empty.');
    status.textContent = 'Loading saved Warboard...';
    status.classList.remove('error');
    const response = await fetch('/api/upload', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, mode: 'full' }),
    });
    const payload = await response.json();
    if (!response.ok) throw new Error(payload?.error || 'Saved Warboard could not be loaded.');
    state.gameText = payload.savedGameText || text;
    localStorage.setItem('warboard-saved-game-text', state.gameText);
    document.getElementById('upload-text').value = '';
    renderDashboard(payload);
    status.textContent = `Loaded ${payload.availableSeasons?.length ?? 0} saved seasons.`;
  } catch (error) {
    status.textContent = error.message || 'Saved Warboard could not be loaded.';
    status.classList.add('error');
  } finally {
    event.target.value = '';
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
  document.getElementById('new-warboard').addEventListener('click', startNewWarboard);
  document.getElementById('save-warboard').addEventListener('click', saveWarboard);
  document.getElementById('load-warboard').addEventListener('change', loadSavedWarboard);

  uploadPanel.classList.add('collapsed');
}

document.addEventListener('DOMContentLoaded', () => {
  bindUploadControls();
  const savedGameText = localStorage.getItem('warboard-saved-game-text') || '';
  state.gameText = savedGameText;
  if (savedGameText) {
    document.getElementById('upload-text').value = savedGameText;
  }
  loadDashboardData();
  state.restorePromise = restoreSavedGameState();
});
