#include "IT8951.h"

int main (int argc, char *argv[])
{
    if(IT8951_Init())
    {
        printf("IT8951_Init error \n");
        return 1;
    }

    if (argc != 4)
    {
        printf("Usage: %s <x> <y> <bmp_file>\n", argv[0]);
        return 1;
    }

    uint32_t x, y;
    sscanf(argv[1], "%d", &x);
    sscanf(argv[2], "%d", &y);

    IT8951_BMP_Example(x, y, argv[3]);

    IT8951_Cancel();

    return 0;
}
