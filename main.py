from pyscript import document

def sign(event):

    results = document.getElementById("results") 
    results.innerText = ""  

    img_results = document.getElementById("img_results")
    img_results.src= ""

    registration = document.getElementById("res_yes").checked
    if registration:
        clearance = document.getElementById("clearance_yes").checked
        if clearance:
            grade = int(document.getElementById("grade").value)
            if grade == 7:
                section = document.getElementById("sec").value
                if section == "Emerald":
                    results.innerText = "Congratulations! You are Green Hornets"
                    img_results.src="g.png"
                elif section == "Ruby":
                    results.innerText = "Congratulations! You are Yellow Tigers"
                    img_results.src="y.png"
                else:
                    results.innerText = "Input a valid section"

            elif grade == 8:
                section = document.getElementById("sec").value
                if section == "Emerald":
                    results.innerText = "Congratulations! You are Red Bulldogs"
                    img_results.src="r.png"
                elif section == "Ruby":
                    results.innerText = "Congratulations! You are Blue Bears"
                    img_results.src="b.png"
                else:
                    results.innerText = "Input a valid section"

            elif grade == 9:
                section = document.getElementById("sec").value
                if section == "Emerald":
                    results.innerText = "Congratulations! You are Red Bulldogs"
                    img_results.src="r.png"
                elif section == "Ruby":
                    results.innerText = "Congratulations! You are Blue Bears"
                    img_results.src="b.png"
                else:
                    results.innerText = "Input a valid section"

            elif grade == 10:
                section = document.getElementById("sec").value
                if section == "Emerald":
                    results.innerText = "Congratulations! You are Green Hornets"
                    img_results.src="g.png"
                elif section == "Ruby":
                    results.innerText = "Congratulations! You are Yellow Tigers"
                    img_results.src="y.png"
                else:
                    results.innerText = "Input a valid section"
            else:
                results.innerText = "Input a valid grade level"
        else:
            results.innerText = "Please Receive Clearance First"
    else:
        results.innerText = "Please Register First"