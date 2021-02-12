DEMO_SRCS=IT8951.c miniGUI.c demo.c AsciiLib.c bmp.c
BMP2P_SRCS=IT8951.c miniGUI.c main.c AsciiLib.c bmp.c
GUI_SRCS=IT8951.c miniGUI.c gui.c AsciiLib.c bmp.c
CC=gcc
DEMO=IT8951
BMP2P=bmp2p
GUI=gui

$(DEMO):$(DEMO_SRCS)
	$(CC) -Wall $(DEMO_SRCS) -o $(DEMO) -lbcm2835
	
$(GUI):$(GUI_SRCS)
	$(CC) -Wall $(GUI_SRCS) -o $(GUI) -lbcm2835

$(BMP2P):$(BMP2P_SRCS)
	$(CC) -Wall $(BMP2P_SRCS) -o $(BMP2P) -lbcm2835

clean:
	rm -f $(DEMO) 
	rm -f $(BMP2P)
	rm -f $(GUI)

all: $(DEMO) $(BMP2P) $(GUI)