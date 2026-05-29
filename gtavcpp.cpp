#include <SDL2/SDL.h>
            drawRect(renderer,
                -cameraX,
                i - cameraY,
                WORLD_WIDTH,
                120,
                70, 70, 70);
        }

        // Buildings
        for(int i = 0; i < 120; i++) {
            int bx = (i * 170) % WORLD_WIDTH;
            int by = ((i * 230) + 500) % WORLD_HEIGHT;

            drawRect(renderer,
                bx - cameraX,
                by - cameraY,
                120,
                120,
                180, 180, 180);
        }

        // Cars
        for(auto &car : cars) {
            drawRect(renderer,
                car.x - cameraX,
                car.y - cameraY,
                50,
                25,
                255, 0, 0);
        }

        // Enemies
        for(auto &enemy : enemies) {
            drawRect(renderer,
                enemy.x - cameraX,
                enemy.y - cameraY,
                enemy.size,
                enemy.size,
                255, 255, 0);
        }

        // Bullets
        for(auto &bullet : bullets) {
            drawRect(renderer,
                bullet.x - cameraX,
                bullet.y - cameraY,
                10,
                5,
                255, 255, 255);
        }

        // Player
        drawRect(renderer,
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2,
            player.size,
            player.size,
            0, 150, 255);

        SDL_RenderPresent(renderer);

        SDL_Delay(16);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);

    SDL_Quit();

    return 0;
}