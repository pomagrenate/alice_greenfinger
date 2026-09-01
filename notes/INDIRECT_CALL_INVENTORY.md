# ALICE GREENFINGERS - EXHAUSTIVE INDIRECT CALL INVENTORY (STEP 3)

*Generated on 2026-09-01 13:19:59*

## INDIRECT CALL METRICS SUMMARY
- **Total Indirect Call Sites Discovered:** 80
- **Functions Containing Indirect Calls:** 48

## INDIRECT CALL DETAIL TABLE

| Containing Function | Address RVA | Call Expression | Target Memory Source | Candidate Targets | Resolution Type | Evidence Classification |
| --- | --- | --- | --- | --- | --- | --- |
| `FUN_0040d6b0` | `0x0040d6b0` | `(*pcVar2)()` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0040e500` | `0x0040e500` | `(*pcVar3)(pvVar2,piVar4)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0040e500` | `0x0040e500` | `(*pcVar3)(p_Var5)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0040e500` | `0x0040e500` | `(*pcVar3)(local_14)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_004102b0` | `0x004102b0` | `(*local_8->lpVtbl->Free)(local_8,local_10)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_004102b0` | `0x004102b0` | `(*local_8->lpVtbl->Release)(local_8)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_004102b0` | `0x004102b0` | `(*local_c->lpVtbl->Release)(local_c)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_004102b0` | `0x004102b0` | `(*local_c->lpVtbl->ParseDisplayName)
             ` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_00410c20` | `0x00410c20` | `(*(code *)param_4)()` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_00410ca0` | `0x00410ca0` | `(*unaff_EBX)()` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_00410cfc` | `0x00410cfc` | `(*(code *)*param_3)()` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_00410de2` | `0x00410de2` | `(*(code *)0xbc614e)(0xbc614e)` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_0041787c` | `0x0041787c` | `(*(code *)PTR_FUN_00490000)(0)` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_00417ef8` | `0x00417ef8` | `(*(code *)PTR_FUN_00490004)(DAT_004966c8)` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_00417ef8` | `0x00417ef8` | `(*UNRECOVERED_JUMPTABLE)()` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_00418337` | `0x00418337` | `(*(code *)PTR_FUN_00490000)(terminate)` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_0041839d` | `0x0041839d` | `(*(code *)PTR_FUN_00490004)(DAT_0049682c)` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_00419192` | `0x00419192` | `(*(code *)PTR_FUN_00490004)
                      ` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_00419192` | `0x00419192` | `(*pcVar8)()` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_00419192` | `0x00419192` | `(*(code *)puVar4)()` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_0041b91b` | `0x0041b91b` | `(*(code *)puVar8)(PTR_LAB_00490d30,pwVar12,&local_` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_0041b91b` | `0x0041b91b` | `(*(code *)puVar8)(PTR_LAB_00490d34,pwVar12,&local_` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_0041b91b` | `0x0041b91b` | `(*pcVar6)()` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0041b91b` | `0x0041b91b` | `(*(code *)PTR_FUN_00490004)
                      ` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_00422d54` | `0x00422d54` | `(*in_EAX)()` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0042e158` | `0x0042e158` | `(*unaff_ESI)(&stack0x0000013c,0,0,0)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0042eb69` | `0x0042eb69` | `(*(code *)PTR_FUN_00491490)(_Size + 1)` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_0043009d` | `0x0043009d` | `(*local_c->lpVtbl->Release)(local_c)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_00434b02` | `0x00434b02` | `(*pFVar5)(&param_1,&param_2)` | `this / param_1 + Offset` | `VTable Method Array` | `VTABLE_DISPATCH` | **[HIGH-CONFIDENCE]** |
| `FUN_004357b7` | `0x004357b7` | `(*pcVar4)(pHVar3,10,Y,param_3 + -0x14,local_14.bot` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_004357b7` | `0x004357b7` | `(*pcVar4)(pHVar3,((int)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_004357b7` | `0x004357b7` | `(*pcVar4)(pHVar3,10,10,param_3 + -0x14,Y + -5,0)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_00437262` | `0x00437262` | `(*DAT_004a7f20)(&local_a8)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_00437262` | `0x00437262` | `(*(code *)PTR_FUN_00491490)(local_30 * 4)` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_00437262` | `0x00437262` | `(*DAT_004a7f20)(&local_78)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_00437262` | `0x00437262` | `(*(code *)PTR_FUN_00491494)(local_34)` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_00441c7b` | `0x00441c7b` | `(*pcVar5)(pHVar7,pWVar8,uVar3,uVar4)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_004457c1` | `0x004457c1` | `(*pcVar1)()` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_00445e52` | `0x00445e52` | `(*pcVar3)(0)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0044663b` | `0x0044663b` | `(*(code *)PTR_FUN_00491494)(local_bc)` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_0044663b` | `0x0044663b` | `(*(code *)PTR_FUN_00491490)(iVar9 * 4)` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_0044786a` | `0x0044786a` | `(*pcVar1)()` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_004491b9` | `0x004491b9` | `(*pcVar10)(pHVar13,local_18,0,local_2108)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_004491b9` | `0x004491b9` | `(*pcVar10)(pHVar13,local_10,0xffffffff,param_3)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_004491b9` | `0x004491b9` | `(*pcVar10)(pHVar13,local_c,iVar5,0)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0044cb87` | `0x0044cb87` | `(*param_3->lpVtbl->QueryInterface)(param_3,(IID *)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0044cb87` | `0x0044cb87` | `(*param_3->lpVtbl->Release)(param_3)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0044cc51` | `0x0044cc51` | `(*pcVar1)()` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_00451d2b` | `0x00451d2b` | `(*pcVar1)(piVar6,0,0x800,&param_1)` | `this / param_1 + Offset` | `VTable Method Array` | `VTABLE_DISPATCH` | **[HIGH-CONFIDENCE]** |
| `FUN_004542ed` | `0x004542ed` | `(*param_5)(param_3,_Memory,&local_c,param_6,param_` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_004542ed` | `0x004542ed` | `(*local_10)(local_c)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_00455a89` | `0x00455a89` | `(*pcVar15)(pHVar4,0xe,0,0)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_004565b2` | `0x004565b2` | `(*pcVar9)(*(undefined4 *)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_004580c4` | `0x004580c4` | `(*pcVar7)(uVar9,uVar10,ppHVar11)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_004594e9` | `0x004594e9` | `(*local_8->lpVtbl->Release)(local_8)` | `AutoIt / Script Handler Pointer` | `FUN_00404170 Event Dispatcher` | `SCRIPT_DISPATCH` | **[VERIFIED]** |
| `FUN_0045da73` | `0x0045da73` | `(*pcVar6)(local_38[0],0,0,0)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0045dc4c` | `0x0045dc4c` | `(*local_8->lpVtbl->Free)(local_8,pidl)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0045dc4c` | `0x0045dc4c` | `(*local_8->lpVtbl->Release)(local_8)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0045e332` | `0x0045e332` | `(*pcVar2)(0,0,0,local_210)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_00462237` | `0x00462237` | `(*(code *)PTR_FUN_00491490)(pbVar3)` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_00462237` | `0x00462237` | `(*(code *)PTR_FUN_00491494)(puVar6)` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_00465489` | `0x00465489` | `(*pcVar5)()` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_00465489` | `0x00465489` | `(*pcVar5)(iVar3,uVar7,puVar8,uVar6)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_00465489` | `0x00465489` | `(*pcVar5)(uStack_240)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_00468f70` | `0x00468f70` | `(*(code *)PTR_FUN_00491494)(piVar2)` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_0046b10f` | `0x0046b10f` | `(*(code *)param_5)()` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_0046b10f` | `0x0046b10f` | `(*(code *)param_6)()` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_0046b10f` | `0x0046b10f` | `(*(code *)param_4)(piVar1)` | `Global Callback Pointer Table` | `Subsystem Event Handlers` | `CALLBACK_TABLE` | **[HIGH-CONFIDENCE]** |
| `FUN_0046b280` | `0x0046b280` | `(*pcVar1)(local_58)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0046b6ab` | `0x0046b6ab` | `(*pcVar4)(hKey,local_38[0],local_5c,uVar2)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0046beb2` | `0x0046beb2` | `(*pcVar2)(local_50)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0046cef3` | `0x0046cef3` | `(*local_78->lpVtbl->Release)(local_78)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0046cef3` | `0x0046cef3` | `(*This->lpVtbl->Release)(This)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0046cef3` | `0x0046cef3` | `(*local_6c->lpVtbl->QueryInterface)(local_6c,(IID ` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0046cef3` | `0x0046cef3` | `(*local_70->lpVtbl->BindToObject)
                ` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0047144e` | `0x0047144e` | `(*pcVar12)(pHVar6,0x113f,0,&uStack_70)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0047144e` | `0x0047144e` | `(*pcVar12)(pHVar6,0x113e,0,&uStack_70)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0047144e` | `0x0047144e` | `(*pcVar12)(pHVar6,0x1015,local_14,param_4)` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_004720db` | `0x004720db` | `(*pcVar8)()` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
| `FUN_0047974b` | `0x0047974b` | `(*pcVar11)(piVar2,local_c,&DAT_00482a18,0x800,para` | `Stack / Indirect Register` | `Unknown / Unverified` | `UNRESOLVED` | **[UNRESOLVED]** |
