DAY_NUMBER="$(printf "%02d" $1)"
echo Create day $DAY_NUMBER?

valid=0
while ! ((valid)); do
    read -p "Continue (y/N)? " choice
    case "$choice" in 
      y|Y    ) valid=1;;
      n|N|"" ) exit;;
      *      ) valid=0;;
    esac
done

folder=Day$DAY_NUMBER
cp -r ADayX $folder
find $folder -type f -print0 | xargs --null sed -i "s/#DAY_NUMBER#/$DAY_NUMBER/g"

echo Everything should be good now!
