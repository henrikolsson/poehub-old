# GGPK 

## Header
Version U32 | Identifier 'GGPK' | Unknown U32 | Root offset U64 | Unknown U64

## PDIR
Name length (characters) U32 | Child count U32 | Checksum 0x20 bytes | UTF-16 c-string name

### Children
Checksum U32 | Child offset U64

## FILE
Name length (Characters) U32 | Checksum 0x20 bytes  | UTF-16 c-string name

# DAT

## Header
Number of records U32

## Records
...

## Data section

Magic U64 (0xBBbbBBbbBBbbBBbb) | data pointed from records follows
