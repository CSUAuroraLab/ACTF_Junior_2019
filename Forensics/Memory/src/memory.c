#define _WIN32_WINNT 0x0500
#include <stdio.h>
#include <windows.h>

int main()
{
	HWND hWnd = GetConsoleWindow();
	ShowWindow(hWnd, SW_HIDE);
	char flag[] = "ACTF{How_to_inspect_memory?}";
	while(1){
		Sleep(100000);
	}
	return 0;
}
	
