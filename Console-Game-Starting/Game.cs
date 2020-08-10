using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    public new static void UpdatePosition(string keyPress, out int xChange, out int yChange)
        {
          yChange = 0;
          xChange = 0;

            if (keyPress == "DownArrow") {
                yChange = 1;
                xChange = 0;
            }
            else if (keyPress == "UpArrow") {
                yChange = -1;
                xChange = 0;
            }
            else if (keyPress == "RightArrow")
            {
                yChange = 0;
                xChange = 1;
            }
            else if (keyPress == "LeftArrow")
            {
                yChange = 0;
                xChange = -1;
            } else {
              yChange = 0;
              xChange = 0;
            }
        }

    public new static char UpdateCursor(string keyPress)
        {

          char cursor = '0';

            if (keyPress == "DownArrow")
            {
                cursor = 'v';
            }
            else if (keyPress == "UpArrow")
            {
                cursor =  '^';
            }
            else if (keyPress == "RightArrow")
            {
                cursor =  '>';
            }
            else if (keyPress == "LeftArrow")
            {
                cursor =  '<';
            } else {
              cursor = 'v';
            }

            return cursor;
        }

        public new static int KeepInBounds(int currentCoord, int maxCoord)
        {

          int newCoord = currentCoord;

            if (currentCoord >= maxCoord)
            {
                newCoord = maxCoord - 1;
            } else if (currentCoord < 0)
            {
                newCoord = 0;
            } else
            {
                newCoord = currentCoord;
            }

            return newCoord;
        }

        public new static bool DidScore(int xChar, int yChar, int xFruit, int yFruit)
        {
            if (xChar == xFruit && yChar == yFruit)
            {
                return true;
            } else
            {
                return false;
            }
        }
  }
}
