## Preface — Why & How This Book Was Made

This is a book about an upgrade, built by an unusual workshop. Here is the honest account of why it exists and how it was made — including what it cost, stated in the units a software project actually spends.

### Why This Book Exists

The mission fits in one sentence: take a licensed Technician to a passed General exam, and from there to worldwide HF. The Technician ticket opens local and regional radio; General removes the fences below 30 MHz and hands you the bands where contacts cross oceans on ordinary antennas. This book is the course for that jump.

The method is teach-first, then exam-aligned. Each chapter teaches its topic at General depth — the math included, step by step — and only then turns to face the exam, closing with verbatim pool questions so you always know when you have a subelement cold. The course assumes what a Technician already knows and builds from there, no more, no less.

Everything exam-facing is aligned to the NCVEC 2023–2027 General pool, the public document every real exam question is drawn from. **That pool is valid for exams through 2027-06-30.** Until then, what you read here is what the exam asks. After that date a successor pool takes over, and the book is designed for exactly that day: the teaching content is durable, and only the pool-facing parts — the Exam Focus picks and Appendix A — swap out, in a contained procedure pinned down in the accuracy canon. If you are reading this late in the window, schedule your exam before it closes.

This is the middle book of a three-book series: *Your First Ham License* is the Technician course, this book is the General course, and *Your Last Ham License* is the Extra course waiting on the far side of General.

### How This Book Was Made

The workshop was a multi-agent AI workflow — one orchestrating session launching dozens of cooperating agents, each with a narrow job, all governed by an accuracy canon treated as law. The canon pinned every fact, definition, notation choice, and rule quotation before a word of prose was written, and where any draft disagreed with the canon, the canon won. It also settled the hard cases in advance — including the FCC's January 2026 rewrite of the 60-meter rules, which postdates the pool: the book teaches the current FCC text and drills the pool's keyed answers exactly as published.

The official NCVEC pool is public domain, and it was ingested verbatim — double-parsed independently from the released .docx and .pdf and cross-checked to zero disagreement, with all six errata releases incorporated and the nine withdrawn questions cataloged and omitted. Chapter writers then worked in parallel, as did the figure authors. Behind them, span auditors re-verified every fact against the canon and every quoted question against the canonical pool files. Finally, an 8-check automated audit ran over the whole book, including a mechanical verbatim-pool fidelity check: all 423 active questions byte-exact, every answer key matching the pool.

The figures are 35 original works — hand-authored themeable SVG and plotted curves. The one pool figure the exam references, G7-1, was redrawn as an original SVG from the question's own description, never copied. The audiobook edition is narrated in eight voices across four accents.

The integrity rules were simple and absolute. All prose is original. Facts, 47 CFR Part 97, and the question pools are public domain and free to quote; everything else is written fresh. No quotation is ever fabricated.

### Production Stats

- 91,920 words (49,639 chapters · 33,081 annotated pool · 9,200 glossary & formulas)

- 35 figures, all original

- 423/423 pool questions annotated — every active question verbatim, answer keyed, one-line why

- 79 tooling tests; 8 audit checks

- ~45 subagent launches (estimate), plus retries after transient engine errors

- Calendar span 2026-07-23 → 2026-07-24, with parallel agents throughout

- ~4.1 million subagent tokens (estimate): this runtime does not meter subagent tokens; the estimate models all agent reads of the canonical files plus written output volume at ~4 characters per token

Two days, one canon, one pool, and a great deal of checking. The upgrade itself is yours to make.
