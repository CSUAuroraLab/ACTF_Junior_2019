#define _WIN32_WINNT 0x0500
#include <windows.h>
#include <iostream>
#include <stdio.h> 
int main()
{
HWND hWnd = GetConsoleWindow();
ShowWindow( hWnd, SW_HIDE );
while(1){
	Sleep(1000);
	FILE *tmp = fopen("C:\\Users\\JuniorCTF\\Videos\\F4Ig.txt","w");
	if (tmp != nullptr) { 
		fputs("ACTF{DoNothing_does_do_something}",tmp);
		fclose(tmp);
	}
;} 
return 0;
}
