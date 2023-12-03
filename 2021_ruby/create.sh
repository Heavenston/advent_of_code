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

if [ -d "$folder" ]
then
  echo "Folder already exits, updating utils only"
  find "ADayX" -maxdepth 1 -type f -exec cp {} "$folder" \;
else
  echo "Creating folder from template"
  cp -r ADayX "$folder"
fi

find "$folder" -type f -exec sed -i "s/#DAY_NUMBER#/$DAY_NUMBER/g" {} \;

echo Trying to download just to try
./"$folder"/download.sh

echo Everything should be good now!
