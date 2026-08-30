# Research Data Governance

## Classification

| Class | Examples | Git policy |
|---|---|---|
| Public | approved presentation images, anonymous thumbnails, published references | permitted after source and license review |
| Internal | manuscripts, working notes, claim ledgers | private repository only |
| Restricted-derived | participant heatmaps, corrected gaze summaries | anonymous IDs only; access review required |
| Restricted-raw | original gaze coordinates, consent records, identifiable participant data | never store in this repository |

Tracked research inputs are grouped under `materials/` by role. Directory
placement does not change their access class: `materials/` is never a public
asset source, and only anonymous optimized files under `src/assets/images/` may
enter the generated presentation.

## Current Migration Risk

The historical `ab2/` filenames appear to contain participant names. They remain in place only as a migration input and must not be copied into public release paths. Their presence in Git history requires a separate human-approved remediation with a verified backup and remote coordination.

## Required Controls

1. Public presentation assets use IDs such as `p01-control`, never names.
2. `deck-manifest.json` records the access class of every presentation asset.
3. A release must contain no restricted-raw material and no identifiable restricted-derived filename.
4. Consent scope, publication permission, retention period, deletion owner, and storage location must be recorded outside the public artifact before restricted-derived data is released.
5. `sources.yml` stores checksums and access levels; `claims.yml` stores wording strength and review status.
6. A blocked claim cannot be strengthened or presented as confirmed without human source review.

## Responsibilities

- Research owner: confirms consent, scientific wording, and source authority.
- Maintainer: enforces paths, IDs, checksums, and release gates.
- Reviewing agent: stops when identity, permission, sample, or metric definitions conflict.

Removing a file from the working tree does not remove it from Git history. History rewriting is destructive and is outside automated maintenance authority.
