// Win32 Tutorial No.1
// Alan Baylis 2004

#include <windows.h>
#include <iostream>
#include "resource.h"

const char ClassName[] = "MainWindowClass";

LRESULT CALLBACK WndProc( HWND    hWnd,
                          UINT    Msg,
                          WPARAM  wParam,          
                          LPARAM  lParam )
{
	switch (Msg)
	{
        case WM_CLOSE:
            DestroyWindow(hWnd);
        break;

        case WM_DESTROY:
			PostQuitMessage(0);
        break;

		default:
			return (DefWindowProc(hWnd, Msg, wParam, lParam));
	}

    return 0;
}

INT WINAPI WinMain(	HINSTANCE  hInstance,
			        HINSTANCE  hPrevInstance,
			        LPSTR      lpCmdLine,
			        INT	       nCmdShow )
{
    WNDCLASSEX    wc;

    wc.cbSize           = sizeof(WNDCLASSEX);
	wc.style		    = 0;
	wc.lpfnWndProc		= (WNDPROC)WndProc;
	wc.cbClsExtra		= 0;
	wc.cbWndExtra		= 0;
	wc.hInstance		= hInstance;
    wc.hIcon            = LoadIcon(hInstance, MAKEINTRESOURCE(IDI_ICON));
    wc.hIconSm          = LoadIcon(hInstance, MAKEINTRESOURCE(IDI_ICON));
	wc.hCursor		    = LoadCursor(NULL, IDC_ARROW);
	wc.hbrBackground	= (HBRUSH)(COLOR_WINDOW + 1);
	wc.lpszMenuName		= NULL;
	wc.lpszClassName    = ClassName;

	if (!RegisterClassEx(&wc))
	{
		MessageBox(NULL, "Failed To Register The Window Class.", "Error", MB_OK | MB_ICONERROR);
		return 0;
	}

    HWND    hWnd;

	hWnd = CreateWindowEx(
    WS_EX_CLIENTEDGE,
	ClassName,
	"Simple Windows",
    WS_OVERLAPPEDWINDOW,
	CW_USEDEFAULT,
    CW_USEDEFAULT,
	400,
    120,
	NULL,
	NULL,
	hInstance,
	NULL);

	if (!hWnd)
	{
		MessageBox(NULL, "Window Creation Failed.", "Error", MB_OK | MB_ICONERROR);
		return 0;
	}
	
	std::cout<<"ACTF{Something_Behind_seemed_harmless_program}"<<std::endl;
	ShowWindow(hWnd, SW_SHOW);
	UpdateWindow(hWnd);

    MSG    Msg;

    while (GetMessage(&Msg, NULL, 0, 0))
    {
        TranslateMessage(&Msg);
        DispatchMessage(&Msg);
    }

    return Msg.wParam;
}
