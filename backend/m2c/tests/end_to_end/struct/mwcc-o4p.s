.include "macros.inc"

.section .text  # 0x0 - 0x24

.global test
test:
/* 00000000 00000000  80 A3 00 00 */	lwz r5, 0(r3)
/* 00000004 00000004  80 03 00 04 */	lwz r0, 4(r3)
/* 00000008 00000008  7C 05 02 14 */	add r0, r5, r0
/* 0000000C 0000000C  90 03 00 04 */	stw r0, 4(r3)
/* 00000010 00000010  80 A3 00 00 */	lwz r5, 0(r3)
/* 00000014 00000014  80 03 00 04 */	lwz r0, 4(r3)
/* 00000018 00000018  90 A4 00 00 */	stw r5, 0(r4)
/* 0000001C 0000001C  90 04 00 04 */	stw r0, 4(r4)
/* 00000020 00000020  4E 80 00 20 */	blr 
