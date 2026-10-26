<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/banner-v2-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="./assets/banner-v2.svg" />
    <img alt="Oliver Zhang (Zhiyuan Zhang) — The Board, The Cage, The Kernel, and A Hundred Doors" src="./assets/banner-v2.svg" width="100%" />
  </picture>
</p>

**Oliver Zhang (Zhiyuan Zhang)** · London / Suzhou / Shenzhen · Account opened 2025.04 · 640 contributions in the last 12 months · Plays chess off-duty.

> Keep goals reachable, make unsafe states unreachable, and prune invalid paths after verification.  
> 探针只检查在不在。缺了就在标准错误里写出变量名。

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/tech-stack-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="./assets/tech-stack.svg" />
    <img alt="C++ · CUDA · MLIR · Rust · Python · Lean 4 · TypeScript · Go" src="./assets/tech-stack.svg" width="100%" />
  </picture>
</p>

### Upstream (`merged`)

| Project | PR | Verdict & Scope |
| :--- | :--- | :--- |
| <img src="https://github.com/tile-ai.png?size=32" width="16" height="16" align="absmiddle" /> [`tile-ai/tilelang`](https://github.com/tile-ai/tilelang) | <img src="./assets/icons/merged.svg" height="16" align="absmiddle" /> [`#3045`](https://github.com/tile-ai/tilelang/pull/3045) | Official compile-only CLI: `python -m tilelang.tools.compile_only` lowers kernels to source without executing them. |
| <img src="https://github.com/compiler-explorer.png?size=32" width="16" height="16" align="absmiddle" /> [`compiler-explorer/compiler-explorer`](https://github.com/compiler-explorer/compiler-explorer) | <img src="./assets/icons/merged.svg" height="16" align="absmiddle" /> [`#9029`](https://github.com/compiler-explorer/compiler-explorer/pull/9029) | Integrated TileLang as a compile-only language in Compiler Explorer. |
| <img src="https://github.com/compiler-explorer.png?size=32" width="16" height="16" align="absmiddle" /> [`compiler-explorer/compiler-explorer`](https://github.com/compiler-explorer/compiler-explorer) | <img src="./assets/icons/merged.svg" height="16" align="absmiddle" /> [`#9210`](https://github.com/compiler-explorer/compiler-explorer/pull/9210) | Single regex parsing binary asm source lines in `objdump` output across Linux, Windows, and `llvm-objdump`. |
| <img src="https://github.com/compiler-explorer.png?size=32" width="16" height="16" align="absmiddle" /> [`compiler-explorer/infra`](https://github.com/compiler-explorer/infra) | <img src="./assets/icons/merged.svg" height="16" align="absmiddle" /> [`#2307`](https://github.com/compiler-explorer/infra/pull/2307) [`#2381`](https://github.com/compiler-explorer/infra/pull/2381) | TileLang `0.1.13` and `0.1.14` pip packages. |
| <img src="https://github.com/The-Last-Math-Competition.png?size=32" width="16" height="16" align="absmiddle" /> [`The-Last-Math-Competition`](https://github.com/The-Last-Math-Competition) | <img src="./assets/icons/merged.svg" height="16" align="absmiddle" /> [`#920`](https://github.com/The-Last-Math-Competition/The-Last-Math-Competition/pull/920) | Disproved Conjecture `00000000408`: for `n = 2`, Kronecker coefficient `g((2,1),(2,1),(2,1)) = 1` is odd while `2` is not triangular. Lean 4.19 proof (`0 sorry`, no `native_decide`, no extra axioms). |

### Public Repositories

<table>
  <thead>
    <tr><th width="56"></th><th align="left" width="190">Repository</th><th align="left">Scope</th><th align="left" width="250">External Gate / Artifact</th></tr>
  </thead>
  <tbody>
    <tr>
      <td width="56" align="center" valign="top"><img src="./assets/icons/caging.svg" width="40" height="40" /></td>
      <td valign="top"><a href="https://github.com/LibertychaserUS/caging-engineering"><strong>caging-engineering</strong></a></td>
      <td valign="top">Reachability framework for reliable AI agents: <em>“Keep goals reachable, make unsafe states unreachable, and prune invalid paths after verification.”</em></td>
      <td valign="top">State-space boundary</td>
    </tr>
    <tr>
      <td width="56" align="center" valign="top"><img src="./assets/icons/terra.svg" width="40" height="40" /></td>
      <td valign="top"><a href="https://github.com/LibertychaserUS/Terra"><strong>Terra</strong></a></td>
      <td valign="top">Rust agent runtime implementing Caging. Every file, memory, and shell operation passes through cage and audit log before execution. <em>Efficiency is Intelligence.</em></td>
      <td valign="top">12 crates · ~10 MB binary · 620 tests · MCP · MIT · <code>v0.2</code></td>
    </tr>
    <tr>
      <td width="56" align="center" valign="top"><img src="./assets/icons/aiops.svg" width="40" height="40" /></td>
      <td valign="top"><a href="https://github.com/LibertychaserUS/AIOps"><strong>AIOps</strong></a></td>
      <td valign="top">Two installable GitHub tools: <strong>Forge</strong> (who can push/open PRs; humans merge) and <strong>Overlay</strong> (reviewable test suite).</td>
      <td valign="top">CI runs <code>active</code>, drops <code>blocked</code>; human merge</td>
    </tr>
    <tr>
      <td width="56" align="center" valign="top"><img src="./assets/icons/officex.svg" width="40" height="40" /></td>
      <td valign="top"><a href="https://github.com/LibertychaserUS/OfficeX-an-AI-agents-for-doc"><strong>OfficeX-an-AI-agents-for-doc</strong></a></td>
      <td valign="top">Document manipulation infrastructure for AI agents and humans. Deterministic execution, CLI + MCP.</td>
      <td valign="top">Three-track check: structural / visual / semantic</td>
    </tr>
    <tr>
      <td width="56" align="center" valign="top"><img src="./assets/icons/microfluidic.svg" width="40" height="40" /></td>
      <td valign="top"><a href="https://github.com/LibertychaserUS/microfluidic-native-physics"><strong>microfluidic-native-physics</strong></a></td>
      <td valign="top">Reliability audit of public microfluidic data: whole surfactant-chemistry group holdouts, sealed labels, negative results retained in record.</td>
      <td valign="top">HF: <a href="https://huggingface.co/datasets/Chaser111/microfluidic-native-physics"><code>Chaser111/microfluidic-native-physics</code></a></td>
    </tr>
    <tr>
      <td width="56" align="center" valign="top"><img src="./assets/icons/wca.svg" width="40" height="40" /></td>
      <td valign="top"><a href="https://github.com/LibertychaserUS/world-cellular-automata"><strong>world-cellular-automata</strong></a> · <a href="https://github.com/LibertychaserUS/world-cellular-automata-technical-report"><strong>report</strong></a></td>
      <td valign="top">Recursive world-state prediction and technical report.</td>
      <td valign="top">Zenodo: <a href="https://doi.org/10.5281/zenodo.21085154"><code>10.5281/zenodo.21085154</code></a></td>
    </tr>
    <tr>
      <td width="56" align="center" valign="top"><img src="./assets/icons/bsaa.svg" width="40" height="40" /></td>
      <td valign="top"><a href="https://github.com/LibertychaserUS/bsaa-gaokao-theory"><strong>bsaa-gaokao-theory</strong></a></td>
      <td valign="top">BSAA/GSIO theory implementation for Gaokao preference recommendation.</td>
      <td valign="top">CI Lean gate (<code>0 sorry</code> + axiom audit)</td>
    </tr>
    <tr>
      <td width="56" align="center" valign="top"><img src="./assets/icons/robot-pm.svg" width="40" height="40" /></td>
      <td valign="top"><a href="https://github.com/LibertychaserUS/robot-pm"><strong>robot-pm</strong></a></td>
      <td valign="top">Project assistant in Feishu group chats (Chinese README). <em>“会议要群里点同意才建立。时间用北京时间。”</em></td>
      <td valign="top">Probe checks presence; group consent required</td>
    </tr>
    <tr>
      <td width="56" align="center" valign="top"><img src="./assets/icons/journeys.svg" width="40" height="40" /></td>
      <td valign="top"><a href="https://github.com/LibertychaserUS/100-journeys"><strong>100-journeys</strong></a></td>
      <td valign="top"><em>100 Impossible Journeys</em> (《100 种不可思议的旅行》), bilingual travel site: <em>“一百扇按各自时辰开的门”</em>.</td>
      <td valign="top"><em>“doors on their own clocks, calmer opening, tighter atlas”</em></td>
    </tr>
  </tbody>
</table>
