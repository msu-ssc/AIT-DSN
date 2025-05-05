# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0] - 2025-05-05

This is the first MSU SSC release after forking from [upstream]((https://github.com/NASA-AMMOS/AIT-DSN)). No other changes have been made.

### Changed

- Switched backend from Poetry to UV.

## [2.0.1-rc1](https://github.com/NASA-AMMOS/AIT-DSN/compare/2.0.0...2.0.1-rc1) - 2022-04-13

### Merged

- Issue #174 - Fix gevent.select typo [`#175`](https://github.com/NASA-AMMOS/AIT-DSN/pull/175)
- Issue #170 - Add plugin for extracting CCSDS packets from AOS packets [`#173`](https://github.com/NASA-AMMOS/AIT-DSN/pull/173)
- issue #168 - Add capability for TCP to publish TCP data into PUB/SUB [`#171`](https://github.com/NASA-AMMOS/AIT-DSN/pull/171)
- Issue #169 - Add select/sendall when using DSN socket [`#172`](https://github.com/NASA-AMMOS/AIT-DSN/pull/172)
- Issue #163 - Create fresh socket for each hostname connection attempt [`#164`](https://github.com/NASA-AMMOS/AIT-DSN/pull/164)
- Issue #160 - Fix calls to refactored hexint() [`#162`](https://github.com/NASA-AMMOS/AIT-DSN/pull/162)
- Issue #139 - Updates to the SLE Manager Interface and example use [`#141`](https://github.com/NASA-AMMOS/AIT-DSN/pull/141)
- Issue #158 - Add TCP Forwarding Plugin [`#157`](https://github.com/NASA-AMMOS/AIT-DSN/pull/157)
- Issue #155 - Add Encrypter Plugin [`#156`](https://github.com/NASA-AMMOS/AIT-DSN/pull/156)
- Issue #143 - Updated release of AIT encryption support [`#154`](https://github.com/NASA-AMMOS/AIT-DSN/pull/154)
- Issue #115 - Add support for TC transfer frames [`#153`](https://github.com/NASA-AMMOS/AIT-DSN/pull/153)
- Issue #140 - Engineering release of AIT encryption support [`#142`](https://github.com/NASA-AMMOS/AIT-DSN/pull/142)

### Commits

- issue-#158 Add TCP Forwarding Plugin [`f2ecfa6`](https://github.com/NASA-AMMOS/AIT-DSN/commit/f2ecfa6635b531fc8b089b8e452aa492dab8425f)
- issue-#174 Fix select typo [`139b8c8`](https://github.com/NASA-AMMOS/AIT-DSN/commit/139b8c8b43cd9adbdcd59ca0d36d069f2830c7a4)

## [2.0.0](https://github.com/NASA-AMMOS/AIT-DSN/compare/1.1.0...2.0.0)

### Merged

- Add the SLE Interface Manager [`#131`](https://github.com/NASA-AMMOS/AIT-DSN/pull/131)
- Issue #132 - Pin greenlets to 0.4.16 [`#133`](https://github.com/NASA-AMMOS/AIT-DSN/pull/133)
- Issue #118 - Convert string to byte string on common.py [`#120`](https://github.com/NASA-AMMOS/AIT-DSN/pull/120)
- Fix Issue #124– Check if SLE instance is connected to the DSN before sending heartbeats [`#126`](https://github.com/NASA-AMMOS/AIT-DSN/pull/126)
- Issue #113 - Relocation aos_deframer example and add header [`#114`](https://github.com/NASA-AMMOS/AIT-DSN/pull/114)
- Added baseline AOS deframer code for LunaH-Map [`#97`](https://github.com/NASA-AMMOS/AIT-DSN/pull/97)
- Issue #110 - RAF/RCF emits entire frame contents to a frame-specific … [`#111`](https://github.com/NASA-AMMOS/AIT-DSN/pull/111)
- Issue #108 - Pull all attributes from kwargs and config [`#109`](https://github.com/NASA-AMMOS/AIT-DSN/pull/109)
- Issue #102 - Drop ait_sle_bridge.py [`#103`](https://github.com/NASA-AMMOS/AIT-DSN/pull/103)
- Issue #60: Implement AOS Transfer Frames per Spec [`#98`](https://github.com/NASA-AMMOS/AIT-DSN/pull/98)
- Update Travis build icon [`#106`](https://github.com/NASA-AMMOS/AIT-DSN/pull/106)
- DSN Example script cleanup [`#104`](https://github.com/NASA-AMMOS/AIT-DSN/pull/104)
- Issue #100 - Update Python version in RTD config [`#101`](https://github.com/NASA-AMMOS/AIT-DSN/pull/101)
- Issue #92 - Incorporate BCH code into AIT-DSN [`#96`](https://github.com/NASA-AMMOS/AIT-DSN/pull/96)
- Issue #90 - Implement python 3 support [`#91`](https://github.com/NASA-AMMOS/AIT-DSN/pull/91)
- Issue #85 - Merge config files between AIT-Core and AIT-DSN [`#94`](https://github.com/NASA-AMMOS/AIT-DSN/pull/94)
- Issue #84 - Add SLE parameters to config file [`#89`](https://github.com/NASA-AMMOS/AIT-DSN/pull/89)
- Fix typo in SLE config; update RCF script for new config format (#87) [`#88`](https://github.com/NASA-AMMOS/AIT-DSN/pull/88)

### Commits

- Updated imports [`6049327`](https://github.com/NASA-AMMOS/AIT-DSN/commit/60493273a6ede9d1b6a16ea4fca38e4d81abd268)
- Fixes for cltu and rcf api tests [`fb7f1af`](https://github.com/NASA-AMMOS/AIT-DSN/commit/fb7f1afaa460abcace4dfe68a546f469db8554f0)
- Issue #110 - RAF/RCF emits entire frame contents to a frame-specific port [`b0894c5`](https://github.com/NASA-AMMOS/AIT-DSN/commit/b0894c5db562a67d6b5c1021c831931d65c47550)
- Fixes for cltu_throw_event_test, sspsim_example, tm_downlink_example [`a227892`](https://github.com/NASA-AMMOS/AIT-DSN/commit/a227892390c91a4aacbd6859fe37a0bfce34016f)
- Isse #129 update test step and add SLE cltu config parameters [`c7bcabe`](https://github.com/NASA-AMMOS/AIT-DSN/commit/c7bcabe5a5f2b9726bdb1dcc0ba69e25af998ea9)
- Issue #85 - replace gui section to AIT-Core server section [`ab9b5f8`](https://github.com/NASA-AMMOS/AIT-DSN/commit/ab9b5f85768fc62b4cc9ff27a208195888e379a8)
- Fixes for pdu_test [`61379e1`](https://github.com/NASA-AMMOS/AIT-DSN/commit/61379e10ec7390580d1fc7e294ea839e63c3ba58)
- Open file and print statement updates [`7f4e57e`](https://github.com/NASA-AMMOS/AIT-DSN/commit/7f4e57e1ceba7a6a731a46d50c0f0af4f74c64f8)
- Fixes for cfdp_test [`4eb3b00`](https://github.com/NASA-AMMOS/AIT-DSN/commit/4eb3b00d0e914a16a899d323be740d3512abb5ca)
- Issue #118 convert to bytestring [`5dd043f`](https://github.com/NASA-AMMOS/AIT-DSN/commit/5dd043fc8860ae0007cb285380403747dcb15938)
- Fix Issue #124– check if SLE object is connected to DSN before sending heartbeat [`20edfd8`](https://github.com/NASA-AMMOS/AIT-DSN/commit/20edfd8e967efa490426db978b9a795448acacba)
- Issue #84 - change auth_level setting to self._auth_level [`ebd1db5`](https://github.com/NASA-AMMOS/AIT-DSN/commit/ebd1db5708be11c2aceb45caad833bd7d1d57529)
- Issue #129 convert str to byte obj [`00bd8b5`](https://github.com/NASA-AMMOS/AIT-DSN/commit/00bd8b5607d3fd40a630b89de0e1eed63dee8799)
- Updated python version for travis [`936472c`](https://github.com/NASA-AMMOS/AIT-DSN/commit/936472ce99490a8af475bd99a3634950e2963789)
- Issue #85 - add ATI-Core notifications:options [`14d606e`](https://github.com/NASA-AMMOS/AIT-DSN/commit/14d606e90cf022676514c796a4d33c77bb85c037)
- Updated required ait-core version to &gt;=1.4.0 [`cc1fd2e`](https://github.com/NASA-AMMOS/AIT-DSN/commit/cc1fd2e11ac4d98b4b0ca4efbb98d933e2a366d1)
- Updated required ait-core version to &gt;=2.0rc1.dev0 [`767c7aa`](https://github.com/NASA-AMMOS/AIT-DSN/commit/767c7aa392fcb82937f870b8e2a9abb911913651)
- Python 3 import fix [`b496559`](https://github.com/NASA-AMMOS/AIT-DSN/commit/b49655949fc948230d9eb988ff29d0d51045a7e2)
- Added ait-core install step for travis testing [`327795b`](https://github.com/NASA-AMMOS/AIT-DSN/commit/327795b7c01a74a3573d6f1f42ccf3be1f74da40)
- Removed ait-core install step from travis config [`eaa102f`](https://github.com/NASA-AMMOS/AIT-DSN/commit/eaa102fdae1c1aeb895ef453075df859f84b5ebd)

## [1.1.0](https://github.com/NASA-AMMOS/AIT-DSN/compare/1.0.0...1.1.0) - 2019-10-10

### Merged

- Issue #73 - CFDP send/receive over UDP socket connection [`#81`](https://github.com/NASA-AMMOS/AIT-DSN/pull/81)
- Issue #64 - Attempt SLE connection to multiple hostnames [`#86`](https://github.com/NASA-AMMOS/AIT-DSN/pull/86)
- Issue 76 - add option to pull hostname / port from config [`#83`](https://github.com/NASA-AMMOS/AIT-DSN/pull/83)
- Issue #77 - Update SLE config parameters [`#82`](https://github.com/NASA-AMMOS/AIT-DSN/pull/82)
- CFDP send/receive over UPD ports [`#73`](https://github.com/NASA-AMMOS/AIT-DSN/pull/73)
- Issue #71 - Add SLE documentation [`#80`](https://github.com/NASA-AMMOS/AIT-DSN/pull/80)
- Bugfixes [`#55`](https://github.com/NASA-AMMOS/AIT-DSN/pull/55)
- Issue 83 in AIT-CORE: Baseline example configs across repos [`#51`](https://github.com/NASA-AMMOS/AIT-DSN/pull/51)

### Commits

- Issue #67 - Remove unused SLE transfer frame definition yamls [`6aa4dc2`](https://github.com/NASA-AMMOS/AIT-DSN/commit/6aa4dc29fd899d87ee0f6944c7075230b2cbe61b)
- Issue #83 - Baseline example configs across repos [`3445a7b`](https://github.com/NASA-AMMOS/AIT-DSN/commit/3445a7b6aeafaa71b8eafe5d22ea8d5d107e8663)
- Issue #83 - Baseline example configs across repos [`bcf7b51`](https://github.com/NASA-AMMOS/AIT-DSN/commit/bcf7b51fcf6e890972a056ccf7f2f88d6715f73d)
- Issue #83 - Baseline example configs across repos [`28a41c7`](https://github.com/NASA-AMMOS/AIT-DSN/commit/28a41c7f0c74d95c53e886a972be57e92c75cac9)
- Additions to SLE docs including examples (#71) [`2e71079`](https://github.com/NASA-AMMOS/AIT-DSN/commit/2e71079ff555a1006bb8a81338e27ae25a57860e)
- Add initial AOS transfer frame implementation [`732d63c`](https://github.com/NASA-AMMOS/AIT-DSN/commit/732d63c0f0b09e72fe78a40d128842a99751363a)
- Formatting updates; some links still broken (#58) [`da0800e`](https://github.com/NASA-AMMOS/AIT-DSN/commit/da0800e90d3b673b7680e990f01366e73a587b29)
- Split inst_id/hostname/port configs across SLE protocols (#64) [`46affa2`](https://github.com/NASA-AMMOS/AIT-DSN/commit/46affa2c5ec721af2eadc73f629069416d223c7f)
- Issue #66 - Add save-to-file method to CLTU [`f2df979`](https://github.com/NASA-AMMOS/AIT-DSN/commit/f2df979e2599c3e479e492596bf20d7f61050239)
- Update API Docs [`7fb34ea`](https://github.com/NASA-AMMOS/AIT-DSN/commit/7fb34ea57284224c36d26a8637ddfb1e6d22e4f7)
- Handle multiple PDUs received by CFDP over socket (#73) [`76e4ae8`](https://github.com/NASA-AMMOS/AIT-DSN/commit/76e4ae831af62d50d0818bf12c6835625233a990)
- Issue #58 - Adding summary of CFDP to docs [`82899b7`](https://github.com/NASA-AMMOS/AIT-DSN/commit/82899b781423666c8c7f673b2392921f144124dc)
- Initial work on adding port communication (#73) [`369c4fd`](https://github.com/NASA-AMMOS/AIT-DSN/commit/369c4fd5ffc4b6b130cfd94200e5c4c74c4fe0f4)
- Add handling of multiple DSN hostnames with same port (#64) [`393c62c`](https://github.com/NASA-AMMOS/AIT-DSN/commit/393c62cdcfcd40d0fe9ce114d612896f5c1a2183)
- Prep for 1.1.0 release [`9a266b0`](https://github.com/NASA-AMMOS/AIT-DSN/commit/9a266b023368695fb540a598d8d44f88de222a8e)
- Updates to example scripts and docs (#64) [`c754115`](https://github.com/NASA-AMMOS/AIT-DSN/commit/c754115479fd1ad1a9569251252e8e6bd729ffb4)
- Variable name, docstring, comment, and formatting updates (#73) [`8f23f14`](https://github.com/NASA-AMMOS/AIT-DSN/commit/8f23f141e446bdae31484f40f926d823f37b3853)
- Addition of SLE docs (#71) [`b36f411`](https://github.com/NASA-AMMOS/AIT-DSN/commit/b36f411361db5d30eb3bde70bd5e4e4aab433f6a)
- Add example of creating CFDP entities to docs (#58) [`dbd8c16`](https://github.com/NASA-AMMOS/AIT-DSN/commit/dbd8c163fb49a1440fd4f765cd22c39229e6ec6c)
- Fixed bug [`2adc2d6`](https://github.com/NASA-AMMOS/AIT-DSN/commit/2adc2d6794e2b10315e30e46dda8c8cca27b652a)
- Add description of MIB config fields (#58) [`ddb980d`](https://github.com/NASA-AMMOS/AIT-DSN/commit/ddb980d9870773a7b1d421accfa11f79160f1088)
- Update CFDP to only connect to receiving socket if send socket not specified (#73) [`e7387bb`](https://github.com/NASA-AMMOS/AIT-DSN/commit/e7387bbd326628e446d83d8a7899ae678b26ac99)
- Add documentation on CFDP implementation, MIB config (#58) [`44d8168`](https://github.com/NASA-AMMOS/AIT-DSN/commit/44d81686e0e26ad2bbb48c4ff4611cf0b4948bcd)
- Add error handling for CFDP disconnect procedures (#73) [`bbe8d0f`](https://github.com/NASA-AMMOS/AIT-DSN/commit/bbe8d0ff804e47a06515dad9163aea998f6d1c17)
- Default to send/recv over same socket unless rcv sock specified in kwargs (#73) [`120b024`](https://github.com/NASA-AMMOS/AIT-DSN/commit/120b0245394357594ac6ad4c64aeaedba6703dda)
- Issue #58 - Update lib names/references in example receiver script [`f91c5ec`](https://github.com/NASA-AMMOS/AIT-DSN/commit/f91c5ecf3676643923f7ede77fdff6cf9437f307)
- Add CFDP documentation page (#58) [`f9b2e4e`](https://github.com/NASA-AMMOS/AIT-DSN/commit/f9b2e4efbfc442625a2a8b29a31cadcc46d7e340)
- Issue #76 - add option to pull hostname / port from config [`7a60787`](https://github.com/NASA-AMMOS/AIT-DSN/commit/7a607870321a18f0be40e7607739f056243377dc)
- Update CFDP disconnect error handling (#73) [`4b54ede`](https://github.com/NASA-AMMOS/AIT-DSN/commit/4b54edee796fc67f84941f57ff82b88cb1c41f36)
- Fixed bug [`17d72be`](https://github.com/NASA-AMMOS/AIT-DSN/commit/17d72be576ef4cd57fd29a9df3b1f8ddd7da69ef)
- Fixed bug [`c420858`](https://github.com/NASA-AMMOS/AIT-DSN/commit/c420858bf127b70cfc532ac69b0449d59e3b9ecb)
- Update .gitignore [`28b36e0`](https://github.com/NASA-AMMOS/AIT-DSN/commit/28b36e0a1cd7886166124be34b9c145db8bfadf8)
- Fixed bug [`0234d65`](https://github.com/NASA-AMMOS/AIT-DSN/commit/0234d659582d198bea470321d0c0ff5308b999c0)
- Fixed bug [`214a945`](https://github.com/NASA-AMMOS/AIT-DSN/commit/214a9450f4f21f7f9222e1c22646c41f1bc51fa3)
- Update link to AIT-CORE installation page from JPL GitHub to readthedocs (#58) [`701d192`](https://github.com/NASA-AMMOS/AIT-DSN/commit/701d19246d88159d88183e76a959fd828cff4cd7)
- Remove redundant gevent.sleeps from CFDP handlers (#73) [`d318942`](https://github.com/NASA-AMMOS/AIT-DSN/commit/d3189422c29a47b8137594d927d1d32e41b92da3)
- Fix typo in docs (#64) [`5de71de`](https://github.com/NASA-AMMOS/AIT-DSN/commit/5de71de9a9816cbe8c8ca60c3a6fbfc8ec1dc20c)
- Fixed bug [`720eb22`](https://github.com/NASA-AMMOS/AIT-DSN/commit/720eb22623fc4f2082aa475fa10c3de0eb1cbb4b)
- Remove extraneous logging (#64) [`ade6b91`](https://github.com/NASA-AMMOS/AIT-DSN/commit/ade6b9132075a1d50a31eb0ba981fd3a06cfa72c)
- Drop accidently committed pkl file [`27a12b6`](https://github.com/NASA-AMMOS/AIT-DSN/commit/27a12b60a1c9e621045dddde2830d6abc9fd5fbd)

## 1.0.0 - 2018-07-10

### Merged

- Issue #43 - Convert README.md to .rst and update setup.py in prep for PyPi release [`#44`](https://github.com/NASA-AMMOS/AIT-DSN/pull/44)
- Issue #39 Update FCLTU for V4 and V5 [`#41`](https://github.com/NASA-AMMOS/AIT-DSN/pull/41)
- Issue #40 - Fix credential microsecond handling [`#42`](https://github.com/NASA-AMMOS/AIT-DSN/pull/42)
- Issue #36 - Add build status badge to README [`#37`](https://github.com/NASA-AMMOS/AIT-DSN/pull/37)
- Issue #10 and #11 - Renaming updates [`#38`](https://github.com/NASA-AMMOS/AIT-DSN/pull/38)
- Issue #32 - Update README with contributing and community info [`#33`](https://github.com/NASA-AMMOS/AIT-DSN/pull/33)
- Issue #34 - Fix broken TravisCI build [`#35`](https://github.com/NASA-AMMOS/AIT-DSN/pull/35)
- Issue #19 - Add TravisCI config file [`#31`](https://github.com/NASA-AMMOS/AIT-DSN/pull/31)
- Issue #21 - Update CFDP config paths and check in directories [`#28`](https://github.com/NASA-AMMOS/AIT-DSN/pull/28)
- Issue #29 - Remove doc upgrade script [`#30`](https://github.com/NASA-AMMOS/AIT-DSN/pull/30)
- Issue #24 - Fix TMFrame header bit mask issues [`#27`](https://github.com/NASA-AMMOS/AIT-DSN/pull/27)
- Issue #23 - Update RCF example for version 4 support [`#26`](https://github.com/NASA-AMMOS/AIT-DSN/pull/26)
- Issue #22 - RAF example changes for version 4 support [`#25`](https://github.com/NASA-AMMOS/AIT-DSN/pull/25)
- Issue #17 - Add docs build badge to README [`#18`](https://github.com/NASA-AMMOS/AIT-DSN/pull/18)
- Issue #2 - Bump ait-core version and remove outdated dependency link [`#14`](https://github.com/NASA-AMMOS/AIT-DSN/pull/14)
- Issue #15 - Add CODEOWNERS file [`#16`](https://github.com/NASA-AMMOS/AIT-DSN/pull/16)
- Issue #8 - Publish docs to ReadTheDocs [`#9`](https://github.com/NASA-AMMOS/AIT-DSN/pull/9)
- Issue #3 - Update README [`#4`](https://github.com/NASA-AMMOS/AIT-DSN/pull/4)
- Issue #5 - Implement BIND-level authentication [`#6`](https://github.com/NASA-AMMOS/AIT-DSN/pull/6)

### Commits

- Issue #21 - Update CFDP config paths [`e7d25a8`](https://github.com/NASA-AMMOS/AIT-DSN/commit/e7d25a85f0f846f437e01e35fb3ed7697ac3af33)
- - remove peer auth level [`546e877`](https://github.com/NASA-AMMOS/AIT-DSN/commit/546e8779b76170638aeeb79bcc19e214af567795)
- Preparation for 1.0.0 release [`9a20dea`](https://github.com/NASA-AMMOS/AIT-DSN/commit/9a20deac789472b13d44a1d5a79fa80ace74e15a)
- - Update config paths and test setup/teardown [`819ed2c`](https://github.com/NASA-AMMOS/AIT-DSN/commit/819ed2cb72024c5946178098e2cac5a7f24f4855)
- Init .gitignore [`6e2f139`](https://github.com/NASA-AMMOS/AIT-DSN/commit/6e2f13948109c2246cde1614506c5be6abf99c5e)
- Issue #8 - Publish docs to RTD [`6cafde7`](https://github.com/NASA-AMMOS/AIT-DSN/commit/6cafde773fb3e757b99d4596c2924ec62d2bf3aa)
- Issue 36 - Add build status badge to README [`ed812e0`](https://github.com/NASA-AMMOS/AIT-DSN/commit/ed812e01ed837f0224a5be74b80906565b531e72)
- - fix bliss-core dependency [`364c479`](https://github.com/NASA-AMMOS/AIT-DSN/commit/364c479634e7909e79d4e63782e543e3834609eb)
