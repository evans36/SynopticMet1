<h2>Synoptic Meteorology Labs</h2>
<h4><i>Release v0.1, January 2023</i><br>Clark Evans and Michael Vossen</h4>

This repository contains a set of twelve labs designed for a first-semester undergraduate course in synoptic meteorology, focusing on introductory concepts, atmospheric balances, kinematic properties, atmospheric stability, and fronts, jets, and cyclones. Each lab is currently provided in Microsoft Word format, each of which is supported by one or more Jupyter Notebooks. The Jupyter Notebooks introduce students to accessing and plotting meteorological data (surface and upper-air observations, skew-T ln-p diagrams, and model data) using modern Python tools.

The Jupyter Notebooks cover the following Python-related topics:
<ul>
  <li><b>Lab 1</b> (Meteorological Data): Remotely accessing and decoding METAR and upper-air data; remotely accessing and plotting geostationary satellite data.</li>
  <li><b>Lab 2</b> (Isoplething Upper-Air Data): Remotely accessing and generating station plots of upper-air observations.</li>
  <li><b>Lab 3</b> (Isoplething Surface Data): Remotely accessing and generating station plots of surface and upper-air observations.</li>
  <li><b>Lab 4</b> (Horizontal Advection): Contouring model-derived upper-air data; remotely accessing and plotting geostationary satellite data.</li>
  <li><b>Lab 5</b> (Hypsometric Equation): Remotely accessing, objectively analyzing, and contouring METAR observations; remotely accessing and generation station plots of upper-air observations; contouring model-derived upper-air data.</li>
  <li><b>Lab 6</b> (Geostrophic Balance): Remotely accessing and generating station plots of upper-air observations; contouring model-derived upper-air data; computing and plotting the ageostrophic wind.</li>
  <li><b>Lab 7</b> (Thermal Wind): Remotely accessing and generating skew-T, ln-p diagrams of upper-air observations; contouring model-derived upper-air data.</li>
  <li><b>Lab 8</b> (Fronts): Remotely accessing, objectively analyzing, and contouring METAR observations; contouring model-derived upper-air data.</li>
  <li><b>Lab 9</b> (Jets and Other Force Balances): Computing and plotting the ageostrophic wind and divergence from model data; contouring model-derived upper-air data.</li>
  <li><b>Lab 10</b> (Kinematic Properties): Computing and plotting vertical vorticity from model data; contouring model-derived upper-air data; remotely accessing and plotting geostationary satellite data.</li>
  <li><b>Lab 11</b> (Sounding Applications): Remotely accessing and generating skew-T, ln-p diagrams of upper-air observations.</li>
  <li><b>Lab 12</b> (Sounding-Based Stability Analysis): Remotely accessing and generating skew-T, ln-p diagrams of upper-air observations.</li>
</ul>

Planned future additions/updates include:
<ul>
  <li>Adding labs for a second-semester undergraduate course in synoptic meteorology (frontogenesis/frontolysis, quasi-geostrophic theory, isentropic analysis, isentropic potential vorticity).</li>
  <li>Reworking each lab so that it is fully self-contained in Jupyter Notebooks.</li>
  <li>Reworking labs which reference local data to reference cloud-based data.</li>
</ul>

The primary packages used by these Jupyter Notebooks are cartopy, MetPy, siphon, and xarray. The JupyterHub on which these notebooks were first deployed runs Python 3.7.12, cartopy 0.20.0, MetPy 1.2.0, siphon 0.9, and xarray 0.20.2. It is likely that these notebooks will work with newer versions of each package with few, if any, changes.

Comments, questions, etc.: evans36-at-uwm-dot-edu.
