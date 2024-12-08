DEMO_SRCS=IT8951.c miniGUI.c demo.c AsciiLib.c bmp.c
BMP2P_SRCS=IT8951.c miniGUI.c main.c AsciiLib.c bmp.c
GUI_SRCS=IT8951.c miniGUI.c gui.c AsciiLib.c bmp.c
RENDER_BMP_SRCS=IT8951.c miniGUI.c render_bmp.c AsciiLib.c bmp.c
CC=gcc
DEMO=IT8951
BMP2P=bmp2p
GUI=gui
RENDER_BMP=render_bmp

$(DEMO):$(DEMO_SRCS)
	$(CC) -Wall $(DEMO_SRCS) -o $(DEMO) -lbcm2835
	
$(GUI):$(GUI_SRCS)
	$(CC) -Wall $(GUI_SRCS) -o $(GUI) -lbcm2835

$(BMP2P):$(BMP2P_SRCS)
	$(CC) -Wall $(BMP2P_SRCS) -o $(BMP2P) -lbcm2835

$(RENDER_BMP):$(RENDER_BMP_SRCS)
	$(CC) -Wall $(RENDER_BMP_SRCS) -o $(RENDER_BMP) -lbcm2835

clean:
	rm -f $(DEMO) \
	      $(BMP2P) \
	      $(GUI) \
	      $(RENDER_BMP)

all: $(DEMO) $(BMP2P) $(GUI) $(RENDER_BMP)