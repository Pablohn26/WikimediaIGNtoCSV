#Lee acta_list.txt y llama al script get_acta.py

#!/bin/bash
        while IFS= read -r file
        do
                ./get_acta.py $file
        done < "./acta_list.txt"
