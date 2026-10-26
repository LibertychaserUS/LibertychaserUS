<p align="center">
  <img src="./assets/banner.svg" alt="AI infrastructure and systems engineering — regenerated daily by GitHub Actions" width="100%">
</p>

<div align="center">
  <samp><b>OLIVER ZHANG</b> &nbsp;//&nbsp; AI Infrastructure · Systems Engineering · Compiler Tooling</samp>
</div>

<br>

<table width="100%">
<tr>
<td width="55%" valign="top">

<h3><code>01 // SYSTEM_OVERVIEW</code></h3>

<p>做 <b>AI 基础设施与系统工程</b>：从推理性能、编译器工具链，到能上线的后端服务。偏好把底层问题做到底，再交付可维护的产品。</p>

<ul>
  <li><b>AI 基础设施</b>：推理服务、GPU 异构计算、性能与显存优化</li>
  <li><b>工具链</b>：TileLang / Compiler Explorer 上游贡献，compile-only 工作流</li>
  <li><b>工程落地</b>：现代 C++ / Python / Go 服务，CI 与自动化质量门禁</li>
</ul>

</td>
<td width="45%" valign="top">

<h3><code>02 // TELEMETRY.hpp</code></h3>

<pre><code class="language-cpp">namespace oliver {
  struct Profile {
    const char* role = "AI Infrastructure Engineer";

    // engineering base
    std::vector&lt;const char*&gt; stack = {
      "C++ (modern / async)", "Python", "Rust", "Go"
    };

    // current focus
    std::vector&lt;const char*&gt; focus = {
      "Inference systems",
      "Compiler tooling",
      "Backend services"
    };

    const char* off_duty = "Chess";
  };
}</code></pre>

</td>
</tr>
</table>

<br>

### `03 // ARCHITECTURAL_FOCUS`

| 方向 | 技术栈 | 关注的问题 |
| --- | --- | --- |
| AI 推理与性能 | `C++` `CUDA` `Python` `Profiling` | 算子与显存、批处理与缓存、端到端吞吐 |
| 编译器与工具链 | `TileLang` `MLIR` `Compiler Explorer` | DSL 接入、compile-only 流程、自动化回归 |
| 后端与系统工程 | `Go` `Rust` `Linux` `CI/CD` | 并发与可靠性、可观测性、发布质量门禁 |

<br>

### `04 // SELECTED_WORKS`

**Merged upstream**
- **[TileLang](https://github.com/tile-ai/tilelang)** — official compile-only CLI ([#3045](https://github.com/tile-ai/tilelang/pull/3045))
- **[Compiler Explorer](https://github.com/compiler-explorer/compiler-explorer)** — TileLang language support ([#9029](https://github.com/compiler-explorer/compiler-explorer/pull/9029), [#9210](https://github.com/compiler-explorer/compiler-explorer/pull/9210))

**Systems & products**
- [caging-engineering](https://github.com/LibertychaserUS/caging-engineering) — reliability constraints for AI agent systems
- [AIOps](https://github.com/LibertychaserUS/AIOps) — AI agents as a release gate
- [OfficeX](https://github.com/LibertychaserUS/OfficeX-an-AI-agents-for-doc) — AI agents for documents
- [100-journeys](https://github.com/LibertychaserUS/100-journeys) — 100 个不可思议的旅行

<br>

### `05 // METRICS`

<div align="center">
  <img height="150" src="https://github-readme-stats.vercel.app/api?username=LibertychaserUS&show_icons=true&hide_rank=true&theme=transparent&hide_border=true&title_color=58a6ff&text_color=c9d1d9&icon_color=58a6ff" alt="GitHub stats">
  <img height="150" src="https://github-readme-stats.vercel.app/api/top-langs/?username=LibertychaserUS&layout=compact&theme=transparent&hide_border=true&title_color=58a6ff&text_color=c9d1d9" alt="Top languages">
</div>

<div align="center">
  <samp>Build it, measure it, make it boring.</samp>
</div>
