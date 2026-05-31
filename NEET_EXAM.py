import random
import time
import os
from datetime import datetime

# ─── QUESTION BANK (180 questions, randomised subject-wise) ───────────────────
RAW_QUESTIONS = [
    # ── BIOLOGY ──────────────────────────────────────────────────────────────────
    # Ch1: Breathing and Exchange of Gases
    {"id": 1, "chapter": "Breathing & Exchange of Gases", "subject": "Biology",
     "q": "Which of the following is NOT a part of the conducting zone of the respiratory system?",
     "opts": ["Trachea", "Bronchi", "Alveoli", "Bronchioles"], "ans": 2,
     "exp": "Alveoli are the respiratory zone where actual gas exchange occurs. Trachea, bronchi, and bronchioles form the conducting zone (passageways)."},
    {"id": 2, "chapter": "Breathing & Exchange of Gases", "subject": "Biology",
     "q": "The partial pressure of O₂ in alveolar air is approximately:",
     "opts": ["104 mm Hg", "40 mm Hg", "46 mm Hg", "159 mm Hg"], "ans": 0,
     "exp": "Alveolar PO₂ ≈ 104 mm Hg. Atmospheric PO₂ is 159 mm Hg but it decreases after mixing with residual air and water vapour."},
    {"id": 3, "chapter": "Breathing & Exchange of Gases", "subject": "Biology",
     "q": "Tidal Volume (TV) in a normal adult at rest is approximately:",
     "opts": ["1200 mL", "500 mL", "2500 mL", "3500 mL"], "ans": 1,
     "exp": "Tidal Volume is the volume of air inspired or expired during normal quiet breathing ≈ 500 mL (0.5 L)."},
    {"id": 4, "chapter": "Breathing & Exchange of Gases", "subject": "Biology",
     "q": "Vital Capacity = ?",
     "opts": ["TV + IRV", "ERV + RV", "IRV + TV + ERV", "TLC – RV"], "ans": 2,
     "exp": "Vital Capacity = IRV + TV + ERV. It is the maximum volume that can be breathed out after maximum inhalation."},
    {"id": 5, "chapter": "Breathing & Exchange of Gases", "subject": "Biology",
     "q": "Which enzyme converts CO₂ + H₂O → H₂CO₃ in RBCs?",
     "opts": ["Catalase", "Carbonic anhydrase", "Pepsin", "Urease"], "ans": 1,
     "exp": "Carbonic anhydrase (present in RBCs) catalyses the rapid conversion of CO₂ and H₂O to carbonic acid (H₂CO₃), facilitating CO₂ transport."},
    {"id": 6, "chapter": "Breathing & Exchange of Gases", "subject": "Biology",
     "q": "About 70% of CO₂ is transported in blood as:",
     "opts": ["Dissolved CO₂", "Carbamino-haemoglobin", "Bicarbonate ions (HCO₃⁻)", "Carbonic acid"], "ans": 2,
     "exp": "~70% CO₂ is transported as bicarbonate ions in plasma. ~23% as carbamino-Hb, ~7% dissolved."},
    {"id": 7, "chapter": "Breathing & Exchange of Gases", "subject": "Biology",
     "q": "The primary centre for respiratory rhythm in humans is located in:",
     "opts": ["Cerebellum", "Pons", "Medulla oblongata", "Hypothalamus"], "ans": 2,
     "exp": "The respiratory rhythm centre (DRG and VRG) is in the medulla oblongata. The pneumotaxic centre in pons modulates it."},
    {"id": 8, "chapter": "Breathing & Exchange of Gases", "subject": "Biology",
     "q": "Chloride shift (Hamburger phenomenon) involves the exchange of:",
     "opts": ["Na⁺ and K⁺", "HCO₃⁻ and Cl⁻", "O₂ and CO₂", "H⁺ and Na⁺"], "ans": 1,
     "exp": "In chloride shift, HCO₃⁻ moves out of RBCs into plasma and Cl⁻ moves in to maintain electrical neutrality."},

    # Ch2: Biomolecules
    {"id": 9, "chapter": "Biomolecules", "subject": "Biology",
     "q": "Which bond links amino acids in a protein?",
     "opts": ["Glycosidic", "Phosphodiester", "Peptide", "Hydrogen"], "ans": 2,
     "exp": "Amino acids are linked by peptide bonds (–CO–NH–) formed by a condensation reaction."},
    {"id": 10, "chapter": "Biomolecules", "subject": "Biology",
     "q": "The most abundant organic molecule on Earth is:",
     "opts": ["Protein", "Cellulose", "Starch", "DNA"], "ans": 1,
     "exp": "Cellulose is the most abundant organic/biological molecule on Earth, forming the structural component of plant cell walls."},
    {"id": 11, "chapter": "Biomolecules", "subject": "Biology",
     "q": "Which of the following is a non-reducing sugar?",
     "opts": ["Glucose", "Maltose", "Lactose", "Sucrose"], "ans": 3,
     "exp": "Sucrose is a non-reducing sugar because its anomeric carbons of both glucose and fructose are involved in the glycosidic bond."},
    {"id": 12, "chapter": "Biomolecules", "subject": "Biology",
     "q": "Which vitamin is synthesised by bacteria in the human gut?",
     "opts": ["Vitamin C", "Vitamin D", "Vitamin K", "Vitamin A"], "ans": 2,
     "exp": "Vitamin K (required for blood clotting) is produced by gut bacteria (e.g., E. coli)."},
    {"id": 13, "chapter": "Biomolecules", "subject": "Biology",
     "q": "The secondary structure of proteins is maintained by:",
     "opts": ["Peptide bonds", "Disulfide bonds", "Hydrogen bonds", "Ionic bonds"], "ans": 2,
     "exp": "The α-helix and β-pleated sheet (secondary structures) are stabilised by hydrogen bonds."},
    {"id": 14, "chapter": "Biomolecules", "subject": "Biology",
     "q": "Which enzyme is used as a molecular scissor in recombinant DNA technology?",
     "opts": ["DNA polymerase", "Restriction endonuclease", "Ligase", "Helicase"], "ans": 1,
     "exp": "Restriction endonucleases (e.g., EcoRI) recognise specific palindromic sequences and cut DNA — hence called molecular scissors."},
    {"id": 15, "chapter": "Biomolecules", "subject": "Biology",
     "q": "Which of the following is a lipid-soluble vitamin?",
     "opts": ["Vitamin B12", "Vitamin C", "Vitamin E", "Vitamin B6"], "ans": 2,
     "exp": "Vitamins A, D, E, K are fat-soluble. Vitamin E (tocopherol) is a fat-soluble antioxidant."},
    {"id": 16, "chapter": "Biomolecules", "subject": "Biology",
     "q": "Chitin, found in the exoskeleton of insects, is a polymer of:",
     "opts": ["Glucose", "N-acetylglucosamine", "Galactose", "Fructose"], "ans": 1,
     "exp": "Chitin is a polysaccharide made of N-acetylglucosamine monomers linked by β-1,4 glycosidic bonds."},

    # Ch3: Blood Fluid and Circulation
    {"id": 17, "chapter": "Blood Fluid & Circulation", "subject": "Biology",
     "q": "The pacemaker of the human heart is:",
     "opts": ["AV node", "Bundle of His", "SA node", "Purkinje fibres"], "ans": 2,
     "exp": "The SA (Sinoatrial) node generates impulses at 70–75 times/min, setting the heart rate — hence called the natural pacemaker."},
    {"id": 18, "chapter": "Blood Fluid & Circulation", "subject": "Biology",
     "q": "Which blood group is called 'Universal Donor'?",
     "opts": ["A", "B", "AB", "O"], "ans": 3,
     "exp": "Blood group O (O negative to be precise) lacks A and B antigens on RBCs, so it can be donated to any ABO blood group — universal donor."},
    {"id": 19, "chapter": "Blood Fluid & Circulation", "subject": "Biology",
     "q": "Normal human blood pressure is:",
     "opts": ["80/120 mm Hg", "120/80 mm Hg", "100/70 mm Hg", "140/90 mm Hg"], "ans": 1,
     "exp": "Normal blood pressure = 120 mm Hg (systolic) / 80 mm Hg (diastolic)."},
    {"id": 20, "chapter": "Blood Fluid & Circulation", "subject": "Biology",
     "q": "The yellowish fluid that oozes out when blood clots is called:",
     "opts": ["Plasma", "Lymph", "Serum", "Interstitial fluid"], "ans": 2,
     "exp": "Serum = Plasma – Clotting factors (fibrinogen). After clotting, the clear yellowish fluid that remains is serum."},
    {"id": 21, "chapter": "Blood Fluid & Circulation", "subject": "Biology",
     "q": "Cardiac output = ?",
     "opts": ["Heart rate × Blood pressure", "Stroke volume × Heart rate", "Blood volume / Time", "EDV – ESV"], "ans": 1,
     "exp": "Cardiac Output = Stroke Volume × Heart Rate. Normal CO ≈ 5 L/min."},
    {"id": 22, "chapter": "Blood Fluid & Circulation", "subject": "Biology",
     "q": "Which of the following carries deoxygenated blood in adults?",
     "opts": ["Pulmonary vein", "Aorta", "Pulmonary artery", "Carotid artery"], "ans": 2,
     "exp": "The pulmonary artery carries deoxygenated blood from the right ventricle to the lungs."},
    {"id": 23, "chapter": "Blood Fluid & Circulation", "subject": "Biology",
     "q": "Erythroblastosis fetalis occurs due to incompatibility of:",
     "opts": ["ABO blood group", "Rh factor", "HLA antigens", "Plasma proteins"], "ans": 1,
     "exp": "Rh incompatibility: if Rh– mother carries Rh+ fetus, maternal anti-Rh antibodies attack fetal RBCs."},
    {"id": 24, "chapter": "Blood Fluid & Circulation", "subject": "Biology",
     "q": "Double circulation was first described by:",
     "opts": ["William Harvey", "Landsteiner", "Starling", "Laennec"], "ans": 0,
     "exp": "William Harvey (1628) described the double circulation of blood."},

    # Ch4: Excretory Products and Their Elimination
    {"id": 25, "chapter": "Excretory Products & Elimination", "subject": "Biology",
     "q": "The functional unit of the kidney is:",
     "opts": ["Glomerulus", "Nephron", "Bowman's capsule", "Loop of Henle"], "ans": 1,
     "exp": "The nephron is the structural and functional unit of the kidney."},
    {"id": 26, "chapter": "Excretory Products & Elimination", "subject": "Biology",
     "q": "Which hormone promotes water reabsorption in collecting duct?",
     "opts": ["Aldosterone", "ADH (Vasopressin)", "Renin", "ANF"], "ans": 1,
     "exp": "ADH (Antidiuretic hormone / Vasopressin) increases permeability of collecting duct to water."},
    {"id": 27, "chapter": "Excretory Products & Elimination", "subject": "Biology",
     "q": "Uricotelic animals excrete nitrogenous waste mainly as:",
     "opts": ["Ammonia", "Urea", "Uric acid", "Amino acids"], "ans": 2,
     "exp": "Uricotelic animals (reptiles, birds, insects) excrete uric acid."},
    {"id": 28, "chapter": "Excretory Products & Elimination", "subject": "Biology",
     "q": "The GFR (Glomerular Filtration Rate) in a healthy adult is approximately:",
     "opts": ["12 L/day", "125 mL/min", "25 L/day", "60 mL/min"], "ans": 1,
     "exp": "GFR ≈ 125 mL/min = 180 L/day."},
    {"id": 29, "chapter": "Excretory Products & Elimination", "subject": "Biology",
     "q": "Juxtaglomerular apparatus (JGA) is involved in:",
     "opts": ["Urine concentration", "Renin secretion", "ADH secretion", "Erythropoietin production"], "ans": 1,
     "exp": "JGA secretes renin in response to fall in blood pressure/GFR."},
    {"id": 30, "chapter": "Excretory Products & Elimination", "subject": "Biology",
     "q": "The counter-current mechanism in kidney involves:",
     "opts": ["Proximal tubule and distal tubule", "Loop of Henle and vasa recta", "Glomerulus and Bowman's capsule", "Collecting duct and glomerulus"], "ans": 1,
     "exp": "The counter-current multiplier and exchanger work together to concentrate urine."},
    {"id": 31, "chapter": "Excretory Products & Elimination", "subject": "Biology",
     "q": "Which is NOT a function of the kidney?",
     "opts": ["Regulation of blood pH", "Erythropoietin secretion", "Insulin production", "Osmoregulation"], "ans": 2,
     "exp": "Insulin is produced by β-cells of Islets of Langerhans in the pancreas."},
    {"id": 32, "chapter": "Excretory Products & Elimination", "subject": "Biology",
     "q": "Micturition reflex is controlled by:",
     "opts": ["Hypothalamus", "Spinal cord (S2–S4)", "Cerebellum", "Medulla oblongata"], "ans": 1,
     "exp": "Micturition reflex is a spinal reflex centred at S2–S4 sacral segments."},

    # Ch5: Locomotion and Movement
    {"id": 33, "chapter": "Locomotion & Movement", "subject": "Biology",
     "q": "Which protein is present in the thin filament of a sarcomere?",
     "opts": ["Myosin", "Actin", "Titin", "All of these"], "ans": 1,
     "exp": "Thin filaments = Actin + Troponin + Tropomyosin."},
    {"id": 34, "chapter": "Locomotion & Movement", "subject": "Biology",
     "q": "The functional unit of skeletal muscle is:",
     "opts": ["Myofibril", "Sarcomere", "Muscle fibre", "Motor unit"], "ans": 1,
     "exp": "The sarcomere (between two Z-lines) is the structural and functional unit."},
    {"id": 35, "chapter": "Locomotion & Movement", "subject": "Biology",
     "q": "Which ion is essential for muscle contraction?",
     "opts": ["Na⁺", "K⁺", "Ca²⁺", "Mg²⁺"], "ans": 2,
     "exp": "Ca²⁺ released from SR binds troponin C, displacing tropomyosin."},
    {"id": 36, "chapter": "Locomotion & Movement", "subject": "Biology",
     "q": "A condition caused by excess uric acid deposition in joints is:",
     "opts": ["Osteoporosis", "Gout", "Arthritis", "Myasthenia gravis"], "ans": 1,
     "exp": "Gout results from hyperuricaemia, leading to urate crystal deposition in joints."},
    {"id": 37, "chapter": "Locomotion & Movement", "subject": "Biology",
     "q": "The number of bones in the human skull is:",
     "opts": ["8", "22", "14", "29"], "ans": 1,
     "exp": "The human skull has 22 bones: 8 cranial and 14 facial bones."},
    {"id": 38, "chapter": "Locomotion & Movement", "subject": "Biology",
     "q": "Which joint allows rotation (e.g., atlas–axis)?",
     "opts": ["Hinge joint", "Ball and socket joint", "Pivot joint", "Saddle joint"], "ans": 2,
     "exp": "Pivot joints allow rotational movement."},
    {"id": 39, "chapter": "Locomotion & Movement", "subject": "Biology",
     "q": "Rigor mortis occurs due to:",
     "opts": ["Lack of ATP preventing cross-bridge detachment", "Excess Ca²⁺", "Lack of ACh", "None of these"], "ans": 0,
     "exp": "After death, ATP production stops. Without ATP, myosin heads cannot detach from actin."},
    {"id": 40, "chapter": "Locomotion & Movement", "subject": "Biology",
     "q": "The pectoral girdle consists of:",
     "opts": ["Clavicle and scapula", "Ilium, ischium, pubis", "Femur and tibia", "Radius and ulna"], "ans": 0,
     "exp": "Pectoral (shoulder) girdle = Clavicle + Scapula."},

    # Ch6: Cell Structure
    {"id": 41, "chapter": "Cell Structure", "subject": "Biology",
     "q": "Which organelle is called the 'powerhouse of the cell'?",
     "opts": ["Nucleus", "Ribosome", "Mitochondria", "Golgi apparatus"], "ans": 2,
     "exp": "Mitochondria produce ATP via oxidative phosphorylation."},
    {"id": 42, "chapter": "Cell Structure", "subject": "Biology",
     "q": "The fluid mosaic model of cell membrane was proposed by:",
     "opts": ["Watson and Crick", "Singer and Nicolson", "Schleiden and Schwann", "Davson and Danielli"], "ans": 1,
     "exp": "Singer and Nicolson (1972) proposed the fluid mosaic model."},
    {"id": 43, "chapter": "Cell Structure", "subject": "Biology",
     "q": "Which cell organelle is the site of protein synthesis?",
     "opts": ["Lysosome", "Ribosome", "SER", "Peroxisome"], "ans": 1,
     "exp": "Ribosomes are the sites of translation (protein synthesis)."},
    {"id": 44, "chapter": "Cell Structure", "subject": "Biology",
     "q": "The 9+2 arrangement of microtubules is seen in:",
     "opts": ["Cilia and flagella", "Centrioles", "Spindle fibres", "Microvilli"], "ans": 0,
     "exp": "Cilia and flagella have 9 doublet microtubules + 2 central singlets (9+2 axoneme)."},
    {"id": 45, "chapter": "Cell Structure", "subject": "Biology",
     "q": "Which organelle is involved in detoxification of drugs?",
     "opts": ["RER", "SER", "Golgi body", "Lysosome"], "ans": 1,
     "exp": "Smooth ER (SER) contains enzymes for detoxification."},
    {"id": 46, "chapter": "Cell Structure", "subject": "Biology",
     "q": "Prokaryotic ribosomes are:",
     "opts": ["80S", "70S", "60S", "40S"], "ans": 1,
     "exp": "Prokaryotic ribosomes = 70S (50S + 30S subunits)."},
    {"id": 47, "chapter": "Cell Structure", "subject": "Biology",
     "q": "Lysosomes are formed from:",
     "opts": ["Mitochondria", "Golgi apparatus", "Nucleus", "ER only"], "ans": 1,
     "exp": "Lysosomes are formed by pinching off from the Golgi apparatus."},
    {"id": 48, "chapter": "Cell Structure", "subject": "Biology",
     "q": "The nucleolus is the site of:",
     "opts": ["DNA replication", "rRNA synthesis", "mRNA processing", "Protein synthesis"], "ans": 1,
     "exp": "The nucleolus is where rRNA is transcribed and ribosomal subunits are assembled."},

    # Ch7: Cell Cycle
    {"id": 49, "chapter": "Cell Cycle", "subject": "Biology",
     "q": "In which phase of mitosis do chromosomes align at the equatorial plate?",
     "opts": ["Prophase", "Anaphase", "Metaphase", "Telophase"], "ans": 2,
     "exp": "During metaphase, chromosomes align at the metaphase plate."},
    {"id": 50, "chapter": "Cell Cycle", "subject": "Biology",
     "q": "S-phase of the cell cycle is the phase of:",
     "opts": ["Cell growth", "DNA synthesis", "Organelle duplication", "Cell division"], "ans": 1,
     "exp": "S (Synthesis) phase: DNA replication occurs."},
    {"id": 51, "chapter": "Cell Cycle", "subject": "Biology",
     "q": "Cytokinesis in animal cells occurs by:",
     "opts": ["Cell plate formation", "Cleavage furrow", "Phragmoplast", "None"], "ans": 1,
     "exp": "Animal cells divide by cleavage furrow."},
    {"id": 52, "chapter": "Cell Cycle", "subject": "Biology",
     "q": "Which checkpoint ensures DNA is replicated correctly before mitosis?",
     "opts": ["G1 checkpoint", "G2 checkpoint", "M checkpoint", "S checkpoint"], "ans": 1,
     "exp": "G2 checkpoint checks for complete, undamaged DNA replication."},
    {"id": 53, "chapter": "Cell Cycle", "subject": "Biology",
     "q": "In meiosis, crossing over occurs during:",
     "opts": ["Leptotene", "Zygotene", "Pachytene", "Diplotene"], "ans": 2,
     "exp": "Crossing over occurs during pachytene of prophase I."},
    {"id": 54, "chapter": "Cell Cycle", "subject": "Biology",
     "q": "Meiosis results in:",
     "opts": ["2 diploid cells", "4 diploid cells", "4 haploid cells", "2 haploid cells"], "ans": 2,
     "exp": "Meiosis produces 4 genetically unique haploid cells."},
    {"id": 55, "chapter": "Cell Cycle", "subject": "Biology",
     "q": "Which of the following is correct for G0 phase?",
     "opts": ["Cells are actively dividing", "Cells exit cell cycle and are quiescent", "DNA is being replicated", "Cells are in M phase"], "ans": 1,
     "exp": "G0 (quiescent phase): cells exit cell cycle and remain metabolically active."},
    {"id": 56, "chapter": "Cell Cycle", "subject": "Biology",
     "q": "Synapsis occurs during which stage of meiosis I?",
     "opts": ["Leptotene", "Zygotene", "Pachytene", "Diakinesis"], "ans": 1,
     "exp": "Synapsis begins in zygotene."},

    # Ch8: The Living World
    {"id": 57, "chapter": "The Living World", "subject": "Biology",
     "q": "The five kingdom classification was proposed by:",
     "opts": ["Linnaeus", "Whittaker", "Haeckel", "Woese"], "ans": 1,
     "exp": "R.H. Whittaker (1969) proposed 5-kingdom classification."},
    {"id": 58, "chapter": "The Living World", "subject": "Biology",
     "q": "The term 'species' was coined by:",
     "opts": ["Linnaeus", "John Ray", "Aristotle", "Darwin"], "ans": 1,
     "exp": "John Ray coined the term 'species'."},
    {"id": 59, "chapter": "The Living World", "subject": "Biology",
     "q": "Binomial nomenclature was introduced by:",
     "opts": ["Darwin", "Linnaeus", "Whittaker", "Aristotle"], "ans": 1,
     "exp": "Carl Linnaeus introduced binomial nomenclature."},
    {"id": 60, "chapter": "The Living World", "subject": "Biology",
     "q": "Which is the most widely accepted definition of 'life'?",
     "opts": ["Ability to move", "Self-replication and metabolism", "Cellular organisation", "Response to stimuli"], "ans": 1,
     "exp": "Life is best characterised by self-replication and metabolism."},
    {"id": 61, "chapter": "The Living World", "subject": "Biology",
     "q": "National Botanical Research Institute (NBRI) is in:",
     "opts": ["Kolkata", "Mumbai", "Lucknow", "Chennai"], "ans": 2,
     "exp": "NBRI is located in Lucknow, Uttar Pradesh."},
    {"id": 62, "chapter": "The Living World", "subject": "Biology",
     "q": "In biological classification, which is the highest taxon?",
     "opts": ["Kingdom", "Phylum", "Class", "Division"], "ans": 0,
     "exp": "Kingdom is the highest taxon."},
    {"id": 63, "chapter": "The Living World", "subject": "Biology",
     "q": "Taxonomy includes:",
     "opts": ["Identification only", "Classification only", "Nomenclature only", "Identification, Classification, and Nomenclature"], "ans": 3,
     "exp": "Taxonomy = Identification + Classification + Nomenclature."},
    {"id": 64, "chapter": "The Living World", "subject": "Biology",
     "q": "Metabolic reactions in organisms are catalysed by:",
     "opts": ["Hormones", "Enzymes", "Vitamins", "Coenzymes"], "ans": 1,
     "exp": "Enzymes are biological catalysts that speed up metabolic reactions."},

    # Ch9: Biological Classification
    {"id": 65, "chapter": "Biological Classification", "subject": "Biology",
     "q": "Which kingdom includes prokaryotes?",
     "opts": ["Protista", "Fungi", "Monera", "Plantae"], "ans": 2,
     "exp": "Kingdom Monera includes all prokaryotes."},
    {"id": 66, "chapter": "Biological Classification", "subject": "Biology",
     "q": "Mycorrhiza is a symbiotic association between:",
     "opts": ["Algae and fungi", "Fungi and plant roots", "Bacteria and legume roots", "Lichen and rock"], "ans": 1,
     "exp": "Mycorrhiza = fungus (myco) + root (rhiza)."},
    {"id": 67, "chapter": "Biological Classification", "subject": "Biology",
     "q": "Viruses are considered living because they:",
     "opts": ["Have cell walls", "Can reproduce inside host cells", "Carry out respiration", "Show growth"], "ans": 1,
     "exp": "Viruses replicate inside host cells using the host's machinery."},
    {"id": 68, "chapter": "Biological Classification", "subject": "Biology",
     "q": "Which organism causes malaria?",
     "opts": ["Entamoeba", "Plasmodium", "Leishmania", "Trypanosoma"], "ans": 1,
     "exp": "Plasmodium causes malaria, transmitted by female Anopheles mosquito."},
    {"id": 69, "chapter": "Biological Classification", "subject": "Biology",
     "q": "Lichens are symbiotic associations of:",
     "opts": ["Algae and mosses", "Fungi and algae/cyanobacteria", "Bacteria and fungi", "Fern and algae"], "ans": 1,
     "exp": "Lichens = Fungal component + Photosynthetic component."},
    {"id": 70, "chapter": "Biological Classification", "subject": "Biology",
     "q": "Cell wall of fungi is made of:",
     "opts": ["Cellulose", "Chitin", "Peptidoglycan", "Lignin"], "ans": 1,
     "exp": "Fungal cell walls are composed of chitin."},
    {"id": 71, "chapter": "Biological Classification", "subject": "Biology",
     "q": "Which group of algae is responsible for red tides?",
     "opts": ["Chlorophyta", "Chrysophyta", "Phaeophyta", "Dinoflagellates"], "ans": 3,
     "exp": "Dinoflagellates (e.g., Gonyaulax) cause red tides."},
    {"id": 72, "chapter": "Biological Classification", "subject": "Biology",
     "q": "Prions are:",
     "opts": ["DNA viruses", "RNA viruses", "Infectious proteins", "Viroids"], "ans": 2,
     "exp": "Prions are misfolded proteins that cause neurodegenerative diseases."},

    # Ch10: Plant Kingdom
    {"id": 73, "chapter": "Plant Kingdom", "subject": "Biology",
     "q": "Which group of plants is called 'amphibians of the plant kingdom'?",
     "opts": ["Algae", "Bryophytes", "Pteridophytes", "Gymnosperms"], "ans": 1,
     "exp": "Bryophytes need water for fertilisation but live on land."},
    {"id": 74, "chapter": "Plant Kingdom", "subject": "Biology",
     "q": "The dominant phase in bryophytes is:",
     "opts": ["Sporophyte", "Gametophyte", "Both equal", "Neither"], "ans": 1,
     "exp": "In bryophytes, the gametophyte is the dominant free-living phase."},
    {"id": 75, "chapter": "Plant Kingdom", "subject": "Biology",
     "q": "Which plant group was the first to colonise land?",
     "opts": ["Algae", "Bryophytes", "Pteridophytes", "Gymnosperms"], "ans": 1,
     "exp": "Bryophytes were the first land plants."},
    {"id": 76, "chapter": "Plant Kingdom", "subject": "Biology",
     "q": "Heterospory is a characteristic of:",
     "opts": ["All pteridophytes", "All bryophytes", "Selaginella and Salvinia", "Pinus only"], "ans": 2,
     "exp": "Heterospory occurs in Selaginella, Salvinia, Marsilea among pteridophytes."},
    {"id": 77, "chapter": "Plant Kingdom", "subject": "Biology",
     "q": "Which is the national tree of India?",
     "opts": ["Teak", "Banyan (Ficus benghalensis)", "Peepal", "Neem"], "ans": 1,
     "exp": "Banyan tree is India's national tree."},
    {"id": 78, "chapter": "Plant Kingdom", "subject": "Biology",
     "q": "Seeds are produced by:",
     "opts": ["Algae and Bryophytes", "Pteridophytes only", "Gymnosperms and Angiosperms", "All land plants"], "ans": 2,
     "exp": "Only spermatophytes (seed plants) produce seeds."},
    {"id": 79, "chapter": "Plant Kingdom", "subject": "Biology",
     "q": "Double fertilisation is a unique feature of:",
     "opts": ["Gymnosperms", "Angiosperms", "Pteridophytes", "Bryophytes"], "ans": 1,
     "exp": "Double fertilisation is unique to angiosperms."},
    {"id": 80, "chapter": "Plant Kingdom", "subject": "Biology",
     "q": "Agar-agar is obtained from:",
     "opts": ["Red algae (Gelidium)", "Brown algae", "Green algae", "Diatoms"], "ans": 0,
     "exp": "Agar is a polysaccharide extracted from red algae."},

    # Ch11: Morphology of Flowering Plants
    {"id": 81, "chapter": "Morphology of Flowering Plants", "subject": "Biology",
     "q": "Which root modification stores food (e.g., carrot)?",
     "opts": ["Prop roots", "Stilt roots", "Tap root (conical/fusiform)", "Fibrous roots"], "ans": 2,
     "exp": "Carrot, radish, and turnip are modified tap roots that store food."},
    {"id": 82, "chapter": "Morphology of Flowering Plants", "subject": "Biology",
     "q": "The thorn of Bougainvillea is a modification of:",
     "opts": ["Leaf", "Stipule", "Stem", "Root"], "ans": 2,
     "exp": "Bougainvillea thorns are axillary buds modified into thorns."},
    {"id": 83, "chapter": "Morphology of Flowering Plants", "subject": "Biology",
     "q": "Which is the correct formula for a bisexual actinomorphic flower?",
     "opts": ["⊕ ♀", "⊕ ⚥", "↑ ⚥", "↑ ♀"], "ans": 1,
     "exp": "⊕ = actinomorphic, ⚥ = bisexual."},
    {"id": 84, "chapter": "Morphology of Flowering Plants", "subject": "Biology",
     "q": "Epipetalous stamens are found in:",
     "opts": ["Solanaceae", "Fabaceae", "Liliaceae", "Malvaceae"], "ans": 0,
     "exp": "Epipetalous stamens are found in Solanaceae."},
    {"id": 85, "chapter": "Morphology of Flowering Plants", "subject": "Biology",
     "q": "A leaf with reticulate venation is typical of:",
     "opts": ["Monocots", "Dicots", "Pteridophytes", "Gymnosperms"], "ans": 1,
     "exp": "Dicots typically have reticulate venation."},
    {"id": 86, "chapter": "Morphology of Flowering Plants", "subject": "Biology",
     "q": "Which type of aestivation is found in Cassia?",
     "opts": ["Valvate", "Twisted", "Imbricate", "Vexillary"], "ans": 2,
     "exp": "Cassia has imbricate aestivation."},
    {"id": 87, "chapter": "Morphology of Flowering Plants", "subject": "Biology",
     "q": "Pneumatophores (respiratory roots) are found in:",
     "opts": ["Mangroves (Rhizophora)", "Maize", "Banyan", "Orchids"], "ans": 0,
     "exp": "Pneumatophores are found in mangroves growing in waterlogged soil."},
    {"id": 88, "chapter": "Morphology of Flowering Plants", "subject": "Biology",
     "q": "The edible part of mango is:",
     "opts": ["Epicarp", "Mesocarp", "Endocarp", "Seed"], "ans": 1,
     "exp": "In mango, the fleshy mesocarp is edible."},

    # Ch12: Anatomy of Flowering Plants
    {"id": 89, "chapter": "Anatomy of Flowering Plants", "subject": "Biology",
     "q": "Which tissue provides mechanical support and has dead cells at maturity?",
     "opts": ["Collenchyma", "Parenchyma", "Sclerenchyma", "Chlorenchyma"], "ans": 2,
     "exp": "Sclerenchyma has thick lignified cell walls and cells are dead at maturity."},
    {"id": 90, "chapter": "Anatomy of Flowering Plants", "subject": "Biology",
     "q": "The Casparian strip is present in:",
     "opts": ["Epidermis", "Endodermis", "Pericycle", "Cortex"], "ans": 1,
     "exp": "Casparian strip is a waxy band in the endodermis cell walls."},
    {"id": 91, "chapter": "Anatomy of Flowering Plants", "subject": "Biology",
     "q": "In a dicot stem, vascular bundles are:",
     "opts": ["Scattered", "In a ring", "Absent", "In two separate rings"], "ans": 1,
     "exp": "Dicot stem: vascular bundles arranged in a ring."},
    {"id": 92, "chapter": "Anatomy of Flowering Plants", "subject": "Biology",
     "q": "Which meristem is responsible for increase in girth of a plant?",
     "opts": ["Apical meristem", "Lateral meristem", "Intercalary meristem", "None"], "ans": 1,
     "exp": "Lateral meristems are responsible for secondary growth."},
    {"id": 93, "chapter": "Anatomy of Flowering Plants", "subject": "Biology",
     "q": "Companion cells are associated with:",
     "opts": ["Xylem vessels", "Sieve tubes", "Tracheids", "Wood fibres"], "ans": 1,
     "exp": "Companion cells are associated with sieve tubes in phloem."},
    {"id": 94, "chapter": "Anatomy of Flowering Plants", "subject": "Biology",
     "q": "Annual rings in wood are formed due to:",
     "opts": ["Primary growth", "Secondary growth by cambium", "Differentiation of pith", "Activity of phellogen"], "ans": 1,
     "exp": "Annual rings are formed by the seasonal activity of vascular cambium."},
    {"id": 95, "chapter": "Anatomy of Flowering Plants", "subject": "Biology",
     "q": "The outermost layer of cortex (in roots) is:",
     "opts": ["Endodermis", "Epidermis", "Exodermis", "Pericycle"], "ans": 2,
     "exp": "Exodermis is the outermost cortical layer with suberin deposits."},
    {"id": 96, "chapter": "Anatomy of Flowering Plants", "subject": "Biology",
     "q": "Bulliform (motor) cells are found in:",
     "opts": ["Dicot leaves", "Monocot leaves", "Dicot stems", "Roots"], "ans": 1,
     "exp": "Bulliform cells are found in the upper epidermis of monocot leaves."},

    # ── PHYSICS ──────────────────────────────────────────────────────────────────
    {"id": 97, "chapter": "Units & Dimensions", "subject": "Physics",
     "q": "The dimensional formula for pressure is:",
     "opts": ["[MLT⁻²]", "[ML⁻¹T⁻²]", "[ML²T⁻²]", "[M⁰L⁻¹T⁻²]"], "ans": 1,
     "exp": "Pressure = Force/Area = [MLT⁻²]/[L²] = [ML⁻¹T⁻²]."},
    {"id": 98, "chapter": "Units & Dimensions", "subject": "Physics",
     "q": "Which of the following pairs has the same dimensions?",
     "opts": ["Work and Power", "Torque and Energy", "Force and Momentum", "Impulse and Pressure"], "ans": 1,
     "exp": "Both Torque and Energy have dimensions [ML²T⁻²]."},
    {"id": 99, "chapter": "Units & Dimensions", "subject": "Physics",
     "q": "The SI unit of luminous intensity is:",
     "opts": ["Lumen", "Lux", "Candela", "Watt"], "ans": 2,
     "exp": "Candela (cd) is the SI base unit of luminous intensity."},
    {"id": 100, "chapter": "Units & Dimensions", "subject": "Physics",
     "q": "Dimensional formula for Planck's constant is:",
     "opts": ["[ML²T⁻¹]", "[MLT⁻²]", "[ML²T⁻²]", "[M⁰L⁰T⁰]"], "ans": 0,
     "exp": "h = E/ν = [ML²T⁻²]/[T⁻¹] = [ML²T⁻¹]."},
    {"id": 101, "chapter": "Units & Dimensions", "subject": "Physics",
     "q": "Which quantity is dimensionless?",
     "opts": ["Strain", "Stress", "Pressure", "Young's modulus"], "ans": 0,
     "exp": "Strain = ΔL/L is a ratio of lengths — dimensionless."},
    {"id": 102, "chapter": "Units & Dimensions", "subject": "Physics",
     "q": "The number of significant figures in 0.00345 is:",
     "opts": ["5", "3", "6", "2"], "ans": 1,
     "exp": "Leading zeros are not significant. Only 3, 4, 5 are significant → 3 significant figures."},

    {"id": 103, "chapter": "Vectors", "subject": "Physics",
     "q": "The cross product of two parallel vectors is:",
     "opts": ["Maximum", "Unity", "Zero", "Cannot be determined"], "ans": 2,
     "exp": "A × B = |A||B|sin θ. For θ = 0°, sin 0° = 0 → cross product = 0."},
    {"id": 104, "chapter": "Vectors", "subject": "Physics",
     "q": "If A⃗ + B⃗ = C⃗ and |A| = |B| = |C|, the angle between A and B is:",
     "opts": ["60°", "90°", "120°", "180°"], "ans": 2,
     "exp": "Using C² = A² + B² + 2AB cos θ, we get cos θ = –1/2 → θ = 120°."},
    {"id": 105, "chapter": "Vectors", "subject": "Physics",
     "q": "Unit vector is a vector with:",
     "opts": ["Zero magnitude", "Magnitude = 1", "Any magnitude", "Magnitude = 10"], "ans": 1,
     "exp": "A unit vector has magnitude exactly 1 (dimensionless)."},
    {"id": 106, "chapter": "Vectors", "subject": "Physics",
     "q": "The dot product A⃗·B⃗ = 0 implies:",
     "opts": ["A and B are parallel", "A and B are perpendicular", "|A| = 0", "Both A and B"], "ans": 1,
     "exp": "A⃗·B⃗ = |A||B|cos θ = 0 implies cos θ = 0 → θ = 90°."},
    {"id": 107, "chapter": "Vectors", "subject": "Physics",
     "q": "The resultant of two equal vectors each of magnitude F at 90° is:",
     "opts": ["F", "F√2", "2F", "F/√2"], "ans": 1,
     "exp": "R = √(F² + F² + 2F²cos 90°) = √(2F²) = F√2."},
    {"id": 108, "chapter": "Vectors", "subject": "Physics",
     "q": "Which of the following is a scalar quantity?",
     "opts": ["Velocity", "Acceleration", "Work", "Force"], "ans": 2,
     "exp": "Work = F⃗·d⃗ (dot product) is a scalar."},

    {"id": 109, "chapter": "Kinematics", "subject": "Physics",
     "q": "A body starts from rest and accelerates uniformly at 4 m/s². Its velocity after 5 s is:",
     "opts": ["10 m/s", "20 m/s", "25 m/s", "40 m/s"], "ans": 1,
     "exp": "v = u + at = 0 + 4×5 = 20 m/s."},
    {"id": 110, "chapter": "Kinematics", "subject": "Physics",
     "q": "The slope of a velocity–time graph gives:",
     "opts": ["Displacement", "Speed", "Acceleration", "Distance"], "ans": 2,
     "exp": "Slope of v-t graph = Δv/Δt = acceleration."},
    {"id": 111, "chapter": "Kinematics", "subject": "Physics",
     "q": "The range of a projectile is maximum when the angle of projection is:",
     "opts": ["30°", "45°", "60°", "90°"], "ans": 1,
     "exp": "R = u²sin 2θ / g. For max R, sin 2θ = 1 → 2θ = 90° → θ = 45°."},
    {"id": 112, "chapter": "Kinematics", "subject": "Physics",
     "q": "A ball thrown vertically upward returns to the same level. The ratio of maximum height to total time of flight gives which relation?",
     "opts": ["H = gT²/8", "H = gT²/4", "H = gT²/2", "H = gT²"], "ans": 0,
     "exp": "T = 2u/g → u = gT/2. H = u²/2g = gT²/8."},
    {"id": 113, "chapter": "Kinematics", "subject": "Physics",
     "q": "A particle moves in a circle of radius r at constant speed. Its acceleration is directed:",
     "opts": ["Tangentially", "Radially outward", "Radially inward", "At 45° to radius"], "ans": 2,
     "exp": "Centripetal acceleration = v²/r, directed radially inward."},
    {"id": 114, "chapter": "Kinematics", "subject": "Physics",
     "q": "Equations of motion are valid only for:",
     "opts": ["Non-uniform acceleration", "Uniform acceleration", "All types of motion", "Rotational motion"], "ans": 1,
     "exp": "The kinematic equations are valid only for uniform (constant) acceleration."},

    {"id": 115, "chapter": "Laws of Motion", "subject": "Physics",
     "q": "Newton's First Law of Motion is also known as:",
     "opts": ["Law of Acceleration", "Law of Inertia", "Law of Action-Reaction", "Law of Gravitation"], "ans": 1,
     "exp": "Newton's 1st Law is called 'Law of Inertia'."},
    {"id": 116, "chapter": "Laws of Motion", "subject": "Physics",
     "q": "A 5 kg block slides on a frictionless surface under a 20 N force. Its acceleration is:",
     "opts": ["4 m/s²", "2 m/s²", "100 m/s²", "0.25 m/s²"], "ans": 0,
     "exp": "F = ma → a = F/m = 20/5 = 4 m/s²."},
    {"id": 117, "chapter": "Laws of Motion", "subject": "Physics",
     "q": "The impulse-momentum theorem states:",
     "opts": ["F = ma", "Impulse = change in momentum", "Work = ΔKE", "P = mv"], "ans": 1,
     "exp": "Impulse = F·Δt = Δ(mv) = change in momentum."},
    {"id": 118, "chapter": "Laws of Motion", "subject": "Physics",
     "q": "The angle of friction equals the angle of repose. What does this imply?",
     "opts": ["Object is accelerating", "Coefficient of static friction equals tan of that angle", "Object has no weight", "Friction is zero"], "ans": 1,
     "exp": "tan(angle of repose) = μs."},
    {"id": 119, "chapter": "Laws of Motion", "subject": "Physics",
     "q": "A rocket works on the principle of conservation of:",
     "opts": ["Energy", "Angular momentum", "Linear momentum", "Mass"], "ans": 2,
     "exp": "Rocket works on conservation of linear momentum."},
    {"id": 120, "chapter": "Laws of Motion", "subject": "Physics",
     "q": "Banking of roads is done to provide:",
     "opts": ["Kinetic friction", "Centripetal force", "Normal reaction", "Static friction"], "ans": 1,
     "exp": "Road banking provides the centripetal force required for circular motion."},

    {"id": 121, "chapter": "Work, Power & Energy", "subject": "Physics",
     "q": "Work done by friction on a rough surface is:",
     "opts": ["Positive", "Zero", "Negative", "Depends on motion"], "ans": 2,
     "exp": "Friction force acts opposite to displacement, so work is always negative."},
    {"id": 122, "chapter": "Work, Power & Energy", "subject": "Physics",
     "q": "1 kWh = ?",
     "opts": ["3.6 × 10⁶ J", "3.6 × 10³ J", "3.6 × 10⁹ J", "360 J"], "ans": 0,
     "exp": "1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J."},
    {"id": 123, "chapter": "Work, Power & Energy", "subject": "Physics",
     "q": "The work-energy theorem states:",
     "opts": ["W = ΔPE", "W_net = ΔKE", "W = mgh", "W = Pt"], "ans": 1,
     "exp": "Net work done = change in kinetic energy."},
    {"id": 124, "chapter": "Work, Power & Energy", "subject": "Physics",
     "q": "A spring of spring constant k is compressed by x. Elastic PE stored is:",
     "opts": ["kx", "kx²", "½kx²", "2kx²"], "ans": 2,
     "exp": "PE = ½kx²."},
    {"id": 125, "chapter": "Work, Power & Energy", "subject": "Physics",
     "q": "Power has SI unit:",
     "opts": ["Joule", "Newton", "Watt", "Pascal"], "ans": 2,
     "exp": "Power = Work/Time. SI unit = J/s = Watt."},
    {"id": 126, "chapter": "Work, Power & Energy", "subject": "Physics",
     "q": "In a perfectly inelastic collision:",
     "opts": ["KE is conserved", "Momentum is not conserved", "Both objects stick together", "Energy is created"], "ans": 2,
     "exp": "In perfectly inelastic collision, objects stick together."},

    {"id": 127, "chapter": "Rotational Motion", "subject": "Physics",
     "q": "The moment of inertia of a solid sphere about its diameter is:",
     "opts": ["½MR²", "⅔MR²", "MR²", "⅖MR²"], "ans": 3,
     "exp": "I = 2MR²/5 for a solid sphere about its diameter."},
    {"id": 128, "chapter": "Rotational Motion", "subject": "Physics",
     "q": "Angular momentum L = ?",
     "opts": ["mvr", "Iω", "r × p⃗", "All of the above"], "ans": 3,
     "exp": "Angular momentum = Iω = mvr = r⃗ × p⃗."},
    {"id": 129, "chapter": "Rotational Motion", "subject": "Physics",
     "q": "A spinning ice-skater pulls in her arms. Her angular velocity:",
     "opts": ["Decreases", "Increases", "Stays same", "Becomes zero"], "ans": 1,
     "exp": "By conservation of angular momentum, reducing I increases ω."},
    {"id": 130, "chapter": "Rotational Motion", "subject": "Physics",
     "q": "Torque = ?",
     "opts": ["F × r (cross product)", "F · r (dot product)", "F/r", "F + r"], "ans": 0,
     "exp": "Torque τ⃗ = r⃗ × F⃗."},
    {"id": 131, "chapter": "Rotational Motion", "subject": "Physics",
     "q": "The radius of gyration k is related to moment of inertia I and mass M by:",
     "opts": ["I = Mk²", "I = M/k²", "I = k/M", "k = MI"], "ans": 0,
     "exp": "I = Mk² → k = √(I/M)."},
    {"id": 132, "chapter": "Rotational Motion", "subject": "Physics",
     "q": "Theorem of parallel axes states: I = Icm + ?",
     "opts": ["MR²", "Md²", "2Md", "½Md²"], "ans": 1,
     "exp": "Parallel axis theorem: I = I_cm + Md²."},

    {"id": 133, "chapter": "Gravitation", "subject": "Physics",
     "q": "Gravitational constant G has SI units:",
     "opts": ["N m² kg⁻²", "N kg⁻²", "N m kg⁻²", "m³ kg⁻¹ s⁻²"], "ans": 0,
     "exp": "G = Fr²/m₁m₂ = N·m²/kg²."},
    {"id": 134, "chapter": "Gravitation", "subject": "Physics",
     "q": "The escape velocity from Earth's surface is approximately:",
     "opts": ["7.9 km/s", "11.2 km/s", "25 km/s", "3 km/s"], "ans": 1,
     "exp": "Escape velocity v_e = √(2gR) ≈ 11.2 km/s."},
    {"id": 135, "chapter": "Gravitation", "subject": "Physics",
     "q": "According to Kepler's 3rd law, T² ∝ ?",
     "opts": ["r", "r²", "r³", "r⁴"], "ans": 2,
     "exp": "Kepler's 3rd law: T² ∝ a³."},
    {"id": 136, "chapter": "Gravitation", "subject": "Physics",
     "q": "Geostationary satellites orbit at a height of approximately:",
     "opts": ["200 km", "800 km", "36,000 km", "400 km"], "ans": 2,
     "exp": "Geostationary orbit ≈ 36,000 km above Earth's surface."},
    {"id": 137, "chapter": "Gravitation", "subject": "Physics",
     "q": "The gravitational potential energy at infinite distance from Earth is taken as:",
     "opts": ["Zero", "Positive maximum", "Negative maximum", "GMm/R"], "ans": 0,
     "exp": "By convention, gravitational PE = 0 at r = ∞."},
    {"id": 138, "chapter": "Gravitation", "subject": "Physics",
     "q": "The weight of a body at the centre of the Earth is:",
     "opts": ["Maximum", "Same as surface", "Zero", "Twice surface value"], "ans": 2,
     "exp": "At centre g = 0, so weight = mg = 0."},

    # ── CHEMISTRY ────────────────────────────────────────────────────────────────
    {"id": 139, "chapter": "Structure of Atom", "subject": "Chemistry",
     "q": "The de Broglie wavelength of an electron with momentum p is:",
     "opts": ["λ = hp", "λ = h/p", "λ = p/h", "λ = √(h/p)"], "ans": 1,
     "exp": "de Broglie relation: λ = h/p = h/mv."},
    {"id": 140, "chapter": "Structure of Atom", "subject": "Chemistry",
     "q": "Heisenberg's uncertainty principle states:",
     "opts": ["Δx · Δp ≥ h/4π", "ΔE · Δt ≤ h/4π", "Δx · Δv ≥ h/4π", "Both Δx·Δp ≥ h/4π and ΔE·Δt ≥ h/4π"], "ans": 3,
     "exp": "Both Δx·Δp ≥ h/4π and ΔE·Δt ≥ h/4π are forms of Heisenberg's uncertainty principle."},
    {"id": 141, "chapter": "Structure of Atom", "subject": "Chemistry",
     "q": "The maximum number of electrons in a shell with principal quantum number n is:",
     "opts": ["n²", "2n", "2n²", "n²/2"], "ans": 2,
     "exp": "Maximum electrons per shell = 2n²."},
    {"id": 142, "chapter": "Structure of Atom", "subject": "Chemistry",
     "q": "The shape of a p-orbital is:",
     "opts": ["Spherical", "Dumbbell", "Double dumbbell", "Cloverleaf"], "ans": 1,
     "exp": "p-orbitals are dumbbell-shaped."},
    {"id": 143, "chapter": "Structure of Atom", "subject": "Chemistry",
     "q": "The Bohr model is applicable to:",
     "opts": ["All atoms", "Hydrogen-like species (one electron)", "Only hydrogen", "Multi-electron atoms"], "ans": 1,
     "exp": "Bohr model works for hydrogen-like (one-electron) species."},
    {"id": 144, "chapter": "Structure of Atom", "subject": "Chemistry",
     "q": "Aufbau principle states that orbitals are filled in order of:",
     "opts": ["Increasing n", "Increasing l", "Increasing n + l", "Decreasing energy"], "ans": 2,
     "exp": "Aufbau principle: orbitals fill in order of increasing (n + l)."},
    {"id": 145, "chapter": "Structure of Atom", "subject": "Chemistry",
     "q": "The spin quantum number (ms) can have values:",
     "opts": ["+1/2 only", "–1/2 only", "+1/2 or –1/2", "0, +1/2, –1/2"], "ans": 2,
     "exp": "Spin quantum number ms = +½ (spin up) or –½ (spin down)."},
    {"id": 146, "chapter": "Structure of Atom", "subject": "Chemistry",
     "q": "Rutherford's gold foil experiment led to the discovery of:",
     "opts": ["Electron", "Neutron", "Nucleus", "Proton"], "ans": 2,
     "exp": "Rutherford's experiment demonstrated the existence of the nucleus."},

    {"id": 147, "chapter": "Periodic Table", "subject": "Chemistry",
     "q": "Modern Periodic Law states that properties of elements are periodic functions of their:",
     "opts": ["Atomic mass", "Atomic number", "Neutron number", "Electron number"], "ans": 1,
     "exp": "Properties depend on atomic number."},
    {"id": 148, "chapter": "Periodic Table", "subject": "Chemistry",
     "q": "Which has the highest electronegativity?",
     "opts": ["Oxygen", "Chlorine", "Fluorine", "Nitrogen"], "ans": 2,
     "exp": "Fluorine has the highest electronegativity (3.98)."},
    {"id": 149, "chapter": "Periodic Table", "subject": "Chemistry",
     "q": "Ionisation energy generally _____ across a period (left to right):",
     "opts": ["Decreases", "Increases", "Remains same", "First increases then decreases"], "ans": 1,
     "exp": "IE increases across a period due to increasing nuclear charge."},
    {"id": 150, "chapter": "Periodic Table", "subject": "Chemistry",
     "q": "The element with electronic configuration [Xe] 4f¹⁴ 5d¹⁰ 6s¹ is:",
     "opts": ["Gold (Au)", "Mercury (Hg)", "Platinum (Pt)", "Silver (Ag)"], "ans": 0,
     "exp": "Au (Gold, Z=79): [Xe] 4f¹⁴ 5d¹⁰ 6s¹."},
    {"id": 151, "chapter": "Periodic Table", "subject": "Chemistry",
     "q": "Shielding (screening) effect _____ electron affinity:",
     "opts": ["Increases", "Decreases", "Does not affect", "Doubles"], "ans": 1,
     "exp": "Greater shielding reduces effective nuclear charge, decreasing electron affinity."},
    {"id": 152, "chapter": "Periodic Table", "subject": "Chemistry",
     "q": "Which period contains the d-block elements (first transition series)?",
     "opts": ["Period 2", "Period 3", "Period 4", "Period 5"], "ans": 2,
     "exp": "First transition series (Sc to Zn) are in Period 4."},
    {"id": 153, "chapter": "Periodic Table", "subject": "Chemistry",
     "q": "Diagonal relationship exists between:",
     "opts": ["Li and Mg", "Na and Ca", "K and Ca", "Be and Al"], "ans": 3,
     "exp": "Diagonal relationships: Li-Mg, Be-Al, B-Si."},
    {"id": 154, "chapter": "Periodic Table", "subject": "Chemistry",
     "q": "The size of isoelectronic species decreases with:",
     "opts": ["Decreasing nuclear charge", "Increasing nuclear charge", "Increasing electron number", "Decreasing atomic mass"], "ans": 1,
     "exp": "Higher nuclear charge → smaller size."},

    {"id": 155, "chapter": "Chemical Bonding", "subject": "Chemistry",
     "q": "According to VSEPR theory, the shape of SF₆ is:",
     "opts": ["Tetrahedral", "Octahedral", "Trigonal bipyramidal", "Square planar"], "ans": 1,
     "exp": "SF₆ has 6 bond pairs and 0 lone pairs → octahedral geometry."},
    {"id": 156, "chapter": "Chemical Bonding", "subject": "Chemistry",
     "q": "Which of the following has the maximum bond angle?",
     "opts": ["NH₃", "H₂O", "CH₄", "PCl₃"], "ans": 2,
     "exp": "CH₄: 109.5° (4 BP, 0 LP). NH₃: 107°. H₂O: 104.5°."},
    {"id": 157, "chapter": "Chemical Bonding", "subject": "Chemistry",
     "q": "Hydrogen bond is strongest in:",
     "opts": ["HF", "H₂O", "NH₃", "HCl"], "ans": 0,
     "exp": "Hydrogen bond strength: F–H···F > O–H···O > N–H···N."},
    {"id": 158, "chapter": "Chemical Bonding", "subject": "Chemistry",
     "q": "The hybridisation of carbon in ethyne (C₂H₂) is:",
     "opts": ["sp³", "sp²", "sp", "dsp²"], "ans": 2,
     "exp": "Ethyne: triple bond, sp hybridisation, linear geometry."},
    {"id": 159, "chapter": "Chemical Bonding", "subject": "Chemistry",
     "q": "Formal charge on oxygen in O₃ (ozone) central atom is:",
     "opts": ["0", "+1", "–1", "+2"], "ans": 1,
     "exp": "Central O: formal charge = 6 – 2 – ½(6) = +1."},
    {"id": 160, "chapter": "Chemical Bonding", "subject": "Chemistry",
     "q": "Which molecule is non-polar despite having polar bonds?",
     "opts": ["HF", "H₂O", "CO₂", "NH₃"], "ans": 2,
     "exp": "CO₂ is linear — the two C=O dipoles cancel → non-polar."},
    {"id": 161, "chapter": "Chemical Bonding", "subject": "Chemistry",
     "q": "The bond order in O₂ according to MO theory is:",
     "opts": ["1", "2", "3", "2.5"], "ans": 1,
     "exp": "O₂ MO: bond order = (10–6)/2 = 2."},
    {"id": 162, "chapter": "Chemical Bonding", "subject": "Chemistry",
     "q": "Which of the following has the highest lattice energy?",
     "opts": ["NaCl", "MgO", "KCl", "LiF"], "ans": 1,
     "exp": "MgO has higher charges → much higher lattice energy."},
    {"id": 163, "chapter": "Chemical Bonding", "subject": "Chemistry",
     "q": "The resonance structures of benzene differ in:",
     "opts": ["Position of atoms", "Position of electrons", "Both atoms and electrons", "Neither"], "ans": 1,
     "exp": "Resonance structures differ only in the arrangement of electrons."},
    {"id": 164, "chapter": "Chemical Bonding", "subject": "Chemistry",
     "q": "The back-bonding (pπ–dπ) occurs between:",
     "opts": ["C and H", "N and H", "B and N in BF₃ (F→B)", "O and H"], "ans": 2,
     "exp": "In BF₃, fluorine lone pair donates to empty p orbital of boron."},

    {"id": 165, "chapter": "Kinematics", "subject": "Physics",
     "q": "A stone is dropped from height 80 m. Time to reach ground (g = 10 m/s²):",
     "opts": ["2 s", "4 s", "8 s", "16 s"], "ans": 1,
     "exp": "s = ½gt² → 80 = ½×10×t² → t² = 16 → t = 4 s."},
    {"id": 166, "chapter": "Laws of Motion", "subject": "Physics",
     "q": "Which of Newton's laws explains why we lean forward when a bus brakes suddenly?",
     "opts": ["1st law", "2nd law", "3rd law", "Law of Gravitation"], "ans": 0,
     "exp": "Newton's 1st law (inertia): body tends to continue its state of motion."},
    {"id": 167, "chapter": "Gravitation", "subject": "Physics",
     "q": "At what height above Earth's surface is g half its surface value? (R = radius of Earth)",
     "opts": ["R/2", "R(√2 – 1)", "R", "2R"], "ans": 1,
     "exp": "g' = GM/(R+h)² = g/2 → h = R(√2 – 1) ≈ 0.414R."},
    {"id": 168, "chapter": "Work, Power & Energy", "subject": "Physics",
     "q": "A body of mass 2 kg moving at 4 m/s collides and sticks to a stationary 2 kg body. Final KE is:",
     "opts": ["16 J", "8 J", "4 J", "2 J"], "ans": 1,
     "exp": "v_f = (2×4)/(2+2) = 2 m/s. KE = ½×4×4 = 8 J."},

    {"id": 169, "chapter": "Structure of Atom", "subject": "Chemistry",
     "q": "The wavelength of light emitted when electron in H-atom falls from n=3 to n=2 (Balmer series) is approximately:",
     "opts": ["656 nm", "486 nm", "434 nm", "410 nm"], "ans": 0,
     "exp": "n=3→2 transition gives the Hα line at ~656 nm."},
    {"id": 170, "chapter": "Periodic Table", "subject": "Chemistry",
     "q": "Which of the following is a noble gas configuration?",
     "opts": ["1s²2s²2p⁶3s²", "1s²2s²2p⁶3s²3p⁶", "1s²2s²2p⁶3s²3p⁵", "1s²2s²2p⁵"], "ans": 1,
     "exp": "1s²2s²2p⁶3s²3p⁶ = Argon — noble gas with full outer shell."},
    {"id": 171, "chapter": "Chemical Bonding", "subject": "Chemistry",
     "q": "The geometry of XeF₄ is:",
     "opts": ["Tetrahedral", "Square planar", "See-saw", "Octahedral"], "ans": 1,
     "exp": "XeF₄: 4 BP + 2 LP → square planar molecular geometry."},
    {"id": 172, "chapter": "Biomolecules", "subject": "Biology",
     "q": "Which type of RNA carries amino acids to the ribosome?",
     "opts": ["mRNA", "rRNA", "tRNA", "snRNA"], "ans": 2,
     "exp": "tRNA carries specific amino acids to the ribosome."},
    {"id": 173, "chapter": "Cell Structure", "subject": "Biology",
     "q": "Which organelle is absent in animal cells but present in plant cells?",
     "opts": ["Mitochondria", "Chloroplast", "Ribosome", "Golgi apparatus"], "ans": 1,
     "exp": "Chloroplasts are present in plant cells for photosynthesis."},
    {"id": 174, "chapter": "Blood Fluid & Circulation", "subject": "Biology",
     "q": "Thrombocytes (platelets) are derived from:",
     "opts": ["Lymphocytes", "Megakaryocytes", "Erythrocytes", "Monocytes"], "ans": 1,
     "exp": "Platelets are cytoplasmic fragments of megakaryocytes."},
    {"id": 175, "chapter": "Excretory Products & Elimination", "subject": "Biology",
     "q": "Which part of nephron is impermeable to water even in presence of ADH?",
     "opts": ["Proximal tubule", "Descending limb of LoH", "Ascending limb of LoH", "Collecting duct"], "ans": 2,
     "exp": "The ascending limb of Loop of Henle is impermeable to water."},
    {"id": 176, "chapter": "Plant Kingdom", "subject": "Biology",
     "q": "Vascular tissue is absent in:",
     "opts": ["Pteridophytes", "Gymnosperms", "Angiosperms", "Bryophytes"], "ans": 3,
     "exp": "Bryophytes are non-vascular."},
    {"id": 177, "chapter": "Rotational Motion", "subject": "Physics",
     "q": "Moment of inertia of a thin rod about its centre of mass (perpendicular axis):",
     "opts": ["ML²/3", "ML²/12", "ML²/4", "ML²/6"], "ans": 1,
     "exp": "For a thin uniform rod, I about centre = ML²/12."},
    {"id": 178, "chapter": "Biological Classification", "subject": "Biology",
     "q": "Which of the following is the correct scientific name of mango?",
     "opts": ["Mangifera indica", "Indica mangifera", "Mangifera Indica", "mangifera indica"], "ans": 0,
     "exp": "Binomial nomenclature: Mangifera indica."},
    {"id": 179, "chapter": "Units & Dimensions", "subject": "Physics",
     "q": "Dimensional formula for surface tension is:",
     "opts": ["[MLT⁻²]", "[MT⁻²]", "[ML⁻¹T⁻²]", "[ML²T⁻²]"], "ans": 1,
     "exp": "Surface tension = Force/Length = [MLT⁻²]/[L] = [MT⁻²]."},
    {"id": 180, "chapter": "Chemical Bonding", "subject": "Chemistry",
     "q": "Which of the following molecules exhibits sp³d² hybridisation?",
     "opts": ["PCl₃", "PCl₅", "SF₆", "BF₃"], "ans": 2,
     "exp": "SF₆ has 6 bond pairs → sp³d² hybridisation."},
]

