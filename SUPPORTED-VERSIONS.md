# Supported versions

## Formats

- **GB/GBC:** IPS is the expected patch format.
- **GBA:** UPS is the expected patch format.

IPS cannot reliably address a full 16 MiB GBA ROM, so this project does **not** describe GBA patches as IPS-only. Always match the format to the console family and verify the exact source checksum.

## LeafGreen example directory

`examples/leafgreen-color-patches/` contains the new-colors changelog and a clearly marked placeholder because the original new-colors UPS payload was not available in the supplied workspace. It is not a usable patch until the real binary is restored and independently checksum-verified.

The LeafGreen rotation patch UPS file was not on disk anymore; only its changelog was available. Therefore, the rotation patch is **not included** and is not claimed to be in this tree. Do not infer that a changelog is a patch.
