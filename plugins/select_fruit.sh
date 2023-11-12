FRUIT=$1
if [ $FRUIT == APPLE ]; then
    echo "Apple!"
elif [ $FRUIT == ORANGE ]; then
    echo "오링~지!"
elif [ $FRUIT == GRAPE ]; then
    echo "Grape!"
else
    echo "Not Found, Try other command."
fi