TOTAL_TIME = 3 * 60 * 60  # 3 hours in seconds
SUBJECT_COLORS = {"Biology": "\033[92m", "Physics": "\033[94m", "Chemistry": "\033[93m"}
RESET_COLOR = "\033[0m"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def shuffle(arr):
    a = arr.copy()
    for i in range(len(a) - 1, 0, -1):
        j = random.randint(0, i)
        a[i], a[j] = a[j], a[i]
    return a


def build_questions():
    bio = shuffle([q for q in RAW_QUESTIONS if q["subject"] == "Biology"])
    phy = shuffle([q for q in RAW_QUESTIONS if q["subject"] == "Physics"])
    chem = shuffle([q for q in RAW_QUESTIONS if q["subject"] == "Chemistry"])
    questions = bio + phy + chem
    for i, q in enumerate(questions):
        q["no"] = i + 1
    return questions


def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


class NEETMockTest:
    def __init__(self):
        self.questions = []
        self.answers = {}
        self.skipped = set()
        self.marked = set()
        self.current = 0
        self.time_left = TOTAL_TIME
        self.start_time = None
        self.running = False
        self.filter_subject = "All"

    def start_test(self):
        clear_screen()
        print("\n" + "=" * 60)
        print("             NEET MOCK TEST")
        print("=" * 60)
        print("\n📋 TEST INSTRUCTIONS:")
        print("  • 180 questions from Biology, Physics, Chemistry")
        print("  • Time limit: 3 hours")
        print("  • +4 marks for correct | -1 mark for wrong | 0 for skipped")
        print("  • You can skip, mark for review, and navigate freely")
        print("\nPress Enter to start the test...")
        input()
        
        self.questions = build_questions()
        self.answers = {}
        self.skipped = set()
        self.marked = set()
        self.current = 0
        self.time_left = TOTAL_TIME
        self.start_time = time.time()
        self.running = True
        self.run_test()

    def run_test(self):
        while self.running and self.current < len(self.questions):
            elapsed = int(time.time() - self.start_time)
            self.time_left = max(0, TOTAL_TIME - elapsed)
            
            if self.time_left <= 0:
                print("\n⏰ TIME'S UP! Submitting test automatically...")
                self.submit_test()
                return
            
            self.display_question()
            self.handle_input()
        
        if self.current >= len(self.questions):
            self.submit_test()

    def display_question(self):
        clear_screen()
        q = self.questions[self.current]
        elapsed = int(time.time() - self.start_time)
        self.time_left = max(0, TOTAL_TIME - elapsed)
        
        attempted = len(self.answers)
        total = len(self.questions)
        
        print("\n" + "=" * 70)
        print(f"  NEET MOCK TEST - Question {q['no']}/{total}")
        print("=" * 70)
        print(f"  ⏱️  Time Left: {format_time(self.time_left)}  |  ✅ Attempted: {attempted}/{total}")
        print("-" * 70)
        
        # Subject and Chapter
        color = SUBJECT_COLORS.get(q["subject"], "")
        print(f"  {color}📚 {q['subject']}{RESET_COLOR}  |  📖 {q['chapter']}")
        if q["id"] in self.marked:
            print("  🔖 MARKED FOR REVIEW")
        print("-" * 70)
        
        # Question
        print(f"\n  Q{q['no']}. {q['q']}\n")
        
        # Options
        for i, opt in enumerate(q["opts"]):
            prefix = ["A", "B", "C", "D"][i]
            selected = self.answers.get(q["id"]) == i
            marker = " ▶" if selected else ""
            print(f"     {prefix}. {opt}{marker}")
        
        print("\n" + "-" * 70)
        print("  Commands: [A/B/C/D] answer | [S] skip | [M] mark/unmark")
        print("            [N] next | [P] previous | [J] jump to question | [Q] submit test")
        print("-" * 70)
        
        # Status
        status = []
        if q["id"] in self.answers:
            status.append(f"✅ Answered: {['A','B','C','D'][self.answers[q['id']]]}")
        elif q["id"] in self.skipped:
            status.append("⏭️ Skipped")
        else:
            status.append("⭕ Not attempted")
        
        if q["id"] in self.marked:
            status.append("🔖 Marked")
        
        print(f"  Status: {' | '.join(status)}")
        print()

    def handle_input(self):
        q = self.questions[self.current]
        while True:
            cmd = input("  ⚡ Enter command: ").strip().upper()
            
            if cmd in ["A", "B", "C", "D"]:
                idx = ord(cmd) - 65
                if 0 <= idx < 4:
                    self.answers[q["id"]] = idx
                    self.skipped.discard(q["id"])
                    print(f"\n  ✅ Answer saved: {cmd}")
                    time.sleep(0.5)
                    if self.current < len(self.questions) - 1:
                        self.current += 1
                    return
                else:
                    print("  Invalid option!")
            
            elif cmd == "S":
                self.skipped.add(q["id"])
                if q["id"] in self.answers:
                    del self.answers[q["id"]]
                print("  ⏭️ Question skipped")
                time.sleep(0.5)
                if self.current < len(self.questions) - 1:
                    self.current += 1
                return
            
            elif cmd == "M":
                if q["id"] in self.marked:
                    self.marked.discard(q["id"])
                    print("  🔖 Mark removed")
                else:
                    self.marked.add(q["id"])
                    print("  🔖 Question marked for review")
                time.sleep(0.5)
                self.display_question()
                return
            
            elif cmd == "N":
                if self.current < len(self.questions) - 1:
                    self.current += 1
                return
            
            elif cmd == "P":
                if self.current > 0:
                    self.current -= 1
                return
            
            elif cmd == "J":
                try:
                    num = int(input("  Enter question number (1-180): "))
                    if 1 <= num <= len(self.questions):
                        self.current = num - 1
                    else:
                        print(f"  Please enter a number between 1 and {len(self.questions)}")
                except ValueError:
                    print("  Invalid number!")
                return
            
            elif cmd == "Q":
                confirm = input("  Are you sure you want to submit? (y/n): ").strip().lower()
                if confirm == 'y':
                    self.submit_test()
                    return
            else:
                print("  Invalid command! Use A/B/C/D, S, M, N, P, J, or Q")

    def submit_test(self):
        self.running = False
        self.show_results()

    def show_results(self):
        clear_screen()
        correct = 0
        incorrect = 0
        unattempted = 0
        chapter_stats = {}
        
        for q in self.questions:
            chapter = q["chapter"]
            if chapter not in chapter_stats:
                chapter_stats[chapter] = {"total": 0, "correct": 0, "subject": q["subject"]}
            chapter_stats[chapter]["total"] += 1
            
            ans = self.answers.get(q["id"])
            if ans is None:
                unattempted += 1
            elif ans == q["ans"]:
                correct += 1
                chapter_stats[chapter]["correct"] += 1
            else:
                incorrect += 1
        
        score = correct * 4 - incorrect * 1
        max_score = len(self.questions) * 4
        percentage = (score / max_score) * 100
        
        # Determine grade
        if percentage >= 85:
            grade = "Excellent!"
            grade_color = "\033[92m"
        elif percentage >= 65:
            grade = "Good"
            grade_color = "\033[94m"
        elif percentage >= 45:
            grade = "Average"
            grade_color = "\033[93m"
        else:
            grade = "Needs Work"
            grade_color = "\033[91m"
        
        print("\n" + "=" * 70)
        print("                     🏆 TEST RESULTS 🏆")
        print("=" * 70)
        print(f"\n  {grade_color}{grade}{RESET_COLOR}")
        print(f"\n  📊 Score: {score} / {max_score} ({percentage:.1f}%)")
        print("-" * 70)
        print(f"  ✅ Correct:   {correct}  ({correct * 4} marks)")
        print(f"  ❌ Incorrect: {incorrect}  ({incorrect * -1} marks)")
        print(f"  ⏭️ Skipped:   {unattempted}  (0 marks)")
        print("-" * 70)
        
        # Chapter-wise performance
        print("\n  📈 CHAPTER-WISE PERFORMANCE:")
        print("-" * 70)
        
        weak_chapters = []
        for chapter, stats in chapter_stats.items():
            pct = (stats["correct"] / stats["total"]) * 100 if stats["total"] > 0 else 0
            color = "\033[92m" if pct >= 70 else "\033[93m" if pct >= 40 else "\033[91m"
            print(f"    {color}[{stats['subject']}]{RESET_COLOR} {chapter[:30]:30} {stats['correct']}/{stats['total']} ({pct:.0f}%)")
            if pct < 60:
                weak_chapters.append((chapter, stats["subject"], pct, stats["correct"], stats["total"]))
        
        # Weak chapters sorted by percentage
        weak_chapters.sort(key=lambda x: x[2])
        
        if weak_chapters:
            print("\n" + "-" * 70)
            print("  🎯 FOCUS AREAS (Weakest Chapters):")
            print("-" * 70)
            for chapter, subject, pct, corr, total in weak_chapters[:5]:
                print(f"    [{subject}] {chapter}")
                if pct < 30:
                    print(f"      → Critical: Revise concepts from scratch.")
                elif pct < 50:
                    print(f"      → Needs improvement: Review key concepts.")
                else:
                    print(f"      → Good but can be better: Practice more.")
        
        print("\n" + "=" * 70)
        print("  Options: [V] View detailed solutions | [R] Retake test | [X] Exit")
        print("=" * 70)
        
        while True:
            choice = input("\n  Enter choice: ").strip().upper()
            if choice == "V":
                self.show_solutions()
                break
            elif choice == "R":
                self.retake_test()
                break
            elif choice == "X":
                print("\n  Thank you for using NEET Mock Test! Good luck with your preparation! 🚀")
                exit(0)
            else:
                print("  Invalid choice! Please enter V, R, or X")

    def show_solutions(self):
        clear_screen()
        print("\n" + "=" * 70)
        print("                📚 DETAILED SOLUTIONS")
        print("=" * 70)
        
        # Filter options
        print("\n  Filter by subject:")
        print("    [1] All")
        print("    [2] Biology")
        print("    [3] Physics")
        print("    [4] Chemistry")
        
        filter_choice = input("\n  Enter choice: ").strip()
        if filter_choice == "2":
            filter_subject = "Biology"
        elif filter_choice == "3":
            filter_subject = "Physics"
        elif filter_choice == "4":
            filter_subject = "Chemistry"
        else:
            filter_subject = "All"
        
        filtered_qs = self.questions if filter_subject == "All" else [q for q in self.questions if q["subject"] == filter_subject]
        
        for i, q in enumerate(filtered_qs):
            user_ans = self.answers.get(q["id"])
            is_correct = user_ans == q["ans"]
            is_unattempted = user_ans is None
            
            if is_unattempted:
                status_icon = "⭕"
                status_color = "\033[93m"
                status_text = "NOT ATTEMPTED"
            elif is_correct:
                status_icon = "✅"
                status_color = "\033[92m"
                status_text = "CORRECT"
            else:
                status_icon = "❌"
                status_color = "\033[91m"
                status_text = "WRONG"
            
            print(f"\n{status_color}{status_icon} Q{q['no']}. {q['q']}{RESET_COLOR}")
            print(f"   [{q['subject']}] {q['chapter']}")
            
            # Show options with correct/incorrect indicators
            for opt_idx, opt in enumerate(q["opts"]):
                prefix = ["A", "B", "C", "D"][opt_idx]
                if opt_idx == q["ans"]:
                    print(f"      {prefix}. {opt} ✓ CORRECT")
                elif opt_idx == user_ans:
                    print(f"      {prefix}. {opt} ✗ YOUR ANSWER")
                else:
                    print(f"      {prefix}. {opt}")
            
            print(f"\n   💡 EXPLANATION: {q['exp']}")
            print("-" * 70)
            
            if i < len(filtered_qs) - 1:
                input("  Press Enter to continue...")
                clear_screen()
                print("\n" + "=" * 70)
                print("                📚 DETAILED SOLUTIONS")
                print("=" * 70)
        
        input("\n  Press Enter to return to results...")
        self.show_results()

    def retake_test(self):
        print("\n  🔄 Restarting test...")
        time.sleep(1)
        self.start_test()


def main():
    test = NEETMockTest()
    test.start_test()


if __name__ == "__main__":
    main()