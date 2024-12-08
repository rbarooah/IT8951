#include "IT8951.h"
#include <unistd.h> // For sleep function

#define MAX_RETRIES 3

int main (int argc, char *argv[])
{
    IT8951DevInfo devInfo;
    int retries = 0;
    while (retries < MAX_RETRIES)
    {
        if(IT8951_Init())
        {
            printf("IT8951_Init error, retrying... (%d/%d)\n", retries + 1, MAX_RETRIES);
            retries++;
            sleep(1); // Wait for a second before retrying
        }
        else
        {
            break; // Initialization successful
        }
    }

    if (retries == MAX_RETRIES)
    {
        printf("Failed to initialize IT8951 after %d attempts.\n", MAX_RETRIES);
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
