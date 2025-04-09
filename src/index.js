const search = document.querySelector("input");
const show = document.getElementById("printTypeInput");
const translate = document.getElementById("showTranslation");
let cotons = {
  UUU: "phe",
  UUC: "phe",
  UUA: "leu",
  UUG: "leu",
  CUU: "leu",
  CUC: "leu",
  CUA: "leu",
  UCU: "ser",
  UCC: "ser",
  UCA: "ser",
  UCG: "ser",
  CCU: "pro",
  CCC: "pro",
  CCA: "pro",
  CCG: "pro",
  ACU: "thr",
  CUG: "leu",
  AUU: "ile",
  AUC: "ile",
  ACC: "thr",
  ACA: "thr",
  ACG: "thr",
  GCU: "ala",
  GCC: "ala",
  GCA: "ala",
  GCG: "ala",
  AUA: "ile",
  UAU: "tyr",
  UAC: "tyr",
  UAA: "parada",
  UAG: "parada",
  CAU: "his",
  CAC: "his",
  CAA: "gln",
  AUG: "met",
  CAG: "gln",
  AAU: "asn",
  AAC: "asn",
  AAA: "lys",
  AAG: "lys",
  GAU: "asp",
  GUU: "val",
  GUC: "val",
  GUA: "val",
  GUG: "val",
  GAC: "asp",
  GAA: "glu",
  GAG: "glu",
  UGU: "cys",
  UGC: "cys",
  UGA: "parada",
  UGG: "trp",
  CGU: "arg",
  CGC: "arg",
  CGA: "arg",
  CGG: "arg",
  AGU: "ser",
  AGC: "ser",
  AGA: "arg",
  AGG: "arg",
  GGU: "gly",
  GGC: "gly",
  GGA: "gly",
  GGG: "gly",
};

function displayDNA() {
  let input = this.value.toUpperCase();
  let lista = [];
  const regexr = new RegExp(/([ACGU])/gi);
  if (input.length % 3 == 0 && input.length != 0 && regexr.test(input)) {
    for (let i = 0; i <= input.length / 3; i++) {
      for (const index in cotons) {
        if (index === input.substring(3 * i, 3 * (i + 1))) {
          lista.push(cotons[index]);
        }
      }
    }

    let showList = lista.reduce((DifferentPartInDNA, BaseNitrogenada) => {
      if (!DifferentPartInDNA[BaseNitrogenada]) {
        DifferentPartInDNA[BaseNitrogenada] = 0;
      }
      DifferentPartInDNA[BaseNitrogenada]++;
      return DifferentPartInDNA;
    }, {});

    final = "";
    for (const key in showList) {
      final = final + key + "-";
    }
    translate.innerHTML = final;
    input.includes("U")
      ? (show.innerHTML = "🧬 Essa fita é RNA")
      : (show.innerHTML = "🧬 Essa fita é DNA");
  }
}

search.addEventListener("keyup", displayDNA);
