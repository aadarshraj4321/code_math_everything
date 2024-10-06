#include <iostream>
#include <cmath>
#include <windows.h>   // For Sleep on Windows
#include <vector>

const int width = 80;    // Terminal width
const int height = 40;   // Terminal height
const float aspect = (float)width / height;
const float fov = 3.14159 / 2.0; // Field of view (90 degrees)

// A 3D vector structure
struct Vec3D {
    float x, y, z;
};

// 8 vertices of a cube
std::vector<Vec3D> cubeVertices = {
    {-1, -1, -1}, {1, -1, -1}, {1, 1, -1}, {-1, 1, -1},
    {-1, -1,  1}, {1, -1,  1}, {1, 1,  1}, {-1, 1,  1}
};

// 12 edges of the cube defined by pairs of vertex indices
std::vector<std::pair<int, int>> cubeEdges = {
    {0, 1}, {1, 2}, {2, 3}, {3, 0}, // Back face
    {4, 5}, {5, 6}, {6, 7}, {7, 4}, // Front face
    {0, 4}, {1, 5}, {2, 6}, {3, 7}  // Connecting edges
};

// Rotation functions (X, Y, Z axis)
void rotateX(Vec3D &vertex, float angle) {
    float cosA = cos(angle);
    float sinA = sin(angle);
    float y = vertex.y * cosA - vertex.z * sinA;
    float z = vertex.y * sinA + vertex.z * cosA;
    vertex.y = y;
    vertex.z = z;
}

void rotateY(Vec3D &vertex, float angle) {
    float cosA = cos(angle);
    float sinA = sin(angle);
    float x = vertex.x * cosA + vertex.z * sinA;
    float z = -vertex.x * sinA + vertex.z * cosA;
    vertex.x = x;
    vertex.z = z;
}

void rotateZ(Vec3D &vertex, float angle) {
    float cosA = cos(angle);
    float sinA = sin(angle);
    float x = vertex.x * cosA - vertex.y * sinA;
    float y = vertex.x * sinA + vertex.y * cosA;
    vertex.x = x;
    vertex.y = y;
}

// Draw a line between two points using a simple line-drawing algorithm
void drawLine(int x0, int y0, int x1, int y1, std::vector<std::string> &buffer) {
    int dx = std::abs(x1 - x0), sx = x0 < x1 ? 1 : -1;
    int dy = -std::abs(y1 - y0), sy = y0 < y1 ? 1 : -1;
    int err = dx + dy, e2;

    while (true) {
        if (x0 >= 0 && x0 < width && y0 >= 0 && y0 < height)
            buffer[y0][x0] = '#';  // Draw point
        if (x0 == x1 && y0 == y1) break;
        e2 = 2 * err;
        if (e2 >= dy) { err += dy; x0 += sx; }
        if (e2 <= dx) { err += dx; y0 += sy; }
    }
}

// Function to clear the terminal screen (with double buffering)
void clearScreen() {
    // Using system clear (platform-specific)
    system("cls");  // For Windows, change to "clear" for Linux/Unix
}

// Function to project the 3D cube onto 2D screen and render it
void projectAndRender(const std::vector<Vec3D> &vertices, const std::vector<std::pair<int, int>> &edges) {
    // Double buffering for smooth rendering
    std::vector<std::string> buffer(height, std::string(width, ' '));

    for (const auto &edge : edges) {
        Vec3D v1 = vertices[edge.first];
        Vec3D v2 = vertices[edge.second];

        // Project both vertices of the edge to 2D screen space
        float zInv1 = 1.0f / (v1.z + 4);  // Move cube slightly into screen
        int px1 = (int)((v1.x * zInv1 * aspect + 1) * width / 2);
        int py1 = (int)((v1.y * zInv1 + 1) * height / 2);

        float zInv2 = 1.0f / (v2.z + 4);
        int px2 = (int)((v2.x * zInv2 * aspect + 1) * width / 2);
        int py2 = (int)((v2.y * zInv2 + 1) * height / 2);

        // Draw line connecting the two projected points
        drawLine(px1, py1, px2, py2, buffer);
    }

    // Print the buffer
    clearScreen();  // Clear the terminal for smooth rendering
    for (const auto &line : buffer) {
        std::cout << line << "\n";
    }
}

int main() {
    float angleX = 0, angleY = 0, angleZ = 0;

    while (true) {
        std::vector<Vec3D> transformedVertices = cubeVertices;

        for (auto &v : transformedVertices) {
            rotateX(v, angleX);
            rotateY(v, angleY);
            rotateZ(v, angleZ);
        }

        projectAndRender(transformedVertices, cubeEdges);

        // Rotate the cube for the next frame
        angleX += 0.03;
        angleY += 0.02;
        angleZ += 0.04;

        Sleep(50);  // Sleep for 50ms between frames
    }

    return 0;
}
