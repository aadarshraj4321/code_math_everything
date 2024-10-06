#include <iostream>
#include <cmath>
#include <cstring>  // For memset
#include <windows.h>  // For Sleep on Windows

// Constants for the screen size and donut properties
const int screenWidth = 80;
const int screenHeight = 40;
const float thetaSpacing = 0.07;
const float phiSpacing = 0.02;
const float R1 = 1.0;  // Radius of the circle of the donut
const float R2 = 2.0;  // Radius from the center of the hole to the middle of the tube
const float K2 = 5.0;  // Distance from the viewer to the donut
const float K1 = screenWidth * K2 * 3 / (8 * (R1 + R2));  // Scaling factor

// Function to clear the screen (platform-specific)
void clearScreen() {
    system("cls");  // On Windows, use "cls". For Linux or MacOS, use "clear".
}

int main() {
    float A = 0;  // Rotation angle A around the X-axis
    float B = 0;  // Rotation angle B around the Z-axis

    while (true) {
        char output[screenWidth * screenHeight];  // Output buffer
        float zBuffer[screenWidth * screenHeight];  // Z-buffer for depth calculations

        // Initialize buffers
        memset(output, ' ', screenWidth * screenHeight);
        memset(zBuffer, 0, screenWidth * screenHeight * sizeof(float));

        // Loop over the angles theta (around the Y-axis) and phi (around the X-axis)
        for (float theta = 0; theta < 2 * M_PI; theta += thetaSpacing) {
            for (float phi = 0; phi < 2 * M_PI; phi += phiSpacing) {
                // Calculate 3D coordinates of the point on the donut surface
                float cosTheta = cos(theta);
                float sinTheta = sin(theta);
                float cosPhi = cos(phi);
                float sinPhi = sin(phi);

                // Circle in the YZ plane
                float circleX = R2 + R1 * cosTheta;
                float circleY = R1 * sinTheta;

                // 3D coordinates after rotation
                float x = circleX * (cosB * cosPhi + sinA * sinB * sinPhi) - circleY * cosA * sinB;
                float y = circleX * (sinB * cosPhi - sinA * cosB * sinPhi) + circleY * cosA * cosB;
                float z = K2 + cosA * circleX * sinPhi + circleY * sinA;
                float ooz = 1 / z;  // Inverse of z for perspective

                // Project the 3D coordinates into 2D screen space
                int xp = (int)(screenWidth / 2 + K1 * ooz * x);
                int yp = (int)(screenHeight / 2 - K1 * ooz * y);

                // Calculate luminance (brightness) based on the angle of the surface
                float L = cosPhi * cosTheta * sinB - cosA * cosTheta * sinPhi - sinA * sinTheta + cosB * (cosA * sinTheta - cosTheta * sinA * sinPhi);
                
                if (L > 0) {
                    int index = xp + screenWidth * yp;
                    if (index >= 0 && index < screenWidth * screenHeight && ooz > zBuffer[index]) {
                        zBuffer[index] = ooz;

                        // Select a character based on the brightness
                        int luminance_index = L * 8;
                        const char* luminanceChars = ".,-~:;=!*#$@";
                        output[index] = luminanceChars[luminance_index > 0 ? luminance_index : 0];
                    }
                }
            }
        }

        // Display the frame
        clearScreen();
        for (int k = 0; k < screenWidth * screenHeight; k++) {
            putchar(k % screenWidth ? output[k] : '\n');
        }

        // Adjust the rotation angles
        A += 0.04;
        B += 0.02;

        // Control the speed of rotation
        Sleep(50);  // Sleep for 50ms between frames
    }

    return 0;
}
