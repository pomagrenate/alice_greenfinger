# ALICE GREENFINGERS - PHASE 3 CALLGRAPH BEHAVIOR MAP (STEP 3)

*Generated on 2026-09-01 17:25:02*

## SUBSYSTEM CALLGRAPH & FUNCTION DEPENDENCIES

| Function ID | RVA | Subsystem | Direct Callees | Callers | Globals Accessed | Evidence Level |
| --- | --- | --- | --- | --- | --- | --- |
| `FUN_00401000` | `0x00401000` | recovered/recovered_group_a.cpp | None | FUN_00401100, FUN_00468a72, FUN_00465a62 | DAT_004974ea, DAT_00497518 | **[VERIFIED]** |
| `FUN_00401070` | `0x00401070` | recovered/recovered_group_a.cpp | FUN_004111dc | FUN_0046943f, FUN_00401380, FUN_0046906d | None | **[VERIFIED]** |
| `FUN_004010a0` | `0x004010a0` | recovered/recovered_group_a.cpp | None | FUN_00401500, FUN_004279bf | None | **[VERIFIED]** |
| `FUN_004010e0` | `0x004010e0` | recovered/recovered_group_a.cpp | FUN_00401100 | FUN_00410390 | None | **[VERIFIED]** |
| `FUN_00401100` | `0x00401100` | recovered/recovered_group_a.cpp | FUN_0042afca, FUN_0040f190, FUN_0040e0c0 | FUN_004010e0 | DAT_004a95e8, DAT_004a8710, DAT_004974ec | **[VERIFIED]** |
| `FUN_00401250` | `0x00401250` | recovered/recovered_group_a.cpp | FUN_00401b80 | FUN_00401100 | DAT_004974ea, DAT_004974ec | **[VERIFIED]** |
| `FUN_004012f0` | `0x004012f0` | recovered/recovered_group_a.cpp | FUN_004111dc, FUN_004109e0, FUN_00402250 | FUN_00401cb0 | None | **[VERIFIED]** |
| `FUN_00401350` | `0x00401350` | recovered/recovered_group_a.cpp | FUN_004111dc | FUN_0046ea4a, FUN_0047679f, FUN_004689aa | None | **[VERIFIED]** |
| `FUN_00401380` | `0x00401380` | recovered/recovered_group_a.cpp | FUN_00401350, FUN_00401070 | FUN_004012f0, FUN_0046a6e1, FUN_0046f46d | None | **[VERIFIED]** |
| `FUN_004013a0` | `0x004013a0` | recovered/recovered_group_a.cpp | None | FUN_00402160, FUN_004026f0, FUN_00427e13 | None | **[VERIFIED]** |
| `FUN_004013c0` | `0x004013c0` | recovered/recovered_group_a.cpp | FUN_004013a0 | FUN_0046e785, FUN_0047469a, FUN_0046fba4 | None | **[VERIFIED]** |
| `FUN_00401400` | `0x00401400` | recovered/recovered_group_a.cpp | FUN_004111dc, FUN_00410640, FUN_00402250 | FUN_00401cb0, FUN_0047a3ee | None | **[VERIFIED]** |
| `FUN_00401460` | `0x00401460` | recovered/recovered_group_a.cpp | FUN_00402160, FUN_00401500, FUN_00402400 | FUN_0040d590 | None | **[VERIFIED]** |
| `FUN_00401500` | `0x00401500` | core/script_host.cpp | FUN_00427a7e, FUN_00410bf0, FUN_00427a84 | FUN_00401460 | DAT_004a912c, DAT_004a826c, DAT_004a90f8 | **[VERIFIED]** |
| `FUN_00401960` | `0x00401960` | recovered/recovered_group_a.cpp | FUN_00402250 | FUN_0040db70 | None | **[VERIFIED]** |
| `FUN_00401980` | `0x00401980` | recovered/recovered_group_a.cpp | FUN_00432929, FUN_00403e10 | FUN_0042a364, FUN_004733b7, FUN_00401f20 | DAT_004a7f34 | **[VERIFIED]** |
| `FUN_004019d0` | `0x004019d0` | recovered/recovered_group_a.cpp | FUN_00402250, FUN_004111dc | FUN_00468fe1, FUN_00402560, FUN_00410ba0 | None | **[VERIFIED]** |
| `FUN_00401a10` | `0x00401a10` | recovered/recovered_group_a.cpp | FUN_00402160, FUN_00403c30 | FUN_00401f20 | None | **[VERIFIED]** |
| `FUN_00401a50` | `0x00401a50` | recovered/recovered_group_a.cpp | FUN_0046ff4b, FUN_00442a67, FUN_00401b10 | FUN_004091e0, FUN_00401100, FUN_0042dec0 | DAT_004974f4, DAT_004974f0, DAT_004974ec | **[VERIFIED]** |
| `FUN_00401b10` | `0x00401b10` | recovered/recovered_group_a.cpp | None | FUN_00469ed9, FUN_0046b280, FUN_00402560 | None | **[VERIFIED]** |
| `FUN_00401b80` | `0x00401b80` | recovered/recovered_group_a.cpp | FUN_00402160, FUN_004013c0, FUN_0040d200 | FUN_0045fd57, FUN_0040e0c0, FUN_00462dfd | DAT_00497520, DAT_004974e9, DAT_004974ec | **[VERIFIED]** |
| `FUN_00401c90` | `0x00401c90` | recovered/recovered_group_a.cpp | FUN_004026f0 | FUN_00402560, FUN_0046001e, FUN_0045d53e | None | **[VERIFIED]** |
| `FUN_00401cb0` | `0x00401cb0` | recovered/recovered_group_a.cpp | FUN_004111dc, FUN_004012f0, FUN_0040e750 | FUN_00410a00 | DAT_00497518 | **[VERIFIED]** |
| `FUN_00401f20` | `0x00401f20` | recovered/recovered_group_a.cpp | FUN_00402560, FUN_0040e830, FUN_004111dc | FUN_0040d590 | DAT_004a7f6c, DAT_004a7f58, DAT_004a7f54 | **[VERIFIED]** |
| `FUN_00402160` | `0x00402160` | recovered/recovered_group_a.cpp | FUN_0040c600, FUN_00403bd0, FUN_004013a0 | FUN_00402560, FUN_00401460, FUN_0040db10 | None | **[VERIFIED]** |
| `FUN_00402250` | `0x00402250` | recovered/recovered_group_a.cpp | FUN_004111dc | FUN_00401960, FUN_00451b42, FUN_00402560 | None | **[VERIFIED]** |
| `FUN_00402280` | `0x00402280` | recovered/recovered_group_a.cpp | FUN_004431ad | FUN_00427e13, FUN_00402e0a, FUN_00427e43 | None | **[VERIFIED]** |
| `FUN_004022d0` | `0x004022d0` | recovered/recovered_group_a.cpp | FUN_0044c7c0, FUN_004111dc | FUN_00402400, FUN_0040f570 | None | **[VERIFIED]** |
| `FUN_00402400` | `0x00402400` | recovered/recovered_group_a.cpp | FUN_004022d0, FUN_004111dc, FUN_0040d530 | FUN_00401460 | DAT_004a912c, DAT_004a90fc, DAT_004a90f8 | **[VERIFIED]** |
| `FUN_00402560` | `0x00402560` | recovered/recovered_group_a.cpp | FUN_00402160, FUN_004026f0, FUN_0040d7c0 | FUN_00401f20 | None | **[VERIFIED]** |
| `FUN_004026f0` | `0x004026f0` | recovered/recovered_group_a.cpp | FUN_00446618, FUN_004013a0 | FUN_00410bc0, FUN_00402560, FUN_00427e13 | None | **[VERIFIED]** |
| `FUN_00402710` | `0x00402710` | recovered/recovered_group_a.cpp | FUN_004111dc | FUN_00427e13, FUN_00402e0a, FUN_004096a0 | None | **[VERIFIED]** |
| `FUN_00402780` | `0x00402780` | recovered/recovered_group_a.cpp | FUN_004111dc | FUN_00427e13, FUN_00402e0a, FUN_004096a0 | None | **[VERIFIED]** |
| `FUN_00402880` | `0x00402880` | recovered/recovered_group_a.cpp | FUN_004026f0, FUN_00402f80, FUN_004111dc | FUN_00402400, FUN_004813fa, FUN_0047e5aa | DAT_004a90f8 | **[VERIFIED]** |
| `FUN_00402e0a` | `0x00402e0a` | recovered/recovered_group_a.cpp | FUN_004026f0, FUN_00402f80, FUN_004111dc | FUN_00427f16, FUN_00402880, FUN_00427e13 | DAT_004a90f8 | **[VERIFIED]** |
| `FUN_00402f00` | `0x00402f00` | recovered/recovered_group_a.cpp | FUN_004111dc | FUN_00427e13, FUN_00402e0a, FUN_00402f80 | None | **[VERIFIED]** |
| `FUN_00402f80` | `0x00402f80` | recovered/recovered_group_a.cpp | FUN_00460879, FUN_00446618, FUN_00403020 | FUN_00427e13, FUN_00402e0a, FUN_00427e43 | None | **[VERIFIED]** |
| `FUN_00403020` | `0x00403020` | recovered/recovered_group_a.cpp | FUN_004013a0, FUN_00446618, FUN_00402f00 | FUN_0045ffc2, FUN_00402f80, FUN_00427e43 | None | **[VERIFIED]** |
| `FUN_00403060` | `0x00403060` | recovered/recovered_group_a.cpp | FUN_004026f0, FUN_00402710, FUN_00403020 | FUN_00427e13, FUN_00402e0a, FUN_00427e43 | DAT_004a90ec | **[VERIFIED]** |
| `FUN_004031b0` | `0x004031b0` | recovered/recovered_group_a.cpp | FUN_00432cc2, FUN_004273df, FUN_00402710 | FUN_00427e13, FUN_00402e0a, FUN_00427e43 | None | **[VERIFIED]** |
| `FUN_00403350` | `0x00403350` | recovered/recovered_group_a.cpp | None | FUN_00427e13, FUN_0045ffc2, FUN_00402e0a | None | **[VERIFIED]** |
| `FUN_004033c0` | `0x004033c0` | resources/resource_loader.cpp | FUN_004026f0, FUN_004111dc, FUN_004037a0 | FUN_0040f570, FUN_00403a20 | DAT_004a9538 | **[VERIFIED]** |
| `FUN_0040373c` | `0x0040373c` | recovered/recovered_group_a.cpp | FUN_004111dc, FUN_0040da20, FUN_00402250 | FUN_004282d6, FUN_004033c0 | DAT_004a9538 | **[VERIFIED]** |
| `FUN_004037a0` | `0x004037a0` | recovered/recovered_group_a.cpp | FUN_004111dc, FUN_00443df9, FUN_0040df90 | FUN_0046e9ce, FUN_004282d6, FUN_00468961 | None | **[VERIFIED]** |
| `FUN_00403910` | `0x00403910` | recovered/recovered_group_a.cpp | FUN_0040e050 | FUN_00443e69, FUN_004037a0, FUN_00443ee5 | None | **[VERIFIED]** |
| `FUN_004039a0` | `0x004039a0` | recovered/recovered_group_a.cpp | None | FUN_004282d6, FUN_004033c0 | None | **[VERIFIED]** |
| `FUN_00403a20` | `0x00403a20` | recovered/recovered_group_a.cpp | FUN_00444bfc, FUN_00410160, FUN_004111dc | FUN_004282d6, FUN_004033c0 | None | **[VERIFIED]** |
| `FUN_00403a50` | `0x00403a50` | recovered/recovered_group_a.cpp | FUN_004111dc | FUN_004282d6, FUN_0040d590, FUN_004033c0 | None | **[VERIFIED]** |
| `FUN_00403af0` | `0x00403af0` | recovered/recovered_group_a.cpp | FUN_004111dc, FUN_00403b70, FUN_00403350 | FUN_0046ea4a, FUN_0047679f, FUN_004033c0 | None | **[VERIFIED]** |
| `FUN_00403b70` | `0x00403b70` | recovered/recovered_group_a.cpp | FUN_0040c600, FUN_00446618, FUN_004013a0 | FUN_0046afc3, FUN_00474837, FUN_00460a29 | None | **[VERIFIED]** |
| `FUN_00403bd0` | `0x00403bd0` | recovered/recovered_group_a.cpp | FUN_004111dc | FUN_00402160, FUN_00403b70, FUN_00461465 | None | **[VERIFIED]** |
| `FUN_00403c30` | `0x00403c30` | recovered/recovered_group_a.cpp | FUN_00403bd0 | FUN_00403e10, FUN_0040d860, FUN_0040e0a0 | None | **[VERIFIED]** |
| `FUN_00403c90` | `0x00403c90` | recovered/recovered_group_a.cpp | FUN_00403cc0 | FUN_0046b280, FUN_00451b42, FUN_00466b71 | None | **[VERIFIED]** |
| `FUN_00403cc0` | `0x00403cc0` | recovered/recovered_group_a.cpp | None | FUN_0048127d, FUN_0042a364, FUN_004731e1 | None | **[VERIFIED]** |
| `FUN_00403cd0` | `0x00403cd0` | recovered/recovered_group_a.cpp | FUN_00403cc0, FUN_00408f40 | FUN_0046b280, FUN_0048127d, FUN_00466faf | None | **[VERIFIED]** |
| `FUN_00403d10` | `0x00403d10` | recovered/recovered_group_a.cpp | FUN_00403c90, FUN_00408f40, FUN_00404170 | FUN_00408cc0 | None | **[VERIFIED]** |
| `FUN_00403d80` | `0x00403d80` | recovered/recovered_group_a.cpp | FUN_004431ad | FUN_00467ac4, FUN_00452f37, FUN_004531b1 | None | **[VERIFIED]** |
| `FUN_00403da0` | `0x00403da0` | recovered/recovered_group_a.cpp | FUN_0040bcc0, FUN_00403ea0 | FUN_00403e10, FUN_0045ef07 | None | **[VERIFIED]** |
| `FUN_00403e10` | `0x00403e10` | recovered/recovered_group_a.cpp | FUN_00408e80, FUN_00403c30, FUN_00403da0 | FUN_004096a0, FUN_0042a364, FUN_00401980 | None | **[VERIFIED]** |
| `FUN_00403ea0` | `0x00403ea0` | recovered/recovered_group_a.cpp | FUN_0040bc70 | FUN_004534c0, FUN_00403da0, FUN_0040c2c0 | DAT_004a95dc, DAT_004a95c4, DAT_004a95e0 | **[VERIFIED]** |
| `FUN_00404100` | `0x00404100` | recovered/recovered_group_a.cpp | FUN_00404170 | None | None | **[VERIFIED]** |
| `FUN_00404170` | `0x00404170` | events/event_dispatcher.cpp | FUN_0046b280, FUN_0047a330, FUN_0045abcf | FUN_00404100, FUN_0040c7f0, FUN_00403d10 | DAT_0048a904, DAT_004893c0, DAT_00488ec4 | **[VERIFIED]** |
| `FUN_00408cc0` | `0x00408cc0` | recovered/recovered_group_a.cpp | FUN_00408d90, FUN_004111dc, FUN_00403d10 | FUN_0042e124, FUN_0042b1a0, FUN_0042dec0 | None | **[VERIFIED]** |
| `FUN_00408d90` | `0x00408d90` | recovered/recovered_group_a.cpp | FUN_0040bec0, FUN_0040ba10, FUN_0045e737 | FUN_00408cc0, FUN_0047dcbb | None | **[VERIFIED]** |
| `FUN_00408e80` | `0x00408e80` | recovered/recovered_group_a.cpp | FUN_004111dc, FUN_0044b8a3, FUN_00470870 | FUN_0047390f, FUN_0048127d, FUN_0042a364 | None | **[VERIFIED]** |
| `FUN_00408f40` | `0x00408f40` | recovered/recovered_group_a.cpp | FUN_0044b3d9, FUN_0040e270, FUN_004111dc | FUN_00451b42, FUN_0047a330, FUN_00462fc8 | None | **[VERIFIED]** |
| `FUN_00408fc0` | `0x00408fc0` | recovered/recovered_group_a.cpp | FUN_00451b42, FUN_004111dc, FUN_00452f37 | FUN_004091e0, FUN_0042dec0, FUN_0042e124 | DAT_004a7f24, DAT_004a7f34 | **[VERIFIED]** |
| `FUN_004091b0` | `0x004091b0` | recovered/recovered_group_a.cpp | FUN_0040ba10, FUN_0040bc70, FUN_00401980 | FUN_004091e0, FUN_0042dec0, FUN_0042e124 | DAT_004a9138, DAT_004a7f04, DAT_004a7f34 | **[VERIFIED]** |
| `FUN_004091e0` | `0x004091e0` | recovered/recovered_group_a.cpp | FUN_0040d150, FUN_004521b3, FUN_004111dc | FUN_00481511, FUN_004811c5, FUN_0048156a | DAT_004a954c, DAT_004974e2, DAT_004974ec | **[VERIFIED]** |
| `FUN_004096a0` | `0x004096a0` | engine/game_loop.cpp | FUN_0044b3d9, FUN_0040e1c0, FUN_0047390f | FUN_0042e124, FUN_0047e5aa, FUN_0042b1a0 | DAT_004a7f3c, DAT_004a7f3d, DAT_004a95dc | **[VERIFIED]** |
| `FUN_0040a780` | `0x0040a780` | recovered/recovered_group_a.cpp | FUN_00451b42, FUN_0044b3d9, FUN_004530c9 | FUN_00408d90, FUN_0042a364, FUN_0040afa0 | DAT_004a95f8, DAT_004a95f0 | **[VERIFIED]** |
| `FUN_0040afa0` | `0x0040afa0` | recovered/recovered_group_a.cpp | FUN_00467c5c, FUN_0040c650, FUN_0044b3d9 | FUN_004091e0, FUN_0042dec0, FUN_0042e124 | DAT_004921f4, DAT_004921e8 | **[VERIFIED]** |
| `FUN_0040b400` | `0x0040b400` | recovered/recovered_group_a.cpp | FUN_0044b3d9, FUN_0040e270, FUN_004111dc | FUN_004096a0, FUN_0042a364, FUN_0040e2a0 | None | **[VERIFIED]** |
| `FUN_0040b510` | `0x0040b510` | recovered/recovered_group_a.cpp | FUN_0040c650, FUN_0040baa0, FUN_004431ad | FUN_0040bd20, FUN_0040b5f0, FUN_0040afa0 | None | **[VERIFIED]** |
| `FUN_0040b5f0` | `0x0040b5f0` | recovered/recovered_group_a.cpp | FUN_00442f36, FUN_00467c5c, FUN_004530c9 | FUN_0042b1a0, FUN_0040a780, FUN_0042bac5 | None | **[VERIFIED]** |
| `FUN_0040b910` | `0x0040b910` | recovered/recovered_group_a.cpp | FUN_004111dc, FUN_0044b911, FUN_00408f40 | FUN_0040b5f0 | None | **[VERIFIED]** |
| `FUN_0040b960` | `0x0040b960` | recovered/recovered_group_a.cpp | FUN_004111dc, FUN_00470870, FUN_0044b8a3 | FUN_00479714, FUN_00470e55, FUN_0040ba10 | None | **[VERIFIED]** |
| `FUN_0040ba10` | `0x0040ba10` | recovered/recovered_group_a.cpp | FUN_004111dc, FUN_0040b960 | FUN_00408d90, FUN_004096a0, FUN_0047b954 | None | **[VERIFIED]** |
| `FUN_0040baa0` | `0x0040baa0` | recovered/recovered_group_a.cpp | FUN_00432cc2 | FUN_00457451, FUN_00452f37, FUN_0040bb80 | None | **[VERIFIED]** |
| `FUN_0040bb00` | `0x0040bb00` | recovered/recovered_group_a.cpp | FUN_0040baa0, FUN_004431ad, FUN_00408f40 | FUN_0042c504, FUN_0040b5f0, FUN_00408fc0 | None | **[VERIFIED]** |
| `FUN_0040bb80` | `0x0040bb80` | recovered/recovered_group_a.cpp | FUN_0040baa0, FUN_004431ad, FUN_00452f05 | FUN_0042c504, FUN_0040b5f0, FUN_0047f135 | None | **[VERIFIED]** |
| `FUN_0040bc10` | `0x0040bc10` | recovered/recovered_group_a.cpp | FUN_0040b960, FUN_00408e80 | FUN_0042b1a0, FUN_0040a780, FUN_0042bac5 | None | **[VERIFIED]** |
| `FUN_0040bc70` | `0x0040bc70` | recovered/recovered_group_a.cpp | None | FUN_0046b280, FUN_00451b42, FUN_004526ec | None | **[VERIFIED]** |
| `FUN_0040bcc0` | `0x0040bcc0` | recovered/recovered_group_a.cpp | FUN_0040d260 | FUN_004096a0, FUN_00457368, FUN_00403da0 | None | **[VERIFIED]** |
| `FUN_0040bd20` | `0x0040bd20` | recovered/recovered_group_a.cpp | FUN_004531b1, FUN_0045e987, FUN_0040b510 | FUN_0042c504, FUN_0040b5f0, FUN_00408fc0 | None | **[VERIFIED]** |
| `FUN_0040bd50` | `0x0040bd50` | recovered/recovered_group_a.cpp | FUN_0040bd80, FUN_00402250, FUN_0040e0a0 | FUN_0046ec4e, FUN_0046993e, FUN_0040bd20 | None | **[VERIFIED]** |
| `FUN_0040bd80` | `0x0040bd80` | recovered/recovered_group_a.cpp | FUN_00402f00 | FUN_0046a6e1, FUN_0040bd50 | None | **[VERIFIED]** |
| `FUN_0040be70` | `0x0040be70` | recovered/recovered_group_a.cpp | FUN_004111dc | FUN_00401500, FUN_0042b1a0, FUN_0042bac5 | None | **[VERIFIED]** |
| `FUN_0040bec0` | `0x0040bec0` | recovered/recovered_group_a.cpp | FUN_00427ad0 | FUN_00408d90 | None | **[VERIFIED]** |
| `FUN_0040bf20` | `0x0040bf20` | recovered/recovered_group_a.cpp | FUN_00467c5c, FUN_00451b42, FUN_0040c650 | FUN_0040afa0 | DAT_004a912c, DAT_004a90f8 | **[VERIFIED]** |
| `FUN_0040c1f0` | `0x0040c1f0` | recovered/recovered_group_a.cpp | FUN_00408e80, FUN_0040c2c0, FUN_00472f47 | FUN_0042b1a0, FUN_0047e4e3, FUN_0040a780 | None | **[VERIFIED]** |
| `FUN_0040c2c0` | `0x0040c2c0` | recovered/recovered_group_a.cpp | FUN_00432929, FUN_00403ea0, FUN_004534e3 | FUN_0040bf20, FUN_00480a8d, FUN_004805bf | DAT_004a7f2c, DAT_004a7f24, DAT_004a7f34 | **[VERIFIED]** |
| `FUN_0040c360` | `0x0040c360` | recovered/recovered_group_a.cpp | FUN_00401b10, FUN_0040bc70 | None | DAT_004a8748, DAT_004a873c, DAT_004a88bc | **[VERIFIED]** |
| `FUN_0040c4c0` | `0x0040c4c0` | recovered/recovered_group_a.cpp | None | FUN_0040b5f0 | None | **[VERIFIED]** |
| `FUN_0040c4e0` | `0x0040c4e0` | recovered/recovered_group_a.cpp | FUN_0040c650, FUN_0040e950, FUN_0040cf00 | FUN_0040bf20, FUN_004096a0, FUN_0040c1f0 | None | **[VERIFIED]** |
| `FUN_0040c600` | `0x0040c600` | recovered/recovered_group_a.cpp | FUN_004026f0 | FUN_0045fa41, FUN_0046001e, FUN_00468f70 | None | **[VERIFIED]** |
| `FUN_0040c620` | `0x0040c620` | recovered/recovered_group_a.cpp | None | FUN_004091e0, FUN_0042dec0, FUN_0042e124 | None | **[VERIFIED]** |
| `FUN_0040c650` | `0x0040c650` | recovered/recovered_group_a.cpp | FUN_00425a80, FUN_00413190, FUN_00432bc3 | FUN_0046b280, FUN_00466b71, FUN_00459b7c | None | **[VERIFIED]** |
| `FUN_0040c670` | `0x0040c670` | recovered/recovered_group_a.cpp | FUN_0040c650, FUN_0040baa0, FUN_00445bc3 | FUN_0040bf20, FUN_00467c5c, FUN_0040b5f0 | DAT_004921e8 | **[VERIFIED]** |
| `FUN_0040c6e0` | `0x0040c6e0` | recovered/recovered_group_a.cpp | FUN_004259eb, FUN_0040c650, FUN_0040baa0 | FUN_00404170 | None | **[VERIFIED]** |
