# 3.0.0 (2020-01-06)
### Bug Fixes
* **ivy**  validate the NgModule declarations field (#34404) (763f8d4)
* **language-service**  HTML path should include last node before cursor (#34440) (5df8a3b)
* **language-service**  Remove completions for let and of in ngFor (#34434) (5eaab85)
* **ivy**  reorder provider type checks to align with VE (#34433) (357a073)
* **animations**  leaking detached nodes when parent has a leave transition (#34409) (835ed0f)
* **common**  ngStyle should ignore undefined values (#34422) (1144ce9)
* **ivy**  record correct absolute source span for ngForOf expressions (#31813) (ddc229b)
### Features
* **forms**  expand NgModel disabled type to work with strict template type checking (#34438) (5cecd97)
# 2.0.0 (2020-01-06)
### Bug Fixes
* **ngcc**  use the correct identifiers when updating typings files (#34254) (31be29a)
* **ngcc**  correctly match aliased classes between src and dts files (#34254) (f22a6eb)
* **ngcc**  handle UMD re-exports (#34254) (e9fb5fd)
* **ngcc**  handle CommonJS re-exports by reference (#34254) (47666f5)
* **language-service**  Proper completions for properties and events (#34445) (a04f7c0)
* **ivy**  improve ExpressionChangedAfterChecked error (#34381) (9d1175e)
* **ivy**  correctly associate output bound events with directives (#31938) (3e20118)
# 1.0.0 (2020-01-06)
### Bug Fixes
* **language-service**  completions after "let x of |" in ngFor (#34473) (2dffe65)
* **ivy**  don't produce template diagnostics when scope is invalid (#34460) (498a2ff)
* **ivy**  avoid duplicate errors in safe navigations and template guards (#34417) (3959511)
### Features
* **language-service**  Append symbol type to hover tooltip (#34515) (9b9116c)
* **ivy**  error in ivy when inheriting a ctor from an undecorated base (#34460) (cf37c00)
* **ivy**  throw compilation error when providing undecorated classes (#34460) (dcc8ff4)
