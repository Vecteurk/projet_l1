
facultes = {
    "si" : [
        {
            "code": "ig",
            "intitule": "Informatique de gestion et des administrations"
        },
        {
            "code": "ir",
            "intitule": "Informatique des reseaux et des infrastructures" 
        },
        {
            "code": "cs",
            "intitule": "Calcul Scientifique"
        }
    ],
    "sg" : [
        {
            "code": "ge",
            "intitule": "Gestion des entreprises"
        },
        {
            "code": "ba",
            "intitule": "Banques et assurances"
        },
        {
            "code": "grh",
            "intitule": "Gestion des ressources humaines"
        },
        {
            "code": "cm",
            "intitule": "Commerce et marketing"
        }
    ]
}

document.getElementById("sp2").addEventListener("click", function(e){
    var idFac = document.getElementById("facultes").value;
    var listeFil = facultes[idFac];
    var listeFilHtml = "";
    listeFil.forEach(filiere => {
        listeFilHtml = listeFilHtml + "<option value='" + filiere.code + "'>" + filiere.intitule + "</option>"
    });
    document.getElementById("filieres").innerHTML = listeFilHtml;

    document.getElementById("fpartie1").style.display = "none";
    document.getElementById("fpartie2").style.display = "block";
})

document.getElementById("sp3").addEventListener("click", function (e){
    document.getElementById("fpartie2").style.display = "none";
    document.getElementById("fpartie3").style.display = "block";
})

