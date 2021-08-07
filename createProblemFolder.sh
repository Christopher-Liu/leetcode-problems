# Project name dictates folder and file names

read -p "Enter problem number: " probNum
read -p "enter problem name: " probName

if [[ -d "${probNum} - ${probName}" ]]; then
    echo "\"${probNum} - ${probName}\" already exists."

    exit 1
else
    mkdir "${probNum} - ${probName}"

    cd "${probNum} - ${probName}"

    touch "${probName}.py"

    echo "# ${probName}

## Description

## Notes" > "Notes - ${probName}.md"

    exit 0
fi
